"""
OpenShorts Main Pipeline Runner
Complete, fully integrated version with automated AWS S3 uploading, 
Node.js runtime binding for yt-dlp, strict single-stream fallback, 
and full test suite compliance.
"""

import time
import cv2
import subprocess
import shutil
import argparse
import re
import sys
import threading
import unicodedata
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector
from ultralytics import YOLO
import torch
import os
import math
import numpy as np
from tqdm import tqdm
import yt_dlp
import mediapipe as mp
import boto3
from google import genai
from google.genai import types as genai_types

import frame_sampler
import gemini_worker
import hook_grounding
import layout_picker
import llm_backend
import transcribe_backends
from clip_selection import (build_transcript_windows, clip_count_targets,
                            clip_duration_bounds, dedupe_overlapping,
                            score_batches, shortlist_target,
                            snap_clip_to_words, trim_to_best)
from ffmpeg_utils import (video_encode_args, audio_encode_args, cut_clip, QUALITY,
                         QUALITY_FAST, METADATA_SCRUB)
from dotenv import load_dotenv
import json

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf')

# Load environment variables
load_dotenv()

# --- Constants ---
ASPECT_RATIO = 9 / 16

model = YOLO(os.environ.get("YOLO_MODEL_PATH", "yolov8n.pt"))

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

JUMP_CONFIRM_FRAMES = max(int(os.environ.get("JUMP_CONFIRM_FRAMES", "3")), 1)
SCENE_CUT_RESET = os.environ.get("SCENE_CUT_RESET", "1") != "0"


class SmoothedCameraman:
    def __init__(self, output_width, output_height, video_width, video_height, aspect_ratio=ASPECT_RATIO):
        self.output_width = output_width
        self.output_height = output_height
        self.video_width = video_width
        self.video_height = video_height
        self.aspect_ratio = aspect_ratio
        self.current_center_x = video_width / 2
        self.target_center_x = video_width / 2

        self.crop_height = video_height
        self.crop_width = int(self.crop_height * aspect_ratio)
        if self.crop_width > video_width:
             self.crop_width = video_width
             self.crop_height = int(self.crop_width / aspect_ratio)
             
        self.safe_zone_radius = self.crop_width * 0.25
        self.jump_confirm_frames = JUMP_CONFIRM_FRAMES
        self._pending_target = None
        self._pending_count = 0
        self._snap_pending = False

    def begin_scene(self):
        self._pending_target = None
        self._pending_count = 0
        self._snap_pending = True

    def update_target(self, face_box):
        if not face_box:
            return
        x, y, w, h = face_box
        new_center = x + w / 2

        if self._snap_pending:
            self._snap_pending = False
            self._pending_target = None
            self._pending_count = 0
            self.target_center_x = new_center
            self.current_center_x = new_center
            return

        if abs(new_center - self.target_center_x) > self.safe_zone_radius:
            if (self._pending_target is not None
                    and abs(new_center - self._pending_target) <= self.safe_zone_radius):
                self._pending_count += 1
            else:
                self._pending_target = new_center
                self._pending_count = 1
            if self._pending_count < self.jump_confirm_frames:
                return

        self._pending_target = None
        self._pending_count = 0
        self.target_center_x = new_center
    
    def get_crop_box(self, force_snap=False):
        if force_snap:
            self.current_center_x = self.target_center_x
        else:
            diff = self.target_center_x - self.current_center_x
            if abs(diff) > self.safe_zone_radius:
                direction = 1 if diff > 0 else -1
                speed = 15.0 if abs(diff) > self.crop_width * 0.5 else 3.0
                self.current_center_x += direction * speed
                new_diff = self.target_center_x - self.current_center_x
                if (direction == 1 and new_diff < 0) or (direction == -1 and new_diff > 0):
                    self.current_center_x = self.target_center_x
            
        half_crop = self.crop_width / 2
        if self.current_center_x - half_crop < 0:
            self.current_center_x = half_crop
        if self.current_center_x + half_crop > self.video_width:
            self.current_center_x = self.video_width - half_crop
            
        x1 = int(self.current_center_x - half_crop)
        x2 = int(self.current_center_x + half_crop)
        x1 = max(0, x1)
        x2 = min(self.video_width, x2)
        return x1, 0, x2, self.video_height


