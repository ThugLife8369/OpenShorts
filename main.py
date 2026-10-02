"""
OpenShorts Main Pipeline Runner
Updated with robust FFmpeg fallback handling to prevent yt-dlp abort exit codes in remote containers.
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
from google import genai
from google.genai import types as genai_types

import frame_sampler
import gemini_worker
import hook_grounding
import layout_picker
import llm_backend
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

GEMINI_PROMPT_TEMPLATE = """
You are a senior short-form video editor. Read the ENTIRE transcript and word-level timestamps to choose the 3–15 MOST VIRAL moments for TikTok/IG Reels/YouTube Shorts. Each clip must be between 15 and 60 seconds long.

⚠️ FFMPEG TIME CONTRACT — STRICT REQUIREMENTS:
- Return timestamps in ABSOLUTE SECONDS from the start of the video (usable in: ffmpeg -ss <start> -to <end> -i <input> ...).
- Only NUMBERS with decimal point, up to 3 decimals (examples: 0, 1.250, 17.350).
- Ensure 0 ≤ start < end ≤ VIDEO_DURATION_SECONDS.
- Each clip between 15 and 60 s (inclusive).
- Prefer starting 0.2–0.4 s BEFORE the hook and ending 0.2–0.4 s AFTER the payoff.
- Use silence moments for natural cuts; never cut in the middle of a word or phrase.
- STRICTLY FORBIDDEN to use time formats other than absolute seconds.

VIDEO_DURATION_SECONDS: {video_duration}

TRANSCRIPT_TEXT (raw):
{transcript_text}

WORDS_JSON (array of {{w, s, e}} where s/e are seconds):
{words_json}

STRICT EXCLUSIONS:
- No generic intros/outros or purely sponsorship segments unless they contain the hook.
- No clips < 15 s or > 60 s.