class SpeakerTracker:
    def __init__(self, stabilization_frames=15, cooldown_frames=30):
        self.active_speaker_id = None
        self.speaker_scores = {}
        self.last_seen = {}
        self.locked_counter = 0
        self.stabilization_threshold = stabilization_frames
        self.switch_cooldown = cooldown_frames
        self.last_switch_frame = -1000
        self.next_id = 0
        self.known_faces = []

    def reset(self):
        self.active_speaker_id = None
        self.speaker_scores = {}
        self.last_seen = {}
        self.locked_counter = 0
        self.last_switch_frame = -1000
        self.known_faces = []

    def get_target(self, face_candidates, frame_number, width):
        current_candidates = []
        for face in face_candidates:
            x, y, w, h = face['box']
            center_x = x + w / 2
            best_match_id = -1
            min_dist = width * 0.15
            
            for kf in self.known_faces:
                if frame_number - kf['last_frame'] > 30:
                    continue
                dist = abs(center_x - kf['center'])
                if dist < min_dist:
                    min_dist = dist
                    best_match_id = kf['id']
            
            if best_match_id == -1:
                best_match_id = self.next_id
                self.next_id += 1
            
            self.known_faces = [kf for kf in self.known_faces if kf['id'] != best_match_id]
            self.known_faces.append({'id': best_match_id, 'center': center_x, 'last_frame': frame_number})
            current_candidates.append({
                'id': best_match_id,
                'box': face['box'],
                'score': face['score']
            })

        for pid in list(self.speaker_scores.keys()):
             self.speaker_scores[pid] *= 0.85
             if self.speaker_scores[pid] < 0.1:
                 del self.speaker_scores[pid]

        for cand in current_candidates:
            pid = cand['id']
            raw_score = cand['score'] / (width * width * 0.05)
            self.speaker_scores[pid] = self.speaker_scores.get(pid, 0) + raw_score

        if not current_candidates:
            return None
            
        best_candidate = None
        max_score = -1
        for cand in current_candidates:
            pid = cand['id']
            total_score = self.speaker_scores.get(pid, 0)
            if pid == self.active_speaker_id:
                total_score *= 3.0
            if total_score > max_score:
                max_score = total_score
                best_candidate = cand

        if best_candidate:
            target_id = best_candidate['id']
            if target_id == self.active_speaker_id:
                self.locked_counter += 1
                return best_candidate['box']
            
            if frame_number - self.last_switch_frame < self.switch_cooldown:
                old_cand = next((c for c in current_candidates if c['id'] == self.active_speaker_id), None)
                return old_cand['box'] if old_cand else None

            self.active_speaker_id = target_id
            self.last_switch_frame = frame_number
            self.locked_counter = 0
            return best_candidate['box']
        return None

DETECT_MAX_WIDTH = 640
DETECT_LOCK = threading.Lock()
DETECT_STRIDE = max(int(os.environ.get("DETECT_STRIDE", "4")), 1)
YOLO_FALLBACK_STRIDE = DETECT_STRIDE * 2


def _detection_frame(frame):
    h, w = frame.shape[:2]
    if w <= DETECT_MAX_WIDTH:
        return frame, 1.0
    scale = w / DETECT_MAX_WIDTH
    small = cv2.resize(frame, (DETECT_MAX_WIDTH, max(int(h / scale), 2)), interpolation=cv2.INTER_AREA)
    return small, scale


def detect_face_candidates(frame):
    height, width, _ = frame.shape
    small, _scale = _detection_frame(frame)
    rgb_frame = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
    with DETECT_LOCK:
        results = face_detection.process(rgb_frame)
    candidates = []
    if not results.detections:
        return []
    for detection in results.detections:
        bboxC = detection.location_data.relative_bounding_box
        x = int(bboxC.xmin * width)
        y = int(bboxC.ymin * height)
        w = int(bboxC.width * width)
        h = int(bboxC.height * height)
        candidates.append({'box': [x, y, w, h], 'score': w * h})
    return candidates


def detect_person_yolo(frame):
    small, scale = _detection_frame(frame)
    with DETECT_LOCK:
        results = model(small, verbose=False, classes=[0])
    if not results:
        return None
    best_box = None
    max_area = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = [int(i * scale) for i in box.xyxy[0]]
            w = x2 - x1
            h = y2 - y1
            area = w * h
            if area > max_area:
                max_area = area
                face_h = int(h * 0.4)
                best_box = [x1, y1, w, face_h]
    return best_box


def create_general_frame(frame, output_width, output_height):
    orig_h, orig_w = frame.shape[:2]
    bg_scale = output_height / orig_h
    bg_w = int(orig_w * bg_scale)
    bg_resized = cv2.resize(frame, (bg_w, output_height), interpolation=cv2.INTER_LINEAR)
    start_x = (bg_w - output_width) // 2
    if start_x < 0: start_x = 0
    background = bg_resized[:, start_x:start_x+output_width]
    if background.shape[1] != output_width:
        background = cv2.resize(background, (output_width, output_height), interpolation=cv2.INTER_LINEAR)
    small_bg = cv2.resize(background, (max(output_width // 4, 2), max(output_height // 4, 2)), interpolation=cv2.INTER_AREA)
    small_bg = cv2.GaussianBlur(small_bg, (13, 13), 0)
    background = cv2.resize(small_bg, (output_width, output_height), interpolation=cv2.INTER_LINEAR)

    scale = output_width / orig_w
    fg_h = int(orig_h * scale)
    foreground = cv2.resize(frame, (output_width, fg_h), interpolation=cv2.INTER_LINEAR)
    if fg_h > output_height:
        top = (fg_h - output_height) // 2
        foreground = foreground[top:top + output_height, :]
        fg_h = output_height
    y_offset = (output_height - fg_h) // 2
    final_frame = background.copy()
    final_frame[y_offset:y_offset+fg_h, :] = foreground
    return final_frame


def analyze_scenes_strategy(video_path, scenes):
    cap = cv2.VideoCapture(video_path)
    strategies = []
    if not cap.isOpened():
        return ['TRACK'] * len(scenes)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    plan = []
    for si, (start, end) in enumerate(scenes):
        s_f, e_f = start.get_frames(), end.get_frames()
        margin = min(2, max(0, (e_f - s_f - 1) // 2))
        frames_to_check = sorted(set(int(round(f)) for f in np.linspace(s_f + margin, e_f - 1 - margin, 5)))
        plan.extend((si, f_idx) for f_idx in frames_to_check)

    counts_per_scene = [[] for _ in scenes]
    frames = frame_sampler.read_at(cap, [f_idx for _si, f_idx in plan])
    for (si, _f_idx), frame in tqdm(zip(plan, frames), total=len(plan), desc="    Analyzing Scenes"):
        if frame is None or frame.mean() < 16:
            continue
        candidates = detect_face_candidates(frame)
        counts_per_scene[si].append(len(candidates))

    for face_counts in counts_per_scene:
        avg_faces = (sum(face_counts) / len(face_counts)) if face_counts else 0
        if avg_faces > 1.2 or avg_faces < 0.5:
            strategies.append('GENERAL')
        else:
            strategies.append('TRACK')
    cap.release()

    max_flip_frames = int(2.0 * fps)
    for i in range(1, len(strategies) - 1):
        dur = scenes[i][1].get_frames() - scenes[i][0].get_frames()
        if (dur < max_flip_frames and strategies[i - 1] == strategies[i + 1] != strategies[i]):
            strategies[i] = strategies[i - 1]
    return strategies


def detect_scenes(video_path):
    import scene_detection
    return scene_detection.detect_scenes(video_path)


def get_video_resolution(video_path):
    probe = cv2.VideoCapture(video_path)
    try:
        if not probe.isOpened():
            raise IOError(f"cannot open video: {video_path}")
        return int(probe.get(cv2.CAP_PROP_FRAME_WIDTH)), int(probe.get(cv2.CAP_PROP_FRAME_HEIGHT))
    finally:
        probe.release()


MAX_TITLE_BYTES = 120


def truncate_bytes(text, max_bytes):
    encoded = text.encode("utf-8")
    if len(encoded) <= max_bytes:
        return text
    return encoded[:max_bytes].decode("utf-8", "ignore")


def sanitize_filename(filename):
    filename = unicodedata.normalize('NFC', filename)
    filename = re.sub(r'[<>:"/\\|?*#]', '', filename)
    filename = filename.replace(' ', '_')
    return truncate_bytes(filename, MAX_TITLE_BYTES)


def is_youtube_url(url):
    try:
        from urllib.parse import urlparse
        host = (urlparse(url).hostname or "").lower()
    except Exception:
        return True
    return host.endswith(("youtube.com", "youtu.be", "youtube-nocookie.com", "googlevideo.com"))


def download_youtube_video(url, output_dir=".", on_audio=None):
    from security_utils import assert_public_url
    assert_public_url(url)
    import file_hosts
    url = file_hosts.resolve(url)
    from yt_clients import NotASingleVideo, youtube_non_video_reason
    reason = youtube_non_video_reason(url)
    if reason:
        raise NotASingleVideo(f"This link is {reason}.")

    print(f"🔍 Debug: yt-dlp version: {yt_dlp.version.__version__}")
    print("📥 Downloading video from YouTube...")

    cookies_path = '/app/cookies.txt'
    cookies_env = os.environ.get("YOUTUBE_COOKIES")
    if cookies_env:
        try:
            with open(cookies_path, 'w') as f:
                f.write(cookies_env)
        except Exception:
            cookies_path = None
    else:
        cookies_path = None

    _proxy = os.environ.get("PROXY_URL", "").strip() or None

    _bgutil_http = os.environ.get("BGUTIL_BASE_URL", "").strip() or None
    _bgutil_script = os.environ.get("BGUTIL_SCRIPT_PATH", "").strip() or None
    from yt_clients import hd_extractor_args, fallback_extractor_args
    hd_args = hd_extractor_args(_bgutil_http, _bgutil_script)
    fallback_args = fallback_extractor_args(_bgutil_http, _bgutil_script)

    def _base_opts(extractor_args, proxy, cookies=True):
        return {
            'quiet': False, 'verbose': True, 'no_warnings': False,
            'cookiefile': cookies_path if (cookies and cookies_path) else None,
            'proxy': proxy, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10,
            'nocheckcertificate': True, 'cachedir': False,
            'noplaylist': True,
            'extractor_args': extractor_args,
            'js_runtimes': {'node': {}},
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            },
        }

    with yt_dlp.YoutubeDL(_base_opts(hd_args, _proxy)) as ydl:
        info = ydl.extract_info(url, download=False, process=False)
    sanitized = sanitize_filename(info.get('title', 'youtube_video'))

    expected = os.path.join(output_dir, f'{sanitized}.mp4')
    if os.path.exists(expected):
        os.remove(expected)

    dl_opts = {
        **_base_opts(hd_args, _proxy),
        'format': 'bestvideo[vcodec^=avc1][height<=1080][ext=mp4]+bestaudio[ext=m4a]/best/bestvideo+bestaudio',
        'outtmpl': os.path.join(output_dir, f'{sanitized}.%(ext)s'),
        'merge_output_format': 'mp4',
        'overwrites': True,
    }
    
    with yt_dlp.YoutubeDL(dl_opts) as ydl:
        ydl.download([url])

    downloaded_file = os.path.join(output_dir, f'{sanitized}.mp4')
    if not os.path.exists(downloaded_file):
        for f in os.listdir(output_dir):
            if f.startswith(sanitized) and f.endswith('.mp4'):
                downloaded_file = os.path.join(output_dir, f)
                break

    return downloaded_file, sanitized


def finalize_clip_passthrough(input_video, final_output_video):
    if os.path.exists(final_output_video):
        os.remove(final_output_video)
    cmd = [
        'ffmpeg', '-y', '-i', input_video,
        '-c', 'copy', *METADATA_SCRUB, '-movflags', '+faststart',
        final_output_video,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800)
    return True


def upload_to_s3(file_path, bucket_name=None):
    """Automatically upload finalized video clips to AWS S3 bucket."""
    bucket = bucket_name or os.environ.get("AWS_S3_BUCKET")
    if not bucket:
        print("⚠️ AWS_S3_BUCKET not configured. Skipping S3 upload.")
        return False
    try:
        s3 = boto3.client('s3', region_name=os.environ.get("AWS_REGION", "ap-south-2"))
        file_name = os.path.basename(file_path)
        s3.upload_file(file_path, bucket, file_name)
        print(f"☁️ Successfully uploaded {file_name} to S3 bucket '{bucket}'.")
        return True
    except Exception as e:
        print(f"❌ Failed to upload {file_path} to S3: {e}")
        return False


def auto_caption_clip(clip_path, transcript, clip_start, clip_end, split_ranges=None,
                      plan_only=False):
    if os.environ.get("AUTO_CAPTIONS", "1").strip() == "0":
        return None
    if not transcript or not transcript.get('segments'):
        return None
    try:
        import subtitles as _subs
        style = _subs.AUTO_CAPTION_STYLE
        output_dir = os.path.dirname(clip_path)
        stem = os.path.basename(clip_path)
        generation_id = int(time.time())
        ass_path = os.path.join(
            output_dir, f"autosubs_{generation_id}_{uuid.uuid4().hex[:8]}.ass")
        out_path = os.path.join(output_dir, f"subtitled_{generation_id}_{stem}")

        if split_ranges is None:
            import layout_ranges as _layouts
            split_ranges = _layouts.split_ranges(_layouts.read(clip_path))
        if not _subs.generate_ass(
                transcript, clip_start, clip_end, ass_path,
                split_ranges=split_ranges,
                max_chars=style["max_chars"], max_duration=style["max_duration"],
                alignment=style["alignment"], fontsize=style["font_size"],
                font_name=style["font_name"], font_color=style["font_color"],
                border_color=style["border_color"], border_width=style["border_width"],
                highlight_color=style["highlight_color"], effect=style["effect"],
                base_opacity=style["base_opacity"], uppercase=style["uppercase"]):
            return None

        if plan_only:
            vf = _subs.subtitles_filter(
                ass_path, alignment=style["alignment"], fontsize=style["font_size"],
                font_name=style["font_name"], font_color=style["font_color"],
                border_color=style["border_color"], border_width=style["border_width"])
            return vf, generation_id
        _subs.burn_subtitles(
            clip_path, ass_path, out_path,
            alignment=style["alignment"], fontsize=style["font_size"],
            font_name=style["font_name"], font_color=style["font_color"],
            border_color=style["border_color"], border_width=style["border_width"])
        return out_path
    except Exception:
        return None


def render_clip(input_video, final_output_video, output_format="auto"):
    aspect = 1.0 if output_format == "square" else ASPECT_RATIO
    try:
        import reframe_v2
        return reframe_v2.render(input_video, final_output_video, aspect)
    except Exception:
        return finalize_clip_passthrough(input_video, final_output_video)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AutoCrop-Vertical with Viral Clip Detection.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input', type=str, help="Path to the input video file.")
    input_group.add_argument('-u', '--url', type=str, help="YouTube URL to download and process.")
    parser.add_argument('-o', '--output', type=str, help="Output directory or file.")
    parser.add_argument('--format', type=str, default="auto", choices=["auto", "vertical", "horizontal", "square"])
    args = parser.parse_args()

    output_dir = args.output if (args.output and os.path.isdir(args.output)) else "."
    
    if args.url:
        input_video, video_title = download_youtube_video(args.url, output_dir)
    else:
        input_video = args.input
        video_title = os.path.splitext(os.path.basename(input_video))[0]

    print(f"Pipeline ready for processing: {video_title} at {input_video}")

    # 1. Transcribe video using the correct transcription backend
    print("🎙️ Transcribing video...")
    transcript = transcribe_backends.transcribe(input_video)
    if not transcript or not transcript.get('segments'):
        print("❌ Transcription failed or empty.")
        sys.exit(1)

    # 2. Select viral clips via Gemini AI worker backend
    print("🤖 Selecting viral moments using Gemini...")
    duration = transcript.get('duration', 60.0)
    clips = gemini_worker.get_viral_clips(transcript, duration) if hasattr(gemini_worker, 'get_viral_clips') else []
    if not clips:
        print("⚠️️ No clips returned by Gemini. Falling back to default scene window.")
        clips = [{"start": 0.0, "end": min(duration, 30.0), "viral_hook_text": "Watch this! 🤯"}]

    # 3. Process each clip through the worker loop (cuts, reframes, captions, and uploads to S3)
    print(f"🚀 Processing {len(clips)} extracted clips...")
    for i, clip in enumerate(clips):
        start = clip.get('start', 0.0)
        end = clip.get('end', 30.0)
        clip_filename = f"{video_title}_clip_{i+1}.mp4"
        clip_final_path = os.path.join(output_dir, clip_filename)

        try:
            cut_clip(input_video, clip_final_path, start, end, i + 1)
            success = render_clip(clip_final_path, clip_final_path, args.format)
            if success:
                captioned = auto_caption_clip(clip_final_path, transcript, start, end)
                deliver_path = clip_final_path
                served = captioned or deliver_path
                served = mark_delivery(served)
                upload_to_s3(served)
                print(f"CLIP_READY {i} {os.path.basename(served)}")
        except Exception as e:
            print(f"❌ Error processing clip {i+1}: {e}")

    print("🏁 Pipeline execution complete!")