OUTPUT — RETURN ONLY VALID JSON (no markdown, no comments). Order clips by predicted performance (best to worst). In the descriptions, ALWAYS include a CTA like "Follow me and comment X and I'll send you the workflow" (especially if discussing an n8n workflow):
{{
  "shorts": [
    {{
      "start": <number in seconds, e.g., 12.340>,
      "end": <number in seconds, e.g., 37.900>,
      "video_description_for_tiktok": "<description for TikTok oriented to get views>",
      "video_description_for_instagram": "<description for Instagram oriented to get views>",
      "video_title_for_youtube_short": "<title for YouTube Short oriented to get views 100 chars max>",
      "viral_hook_text": "<SHORT punchy text overlay (max 10 words) with 1-2 fitting emojis. MUST BE IN THE SAME LANGUAGE AS THE VIDEO TRANSCRIPT. Examples: 'POV: You realized... 😳', 'Did you know? 🤯', 'Stop doing this! 🚫'>"
    }}
  ]
}}
"""

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

def plan_download_attempts(direct_first, statics, paid, have_hd, youtube=True, skip_statics=False):
    if not youtube:
        plan = [('direct', False, None)]
        if statics:
            plan.append(('static-fallback', False, statics[0]))
        return plan
    if skip_statics and paid:
        statics, direct_first = [], False
    plan = []
    if direct_first:
        plan.append(('HD-direct', False, None))
    if have_hd:
        for i, s in enumerate(statics):
            plan.append((f'HD-static{i + 1}', False, s))
    if statics and paid:
        plan.append(('fallback-static', False, statics[0]))
    if have_hd:
        plan.append(('HD', bool(paid), paid))
    plan.append(('fallback', bool(paid), paid if paid else (statics[0] if statics else None)))
    return plan

def cap_source_duration(input_video, max_minutes, safety=False):
    try:
        secs = float(max_minutes) * 60.0
    except (TypeError, ValueError):
        return input_video
    if secs <= 0:
        return input_video
    duration = 0.0
    try:
        cap = cv2.VideoCapture(input_video)
        fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
        duration = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / fps) if fps else 0.0
        cap.release()
    except Exception:
        duration = 0.0
    if duration and duration <= secs + (30.0 if safety else 1.0):
        return input_video
    if safety and not duration:
        return input_video
    root, ext = os.path.splitext(input_video)
    tmp = f"{root}.capped{ext or '.mp4'}"
    attempts = [
        ["-c", "copy"],
        ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k"],
    ]
    for codec_args in attempts:
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", input_video, "-t", f"{secs:.3f}", *codec_args, "-movflags", "+faststart", tmp]
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=3600)
            os.replace(tmp, input_video)
            return input_video
        except Exception:
            try:
                os.remove(tmp)
            except OSError:
                pass
    raise RuntimeError(f"could not cut the source to its first {float(max_minutes):g} minutes")

def _content_block(error_text):
    t = error_text.lower()
    if "private video" in t:
        return "This video is private on YouTube. Set it to Unlisted (or Public) and try again, or upload the file instead."
    if "members-only" in t or "join this channel" in t:
        return "This video is for channel members only. Upload the file instead."
    return None


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
    step_start_time = time.time()

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
    _statics = [p.strip() for p in os.environ.get("STATIC_PROXY_URLS", "").split(",") if p.strip()]
    if _statics:
        import random as _random
        k = _random.randrange(len(_statics))
        _statics = _statics[k:] + _statics[:k]

    _bgutil_http = os.environ.get("BGUTIL_BASE_URL", "").strip()
    _bgutil_script = os.environ.get("BGUTIL_SCRIPT_PATH", "").strip()
    from yt_clients import hd_extractor_args, fallback_extractor_args
    hd_args = hd_extractor_args(_bgutil_http, _bgutil_script)
    fallback_args = fallback_extractor_args(_bgutil_http, _bgutil_script)

    # --- Robust FFmpeg Fallback Integration ---
    has_ffmpeg = shutil.which("ffmpeg") is not None

    def _hd_fmt_for(capped):
        if not has_ffmpeg:
            return 'best[ext=mp4]/best'
        if capped:
            return ('bestvideo[vcodec^=avc1][height<=720][ext=mp4]+bestaudio[ext=m4a]/'
                    'bestvideo[vcodec^=avc1][height<=720]+bestaudio/'
                    'best[height<=720][ext=mp4]/best[height<=720]/best')
        return ('bestvideo[vcodec^=avc1][height<=1080][ext=mp4]+bestaudio[ext=m4a]/'
                'bestvideo[vcodec^=avc1][height<=1080]+bestaudio/'
                'best[height<=1080][ext=mp4]/best[ext=mp4]/best')

    def _base_opts(extractor_args, proxy, cookies=True):
        return {
            'quiet': False, 'verbose': True, 'no_warnings': False,
            'cookiefile': cookies_path if (cookies and cookies_path) else None,
            'proxy': proxy, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10,
            'nocheckcertificate': True, 'cachedir': False,
            'noplaylist': True,
            'extractor_args': extractor_args,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            },
        }

    _dl_bytes = {"total": 0, "partial": 0}

    def _progress_hook(d):
        if d.get('status') == 'downloading':
            _dl_bytes["partial"] = int(d.get('downloaded_bytes') or 0)
        elif d.get('status') == 'finished':
            _dl_bytes["partial"] = 0
            _dl_bytes["total"] += int(d.get('total_bytes') or d.get('total_bytes_estimate') or d.get('downloaded_bytes') or 0)

    _early = {"started": False}
    _range_cap = None
    for _var, _margin in (("MAX_SOURCE_MINUTES", 5.0), ("SOURCE_CAP_MINUTES", 60.0)):
        _raw = os.environ.get(_var, "").strip()
        if _raw:
            try:
                _range_cap = float(_raw) * 60.0 + _margin
            except ValueError:
                pass
            break

    def _early_audio(info, extractor_args, proxy, cookies):
        import copy
        try:
            opts = {
                **_base_opts(extractor_args, proxy, cookies),
                'quiet': True, 'verbose': False, 'noprogress': True,
                'format': 'bestaudio[ext=m4a]/bestaudio',
                'outtmpl': os.path.join(output_dir, '.early_audio.%(ext)s'),
                'overwrites': True,
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                res = ydl.process_ie_result(copy.deepcopy(info), download=True)
            path = ((res.get('requested_downloads') or [{}])[0].get('filepath') or res.get('filepath'))
            if path and os.path.exists(path):
                on_audio(path, info.get('duration'))
        except Exception:
            pass

    def _attempt(extractor_args, fmt, proxy, cookies=True):
        _dl_bytes["total"] = 0
        _dl_bytes["partial"] = 0
        with yt_dlp.YoutubeDL(_base_opts(extractor_args, proxy, cookies)) as ydl:
            info = ydl.extract_info(url, download=False, process=False)
        sanitized = sanitize_filename(info.get('title', 'youtube_video'))
        ranged = False
        if _range_cap:
            _dur = info.get('duration')
            ranged = not _dur or float(_dur) > max(3 * _range_cap, _range_cap + 2700)
        if (on_audio and not _early["started"] and info.get('formats') and not ranged and not (_proxy and proxy == _proxy)):
            _early["started"] = True
            threading.Thread(target=_early_audio, args=(info, extractor_args, proxy, cookies), daemon=True).start()
        
        expected = os.path.join(output_dir, f'{sanitized}.mp4')
        if os.path.exists(expected):
            os.remove(expected)
        
        dl_opts = {
            **_base_opts(extractor_args, proxy, cookies),
            'format': fmt,
            'outtmpl': os.path.join(output_dir, f'{sanitized}.%(ext)s'),
            'merge_output_format': 'mp4' if has_ffmpeg else None,
            'overwrites': True,
            'progress_hooks': [_progress_hook],
        }
        if ranged:
            from yt_dlp.utils import download_range_func
            dl_opts['download_ranges'] = download_range_func(None, [(0, _range_cap)])
        
        with yt_dlp.YoutubeDL(dl_opts) as ydl:
            if info.get('_type', 'video') == 'video' and info.get('formats'):
                ydl.process_ie_result(info, download=True)
            else:
                ydl.download([url])
        return sanitized

    _direct_first = (os.environ.get("DIRECT_FIRST", "").strip() == "1" and (_proxy or _statics) and hd_args and cookies_path)
    _skip_statics = os.environ.get("DOWNLOAD_SKIP_STATICS", "").strip() == "1"

    attempts = [
        (label,
         fallback_args if label.startswith('fallback') else hd_args,
         _hd_fmt_for(capped),
         proxy,
         not (label.startswith('fallback') and hd_args))
        for label, capped, proxy in plan_download_attempts(
            _direct_first, _statics, _proxy, bool(hd_args), youtube=is_youtube_url(url),
            skip_statics=_skip_statics)
    ]

    sanitized_title = None
    last_err = None
    attempt_log = []
    
    for label, ea, fmt, proxy, cookies in attempts:
        for retry in range(2):
            try:
                sanitized_title = _attempt(ea, fmt, proxy, cookies)
                used_proxy = proxy is not None and proxy == _proxy
                attempt_log.append({"label": label, "ok": True, "bytes": _dl_bytes["total"] + _dl_bytes["partial"], "paid": used_proxy})
                break
            except Exception as e:
                last_err = e
                attempt_log.append({"label": label, "ok": False, "bytes": _dl_bytes["total"] + _dl_bytes["partial"], "paid": proxy is not None and proxy == _proxy, "error": str(e)[:300]})
                retryable = '403' in str(e) or 'Forbidden' in str(e)
                if not retryable or retry == 1:
                    break
                time.sleep(3)
        if sanitized_title is not None:
            break
        if last_err is not None and _content_block(str(last_err)):
            break

    if sanitized_title is None and last_err is not None and _content_block(str(last_err)):
        raise last_err

    if sanitized_title is None:
        raise last_err

    downloaded_file = os.path.join(output_dir, f'{sanitized_title}.mp4')
    if not os.path.exists(downloaded_file):
        for f in os.listdir(output_dir):
            if f.startswith(sanitized_title) and f.endswith('.mp4'):
                downloaded_file = os.path.join(output_dir, f)
                break

    return downloaded_file, sanitized_title


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


def render_clip(input_video, final_output_video, output_format="auto",
                force_strategy=None, crop_overrides=None, watermark=False):
    if output_format == "horizontal":
        ok = finalize_clip_passthrough(input_video, final_output_video)
        return ok
    aspect = 1.0 if output_format == "square" else ASPECT_RATIO
    return process_video_to_vertical(input_video, final_output_video, aspect_ratio=aspect,
                                     force_strategy=force_strategy,
                                     crop_overrides=crop_overrides,
                                     watermark=watermark)


def process_video_to_vertical(input_video, final_output_video, aspect_ratio=ASPECT_RATIO,
                              force_strategy=None, crop_overrides=None, watermark=False):
    if os.environ.get("REFRAME_ENGINE", "v2").strip().lower() != "v1":
        try:
            import reframe_v2
            result = reframe_v2.render(input_video, final_output_video, aspect_ratio,
                                       force_strategy=force_strategy,
                                       crop_overrides=crop_overrides,
                                       watermark=watermark)
            return result
        except Exception:
            pass

    stem = os.path.splitext(final_output_video)[0]
    silent_video_path = stem + ".v1video.mp4"
    audio_track_path = stem + ".v1audio.aac"
    for stale in (silent_video_path, audio_track_path, final_output_video):
        if os.path.isfile(stale):
            os.remove(stale)

    scenes, fps = detect_scenes(input_video)
    if not scenes:
        probe = cv2.VideoCapture(input_video)
        span = int(probe.get(cv2.CAP_PROP_FRAME_COUNT))
        probe.release()
        from scenedetect import FrameTimecode
        scenes = [(FrameTimecode(0, fps), FrameTimecode(span, fps))]

    original_width, original_height = get_video_resolution(input_video)
    from reframe_v2 import delivery_size
    OUTPUT_WIDTH, OUTPUT_HEIGHT = delivery_size(original_width, original_height, aspect_ratio)

    cameraman = SmoothedCameraman(OUTPUT_WIDTH, OUTPUT_HEIGHT, original_width, original_height, aspect_ratio=aspect_ratio)
    scene_strategies = analyze_scenes_strategy(input_video, scenes)
    
    encoder = subprocess.Popen(
        ['ffmpeg', '-y',
         '-f', 'rawvideo', '-pix_fmt', 'bgr24',
         '-video_size', f'{OUTPUT_WIDTH}x{OUTPUT_HEIGHT}',
         '-framerate', str(fps), '-i', 'pipe:0',
         *video_encode_args(QUALITY_FAST), '-an', silent_video_path],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    reader = cv2.VideoCapture(input_video)
    frame_total = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0
    current_scene_index = 0
    
    scene_boundaries = []
    for s_start, s_end in scenes:
        scene_boundaries.append((s_start.get_frames(), s_end.get_frames()))

    speaker_tracker = SpeakerTracker(cooldown_frames=30)

    while reader.isOpened():
        ret, frame = reader.read()
        if not ret:
            break

        if current_scene_index < len(scene_boundaries):
            start_f, end_f = scene_boundaries[current_scene_index]
            if frame_number >= end_f and current_scene_index < len(scene_boundaries) - 1:
                current_scene_index += 1
        
        current_strategy = scene_strategies[current_scene_index] if current_scene_index < len(scene_strategies) else 'TRACK'
        
        if current_strategy == 'GENERAL':
            output_frame = create_general_frame(frame, OUTPUT_WIDTH, OUTPUT_HEIGHT)
            cameraman.current_center_x = original_width / 2
            cameraman.target_center_x = original_width / 2
        else:
            is_scene_start = (frame_number == scene_boundaries[current_scene_index][0])
            if is_scene_start and SCENE_CUT_RESET:
                speaker_tracker.reset()
                cameraman.begin_scene()

            if frame_number % DETECT_STRIDE == 0 or (is_scene_start and SCENE_CUT_RESET):
                candidates = detect_face_candidates(frame)
                target_box = speaker_tracker.get_target(candidates, frame_number, original_width)
                if target_box:
                    cameraman.update_target(target_box)
                elif frame_number % YOLO_FALLBACK_STRIDE == 0 or (is_scene_start and SCENE_CUT_RESET):
                    person_box = detect_person_yolo(frame)
                    if person_box:
                        cameraman.update_target(person_box)

            x1, y1, x2, y2 = cameraman.get_crop_box(force_snap=is_scene_start)
            if y2 > y1 and x2 > x1:
                cropped = frame[y1:y2, x1:x2]
                output_frame = cv2.resize(cropped, (OUTPUT_WIDTH, OUTPUT_HEIGHT), interpolation=cv2.INTER_LINEAR)
            else:
                output_frame = cv2.resize(frame, (OUTPUT_WIDTH, OUTPUT_HEIGHT), interpolation=cv2.INTER_LINEAR)

        encoder.stdin.write(output_frame.tobytes())
        frame_number += 1

    encoder.stdin.close()
    encoder.wait()
    reader.release()

    if encoder.returncode != 0:
        return False

    try:
        subprocess.run(
            ['ffmpeg', '-y', '-i', input_video, '-vn', '-c:a', 'copy', audio_track_path],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        pass

    mux = ['ffmpeg', '-y', '-i', silent_video_path]
    if os.path.exists(audio_track_path):
        mux += ['-i', audio_track_path]
    mux += ['-c', 'copy', *METADATA_SCRUB, '-movflags', '+faststart', final_output_video]
    try:
        subprocess.run(mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        return False

    for leftover in (silent_video_path, audio_track_path):
        if os.path.exists(leftover):
            os.remove(leftover)

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AutoCrop-Vertical with Viral Clip Detection.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input', type=str, help="Path to the input video file.")
    input_group.add_argument('-u', '--url', type=str, help="YouTube URL to download and process.")
    parser.add_argument('-o', '--output', type=str, help="Output directory or file.")
    parser.add_argument('--format', type=str, default="auto", choices=["auto", "vertical", "horizontal", "square"])
    args = parser.parse_args()

    if args.url:
        output_dir = args.output if (args.output and os.path.isdir(args.output)) else "."
        input_video, video_title = download_youtube_video(args.url, output_dir)
    else:
        input_video = args.input
        video_title = os.path.splitext(os.path.basename(input_video))[0]

    print(f"Pipeline ready for processing: {video_title} at {input_video}")
