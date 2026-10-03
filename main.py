2026-10-03T16:46:26.8697222Z Current runner version: '2.337.0'
2026-10-03T16:46:26.8731655Z ##[group]Runner Image Provisioner
2026-10-03T16:46:26.8733106Z Hosted Compute Agent
2026-10-03T16:46:26.8734030Z Version: 20260901.588
2026-10-03T16:46:26.8735113Z Commit: f88ec8081b781fac6c440065ac7ff9e710ce3d0b
2026-10-03T16:46:26.8736354Z Build Date: 2026-09-01T19:56:44Z
2026-10-03T16:46:26.8737695Z Worker ID: {195055cd-77d7-4d97-81e8-9b948d0badfa}
2026-10-03T16:46:26.8739213Z Azure Region: eastus
2026-10-03T16:46:26.8740140Z ##[endgroup]
2026-10-03T16:46:26.8742575Z ##[group]Operating System
2026-10-03T16:46:26.8743593Z Ubuntu
2026-10-03T16:46:26.8744496Z 24.04.5
2026-10-03T16:46:26.8745586Z LTS
2026-10-03T16:46:26.8746460Z ##[endgroup]
2026-10-03T16:46:26.8747458Z ##[group]Runner Image
2026-10-03T16:46:26.8748699Z Image: ubuntu-24.04
2026-10-03T16:46:26.8750267Z Version: 20260927.320.1
2026-10-03T16:46:26.8752441Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260927.320/images/ubuntu/Ubuntu2404-Readme.md
2026-10-03T16:46:26.8755251Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260927.320
2026-10-03T16:46:26.8757011Z ##[endgroup]
2026-10-03T16:46:26.8759425Z ##[group]GITHUB_TOKEN Permissions
2026-10-03T16:46:26.8762318Z Contents: read
2026-10-03T16:46:26.8763427Z Metadata: read
2026-10-03T16:46:26.8764361Z Packages: read
2026-10-03T16:46:26.8765375Z ##[endgroup]
2026-10-03T16:46:26.8768598Z Secret source: Actions
2026-10-03T16:46:26.8770219Z Cache mode: write
2026-10-03T16:46:26.8771705Z Prepare workflow directory
2026-10-03T16:46:26.9246928Z Prepare all required actions
2026-10-03T16:46:26.9317714Z Getting action download info
2026-10-03T16:46:27.1777754Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-10-03T16:46:27.3007335Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-10-03T16:46:27.3821926Z Download action repository 'actions/setup-node@v4' (SHA:49933ea5288caeca8642d1e84afbd3f7d6820020)
2026-10-03T16:46:27.6107412Z Complete job name: run-pipeline
2026-10-03T16:46:27.6861468Z ##[group]Run actions/checkout@v4
2026-10-03T16:46:27.6862341Z with:
2026-10-03T16:46:27.6862821Z   repository: ThugLife8369/openshorts
2026-10-03T16:46:27.6866569Z   token: ***
2026-10-03T16:46:27.6867028Z   ssh-strict: true
2026-10-03T16:46:27.6867485Z   ssh-user: git
2026-10-03T16:46:27.6868145Z   persist-credentials: true
2026-10-03T16:46:27.6868659Z   clean: true
2026-10-03T16:46:27.6869123Z   sparse-checkout-cone-mode: true
2026-10-03T16:46:27.6869677Z   fetch-depth: 1
2026-10-03T16:46:27.6870143Z   fetch-tags: false
2026-10-03T16:46:27.6870613Z   show-progress: true
2026-10-03T16:46:27.6871069Z   lfs: false
2026-10-03T16:46:27.6871493Z   submodules: false
2026-10-03T16:46:27.6871950Z   set-safe-directory: true
2026-10-03T16:46:27.6872470Z   allow-unsafe-pr-checkout: false
2026-10-03T16:46:27.6873247Z ##[endgroup]
2026-10-03T16:46:27.7867109Z Syncing repository: ThugLife8369/openshorts
2026-10-03T16:46:27.7869543Z ##[group]Getting Git version info
2026-10-03T16:46:27.7870403Z Working directory is '/home/runner/work/openshorts/openshorts'
2026-10-03T16:46:27.7871532Z [command]/usr/bin/git version
2026-10-03T16:46:27.8005355Z git version 2.55.0
2026-10-03T16:46:27.8034727Z ##[endgroup]
2026-10-03T16:46:27.8053427Z Temporarily overriding HOME='/home/runner/work/_temp/9f427999-f24e-4b59-9dca-458100aa9eec' before making global git config changes
2026-10-03T16:46:27.8055812Z Adding repository directory to the temporary git global config as a safe directory
2026-10-03T16:46:27.8058797Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/openshorts/openshorts
2026-10-03T16:46:27.8129551Z Deleting the contents of '/home/runner/work/openshorts/openshorts'
2026-10-03T16:46:27.8132078Z ##[group]Initializing the repository
2026-10-03T16:46:27.8133597Z [command]/usr/bin/git init /home/runner/work/openshorts/openshorts
2026-10-03T16:46:27.8263078Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-10-03T16:46:27.8265426Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-10-03T16:46:27.8266540Z hint: to use in all of your new repositories, which will suppress this warning,
2026-10-03T16:46:27.8267604Z hint: call:
2026-10-03T16:46:27.8268357Z hint:
2026-10-03T16:46:27.8269510Z hint: 	git config --global init.defaultBranch <name>
2026-10-03T16:46:27.8270633Z hint:
2026-10-03T16:46:27.8271627Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-10-03T16:46:27.8273301Z hint: 'development'. The just-created branch can be renamed via this command:
2026-10-03T16:46:27.8274733Z hint:
2026-10-03T16:46:27.8275561Z hint: 	git branch -m <name>
2026-10-03T16:46:27.8276506Z hint:
2026-10-03T16:46:27.8277825Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-10-03T16:46:27.8280003Z Initialized empty Git repository in /home/runner/work/openshorts/openshorts/.git/
2026-10-03T16:46:27.8290561Z [command]/usr/bin/git remote add origin https://github.com/ThugLife8369/openshorts
2026-10-03T16:46:27.8352649Z ##[endgroup]
2026-10-03T16:46:27.8354371Z ##[group]Disabling automatic garbage collection
2026-10-03T16:46:27.8357415Z [command]/usr/bin/git config --local gc.auto 0
2026-10-03T16:46:27.8427729Z ##[endgroup]
2026-10-03T16:46:27.8429693Z ##[group]Setting up auth
2026-10-03T16:46:27.8432216Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-10-03T16:46:27.8460612Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-10-03T16:46:27.8891223Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-03T16:46:27.8953201Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-10-03T16:46:27.9226550Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-03T16:46:27.9257584Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-03T16:46:27.9495271Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-10-03T16:46:27.9537781Z ##[endgroup]
2026-10-03T16:46:27.9539591Z ##[group]Fetching the repository
2026-10-03T16:46:27.9549549Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +633d6ed4d697f9cf4fcda08c20aa9a66ee2ce0e7:refs/remotes/origin/main
2026-10-03T16:46:29.3915342Z From https://github.com/ThugLife8369/openshorts
2026-10-03T16:46:29.3917470Z  * [new ref]         633d6ed4d697f9cf4fcda08c20aa9a66ee2ce0e7 -> origin/main
2026-10-03T16:46:29.3921405Z ##[endgroup]
2026-10-03T16:46:29.3923187Z ##[group]Determining the checkout info
2026-10-03T16:46:29.3925290Z ##[endgroup]
2026-10-03T16:46:29.3930548Z [command]/usr/bin/git sparse-checkout disable
2026-10-03T16:46:29.3988272Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-10-03T16:46:29.4025483Z ##[group]Checking out the ref
2026-10-03T16:46:29.4030166Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-10-03T16:46:29.7804435Z Switched to a new branch 'main'
2026-10-03T16:46:29.7811395Z branch 'main' set up to track 'origin/main'.
2026-10-03T16:46:29.7830586Z ##[endgroup]
2026-10-03T16:46:29.7880542Z [command]/usr/bin/git log -1 --format=%H
2026-10-03T16:46:29.7907057Z 633d6ed4d697f9cf4fcda08c20aa9a66ee2ce0e7
2026-10-03T16:46:29.8195811Z ##[group]Run actions/setup-python@v5
2026-10-03T16:46:29.8196264Z with:
2026-10-03T16:46:29.8196562Z   python-version: 3.11
2026-10-03T16:46:29.8196898Z   check-latest: false
2026-10-03T16:46:29.8200167Z   token: ***
2026-10-03T16:46:29.8200726Z   update-environment: true
2026-10-03T16:46:29.8201103Z   allow-prereleases: false
2026-10-03T16:46:29.8201445Z   freethreaded: false
2026-10-03T16:46:29.8201759Z ##[endgroup]
2026-10-03T16:46:29.9626400Z ##[group]Installed versions
2026-10-03T16:46:29.9712263Z (node:2274) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-10-03T16:46:29.9713376Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-10-03T16:46:29.9714376Z Successfully set up CPython (3.11.16)
2026-10-03T16:46:29.9715438Z ##[endgroup]
2026-10-03T16:46:29.9965243Z ##[group]Run actions/setup-node@v4
2026-10-03T16:46:29.9965940Z with:
2026-10-03T16:46:29.9966477Z   node-version: 20
2026-10-03T16:46:29.9967008Z   always-auth: false
2026-10-03T16:46:29.9967550Z   check-latest: false
2026-10-03T16:46:29.9973691Z   token: ***
2026-10-03T16:46:29.9974192Z env:
2026-10-03T16:46:29.9974817Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:29.9975859Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-03T16:46:29.9976851Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:29.9977735Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:29.9978809Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:29.9979716Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-03T16:46:29.9980482Z ##[endgroup]
2026-10-03T16:46:30.1641474Z Attempting to download 20...
2026-10-03T16:46:30.1746806Z (node:2282) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-10-03T16:46:30.1748344Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-10-03T16:46:30.6808899Z Acquiring 20.20.2 - x64 from https://github.com/actions/node-versions/releases/download/20.20.2-23521894959/node-20.20.2-linux-x64.tar.gz
2026-10-03T16:46:31.0588833Z Extracting ...
2026-10-03T16:46:31.0787482Z [command]/usr/bin/tar xz --strip 1 --warning=no-unknown-keyword --overwrite -C /home/runner/work/_temp/fe990e6d-13ec-46ba-b70e-01d82db756fb -f /home/runner/work/_temp/068fca6c-a3db-436b-910e-0fecc1c47b59
2026-10-03T16:46:32.0941347Z Adding to the cache ...
2026-10-03T16:46:34.1353540Z ##[group]Environment details
2026-10-03T16:46:34.4703937Z node: v20.20.2
2026-10-03T16:46:34.4704436Z npm: 10.8.2
2026-10-03T16:46:34.4704795Z yarn: 1.22.22
2026-10-03T16:46:34.4705468Z ##[endgroup]
2026-10-03T16:46:34.4890428Z ##[group]Run sudo apt-get update
2026-10-03T16:46:34.4890803Z [36;1msudo apt-get update[0m
2026-10-03T16:46:34.4891099Z [36;1msudo apt-get install -y ffmpeg[0m
2026-10-03T16:46:34.5321670Z shell: /usr/bin/bash -e {0}
2026-10-03T16:46:34.5321993Z env:
2026-10-03T16:46:34.5322336Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:34.5322919Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-03T16:46:34.5323465Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:34.5323961Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:34.5324447Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:46:34.5324926Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-03T16:46:34.5325335Z ##[endgroup]
2026-10-03T16:46:34.6820614Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-10-03T16:46:34.6959121Z Get:6 https://packages.microsoft.com/ubuntu/24.04/prod noble InRelease [3600 B]
2026-10-03T16:46:34.7183132Z Hit:2 http://azure.archive.ubuntu.com/ubuntu noble InRelease
2026-10-03T16:46:34.7195375Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
2026-10-03T16:46:34.7262087Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
2026-10-03T16:46:34.7322762Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble-security InRelease [126 kB]
2026-10-03T16:46:34.8139229Z Get:7 https://packages.microsoft.com/ubuntu/24.04/prod noble/main arm64 Packages [458 kB]
2026-10-03T16:46:34.8330589Z Get:8 https://packages.microsoft.com/ubuntu/24.04/prod noble/main amd64 Packages [511 kB]
2026-10-03T16:46:34.8375567Z Get:9 https://packages.microsoft.com/ubuntu/24.04/prod noble/main armhf Packages [12.6 kB]
2026-10-03T16:46:34.9302957Z Get:10 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1364 kB]
2026-10-03T16:46:34.9375705Z Get:11 http://azure.archive.ubuntu.com/ubuntu noble-updates/main Translation-en [304 kB]
2026-10-03T16:46:34.9392813Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [181 kB]
2026-10-03T16:46:34.9411130Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1699 kB]
2026-10-03T16:46:34.9488678Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe Translation-en [341 kB]
2026-10-03T16:46:34.9510621Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [388 kB]
2026-10-03T16:46:34.9533073Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [1720 kB]
2026-10-03T16:46:34.9611178Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [394 kB]
2026-10-03T16:46:34.9636269Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
2026-10-03T16:46:34.9986056Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [5736 B]
2026-10-03T16:46:35.0433214Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [12.6 kB]
2026-10-03T16:46:35.0600874Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Packages [1069 kB]
2026-10-03T16:46:35.0665204Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble-security/main Translation-en [221 kB]
2026-10-03T16:46:35.0685055Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble-security/main amd64 Components [46.5 kB]
2026-10-03T16:46:35.0693479Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Packages [1216 kB]
2026-10-03T16:46:35.0791065Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble-security/universe Translation-en [244 kB]
2026-10-03T16:46:35.0814626Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-security/universe amd64 Components [76.3 kB]
2026-10-03T16:46:35.0820446Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [1566 kB]
2026-10-03T16:46:35.0925056Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble-security/restricted Translation-en [361 kB]
2026-10-03T16:46:42.9552965Z Fetched 12.6 MB in 1s (8931 kB/s)
2026-10-03T16:46:43.7797433Z Reading package lists...
2026-10-03T16:46:43.8120938Z Reading package lists...
2026-10-03T16:46:44.0043057Z Building dependency tree...
2026-10-03T16:46:44.0052079Z Reading state information...
2026-10-03T16:46:44.1435155Z The following additional packages will be installed:
2026-10-03T16:46:44.1436296Z   i965-va-driver intel-media-va-driver libaacs0 libass9 libasyncns0
2026-10-03T16:46:44.1437603Z   libavc1394-0 libavcodec60 libavdevice60 libavfilter9 libavformat60
2026-10-03T16:46:44.1439115Z   libavutil58 libbdplus0 libblas3 libbluray2 libbs2b0 libcaca0
2026-10-03T16:46:44.1440451Z   libcdio-cdda2t64 libcdio-paranoia2t64 libcdio19t64 libchromaprint1 libcjson1
2026-10-03T16:46:44.1441774Z   libcodec2-1.2 libdav1d7 libdc1394-25 libdecor-0-0 libdecor-0-plugin-1-gtk
2026-10-03T16:46:44.1443143Z   libflac12t64 libflite1 libgbm1 libgl1-mesa-dri libglx-mesa0 libgme0 libgsm1
2026-10-03T16:46:44.1444338Z   libhwy1t64 libiec61883-0 libigdgmm12 libjack-jackd2-0 libjxl0.7 liblapack3
2026-10-03T16:46:44.1445547Z   liblilv-0-0 libmbedcrypto7t64 libmp3lame0 libmpg123-0t64 libmysofa1
2026-10-03T16:46:44.1446735Z   libopenal-data libopenal1 libopenmpt0t64 libopus0 libplacebo338
2026-10-03T16:46:44.1448251Z   libpocketsphinx3 libpostproc57 libpulse0 librav1e0 libraw1394-11 librist4
2026-10-03T16:46:44.1449609Z   librsvg2-2 librsvg2-common librubberband2 libsamplerate0 libsdl2-2.0-0
2026-10-03T16:46:44.1451371Z   libserd-0-0 libshine3 libsndfile1 libsndio7.0 libsord-0-0 libsoxr0 libspeex1
2026-10-03T16:46:44.1452687Z   libsphinxbase3t64 libsratom-0-0 libsrt1.5-gnutls libssh-gcrypt-4
2026-10-03T16:46:44.1453816Z   libsvtav1enc1d1 libswresample4 libswscale7 libtheora0 libtwolame0
2026-10-03T16:46:44.1454762Z   libudfread0 libunibreak5 libva-drm2 libva-x11-2 libva2 libvdpau1
2026-10-03T16:46:44.1455737Z   libvidstab1.1 libvorbisenc2 libvpl2 libvpx9 libx264-164 libx265-199
2026-10-03T16:46:44.1456710Z   libxcb-shape0 libxv1 libxvidcore4 libzimg2 libzix-0-0 libzvbi-common
2026-10-03T16:46:44.1457647Z   libzvbi0t64 mesa-libgallium mesa-va-drivers mesa-vdpau-drivers
2026-10-03T16:46:44.1458965Z   ocl-icd-libopencl1 pocketsphinx-en-us va-driver-all vdpau-driver-all
2026-10-03T16:46:44.1459731Z Suggested packages:
2026-10-03T16:46:44.1460452Z   ffmpeg-doc i965-va-driver-shaders libcuda1 libnvcuvid1 libnvidia-encode1
2026-10-03T16:46:44.1461528Z   libbluray-bdj jackd2 libportaudio2 opus-tools pulseaudio libraw1394-doc
2026-10-03T16:46:44.1462647Z   librsvg2-bin serdi sndiod sordi speex opencl-icd libvdpau-va-gl1
2026-10-03T16:46:44.2159999Z The following NEW packages will be installed:
2026-10-03T16:46:44.2161002Z   ffmpeg i965-va-driver intel-media-va-driver libaacs0 libass9 libasyncns0
2026-10-03T16:46:44.2161964Z   libavc1394-0 libavcodec60 libavdevice60 libavfilter9 libavformat60
2026-10-03T16:46:44.2162830Z   libavutil58 libbdplus0 libblas3 libbluray2 libbs2b0 libcaca0
2026-10-03T16:46:44.2163815Z   libcdio-cdda2t64 libcdio-paranoia2t64 libcdio19t64 libchromaprint1 libcjson1
2026-10-03T16:46:44.2164851Z   libcodec2-1.2 libdav1d7 libdc1394-25 libdecor-0-0 libdecor-0-plugin-1-gtk
2026-10-03T16:46:44.2165844Z   libflac12t64 libflite1 libgme0 libgsm1 libhwy1t64 libiec61883-0 libigdgmm12
2026-10-03T16:46:44.2167042Z   libjack-jackd2-0 libjxl0.7 liblapack3 liblilv-0-0 libmbedcrypto7t64
2026-10-03T16:46:44.2168142Z   libmp3lame0 libmpg123-0t64 libmysofa1 libopenal-data libopenal1
2026-10-03T16:46:44.2169211Z   libopenmpt0t64 libopus0 libplacebo338 libpocketsphinx3 libpostproc57
2026-10-03T16:46:44.2170207Z   libpulse0 librav1e0 libraw1394-11 librist4 librsvg2-2 librsvg2-common
2026-10-03T16:46:44.2171164Z   librubberband2 libsamplerate0 libsdl2-2.0-0 libserd-0-0 libshine3
2026-10-03T16:46:44.2172152Z   libsndfile1 libsndio7.0 libsord-0-0 libsoxr0 libspeex1 libsphinxbase3t64
2026-10-03T16:46:44.2173118Z   libsratom-0-0 libsrt1.5-gnutls libssh-gcrypt-4 libsvtav1enc1d1
2026-10-03T16:46:44.2174675Z   libswresample4 libswscale7 libtheora0 libtwolame0 libudfread0 libunibreak5
2026-10-03T16:46:44.2175814Z   libva-drm2 libva-x11-2 libva2 libvdpau1 libvidstab1.1 libvorbisenc2 libvpl2
2026-10-03T16:46:44.2176847Z   libvpx9 libx264-164 libx265-199 libxcb-shape0 libxv1 libxvidcore4 libzimg2
2026-10-03T16:46:44.2177866Z   libzix-0-0 libzvbi-common libzvbi0t64 mesa-va-drivers mesa-vdpau-drivers
2026-10-03T16:46:44.2179099Z   ocl-icd-libopencl1 pocketsphinx-en-us va-driver-all vdpau-driver-all
2026-10-03T16:46:44.2198890Z The following packages will be upgraded:
2026-10-03T16:46:44.2199844Z   libgbm1 libgl1-mesa-dri libglx-mesa0 mesa-libgallium
2026-10-03T16:46:44.2393289Z 4 upgraded, 99 newly installed, 0 to remove and 21 not upgraded.
2026-10-03T16:46:44.2394080Z Need to get 105 MB of archives.
2026-10-03T16:46:44.2394843Z After this operation, 227 MB of additional disk space will be used.
2026-10-03T16:46:44.2395745Z Get:1 file:/etc/apt/apt-mirrors.txt Mirrorlist [144 B]
2026-10-03T16:46:44.2717371Z Get:2 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libva2 amd64 2.20.0-2ubuntu0.2 [66.4 kB]
2026-10-03T16:46:44.2872165Z Get:3 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libva-drm2 amd64 2.20.0-2ubuntu0.2 [7124 B]
2026-10-03T16:46:44.3015663Z Get:4 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libva-x11-2 amd64 2.20.0-2ubuntu0.2 [12.0 kB]
2026-10-03T16:46:44.3160266Z Get:5 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libvdpau1 amd64 1.5-2build1 [27.8 kB]
2026-10-03T16:46:44.3306971Z Get:6 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libvpl2 amd64 2023.3.0-1build1 [99.8 kB]
2026-10-03T16:46:44.3457012Z Get:7 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ocl-icd-libopencl1 amd64 2.3.2-1build1 [38.5 kB]
2026-10-03T16:46:44.3602638Z Get:8 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libavutil58 amd64 7:6.1.1-3ubuntu5 [401 kB]
2026-10-03T16:46:44.3776536Z Get:9 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcodec2-1.2 amd64 1.2.0-2build1 [8998 kB]
2026-10-03T16:46:44.4532450Z Get:10 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libdav1d7 amd64 1.4.1-1build1 [604 kB]
2026-10-03T16:46:44.4709529Z Get:11 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgsm1 amd64 1.0.22-1build1 [27.8 kB]
2026-10-03T16:46:44.4867269Z Get:12 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libhwy1t64 amd64 1.0.7-8.1build1 [584 kB]
2026-10-03T16:46:44.5045400Z Get:13 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libjxl0.7 amd64 0.7.0-10.2ubuntu6.1 [1001 kB]
2026-10-03T16:46:44.5247175Z Get:14 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libmp3lame0 amd64 3.100-6build1 [142 kB]
2026-10-03T16:46:44.5409664Z Get:15 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libopus0 amd64 1.4-1build1 [208 kB]
2026-10-03T16:46:44.5559270Z Get:16 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 librav1e0 amd64 0.7.1-2 [1022 kB]
2026-10-03T16:46:44.5775434Z Get:17 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 librsvg2-2 amd64 2.58.0+dfsg-1build1 [2135 kB]
2026-10-03T16:46:44.6216386Z Get:18 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libshine3 amd64 3.1.1-2build1 [23.2 kB]
2026-10-03T16:46:44.6363779Z Get:19 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libspeex1 amd64 1.2.1-2ubuntu2.24.04.1 [59.6 kB]
2026-10-03T16:46:44.6936556Z Get:20 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsvtav1enc1d1 amd64 1.7.0+dfsg-2build1 [2425 kB]
2026-10-03T16:46:44.7270744Z Get:21 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsoxr0 amd64 0.1.3-4build3 [80.0 kB]
2026-10-03T16:46:44.7421423Z Get:22 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libswresample4 amd64 7:6.1.1-3ubuntu5 [63.8 kB]
2026-10-03T16:46:44.7570393Z Get:23 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libtheora0 amd64 1.1.1+dfsg.1-16.1build3 [211 kB]
2026-10-03T16:46:44.7724532Z Get:24 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libtwolame0 amd64 0.4.0-2build3 [52.3 kB]
2026-10-03T16:46:44.7870746Z Get:25 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libvorbisenc2 amd64 1.3.7-1build3 [80.8 kB]
2026-10-03T16:46:44.8019155Z Get:26 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libvpx9 amd64 1.14.0-1ubuntu2.3 [1143 kB]
2026-10-03T16:46:44.8229436Z Get:27 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libx264-164 amd64 2:0.164.3108+git31e19f9-1 [604 kB]
2026-10-03T16:46:44.8496330Z Get:28 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libx265-199 amd64 3.5-2build1 [1226 kB]
2026-10-03T16:46:44.8811729Z Get:29 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libxvidcore4 amd64 2:1.3.7-1build1 [219 kB]
2026-10-03T16:46:44.8970318Z Get:30 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libzvbi-common all 0.2.42-2 [42.4 kB]
2026-10-03T16:46:44.9119576Z Get:31 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libzvbi0t64 amd64 0.2.42-2 [261 kB]
2026-10-03T16:46:44.9282249Z Get:32 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libavcodec60 amd64 7:6.1.1-3ubuntu5 [5851 kB]
2026-10-03T16:46:44.9765358Z Get:33 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libraw1394-11 amd64 2.1.2-2build3 [26.2 kB]
2026-10-03T16:46:44.9908954Z Get:34 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libavc1394-0 amd64 0.5.4-5build3 [15.4 kB]
2026-10-03T16:46:45.0069994Z Get:35 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libunibreak5 amd64 5.1-2build1 [25.0 kB]
2026-10-03T16:46:45.0213267Z Get:36 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libass9 amd64 1:0.17.1-2build1 [104 kB]
2026-10-03T16:46:45.0364837Z Get:37 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libudfread0 amd64 1.1.2-1build1 [19.0 kB]
2026-10-03T16:46:45.0509834Z Get:38 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libbluray2 amd64 1:1.3.4-1build1 [159 kB]
2026-10-03T16:46:45.1087258Z Get:39 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libchromaprint1 amd64 1.5.1-5 [30.5 kB]
2026-10-03T16:46:45.1232187Z Get:40 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libgme0 amd64 0.6.3-7build1 [134 kB]
2026-10-03T16:46:45.1384703Z Get:41 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libmpg123-0t64 amd64 1.32.5-1ubuntu1.1 [169 kB]
2026-10-03T16:46:45.1539344Z Get:42 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libopenmpt0t64 amd64 0.7.3-1.1build3 [647 kB]
2026-10-03T16:46:45.1716632Z Get:43 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libcjson1 amd64 1.7.17-1 [24.8 kB]
2026-10-03T16:46:45.1861923Z Get:44 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmbedcrypto7t64 amd64 2.28.8-1 [209 kB]
2026-10-03T16:46:45.2017165Z Get:45 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 librist4 amd64 0.2.10+dfsg-2 [74.9 kB]
2026-10-03T16:46:45.2166345Z Get:46 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsrt1.5-gnutls amd64 1.5.3-1build2 [316 kB]
2026-10-03T16:46:45.2877624Z Get:47 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libssh-gcrypt-4 amd64 0.10.6-2ubuntu0.5 [226 kB]
2026-10-03T16:46:45.3081371Z Get:48 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libavformat60 amd64 7:6.1.1-3ubuntu5 [1153 kB]
2026-10-03T16:46:45.3539595Z Get:49 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libbs2b0 amd64 3.1.0+dfsg-7build1 [10.6 kB]
2026-10-03T16:46:45.3690578Z Get:50 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libflite1 amd64 2.2-6build3 [13.6 MB]
2026-10-03T16:46:45.4755732Z Get:51 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libserd-0-0 amd64 0.32.2-1 [43.6 kB]
2026-10-03T16:46:45.4903020Z Get:52 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libzix-0-0 amd64 0.4.2-2build1 [23.6 kB]
2026-10-03T16:46:45.5049132Z Get:53 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsord-0-0 amd64 0.16.16-2build1 [15.8 kB]
2026-10-03T16:46:45.5194523Z Get:54 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsratom-0-0 amd64 0.6.16-1build1 [17.3 kB]
2026-10-03T16:46:45.5339867Z Get:55 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 liblilv-0-0 amd64 0.24.22-1build1 [41.0 kB]
2026-10-03T16:46:45.5487190Z Get:56 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libmysofa1 amd64 1.3.2+dfsg-2ubuntu2 [1158 kB]
2026-10-03T16:46:45.5701817Z Get:57 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libplacebo338 amd64 6.338.2-2build1 [2654 kB]
2026-10-03T16:46:45.6450835Z Get:58 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libblas3 amd64 3.12.0-3build1.1 [238 kB]
2026-10-03T16:46:45.6615750Z Get:59 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 liblapack3 amd64 3.12.0-3build1.1 [2646 kB]
2026-10-03T16:46:45.6915050Z Get:60 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libasyncns0 amd64 0.8-6build4 [11.3 kB]
2026-10-03T16:46:45.7058512Z Get:61 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libflac12t64 amd64 1.4.3+ds-2.1ubuntu2 [197 kB]
2026-10-03T16:46:45.7216783Z Get:62 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libsndfile1 amd64 1.2.2-1ubuntu5.24.04.1 [209 kB]
2026-10-03T16:46:45.7373949Z Get:63 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libpulse0 amd64 1:16.1+dfsg1-2ubuntu10.1 [292 kB]
2026-10-03T16:46:45.7537734Z Get:64 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsphinxbase3t64 amd64 0.8+5prealpha+1-17build2 [126 kB]
2026-10-03T16:46:45.7689226Z Get:65 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libpocketsphinx3 amd64 0.8.0+real5prealpha+1-15ubuntu5 [133 kB]
2026-10-03T16:46:45.7840791Z Get:66 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libpostproc57 amd64 7:6.1.1-3ubuntu5 [49.9 kB]
2026-10-03T16:46:45.7987048Z Get:67 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libsamplerate0 amd64 0.2.2-4build1 [1344 kB]
2026-10-03T16:46:45.8203233Z Get:68 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 librubberband2 amd64 3.3.0+dfsg-2build1 [130 kB]
2026-10-03T16:46:45.8353494Z Get:69 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libswscale7 amd64 7:6.1.1-3ubuntu5 [193 kB]
2026-10-03T16:46:45.8506897Z Get:70 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libvidstab1.1 amd64 1.1.0-2build1 [38.5 kB]
2026-10-03T16:46:45.8653822Z Get:71 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libzimg2 amd64 3.0.5+ds1-1build1 [254 kB]
2026-10-03T16:46:45.8810376Z Get:72 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libavfilter9 amd64 7:6.1.1-3ubuntu5 [4235 kB]
2026-10-03T16:46:45.9172839Z Get:73 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libcaca0 amd64 0.99.beta20-4ubuntu0.2 [209 kB]
2026-10-03T16:46:45.9326836Z Get:74 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libcdio19t64 amd64 2.1.0-4.1ubuntu1.2 [62.4 kB]
2026-10-03T16:46:45.9475404Z Get:75 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libcdio-cdda2t64 amd64 10.2+2.0.1-1.1build2 [16.5 kB]
2026-10-03T16:46:46.0046731Z Get:76 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libcdio-paranoia2t64 amd64 10.2+2.0.1-1.1build2 [16.6 kB]
2026-10-03T16:46:46.0191471Z Get:77 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libdc1394-25 amd64 2.2.6-4build1 [90.1 kB]
2026-10-03T16:46:46.0340914Z Get:78 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libiec61883-0 amd64 1.2.0-6build1 [24.5 kB]
2026-10-03T16:46:46.0484113Z Get:79 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libjack-jackd2-0 amd64 1.9.21~dfsg-3ubuntu3 [289 kB]
2026-10-03T16:46:46.0641879Z Get:80 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libopenal-data all 1:1.23.1-4build1 [161 kB]
2026-10-03T16:46:46.0793479Z Get:81 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libsndio7.0 amd64 1.9.0-0.3build3 [29.6 kB]
2026-10-03T16:46:46.0935210Z Get:82 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libopenal1 amd64 1:1.23.1-4build1 [540 kB]
2026-10-03T16:46:46.1103633Z Get:83 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libdecor-0-0 amd64 0.2.2-1build2 [16.5 kB]
2026-10-03T16:46:46.1244907Z Get:84 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libgl1-mesa-dri amd64 25.2.8-0ubuntu0.24.04.4 [38.0 kB]
2026-10-03T16:46:46.1389156Z Get:85 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libglx-mesa0 amd64 25.2.8-0ubuntu0.24.04.4 [110 kB]
2026-10-03T16:46:46.1537276Z Get:86 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libgbm1 amd64 25.2.8-0ubuntu0.24.04.4 [34.2 kB]
2026-10-03T16:46:46.1681780Z Get:87 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 mesa-libgallium amd64 25.2.8-0ubuntu0.24.04.4 [10.8 MB]
2026-10-03T16:46:46.2410557Z Get:88 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 libsdl2-2.0-0 amd64 2.30.0+dfsg-1ubuntu3.1 [686 kB]
2026-10-03T16:46:46.2590151Z Get:89 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxcb-shape0 amd64 1.15-1ubuntu2 [6100 B]
2026-10-03T16:46:46.2767657Z Get:90 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libxv1 amd64 2:1.0.11-1.1build1 [10.7 kB]
2026-10-03T16:46:46.2913018Z Get:91 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libavdevice60 amd64 7:6.1.1-3ubuntu5 [82.3 kB]
2026-10-03T16:46:46.3060409Z Get:92 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 ffmpeg amd64 7:6.1.1-3ubuntu5 [1879 kB]
2026-10-03T16:46:46.3302132Z Get:93 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libigdgmm12 amd64 22.3.17+ds1-1ubuntu1 [145 kB]
2026-10-03T16:46:46.3449950Z Get:94 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 intel-media-va-driver amd64 24.1.0+dfsg1-1ubuntu0.2 [3163 kB]
2026-10-03T16:46:46.4248165Z Get:95 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libaacs0 amd64 0.11.1-2build1 [62.9 kB]
2026-10-03T16:46:46.4393514Z Get:96 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 libbdplus0 amd64 0.2.0-3build1 [52.2 kB]
2026-10-03T16:46:46.4541408Z Get:97 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 libdecor-0-plugin-1-gtk amd64 0.2.2-1build2 [22.2 kB]
2026-10-03T16:46:46.4683596Z Get:98 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 librsvg2-common amd64 2.58.0+dfsg-1build1 [11.8 kB]
2026-10-03T16:46:46.4826596Z Get:99 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 mesa-va-drivers amd64 25.2.8-0ubuntu0.24.04.4 [6778 B]
2026-10-03T16:46:46.4987398Z Get:100 http://azure.archive.ubuntu.com/ubuntu noble-updates/main amd64 mesa-vdpau-drivers amd64 25.2.8-0ubuntu0.24.04.4 [23.4 kB]
2026-10-03T16:46:46.5254147Z Get:101 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 i965-va-driver amd64 2.4.1+dfsg1-1ubuntu0.2 [332 kB]
2026-10-03T16:46:46.5846570Z Get:102 http://azure.archive.ubuntu.com/ubuntu noble-updates/universe amd64 va-driver-all amd64 2.20.0-2ubuntu0.2 [5014 B]
2026-10-03T16:46:46.6396905Z Ign:103 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 vdpau-driver-all amd64 1.5-2build1
2026-10-03T16:46:46.8458626Z Get:104 http://azure.archive.ubuntu.com/ubuntu noble/universe amd64 pocketsphinx-en-us all 0.8.0+real5prealpha+1-15ubuntu5 [27.4 MB]
2026-10-03T16:46:48.6161799Z Get:103 http://azure.archive.ubuntu.com/ubuntu noble/main amd64 vdpau-driver-all amd64 1.5-2build1 [4414 B]
2026-10-03T16:46:48.9727180Z Fetched 105 MB in 4s (23.9 MB/s)
2026-10-03T16:46:49.0180990Z Selecting previously unselected package libva2:amd64.
2026-10-03T16:46:49.0811373Z (Reading database ... 
2026-10-03T16:46:49.0811985Z (Reading database ... 5%
2026-10-03T16:46:49.0812368Z (Reading database ... 10%
2026-10-03T16:46:49.0812738Z (Reading database ... 15%
2026-10-03T16:46:49.0813096Z (Reading database ... 20%
2026-10-03T16:46:49.0813447Z (Reading database ... 25%
2026-10-03T16:46:49.0813806Z (Reading database ... 30%
2026-10-03T16:46:49.0814154Z (Reading database ... 35%
2026-10-03T16:46:49.0814549Z (Reading database ... 40%
2026-10-03T16:46:49.0815266Z (Reading database ... 45%
2026-10-03T16:46:49.0815663Z (Reading database ... 50%
2026-10-03T16:46:49.1131724Z (Reading database ... 55%
2026-10-03T16:46:49.5983670Z (Reading database ... 60%
2026-10-03T16:46:49.8869531Z (Reading database ... 65%
2026-10-03T16:46:50.1920870Z (Reading database ... 70%
2026-10-03T16:46:50.4944899Z (Reading database ... 75%
2026-10-03T16:46:50.8839470Z (Reading database ... 80%
2026-10-03T16:46:51.4166139Z (Reading database ... 85%
2026-10-03T16:46:52.0355062Z (Reading database ... 90%
2026-10-03T16:46:52.7160103Z (Reading database ... 95%
2026-10-03T16:46:52.7160841Z (Reading database ... 100%
2026-10-03T16:46:52.7161675Z (Reading database ... 202296 files and directories currently installed.)
2026-10-03T16:46:52.7206662Z Preparing to unpack .../000-libva2_2.20.0-2ubuntu0.2_amd64.deb ...
2026-10-03T16:46:52.7244265Z Unpacking libva2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:52.7505348Z Selecting previously unselected package libva-drm2:amd64.
2026-10-03T16:46:52.7636605Z Preparing to unpack .../001-libva-drm2_2.20.0-2ubuntu0.2_amd64.deb ...
2026-10-03T16:46:52.7644863Z Unpacking libva-drm2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:52.7895555Z Selecting previously unselected package libva-x11-2:amd64.
2026-10-03T16:46:52.8022816Z Preparing to unpack .../002-libva-x11-2_2.20.0-2ubuntu0.2_amd64.deb ...
2026-10-03T16:46:52.8030245Z Unpacking libva-x11-2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:52.8284610Z Selecting previously unselected package libvdpau1:amd64.
2026-10-03T16:46:52.8414867Z Preparing to unpack .../003-libvdpau1_1.5-2build1_amd64.deb ...
2026-10-03T16:46:52.8423605Z Unpacking libvdpau1:amd64 (1.5-2build1) ...
2026-10-03T16:46:52.8660542Z Selecting previously unselected package libvpl2.
2026-10-03T16:46:52.8792887Z Preparing to unpack .../004-libvpl2_2023.3.0-1build1_amd64.deb ...
2026-10-03T16:46:52.8801197Z Unpacking libvpl2 (2023.3.0-1build1) ...
2026-10-03T16:46:52.9035715Z Selecting previously unselected package ocl-icd-libopencl1:amd64.
2026-10-03T16:46:52.9164729Z Preparing to unpack .../005-ocl-icd-libopencl1_2.3.2-1build1_amd64.deb ...
2026-10-03T16:46:52.9173303Z Unpacking ocl-icd-libopencl1:amd64 (2.3.2-1build1) ...
2026-10-03T16:46:52.9536305Z Selecting previously unselected package libavutil58:amd64.
2026-10-03T16:46:52.9666304Z Preparing to unpack .../006-libavutil58_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:52.9680777Z Unpacking libavutil58:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:52.9939289Z Selecting previously unselected package libcodec2-1.2:amd64.
2026-10-03T16:46:53.0067019Z Preparing to unpack .../007-libcodec2-1.2_1.2.0-2build1_amd64.deb ...
2026-10-03T16:46:53.0075032Z Unpacking libcodec2-1.2:amd64 (1.2.0-2build1) ...
2026-10-03T16:46:53.0830088Z Selecting previously unselected package libdav1d7:amd64.
2026-10-03T16:46:53.0959121Z Preparing to unpack .../008-libdav1d7_1.4.1-1build1_amd64.deb ...
2026-10-03T16:46:53.0966547Z Unpacking libdav1d7:amd64 (1.4.1-1build1) ...
2026-10-03T16:46:53.1240710Z Selecting previously unselected package libgsm1:amd64.
2026-10-03T16:46:53.1369924Z Preparing to unpack .../009-libgsm1_1.0.22-1build1_amd64.deb ...
2026-10-03T16:46:53.1381770Z Unpacking libgsm1:amd64 (1.0.22-1build1) ...
2026-10-03T16:46:53.1616011Z Selecting previously unselected package libhwy1t64:amd64.
2026-10-03T16:46:53.1745872Z Preparing to unpack .../010-libhwy1t64_1.0.7-8.1build1_amd64.deb ...
2026-10-03T16:46:53.1754939Z Unpacking libhwy1t64:amd64 (1.0.7-8.1build1) ...
2026-10-03T16:46:53.2089651Z Selecting previously unselected package libjxl0.7:amd64.
2026-10-03T16:46:53.2218707Z Preparing to unpack .../011-libjxl0.7_0.7.0-10.2ubuntu6.1_amd64.deb ...
2026-10-03T16:46:53.2225908Z Unpacking libjxl0.7:amd64 (0.7.0-10.2ubuntu6.1) ...
2026-10-03T16:46:53.2578678Z Selecting previously unselected package libmp3lame0:amd64.
2026-10-03T16:46:53.2709793Z Preparing to unpack .../012-libmp3lame0_3.100-6build1_amd64.deb ...
2026-10-03T16:46:53.2719142Z Unpacking libmp3lame0:amd64 (3.100-6build1) ...
2026-10-03T16:46:53.2952654Z Selecting previously unselected package libopus0:amd64.
2026-10-03T16:46:53.3081940Z Preparing to unpack .../013-libopus0_1.4-1build1_amd64.deb ...
2026-10-03T16:46:53.3090770Z Unpacking libopus0:amd64 (1.4-1build1) ...
2026-10-03T16:46:53.3333117Z Selecting previously unselected package librav1e0:amd64.
2026-10-03T16:46:53.3462703Z Preparing to unpack .../014-librav1e0_0.7.1-2_amd64.deb ...
2026-10-03T16:46:53.3471152Z Unpacking librav1e0:amd64 (0.7.1-2) ...
2026-10-03T16:46:53.3852860Z Selecting previously unselected package librsvg2-2:amd64.
2026-10-03T16:46:53.3980031Z Preparing to unpack .../015-librsvg2-2_2.58.0+dfsg-1build1_amd64.deb ...
2026-10-03T16:46:53.3988496Z Unpacking librsvg2-2:amd64 (2.58.0+dfsg-1build1) ...
2026-10-03T16:46:53.4465230Z Selecting previously unselected package libshine3:amd64.
2026-10-03T16:46:53.4592342Z Preparing to unpack .../016-libshine3_3.1.1-2build1_amd64.deb ...
2026-10-03T16:46:53.4598916Z Unpacking libshine3:amd64 (3.1.1-2build1) ...
2026-10-03T16:46:53.4800294Z Selecting previously unselected package libspeex1:amd64.
2026-10-03T16:46:53.4933711Z Preparing to unpack .../017-libspeex1_1.2.1-2ubuntu2.24.04.1_amd64.deb ...
2026-10-03T16:46:53.4943962Z Unpacking libspeex1:amd64 (1.2.1-2ubuntu2.24.04.1) ...
2026-10-03T16:46:53.5177437Z Selecting previously unselected package libsvtav1enc1d1:amd64.
2026-10-03T16:46:53.5305096Z Preparing to unpack .../018-libsvtav1enc1d1_1.7.0+dfsg-2build1_amd64.deb ...
2026-10-03T16:46:53.5313507Z Unpacking libsvtav1enc1d1:amd64 (1.7.0+dfsg-2build1) ...
2026-10-03T16:46:53.5802063Z Selecting previously unselected package libsoxr0:amd64.
2026-10-03T16:46:53.5927782Z Preparing to unpack .../019-libsoxr0_0.1.3-4build3_amd64.deb ...
2026-10-03T16:46:53.5935346Z Unpacking libsoxr0:amd64 (0.1.3-4build3) ...
2026-10-03T16:46:53.6151618Z Selecting previously unselected package libswresample4:amd64.
2026-10-03T16:46:53.6281245Z Preparing to unpack .../020-libswresample4_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:53.6289934Z Unpacking libswresample4:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:53.6519210Z Selecting previously unselected package libtheora0:amd64.
2026-10-03T16:46:53.6648409Z Preparing to unpack .../021-libtheora0_1.1.1+dfsg.1-16.1build3_amd64.deb ...
2026-10-03T16:46:53.6656138Z Unpacking libtheora0:amd64 (1.1.1+dfsg.1-16.1build3) ...
2026-10-03T16:46:53.6898372Z Selecting previously unselected package libtwolame0:amd64.
2026-10-03T16:46:53.7027137Z Preparing to unpack .../022-libtwolame0_0.4.0-2build3_amd64.deb ...
2026-10-03T16:46:53.7034770Z Unpacking libtwolame0:amd64 (0.4.0-2build3) ...
2026-10-03T16:46:53.7267280Z Selecting previously unselected package libvorbisenc2:amd64.
2026-10-03T16:46:53.7397185Z Preparing to unpack .../023-libvorbisenc2_1.3.7-1build3_amd64.deb ...
2026-10-03T16:46:53.7407569Z Unpacking libvorbisenc2:amd64 (1.3.7-1build3) ...
2026-10-03T16:46:53.7642755Z Selecting previously unselected package libvpx9:amd64.
2026-10-03T16:46:53.7771494Z Preparing to unpack .../024-libvpx9_1.14.0-1ubuntu2.3_amd64.deb ...
2026-10-03T16:46:53.7781654Z Unpacking libvpx9:amd64 (1.14.0-1ubuntu2.3) ...
2026-10-03T16:46:53.8145736Z Selecting previously unselected package libx264-164:amd64.
2026-10-03T16:46:53.8275078Z Preparing to unpack .../025-libx264-164_2%3a0.164.3108+git31e19f9-1_amd64.deb ...
2026-10-03T16:46:53.8282643Z Unpacking libx264-164:amd64 (2:0.164.3108+git31e19f9-1) ...
2026-10-03T16:46:53.8578747Z Selecting previously unselected package libx265-199:amd64.
2026-10-03T16:46:53.8711121Z Preparing to unpack .../026-libx265-199_3.5-2build1_amd64.deb ...
2026-10-03T16:46:53.8718585Z Unpacking libx265-199:amd64 (3.5-2build1) ...
2026-10-03T16:46:53.9403388Z Selecting previously unselected package libxvidcore4:amd64.
2026-10-03T16:46:53.9532013Z Preparing to unpack .../027-libxvidcore4_2%3a1.3.7-1build1_amd64.deb ...
2026-10-03T16:46:53.9540341Z Unpacking libxvidcore4:amd64 (2:1.3.7-1build1) ...
2026-10-03T16:46:53.9764921Z Selecting previously unselected package libzvbi-common.
2026-10-03T16:46:53.9897277Z Preparing to unpack .../028-libzvbi-common_0.2.42-2_all.deb ...
2026-10-03T16:46:53.9909854Z Unpacking libzvbi-common (0.2.42-2) ...
2026-10-03T16:46:54.0517139Z Selecting previously unselected package libzvbi0t64:amd64.
2026-10-03T16:46:54.0647483Z Preparing to unpack .../029-libzvbi0t64_0.2.42-2_amd64.deb ...
2026-10-03T16:46:54.0655717Z Unpacking libzvbi0t64:amd64 (0.2.42-2) ...
2026-10-03T16:46:54.0914384Z Selecting previously unselected package libavcodec60:amd64.
2026-10-03T16:46:54.1044324Z Preparing to unpack .../030-libavcodec60_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:54.1057846Z Unpacking libavcodec60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:54.1943498Z Selecting previously unselected package libraw1394-11:amd64.
2026-10-03T16:46:54.2072174Z Preparing to unpack .../031-libraw1394-11_2.1.2-2build3_amd64.deb ...
2026-10-03T16:46:54.2088837Z Unpacking libraw1394-11:amd64 (2.1.2-2build3) ...
2026-10-03T16:46:54.2305854Z Selecting previously unselected package libavc1394-0:amd64.
2026-10-03T16:46:54.2435841Z Preparing to unpack .../032-libavc1394-0_0.5.4-5build3_amd64.deb ...
2026-10-03T16:46:54.2459182Z Unpacking libavc1394-0:amd64 (0.5.4-5build3) ...
2026-10-03T16:46:54.2665125Z Selecting previously unselected package libunibreak5:amd64.
2026-10-03T16:46:54.2792860Z Preparing to unpack .../033-libunibreak5_5.1-2build1_amd64.deb ...
2026-10-03T16:46:54.2801029Z Unpacking libunibreak5:amd64 (5.1-2build1) ...
2026-10-03T16:46:54.3009342Z Selecting previously unselected package libass9:amd64.
2026-10-03T16:46:54.3137621Z Preparing to unpack .../034-libass9_1%3a0.17.1-2build1_amd64.deb ...
2026-10-03T16:46:54.3145796Z Unpacking libass9:amd64 (1:0.17.1-2build1) ...
2026-10-03T16:46:54.3360499Z Selecting previously unselected package libudfread0:amd64.
2026-10-03T16:46:54.3485839Z Preparing to unpack .../035-libudfread0_1.1.2-1build1_amd64.deb ...
2026-10-03T16:46:54.3493565Z Unpacking libudfread0:amd64 (1.1.2-1build1) ...
2026-10-03T16:46:54.3721164Z Selecting previously unselected package libbluray2:amd64.
2026-10-03T16:46:54.3846301Z Preparing to unpack .../036-libbluray2_1%3a1.3.4-1build1_amd64.deb ...
2026-10-03T16:46:54.3857470Z Unpacking libbluray2:amd64 (1:1.3.4-1build1) ...
2026-10-03T16:46:54.4071495Z Selecting previously unselected package libchromaprint1:amd64.
2026-10-03T16:46:54.4195903Z Preparing to unpack .../037-libchromaprint1_1.5.1-5_amd64.deb ...
2026-10-03T16:46:54.4202891Z Unpacking libchromaprint1:amd64 (1.5.1-5) ...
2026-10-03T16:46:54.4401908Z Selecting previously unselected package libgme0:amd64.
2026-10-03T16:46:54.4526881Z Preparing to unpack .../038-libgme0_0.6.3-7build1_amd64.deb ...
2026-10-03T16:46:54.4534068Z Unpacking libgme0:amd64 (0.6.3-7build1) ...
2026-10-03T16:46:54.4802915Z Selecting previously unselected package libmpg123-0t64:amd64.
2026-10-03T16:46:54.4936239Z Preparing to unpack .../039-libmpg123-0t64_1.32.5-1ubuntu1.1_amd64.deb ...
2026-10-03T16:46:54.4943201Z Unpacking libmpg123-0t64:amd64 (1.32.5-1ubuntu1.1) ...
2026-10-03T16:46:54.5170598Z Selecting previously unselected package libopenmpt0t64:amd64.
2026-10-03T16:46:54.5297022Z Preparing to unpack .../040-libopenmpt0t64_0.7.3-1.1build3_amd64.deb ...
2026-10-03T16:46:54.5307833Z Unpacking libopenmpt0t64:amd64 (0.7.3-1.1build3) ...
2026-10-03T16:46:54.5593001Z Selecting previously unselected package libcjson1:amd64.
2026-10-03T16:46:54.5722016Z Preparing to unpack .../041-libcjson1_1.7.17-1_amd64.deb ...
2026-10-03T16:46:54.5728844Z Unpacking libcjson1:amd64 (1.7.17-1) ...
2026-10-03T16:46:54.5941532Z Selecting previously unselected package libmbedcrypto7t64:amd64.
2026-10-03T16:46:54.6067519Z Preparing to unpack .../042-libmbedcrypto7t64_2.28.8-1_amd64.deb ...
2026-10-03T16:46:54.6075500Z Unpacking libmbedcrypto7t64:amd64 (2.28.8-1) ...
2026-10-03T16:46:54.6295241Z Selecting previously unselected package librist4:amd64.
2026-10-03T16:46:54.6422131Z Preparing to unpack .../043-librist4_0.2.10+dfsg-2_amd64.deb ...
2026-10-03T16:46:54.6429472Z Unpacking librist4:amd64 (0.2.10+dfsg-2) ...
2026-10-03T16:46:54.7382349Z Selecting previously unselected package libsrt1.5-gnutls:amd64.
2026-10-03T16:46:54.7510651Z Preparing to unpack .../044-libsrt1.5-gnutls_1.5.3-1build2_amd64.deb ...
2026-10-03T16:46:54.7519004Z Unpacking libsrt1.5-gnutls:amd64 (1.5.3-1build2) ...
2026-10-03T16:46:54.7778210Z Selecting previously unselected package libssh-gcrypt-4:amd64.
2026-10-03T16:46:54.7904982Z Preparing to unpack .../045-libssh-gcrypt-4_0.10.6-2ubuntu0.5_amd64.deb ...
2026-10-03T16:46:54.7912632Z Unpacking libssh-gcrypt-4:amd64 (0.10.6-2ubuntu0.5) ...
2026-10-03T16:46:54.8501228Z Selecting previously unselected package libavformat60:amd64.
2026-10-03T16:46:54.8627579Z Preparing to unpack .../046-libavformat60_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:54.8636727Z Unpacking libavformat60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:54.8976083Z Selecting previously unselected package libbs2b0:amd64.
2026-10-03T16:46:54.9106770Z Preparing to unpack .../047-libbs2b0_3.1.0+dfsg-7build1_amd64.deb ...
2026-10-03T16:46:54.9115126Z Unpacking libbs2b0:amd64 (3.1.0+dfsg-7build1) ...
2026-10-03T16:46:54.9349237Z Selecting previously unselected package libflite1:amd64.
2026-10-03T16:46:54.9476033Z Preparing to unpack .../048-libflite1_2.2-6build3_amd64.deb ...
2026-10-03T16:46:54.9484217Z Unpacking libflite1:amd64 (2.2-6build3) ...
2026-10-03T16:46:55.0549642Z Selecting previously unselected package libserd-0-0:amd64.
2026-10-03T16:46:55.0674209Z Preparing to unpack .../049-libserd-0-0_0.32.2-1_amd64.deb ...
2026-10-03T16:46:55.0683800Z Unpacking libserd-0-0:amd64 (0.32.2-1) ...
2026-10-03T16:46:55.0891841Z Selecting previously unselected package libzix-0-0:amd64.
2026-10-03T16:46:55.1015802Z Preparing to unpack .../050-libzix-0-0_0.4.2-2build1_amd64.deb ...
2026-10-03T16:46:55.1023276Z Unpacking libzix-0-0:amd64 (0.4.2-2build1) ...
2026-10-03T16:46:55.1225022Z Selecting previously unselected package libsord-0-0:amd64.
2026-10-03T16:46:55.1352907Z Preparing to unpack .../051-libsord-0-0_0.16.16-2build1_amd64.deb ...
2026-10-03T16:46:55.1361142Z Unpacking libsord-0-0:amd64 (0.16.16-2build1) ...
2026-10-03T16:46:55.1568513Z Selecting previously unselected package libsratom-0-0:amd64.
2026-10-03T16:46:55.1694812Z Preparing to unpack .../052-libsratom-0-0_0.6.16-1build1_amd64.deb ...
2026-10-03T16:46:55.1702858Z Unpacking libsratom-0-0:amd64 (0.6.16-1build1) ...
2026-10-03T16:46:55.1915244Z Selecting previously unselected package liblilv-0-0:amd64.
2026-10-03T16:46:55.2043779Z Preparing to unpack .../053-liblilv-0-0_0.24.22-1build1_amd64.deb ...
2026-10-03T16:46:55.2052058Z Unpacking liblilv-0-0:amd64 (0.24.22-1build1) ...
2026-10-03T16:46:55.2268190Z Selecting previously unselected package libmysofa1:amd64.
2026-10-03T16:46:55.2397001Z Preparing to unpack .../054-libmysofa1_1.3.2+dfsg-2ubuntu2_amd64.deb ...
2026-10-03T16:46:55.2405191Z Unpacking libmysofa1:amd64 (1.3.2+dfsg-2ubuntu2) ...
2026-10-03T16:46:55.2645613Z Selecting previously unselected package libplacebo338:amd64.
2026-10-03T16:46:55.2769984Z Preparing to unpack .../055-libplacebo338_6.338.2-2build1_amd64.deb ...
2026-10-03T16:46:55.2777424Z Unpacking libplacebo338:amd64 (6.338.2-2build1) ...
2026-10-03T16:46:55.3329211Z Selecting previously unselected package libblas3:amd64.
2026-10-03T16:46:55.3455471Z Preparing to unpack .../056-libblas3_3.12.0-3build1.1_amd64.deb ...
2026-10-03T16:46:55.3502746Z Unpacking libblas3:amd64 (3.12.0-3build1.1) ...
2026-10-03T16:46:55.3742941Z Selecting previously unselected package liblapack3:amd64.
2026-10-03T16:46:55.3867249Z Preparing to unpack .../057-liblapack3_3.12.0-3build1.1_amd64.deb ...
2026-10-03T16:46:55.3895001Z Unpacking liblapack3:amd64 (3.12.0-3build1.1) ...
2026-10-03T16:46:55.4409514Z Selecting previously unselected package libasyncns0:amd64.
2026-10-03T16:46:55.4533552Z Preparing to unpack .../058-libasyncns0_0.8-6build4_amd64.deb ...
2026-10-03T16:46:55.4540385Z Unpacking libasyncns0:amd64 (0.8-6build4) ...
2026-10-03T16:46:55.4758257Z Selecting previously unselected package libflac12t64:amd64.
2026-10-03T16:46:55.4882374Z Preparing to unpack .../059-libflac12t64_1.4.3+ds-2.1ubuntu2_amd64.deb ...
2026-10-03T16:46:55.4894847Z Unpacking libflac12t64:amd64 (1.4.3+ds-2.1ubuntu2) ...
2026-10-03T16:46:55.5110273Z Selecting previously unselected package libsndfile1:amd64.
2026-10-03T16:46:55.5234298Z Preparing to unpack .../060-libsndfile1_1.2.2-1ubuntu5.24.04.1_amd64.deb ...
2026-10-03T16:46:55.5241508Z Unpacking libsndfile1:amd64 (1.2.2-1ubuntu5.24.04.1) ...
2026-10-03T16:46:55.5483488Z Selecting previously unselected package libpulse0:amd64.
2026-10-03T16:46:55.5609845Z Preparing to unpack .../061-libpulse0_1%3a16.1+dfsg1-2ubuntu10.1_amd64.deb ...
2026-10-03T16:46:55.5678948Z Unpacking libpulse0:amd64 (1:16.1+dfsg1-2ubuntu10.1) ...
2026-10-03T16:46:55.5923285Z Selecting previously unselected package libsphinxbase3t64:amd64.
2026-10-03T16:46:55.6048128Z Preparing to unpack .../062-libsphinxbase3t64_0.8+5prealpha+1-17build2_amd64.deb ...
2026-10-03T16:46:55.6055330Z Unpacking libsphinxbase3t64:amd64 (0.8+5prealpha+1-17build2) ...
2026-10-03T16:46:55.6267047Z Selecting previously unselected package libpocketsphinx3:amd64.
2026-10-03T16:46:55.6391115Z Preparing to unpack .../063-libpocketsphinx3_0.8.0+real5prealpha+1-15ubuntu5_amd64.deb ...
2026-10-03T16:46:55.6405420Z Unpacking libpocketsphinx3:amd64 (0.8.0+real5prealpha+1-15ubuntu5) ...
2026-10-03T16:46:55.6622706Z Selecting previously unselected package libpostproc57:amd64.
2026-10-03T16:46:55.6747284Z Preparing to unpack .../064-libpostproc57_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:55.6754580Z Unpacking libpostproc57:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:55.6963922Z Selecting previously unselected package libsamplerate0:amd64.
2026-10-03T16:46:55.7088968Z Preparing to unpack .../065-libsamplerate0_0.2.2-4build1_amd64.deb ...
2026-10-03T16:46:55.7096929Z Unpacking libsamplerate0:amd64 (0.2.2-4build1) ...
2026-10-03T16:46:55.7354282Z Selecting previously unselected package librubberband2:amd64.
2026-10-03T16:46:55.7479301Z Preparing to unpack .../066-librubberband2_3.3.0+dfsg-2build1_amd64.deb ...
2026-10-03T16:46:55.7486254Z Unpacking librubberband2:amd64 (3.3.0+dfsg-2build1) ...
2026-10-03T16:46:55.7689863Z Selecting previously unselected package libswscale7:amd64.
2026-10-03T16:46:55.7812909Z Preparing to unpack .../067-libswscale7_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:55.7820532Z Unpacking libswscale7:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:55.8086013Z Selecting previously unselected package libvidstab1.1:amd64.
2026-10-03T16:46:55.8210130Z Preparing to unpack .../068-libvidstab1.1_1.1.0-2build1_amd64.deb ...
2026-10-03T16:46:55.8217618Z Unpacking libvidstab1.1:amd64 (1.1.0-2build1) ...
2026-10-03T16:46:55.8417792Z Selecting previously unselected package libzimg2:amd64.
2026-10-03T16:46:55.8541352Z Preparing to unpack .../069-libzimg2_3.0.5+ds1-1build1_amd64.deb ...
2026-10-03T16:46:55.8548978Z Unpacking libzimg2:amd64 (3.0.5+ds1-1build1) ...
2026-10-03T16:46:55.8786168Z Selecting previously unselected package libavfilter9:amd64.
2026-10-03T16:46:55.8910689Z Preparing to unpack .../070-libavfilter9_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:55.8931286Z Unpacking libavfilter9:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:55.9667091Z Selecting previously unselected package libcaca0:amd64.
2026-10-03T16:46:55.9793349Z Preparing to unpack .../071-libcaca0_0.99.beta20-4ubuntu0.2_amd64.deb ...
2026-10-03T16:46:55.9801677Z Unpacking libcaca0:amd64 (0.99.beta20-4ubuntu0.2) ...
2026-10-03T16:46:56.0049358Z Selecting previously unselected package libcdio19t64:amd64.
2026-10-03T16:46:56.0174727Z Preparing to unpack .../072-libcdio19t64_2.1.0-4.1ubuntu1.2_amd64.deb ...
2026-10-03T16:46:56.0181898Z Unpacking libcdio19t64:amd64 (2.1.0-4.1ubuntu1.2) ...
2026-10-03T16:46:56.0389503Z Selecting previously unselected package libcdio-cdda2t64:amd64.
2026-10-03T16:46:56.0514283Z Preparing to unpack .../073-libcdio-cdda2t64_10.2+2.0.1-1.1build2_amd64.deb ...
2026-10-03T16:46:56.0521439Z Unpacking libcdio-cdda2t64:amd64 (10.2+2.0.1-1.1build2) ...
2026-10-03T16:46:56.0719729Z Selecting previously unselected package libcdio-paranoia2t64:amd64.
2026-10-03T16:46:56.0844489Z Preparing to unpack .../074-libcdio-paranoia2t64_10.2+2.0.1-1.1build2_amd64.deb ...
2026-10-03T16:46:56.0851422Z Unpacking libcdio-paranoia2t64:amd64 (10.2+2.0.1-1.1build2) ...
2026-10-03T16:46:56.1053964Z Selecting previously unselected package libdc1394-25:amd64.
2026-10-03T16:46:56.1179735Z Preparing to unpack .../075-libdc1394-25_2.2.6-4build1_amd64.deb ...
2026-10-03T16:46:56.1189028Z Unpacking libdc1394-25:amd64 (2.2.6-4build1) ...
2026-10-03T16:46:56.1399269Z Selecting previously unselected package libiec61883-0:amd64.
2026-10-03T16:46:56.1524944Z Preparing to unpack .../076-libiec61883-0_1.2.0-6build1_amd64.deb ...
2026-10-03T16:46:56.1531919Z Unpacking libiec61883-0:amd64 (1.2.0-6build1) ...
2026-10-03T16:46:56.1732099Z Selecting previously unselected package libjack-jackd2-0:amd64.
2026-10-03T16:46:56.1856258Z Preparing to unpack .../077-libjack-jackd2-0_1.9.21~dfsg-3ubuntu3_amd64.deb ...
2026-10-03T16:46:56.1863544Z Unpacking libjack-jackd2-0:amd64 (1.9.21~dfsg-3ubuntu3) ...
2026-10-03T16:46:56.2101908Z Selecting previously unselected package libopenal-data.
2026-10-03T16:46:56.2227505Z Preparing to unpack .../078-libopenal-data_1%3a1.23.1-4build1_all.deb ...
2026-10-03T16:46:56.2234957Z Unpacking libopenal-data (1:1.23.1-4build1) ...
2026-10-03T16:46:56.2499686Z Selecting previously unselected package libsndio7.0:amd64.
2026-10-03T16:46:56.2625157Z Preparing to unpack .../079-libsndio7.0_1.9.0-0.3build3_amd64.deb ...
2026-10-03T16:46:56.2632629Z Unpacking libsndio7.0:amd64 (1.9.0-0.3build3) ...
2026-10-03T16:46:56.2833488Z Selecting previously unselected package libopenal1:amd64.
2026-10-03T16:46:56.2958603Z Preparing to unpack .../080-libopenal1_1%3a1.23.1-4build1_amd64.deb ...
2026-10-03T16:46:56.2965475Z Unpacking libopenal1:amd64 (1:1.23.1-4build1) ...
2026-10-03T16:46:56.3226490Z Selecting previously unselected package libdecor-0-0:amd64.
2026-10-03T16:46:56.3352797Z Preparing to unpack .../081-libdecor-0-0_0.2.2-1build2_amd64.deb ...
2026-10-03T16:46:56.3360308Z Unpacking libdecor-0-0:amd64 (0.2.2-1build2) ...
2026-10-03T16:46:56.3706099Z Preparing to unpack .../082-libgl1-mesa-dri_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:56.4221699Z Unpacking libgl1-mesa-dri:amd64 (25.2.8-0ubuntu0.24.04.4) over (25.2.8-0ubuntu0.24.04.2) ...
2026-10-03T16:46:56.4893239Z Preparing to unpack .../083-libglx-mesa0_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:56.4916364Z Unpacking libglx-mesa0:amd64 (25.2.8-0ubuntu0.24.04.4) over (25.2.8-0ubuntu0.24.04.2) ...
2026-10-03T16:46:56.5330386Z Preparing to unpack .../084-libgbm1_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:56.5401180Z Unpacking libgbm1:amd64 (25.2.8-0ubuntu0.24.04.4) over (25.2.8-0ubuntu0.24.04.2) ...
2026-10-03T16:46:56.5783592Z Preparing to unpack .../085-mesa-libgallium_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:56.5817791Z Unpacking mesa-libgallium:amd64 (25.2.8-0ubuntu0.24.04.4) over (25.2.8-0ubuntu0.24.04.2) ...
2026-10-03T16:46:56.7465840Z Selecting previously unselected package libsdl2-2.0-0:amd64.
2026-10-03T16:46:56.7592453Z Preparing to unpack .../086-libsdl2-2.0-0_2.30.0+dfsg-1ubuntu3.1_amd64.deb ...
2026-10-03T16:46:56.7600469Z Unpacking libsdl2-2.0-0:amd64 (2.30.0+dfsg-1ubuntu3.1) ...
2026-10-03T16:46:56.7890865Z Selecting previously unselected package libxcb-shape0:amd64.
2026-10-03T16:46:56.8016537Z Preparing to unpack .../087-libxcb-shape0_1.15-1ubuntu2_amd64.deb ...
2026-10-03T16:46:56.8023936Z Unpacking libxcb-shape0:amd64 (1.15-1ubuntu2) ...
2026-10-03T16:46:56.8222212Z Selecting previously unselected package libxv1:amd64.
2026-10-03T16:46:56.8349755Z Preparing to unpack .../088-libxv1_2%3a1.0.11-1.1build1_amd64.deb ...
2026-10-03T16:46:56.8359904Z Unpacking libxv1:amd64 (2:1.0.11-1.1build1) ...
2026-10-03T16:46:56.8567514Z Selecting previously unselected package libavdevice60:amd64.
2026-10-03T16:46:56.8693361Z Preparing to unpack .../089-libavdevice60_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:56.8700932Z Unpacking libavdevice60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:56.8906471Z Selecting previously unselected package ffmpeg.
2026-10-03T16:46:56.9033925Z Preparing to unpack .../090-ffmpeg_7%3a6.1.1-3ubuntu5_amd64.deb ...
2026-10-03T16:46:56.9043628Z Unpacking ffmpeg (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:56.9626805Z Selecting previously unselected package libigdgmm12:amd64.
2026-10-03T16:46:56.9753151Z Preparing to unpack .../091-libigdgmm12_22.3.17+ds1-1ubuntu1_amd64.deb ...
2026-10-03T16:46:56.9760216Z Unpacking libigdgmm12:amd64 (22.3.17+ds1-1ubuntu1) ...
2026-10-03T16:46:56.9990623Z Selecting previously unselected package intel-media-va-driver:amd64.
2026-10-03T16:46:57.0115506Z Preparing to unpack .../092-intel-media-va-driver_24.1.0+dfsg1-1ubuntu0.2_amd64.deb ...
2026-10-03T16:46:57.0123484Z Unpacking intel-media-va-driver:amd64 (24.1.0+dfsg1-1ubuntu0.2) ...
2026-10-03T16:46:57.0763873Z Selecting previously unselected package libaacs0:amd64.
2026-10-03T16:46:57.0895205Z Preparing to unpack .../093-libaacs0_0.11.1-2build1_amd64.deb ...
2026-10-03T16:46:57.0904382Z Unpacking libaacs0:amd64 (0.11.1-2build1) ...
2026-10-03T16:46:57.1170669Z Selecting previously unselected package libbdplus0:amd64.
2026-10-03T16:46:57.1299592Z Preparing to unpack .../094-libbdplus0_0.2.0-3build1_amd64.deb ...
2026-10-03T16:46:57.1314797Z Unpacking libbdplus0:amd64 (0.2.0-3build1) ...
2026-10-03T16:46:57.1520601Z Selecting previously unselected package libdecor-0-plugin-1-gtk:amd64.
2026-10-03T16:46:57.1646656Z Preparing to unpack .../095-libdecor-0-plugin-1-gtk_0.2.2-1build2_amd64.deb ...
2026-10-03T16:46:57.1653990Z Unpacking libdecor-0-plugin-1-gtk:amd64 (0.2.2-1build2) ...
2026-10-03T16:46:57.1857931Z Selecting previously unselected package librsvg2-common:amd64.
2026-10-03T16:46:57.1983769Z Preparing to unpack .../096-librsvg2-common_2.58.0+dfsg-1build1_amd64.deb ...
2026-10-03T16:46:57.1995834Z Unpacking librsvg2-common:amd64 (2.58.0+dfsg-1build1) ...
2026-10-03T16:46:57.2361781Z Selecting previously unselected package mesa-va-drivers:amd64.
2026-10-03T16:46:57.2489186Z Preparing to unpack .../097-mesa-va-drivers_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:57.2504950Z Unpacking mesa-va-drivers:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.2712215Z Selecting previously unselected package mesa-vdpau-drivers:amd64.
2026-10-03T16:46:57.2840879Z Preparing to unpack .../098-mesa-vdpau-drivers_25.2.8-0ubuntu0.24.04.4_amd64.deb ...
2026-10-03T16:46:57.2848043Z Unpacking mesa-vdpau-drivers:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.3067361Z Selecting previously unselected package i965-va-driver:amd64.
2026-10-03T16:46:57.3195262Z Preparing to unpack .../099-i965-va-driver_2.4.1+dfsg1-1ubuntu0.2_amd64.deb ...
2026-10-03T16:46:57.3202954Z Unpacking i965-va-driver:amd64 (2.4.1+dfsg1-1ubuntu0.2) ...
2026-10-03T16:46:57.3484789Z Selecting previously unselected package va-driver-all:amd64.
2026-10-03T16:46:57.3614044Z Preparing to unpack .../100-va-driver-all_2.20.0-2ubuntu0.2_amd64.deb ...
2026-10-03T16:46:57.3624029Z Unpacking va-driver-all:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:57.3822375Z Selecting previously unselected package vdpau-driver-all:amd64.
2026-10-03T16:46:57.3949243Z Preparing to unpack .../101-vdpau-driver-all_1.5-2build1_amd64.deb ...
2026-10-03T16:46:57.3956157Z Unpacking vdpau-driver-all:amd64 (1.5-2build1) ...
2026-10-03T16:46:57.4151437Z Selecting previously unselected package pocketsphinx-en-us.
2026-10-03T16:46:57.4279541Z Preparing to unpack .../102-pocketsphinx-en-us_0.8.0+real5prealpha+1-15ubuntu5_all.deb ...
2026-10-03T16:46:57.4286765Z Unpacking pocketsphinx-en-us (0.8.0+real5prealpha+1-15ubuntu5) ...
2026-10-03T16:46:57.6297411Z Setting up libgme0:amd64 (0.6.3-7build1) ...
2026-10-03T16:46:57.6324385Z Setting up libchromaprint1:amd64 (1.5.1-5) ...
2026-10-03T16:46:57.6346155Z Setting up libssh-gcrypt-4:amd64 (0.10.6-2ubuntu0.5) ...
2026-10-03T16:46:57.6377896Z Setting up libhwy1t64:amd64 (1.0.7-8.1build1) ...
2026-10-03T16:46:57.6409229Z Setting up libudfread0:amd64 (1.1.2-1build1) ...
2026-10-03T16:46:57.6438823Z Setting up mesa-libgallium:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.6466565Z Setting up libraw1394-11:amd64 (2.1.2-2build3) ...
2026-10-03T16:46:57.6489642Z Setting up libspeex1:amd64 (1.2.1-2ubuntu2.24.04.1) ...
2026-10-03T16:46:57.6507929Z Setting up libshine3:amd64 (3.1.1-2build1) ...
2026-10-03T16:46:57.6529640Z Setting up libcaca0:amd64 (0.99.beta20-4ubuntu0.2) ...
2026-10-03T16:46:57.6554468Z Setting up libvpl2 (2023.3.0-1build1) ...
2026-10-03T16:46:57.6577255Z Setting up libx264-164:amd64 (2:0.164.3108+git31e19f9-1) ...
2026-10-03T16:46:57.6608334Z Setting up libtwolame0:amd64 (0.4.0-2build3) ...
2026-10-03T16:46:57.6652146Z Setting up libmbedcrypto7t64:amd64 (2.28.8-1) ...
2026-10-03T16:46:57.6700475Z Setting up libgbm1:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.6732204Z Setting up libgsm1:amd64 (1.0.22-1build1) ...
2026-10-03T16:46:57.6752669Z Setting up libsoxr0:amd64 (0.1.3-4build3) ...
2026-10-03T16:46:57.6771501Z Setting up libzix-0-0:amd64 (0.4.2-2build1) ...
2026-10-03T16:46:57.6798957Z Setting up libcodec2-1.2:amd64 (1.2.0-2build1) ...
2026-10-03T16:46:57.6820153Z Setting up libgl1-mesa-dri:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.6899775Z Setting up libmysofa1:amd64 (1.3.2+dfsg-2ubuntu2) ...
2026-10-03T16:46:57.6924435Z Setting up libxcb-shape0:amd64 (1.15-1ubuntu2) ...
2026-10-03T16:46:57.6955242Z Setting up libcdio19t64:amd64 (2.1.0-4.1ubuntu1.2) ...
2026-10-03T16:46:57.6995161Z Setting up libsvtav1enc1d1:amd64 (1.7.0+dfsg-2build1) ...
2026-10-03T16:46:57.7025043Z Setting up libigdgmm12:amd64 (22.3.17+ds1-1ubuntu1) ...
2026-10-03T16:46:57.7043033Z Setting up libmpg123-0t64:amd64 (1.32.5-1ubuntu1.1) ...
2026-10-03T16:46:57.7067003Z Setting up libcjson1:amd64 (1.7.17-1) ...
2026-10-03T16:46:57.7094070Z Setting up libxvidcore4:amd64 (2:1.3.7-1build1) ...
2026-10-03T16:46:57.7116932Z Setting up librav1e0:amd64 (0.7.1-2) ...
2026-10-03T16:46:57.7144688Z Setting up libcdio-cdda2t64:amd64 (10.2+2.0.1-1.1build2) ...
2026-10-03T16:46:57.7169142Z Setting up librist4:amd64 (0.2.10+dfsg-2) ...
2026-10-03T16:46:57.7196957Z Setting up librsvg2-2:amd64 (2.58.0+dfsg-1build1) ...
2026-10-03T16:46:57.7219048Z Setting up libblas3:amd64 (3.12.0-3build1.1) ...
2026-10-03T16:46:57.7284108Z update-alternatives: using /usr/lib/x86_64-linux-gnu/blas/libblas.so.3 to provide /usr/lib/x86_64-linux-gnu/libblas.so.3 (libblas.so.3-x86_64-linux-gnu) in auto mode
2026-10-03T16:46:57.7304108Z Setting up libplacebo338:amd64 (6.338.2-2build1) ...
2026-10-03T16:46:57.7323515Z Setting up libva2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:57.7344005Z Setting up libopus0:amd64 (1.4-1build1) ...
2026-10-03T16:46:57.7364143Z Setting up libcdio-paranoia2t64:amd64 (10.2+2.0.1-1.1build2) ...
2026-10-03T16:46:57.7383591Z Setting up libdc1394-25:amd64 (2.2.6-4build1) ...
2026-10-03T16:46:57.7428582Z Setting up intel-media-va-driver:amd64 (24.1.0+dfsg1-1ubuntu0.2) ...
2026-10-03T16:46:57.7449833Z Setting up libxv1:amd64 (2:1.0.11-1.1build1) ...
2026-10-03T16:46:57.7478370Z Setting up libunibreak5:amd64 (5.1-2build1) ...
2026-10-03T16:46:57.7501393Z Setting up libaacs0:amd64 (0.11.1-2build1) ...
2026-10-03T16:46:57.7520386Z Setting up libjxl0.7:amd64 (0.7.0-10.2ubuntu6.1) ...
2026-10-03T16:46:57.7542276Z Setting up librsvg2-common:amd64 (2.58.0+dfsg-1build1) ...
2026-10-03T16:46:57.7656545Z Setting up pocketsphinx-en-us (0.8.0+real5prealpha+1-15ubuntu5) ...
2026-10-03T16:46:57.7676990Z Setting up libx265-199:amd64 (3.5-2build1) ...
2026-10-03T16:46:57.7696495Z Setting up libsndio7.0:amd64 (1.9.0-0.3build3) ...
2026-10-03T16:46:57.7777813Z Setting up libbdplus0:amd64 (0.2.0-3build1) ...
2026-10-03T16:46:57.7799953Z Setting up libvidstab1.1:amd64 (1.1.0-2build1) ...
2026-10-03T16:46:57.7830250Z Setting up libvpx9:amd64 (1.14.0-1ubuntu2.3) ...
2026-10-03T16:46:57.7855936Z Setting up libsrt1.5-gnutls:amd64 (1.5.3-1build2) ...
2026-10-03T16:46:57.7891312Z Setting up libflite1:amd64 (2.2-6build3) ...
2026-10-03T16:46:57.7919485Z Setting up libdav1d7:amd64 (1.4.1-1build1) ...
2026-10-03T16:46:57.7945319Z Setting up libva-drm2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:57.7965952Z Setting up ocl-icd-libopencl1:amd64 (2.3.2-1build1) ...
2026-10-03T16:46:57.7994137Z Setting up libasyncns0:amd64 (0.8-6build4) ...
2026-10-03T16:46:57.8016924Z Setting up libvdpau1:amd64 (1.5-2build1) ...
2026-10-03T16:46:57.8054825Z Setting up libbs2b0:amd64 (3.1.0+dfsg-7build1) ...
2026-10-03T16:46:57.8083552Z Setting up libtheora0:amd64 (1.1.1+dfsg.1-16.1build3) ...
2026-10-03T16:46:57.8102477Z Setting up libdecor-0-0:amd64 (0.2.2-1build2) ...
2026-10-03T16:46:57.8131211Z Setting up libzimg2:amd64 (3.0.5+ds1-1build1) ...
2026-10-03T16:46:57.8150444Z Setting up libopenal-data (1:1.23.1-4build1) ...
2026-10-03T16:46:57.8177701Z Setting up libflac12t64:amd64 (1.4.3+ds-2.1ubuntu2) ...
2026-10-03T16:46:57.8198944Z Setting up mesa-va-drivers:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.8223935Z Setting up libbluray2:amd64 (1:1.3.4-1build1) ...
2026-10-03T16:46:57.8246585Z Setting up libsamplerate0:amd64 (0.2.2-4build1) ...
2026-10-03T16:46:57.8275357Z Setting up libva-x11-2:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:57.8298606Z Setting up libdecor-0-plugin-1-gtk:amd64 (0.2.2-1build2) ...
2026-10-03T16:46:57.8322300Z Setting up libopenmpt0t64:amd64 (0.7.3-1.1build3) ...
2026-10-03T16:46:57.8356168Z Setting up libzvbi-common (0.2.42-2) ...
2026-10-03T16:46:57.8377011Z Setting up libmp3lame0:amd64 (3.100-6build1) ...
2026-10-03T16:46:57.8396484Z Setting up i965-va-driver:amd64 (2.4.1+dfsg1-1ubuntu0.2) ...
2026-10-03T16:46:57.8435054Z Setting up libvorbisenc2:amd64 (1.3.7-1build3) ...
2026-10-03T16:46:57.8461167Z Setting up libiec61883-0:amd64 (1.2.0-6build1) ...
2026-10-03T16:46:57.8482048Z Setting up libserd-0-0:amd64 (0.32.2-1) ...
2026-10-03T16:46:57.8509652Z Setting up libavc1394-0:amd64 (0.5.4-5build3) ...
2026-10-03T16:46:57.8529751Z Setting up mesa-vdpau-drivers:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.8555673Z Setting up liblapack3:amd64 (3.12.0-3build1.1) ...
2026-10-03T16:46:57.8622593Z update-alternatives: using /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3 to provide /usr/lib/x86_64-linux-gnu/liblapack.so.3 (liblapack.so.3-x86_64-linux-gnu) in auto mode
2026-10-03T16:46:57.8643147Z Setting up libglx-mesa0:amd64 (25.2.8-0ubuntu0.24.04.4) ...
2026-10-03T16:46:57.8665405Z Setting up libzvbi0t64:amd64 (0.2.42-2) ...
2026-10-03T16:46:57.8689799Z Setting up libavutil58:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.8710155Z Setting up libopenal1:amd64 (1:1.23.1-4build1) ...
2026-10-03T16:46:57.8731532Z Setting up libass9:amd64 (1:0.17.1-2build1) ...
2026-10-03T16:46:57.9108252Z Setting up libswresample4:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9132980Z Setting up va-driver-all:amd64 (2.20.0-2ubuntu0.2) ...
2026-10-03T16:46:57.9159692Z Setting up libavcodec60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9209023Z Setting up librubberband2:amd64 (3.3.0+dfsg-2build1) ...
2026-10-03T16:46:57.9238782Z Setting up libjack-jackd2-0:amd64 (1.9.21~dfsg-3ubuntu3) ...
2026-10-03T16:46:57.9268101Z Setting up vdpau-driver-all:amd64 (1.5-2build1) ...
2026-10-03T16:46:57.9288320Z Setting up libsord-0-0:amd64 (0.16.16-2build1) ...
2026-10-03T16:46:57.9308312Z Setting up libpostproc57:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9330924Z Setting up libsratom-0-0:amd64 (0.6.16-1build1) ...
2026-10-03T16:46:57.9356071Z Setting up libsndfile1:amd64 (1.2.2-1ubuntu5.24.04.1) ...
2026-10-03T16:46:57.9379381Z Setting up liblilv-0-0:amd64 (0.24.22-1build1) ...
2026-10-03T16:46:57.9410935Z Setting up libswscale7:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9435313Z Setting up libpulse0:amd64 (1:16.1+dfsg1-2ubuntu10.1) ...
2026-10-03T16:46:57.9523670Z Setting up libavformat60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9552667Z Setting up libsphinxbase3t64:amd64 (0.8+5prealpha+1-17build2) ...
2026-10-03T16:46:57.9573688Z Setting up libsdl2-2.0-0:amd64 (2.30.0+dfsg-1ubuntu3.1) ...
2026-10-03T16:46:57.9598845Z Setting up libpocketsphinx3:amd64 (0.8.0+real5prealpha+1-15ubuntu5) ...
2026-10-03T16:46:57.9658445Z Setting up libavfilter9:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9697165Z Setting up libavdevice60:amd64 (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9732481Z Setting up ffmpeg (7:6.1.1-3ubuntu5) ...
2026-10-03T16:46:57.9761261Z Processing triggers for man-db (2.12.0-4build2) ...
2026-10-03T16:46:57.9785217Z Not building database; man-db/auto-update is not 'true'.
2026-10-03T16:46:57.9804532Z Processing triggers for libgdk-pixbuf-2.0-0:amd64 (2.42.10+dfsg-3ubuntu3.3) ...
2026-10-03T16:46:58.1766477Z Processing triggers for libc-bin (2.39-0ubuntu8.9) ...
2026-10-03T16:46:59.4027125Z 
2026-10-03T16:46:59.4027766Z Running kernel seems to be up-to-date.
2026-10-03T16:46:59.4028387Z 
2026-10-03T16:46:59.4028597Z No services need to be restarted.
2026-10-03T16:46:59.4028840Z 
2026-10-03T16:46:59.4029032Z No containers need to be restarted.
2026-10-03T16:46:59.4029271Z 
2026-10-03T16:46:59.4029514Z No user sessions are running outdated binaries.
2026-10-03T16:46:59.4029831Z 
2026-10-03T16:46:59.4030221Z No VM guests are running outdated hypervisor (qemu) binaries on this host.
2026-10-03T16:47:00.3923374Z ##[group]Run python -m pip install --upgrade pip
2026-10-03T16:47:00.3923797Z [36;1mpython -m pip install --upgrade pip[0m
2026-10-03T16:47:00.3924160Z [36;1mpip install -r requirements.txt[0m
2026-10-03T16:47:00.3989925Z shell: /usr/bin/bash -e {0}
2026-10-03T16:47:00.3990199Z env:
2026-10-03T16:47:00.3990489Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:47:00.3991182Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-03T16:47:00.3991672Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:47:00.3992110Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:47:00.3992546Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:47:00.3992983Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-03T16:47:00.3993352Z ##[endgroup]
2026-10-03T16:47:02.5765635Z Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages (26.2.1)
2026-10-03T16:47:03.2013200Z Collecting scenedetect==0.7 (from -r requirements.txt (line 1))
2026-10-03T16:47:03.2503137Z   Downloading scenedetect-0.7-py3-none-any.whl.metadata (3.9 kB)
2026-10-03T16:47:03.2653368Z Collecting transnetv2-pytorch==1.0.5 (from -r requirements.txt (line 2))
2026-10-03T16:47:03.2695749Z   Downloading transnetv2_pytorch-1.0.5-py3-none-any.whl.metadata (10 kB)
2026-10-03T16:47:03.3750009Z Collecting ultralytics==8.4.46 (from -r requirements.txt (line 3))
2026-10-03T16:47:03.3801814Z   Downloading ultralytics-8.4.46-py3-none-any.whl.metadata (39 kB)
2026-10-03T16:47:03.4442846Z Collecting torch==2.11.0 (from -r requirements.txt (line 4))
2026-10-03T16:47:03.4501180Z   Downloading torch-2.11.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (29 kB)
2026-10-03T16:47:03.5023940Z Collecting torchvision==0.26.0 (from -r requirements.txt (line 5))
2026-10-03T16:47:03.5073323Z   Downloading torchvision-0.26.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (5.5 kB)
2026-10-03T16:47:03.5313053Z Collecting tqdm==4.67.3 (from -r requirements.txt (line 6))
2026-10-03T16:47:03.5360534Z   Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
2026-10-03T16:47:03.6126488Z Collecting yt-dlp (from -r requirements.txt (line 7))
2026-10-03T16:47:03.6283964Z   Downloading yt_dlp-2026.8.19-py3-none-any.whl.metadata (183 kB)
2026-10-03T16:47:03.6552609Z Collecting faster-whisper==1.2.1 (from -r requirements.txt (line 8))
2026-10-03T16:47:03.6586496Z   Downloading faster_whisper-1.2.1-py3-none-any.whl.metadata (16 kB)
2026-10-03T16:47:03.6773504Z Collecting py3langid==0.3.0 (from -r requirements.txt (line 9))
2026-10-03T16:47:03.6820080Z   Downloading py3langid-0.3.0-py3-none-any.whl.metadata (13 kB)
2026-10-03T16:47:03.7047571Z Collecting google-genai==1.75.0 (from -r requirements.txt (line 10))
2026-10-03T16:47:03.7080007Z   Downloading google_genai-1.75.0-py3-none-any.whl.metadata (52 kB)
2026-10-03T16:47:03.7269376Z Collecting python-dotenv==1.2.2 (from -r requirements.txt (line 11))
2026-10-03T16:47:03.7302442Z   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
2026-10-03T16:47:03.7546071Z Collecting mediapipe==0.10.14 (from -r requirements.txt (line 12))
2026-10-03T16:47:03.7619194Z   Downloading mediapipe-0.10.14-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.7 kB)
2026-10-03T16:47:03.9581922Z Collecting boto3==1.43.4 (from -r requirements.txt (line 13))
2026-10-03T16:47:03.9651259Z   Downloading boto3-1.43.4-py3-none-any.whl.metadata (6.5 kB)
2026-10-03T16:47:04.0032164Z Collecting fastapi==0.136.1 (from -r requirements.txt (line 15))
2026-10-03T16:47:04.0078628Z   Downloading fastapi-0.136.1-py3-none-any.whl.metadata (28 kB)
2026-10-03T16:47:04.0345812Z Collecting uvicorn==0.46.0 (from -r requirements.txt (line 16))
2026-10-03T16:47:04.0391090Z   Downloading uvicorn-0.46.0-py3-none-any.whl.metadata (6.7 kB)
2026-10-03T16:47:04.0526616Z Collecting python-multipart==0.0.27 (from -r requirements.txt (line 17))
2026-10-03T16:47:04.0589775Z   Downloading python_multipart-0.0.27-py3-none-any.whl.metadata (2.1 kB)
2026-10-03T16:47:04.0756331Z Collecting httpx==0.28.1 (from -r requirements.txt (line 18))
2026-10-03T16:47:04.0792627Z   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-10-03T16:47:04.2350865Z Collecting Pillow==12.2.0 (from -r requirements.txt (line 19))
2026-10-03T16:47:04.2419281Z   Downloading pillow-12.2.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
2026-10-03T16:47:04.2600231Z Collecting beautifulsoup4==4.14.3 (from -r requirements.txt (line 20))
2026-10-03T16:47:04.2644174Z   Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
2026-10-03T16:47:04.2818493Z Collecting click!=8.3.0,~=8.0 (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-03T16:47:04.2857072Z   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
2026-10-03T16:47:04.5003500Z Collecting numpy (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-03T16:47:04.5039641Z   Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
2026-10-03T16:47:04.5639285Z Collecting opencv-python (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-03T16:47:04.5701865Z   Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (19 kB)
2026-10-03T16:47:04.5906804Z Collecting platformdirs (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-03T16:47:04.5940402Z   Downloading platformdirs-4.12.2-py3-none-any.whl.metadata (5.5 kB)
2026-10-03T16:47:04.6051730Z Collecting ffmpeg-python (from transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-03T16:47:04.6107443Z   Downloading ffmpeg_python-0.2.0-py3-none-any.whl.metadata (1.7 kB)
2026-10-03T16:47:04.7213511Z Collecting pandas (from transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-03T16:47:04.7253928Z   Downloading pandas-3.0.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
2026-10-03T16:47:04.9174047Z Collecting matplotlib>=3.3.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:04.9215944Z   Downloading matplotlib-3.11.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (80 kB)
2026-10-03T16:47:04.9747175Z Collecting pyyaml>=5.3.1 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:04.9782970Z   Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-10-03T16:47:04.9985335Z Collecting requests>=2.23.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:05.0018904Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-10-03T16:47:05.1232480Z Collecting scipy>=1.4.1 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:05.1270581Z   Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
2026-10-03T16:47:05.2029341Z Collecting psutil>=5.8.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:05.2064803Z   Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl.metadata (22 kB)
2026-10-03T16:47:05.3202743Z Collecting polars>=0.20.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:05.3241095Z   Downloading polars-1.44.2-py3-none-any.whl.metadata (11 kB)
2026-10-03T16:47:05.3440187Z Collecting ultralytics-thop>=2.0.18 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:05.3485493Z   Downloading ultralytics_thop-2.2.2-py3-none-any.whl.metadata (14 kB)
2026-10-03T16:47:05.3737254Z Collecting filelock (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.3772103Z   Downloading filelock-4.0.9-py3-none-any.whl.metadata (2.0 kB)
2026-10-03T16:47:05.4012278Z Collecting typing-extensions>=4.10.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.4047123Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-10-03T16:47:05.4088957Z Requirement already satisfied: setuptools<82 in /opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages (from torch==2.11.0->-r requirements.txt (line 4)) (79.0.1)
2026-10-03T16:47:05.4217873Z Collecting sympy>=1.13.3 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.4253289Z   Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
2026-10-03T16:47:05.4487065Z Collecting networkx>=2.5.1 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.4531890Z   Downloading networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
2026-10-03T16:47:05.4707614Z Collecting jinja2 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.4744707Z   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2026-10-03T16:47:05.4947692Z Collecting fsspec>=0.8.5 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.4980686Z   Downloading fsspec-2026.9.0-py3-none-any.whl.metadata (10 kB)
2026-10-03T16:47:05.5300199Z Collecting cuda-toolkit==13.0.2 (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.5344411Z   Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl.metadata (9.4 kB)
2026-10-03T16:47:05.6149382Z Collecting cuda-bindings<14,>=13.0.3 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.6185677Z   Downloading cuda_bindings-13.4.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-10-03T16:47:05.6336313Z Collecting nvidia-cudnn-cu13==9.19.0.56 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.6415921Z   Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_x86_64.whl.metadata (1.9 kB)
2026-10-03T16:47:05.6535840Z Collecting nvidia-cusparselt-cu13==0.8.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.6618724Z   Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_x86_64.whl.metadata (12 kB)
2026-10-03T16:47:05.6731024Z Collecting nvidia-nccl-cu13==2.28.9 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.6927009Z   Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_x86_64.whl.metadata (2.0 kB)
2026-10-03T16:47:05.7042579Z Collecting nvidia-nvshmem-cu13==3.4.5 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.7077327Z   Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)
2026-10-03T16:47:05.7266114Z Collecting triton==3.6.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:05.7324797Z   Downloading triton-3.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:05.8143869Z Collecting ctranslate2<5,>=4.0 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:05.8179173Z   Downloading ctranslate2-4.8.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
2026-10-03T16:47:05.8730070Z Collecting huggingface-hub>=0.21 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:05.8772103Z   Downloading huggingface_hub-2.1.1-py3-none-any.whl.metadata (16 kB)
2026-10-03T16:47:06.0222074Z Collecting tokenizers<1,>=0.13 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:06.0263956Z   Downloading tokenizers-0.23.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.8 kB)
2026-10-03T16:47:06.0887323Z Collecting onnxruntime<2,>=1.14 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:06.0924031Z   Downloading onnxruntime-1.30.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (5.7 kB)
2026-10-03T16:47:06.1399504Z Collecting av>=11 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:06.1435252Z   Downloading av-18.1.0-cp311-abi3-manylinux_2_28_x86_64.whl.metadata (5.0 kB)
2026-10-03T16:47:06.1655161Z Collecting anyio<5.0.0,>=4.8.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.1691027Z   Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
2026-10-03T16:47:06.2531028Z Collecting google-auth<3.0.0,>=2.48.1 (from google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.2565723Z   Downloading google_auth-2.59.1-py3-none-any.whl.metadata (6.0 kB)
2026-10-03T16:47:06.3646951Z Collecting pydantic<3.0.0,>=2.9.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.3686653Z   Downloading pydantic-2.13.5-py3-none-any.whl.metadata (110 kB)
2026-10-03T16:47:06.3954244Z Collecting tenacity<9.2.0,>=8.2.3 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.3990562Z   Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
2026-10-03T16:47:06.5092507Z Collecting websockets<17.0,>=13.0.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.5127537Z   Downloading websockets-16.1.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
2026-10-03T16:47:06.5266070Z Collecting distro<2,>=1.7.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.5300722Z   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
2026-10-03T16:47:06.5398098Z Collecting sniffio (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:06.5429028Z   Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
2026-10-03T16:47:06.5621179Z Collecting certifi (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-03T16:47:06.5660534Z   Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
2026-10-03T16:47:06.5806227Z Collecting httpcore==1.* (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-03T16:47:06.6176141Z   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-10-03T16:47:06.6360954Z Collecting idna (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-03T16:47:06.6400476Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
2026-10-03T16:47:06.6552124Z Collecting absl-py (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.6622575Z   Downloading absl_py-2.5.0-py3-none-any.whl.metadata (3.3 kB)
2026-10-03T16:47:06.6764286Z Collecting attrs>=19.1.0 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.6861960Z   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
2026-10-03T16:47:06.6992055Z Collecting flatbuffers>=2.0 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.7023533Z   Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
2026-10-03T16:47:06.7305371Z Collecting jax (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.7350116Z   Downloading jax-0.10.2-py3-none-any.whl.metadata (13 kB)
2026-10-03T16:47:06.7819906Z Collecting jaxlib (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.7865959Z   Downloading jaxlib-0.10.2-cp311-cp311-manylinux_2_27_x86_64.whl.metadata (1.3 kB)
2026-10-03T16:47:06.8426588Z Collecting opencv-contrib-python (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:06.8485724Z   Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (19 kB)
2026-10-03T16:47:07.0389353Z Collecting protobuf<5,>=4.25.3 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:07.0425650Z   Downloading protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)
2026-10-03T16:47:07.0665658Z Collecting sounddevice>=0.4.4 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:07.0700096Z   Downloading sounddevice-0.5.6-py3-none-any.whl.metadata (1.4 kB)
2026-10-03T16:47:07.2783914Z Collecting botocore<1.44.0,>=1.43.4 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:07.2819941Z   Downloading botocore-1.43.108-py3-none-any.whl.metadata (5.6 kB)
2026-10-03T16:47:07.2941375Z Collecting jmespath<2.0.0,>=0.7.1 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:07.2980000Z   Downloading jmespath-1.1.0-py3-none-any.whl.metadata (7.6 kB)
2026-10-03T16:47:07.3367181Z Collecting s3transfer<0.18.0,>=0.17.0 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:07.3399968Z   Downloading s3transfer-0.17.1-py3-none-any.whl.metadata (1.7 kB)
2026-10-03T16:47:07.3638498Z Collecting starlette>=0.46.0 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-03T16:47:07.3697106Z   Downloading starlette-1.7.0-py3-none-any.whl.metadata (6.6 kB)
2026-10-03T16:47:07.3836759Z Collecting typing-inspection>=0.4.2 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-03T16:47:07.3874723Z   Downloading typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
2026-10-03T16:47:07.3984905Z Collecting annotated-doc>=0.0.2 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-03T16:47:07.4019630Z   Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)
2026-10-03T16:47:07.4172401Z Collecting h11>=0.8 (from uvicorn==0.46.0->-r requirements.txt (line 16))
2026-10-03T16:47:07.4242668Z   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-10-03T16:47:07.4431860Z Collecting soupsieve>=1.6.1 (from beautifulsoup4==4.14.3->-r requirements.txt (line 20))
2026-10-03T16:47:07.4472910Z   Downloading soupsieve-2.10-py3-none-any.whl.metadata (4.4 kB)
2026-10-03T16:47:07.4649902Z Collecting nvidia-cublas==13.1.0.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.4716478Z   Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.4840517Z Collecting nvidia-cuda-runtime==13.0.96.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.4881143Z   Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.5003023Z Collecting nvidia-cufft==12.0.0.61.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5034050Z   Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-10-03T16:47:07.5147037Z Collecting nvidia-cufile==1.15.1.6.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5181010Z   Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.5299439Z Collecting nvidia-cuda-cupti==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5330982Z   Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.5442327Z Collecting nvidia-curand==10.4.0.35.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5480765Z   Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.5601008Z Collecting nvidia-cusolver==12.0.4.66.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5632967Z   Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
2026-10-03T16:47:07.5764891Z Collecting nvidia-cusparse==12.6.3.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.5968716Z   Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-10-03T16:47:07.6100958Z Collecting nvidia-nvjitlink==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.6145770Z   Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.6266248Z Collecting nvidia-cuda-nvrtc==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.6304005Z   Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-10-03T16:47:07.6423755Z Collecting nvidia-nvtx==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.6468969Z   Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (1.8 kB)
2026-10-03T16:47:07.7364249Z Collecting python-dateutil<3.0.0,>=2.1 (from botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:07.7396866Z   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
2026-10-03T16:47:07.7600402Z Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:07.7636904Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
2026-10-03T16:47:07.7808259Z Collecting cuda-pathfinder>=1.4.2 (from cuda-bindings<14,>=13.0.3->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:07.7849850Z   Downloading cuda_pathfinder-1.8.3-py3-none-any.whl.metadata (1.9 kB)
2026-10-03T16:47:07.8069497Z Collecting pyasn1-modules>=0.2.1 (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:07.8103195Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
2026-10-03T16:47:07.9877784Z Collecting cryptography>=38.0.3 (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:07.9949577Z   Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.4 kB)
2026-10-03T16:47:08.0304928Z Collecting packaging (from onnxruntime<2,>=1.14->faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:08.0343941Z   Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
2026-10-03T16:47:08.0490566Z Collecting annotated-types>=0.6.0 (from pydantic<3.0.0,>=2.9.0->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:08.0525707Z   Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
2026-10-03T16:47:08.7352918Z Collecting pydantic-core==2.46.5 (from pydantic<3.0.0,>=2.9.0->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:08.7396254Z   Downloading pydantic_core-2.46.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
2026-10-03T16:47:08.7567042Z Collecting six>=1.5 (from python-dateutil<3.0.0,>=2.1->botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-03T16:47:08.7598831Z   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-10-03T16:47:08.8825748Z Collecting charset_normalizer<4,>=2 (from requests>=2.23.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:08.8903736Z   Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
2026-10-03T16:47:08.9397141Z Collecting huggingface-hub>=0.21 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:08.9434032Z   Downloading huggingface_hub-1.33.0-py3-none-any.whl.metadata (16 kB)
2026-10-03T16:47:08.9953861Z Collecting hf-xet<2.0.0,>=1.6.0 (from huggingface-hub>=0.21->faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-03T16:47:09.0006949Z   Downloading hf_xet-1.6.0-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-10-03T16:47:09.1160255Z Collecting cffi>=2.0.0 (from cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:09.1195583Z   Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
2026-10-03T16:47:09.1323339Z Collecting pycparser (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:09.1355410Z   Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
2026-10-03T16:47:09.2910439Z Collecting contourpy>=1.0.1 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.3006091Z   Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)
2026-10-03T16:47:09.3235665Z Collecting cycler>=0.10 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.3280305Z   Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
2026-10-03T16:47:09.4768230Z Collecting fonttools>=4.28.2 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.4811385Z   Downloading fonttools-4.66.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (130 kB)
2026-10-03T16:47:09.5571522Z Collecting kiwisolver>=1.3.1 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.5610414Z   Downloading kiwisolver-1.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (5.2 kB)
2026-10-03T16:47:09.5890799Z Collecting pyparsing>=3 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.5998894Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
2026-10-03T16:47:09.6325686Z Collecting polars-runtime-32==1.44.2 (from polars>=0.20.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-03T16:47:09.6365578Z   Downloading polars_runtime_32-1.44.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
2026-10-03T16:47:09.6607860Z Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-03T16:47:09.6676715Z   Downloading pyasn1-0.6.4-py3-none-any.whl.metadata (8.4 kB)
2026-10-03T16:47:09.6910102Z Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:09.6942593Z   Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
2026-10-03T16:47:09.7132245Z Collecting future (from ffmpeg-python->transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-03T16:47:09.7166498Z   Downloading future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
2026-10-03T16:47:09.7449098Z Collecting ml_dtypes>=0.5.0 (from jax->mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:09.7484867Z   Downloading ml_dtypes-0.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
2026-10-03T16:47:09.7631266Z Collecting opt_einsum (from jax->mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-03T16:47:09.7665786Z   Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
2026-10-03T16:47:09.8255924Z Collecting MarkupSafe>=2.0 (from jinja2->torch==2.11.0->-r requirements.txt (line 4))
2026-10-03T16:47:09.8294012Z   Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
2026-10-03T16:47:09.8513493Z Downloading scenedetect-0.7-py3-none-any.whl (134 kB)
2026-10-03T16:47:09.8639057Z Downloading transnetv2_pytorch-1.0.5-py3-none-any.whl (32.7 MB)
2026-10-03T16:47:10.1937544Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.7/32.7 MB 100.5 MB/s  0:00:00
2026-10-03T16:47:10.2022386Z Downloading ultralytics-8.4.46-py3-none-any.whl (1.2 MB)
2026-10-03T16:47:10.2164650Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 107.1 MB/s  0:00:00
2026-10-03T16:47:10.2217427Z Downloading torch-2.11.0-cp311-cp311-manylinux_2_28_x86_64.whl (530.6 MB)
2026-10-03T16:47:16.0100869Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 530.6/530.6 MB 66.8 MB/s  0:00:05
2026-10-03T16:47:16.0149102Z Downloading torchvision-0.26.0-cp311-cp311-manylinux_2_28_x86_64.whl (7.5 MB)
2026-10-03T16:47:16.0556467Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 189.7 MB/s  0:00:00
2026-10-03T16:47:16.0603892Z Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
2026-10-03T16:47:16.0667873Z Downloading faster_whisper-1.2.1-py3-none-any.whl (1.1 MB)
2026-10-03T16:47:16.0956955Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 37.5 MB/s  0:00:00
2026-10-03T16:47:16.1015504Z Downloading py3langid-0.3.0-py3-none-any.whl (746 kB)
2026-10-03T16:47:16.1071036Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 746.1/746.1 kB 159.0 MB/s  0:00:00
2026-10-03T16:47:16.1106591Z Downloading google_genai-1.75.0-py3-none-any.whl (793 kB)
2026-10-03T16:47:16.1221116Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 793.7/793.7 kB 89.9 MB/s  0:00:00
2026-10-03T16:47:16.1259305Z Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-10-03T16:47:16.1320449Z Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
2026-10-03T16:47:16.1406760Z Downloading mediapipe-0.10.14-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (35.7 MB)
2026-10-03T16:47:16.4534389Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.7/35.7 MB 114.3 MB/s  0:00:00
2026-10-03T16:47:16.4577885Z Downloading boto3-1.43.4-py3-none-any.whl (140 kB)
2026-10-03T16:47:16.4667815Z Downloading fastapi-0.136.1-py3-none-any.whl (117 kB)
2026-10-03T16:47:16.4723031Z Downloading uvicorn-0.46.0-py3-none-any.whl (70 kB)
2026-10-03T16:47:16.4774621Z Downloading python_multipart-0.0.27-py3-none-any.whl (29 kB)
2026-10-03T16:47:16.4884474Z Downloading pillow-12.2.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
2026-10-03T16:47:16.5726765Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 83.8 MB/s  0:00:00
2026-10-03T16:47:16.5766190Z Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
2026-10-03T16:47:16.5823263Z Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl (2.4 kB)
2026-10-03T16:47:16.5875255Z Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_x86_64.whl (366.1 MB)
2026-10-03T16:47:20.0985050Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 366.1/366.1 MB 94.5 MB/s  0:00:03
2026-10-03T16:47:20.1054373Z Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_x86_64.whl (169.9 MB)
2026-10-03T16:47:21.5410981Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 169.9/169.9 MB 118.4 MB/s  0:00:01
2026-10-03T16:47:21.5467464Z Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_x86_64.whl (196.5 MB)
2026-10-03T16:47:23.3984583Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 196.5/196.5 MB 106.2 MB/s  0:00:01
2026-10-03T16:47:23.4028227Z Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (60.4 MB)
2026-10-03T16:47:23.6469040Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.4/60.4 MB 249.8 MB/s  0:00:00
2026-10-03T16:47:23.6542439Z Downloading triton-3.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (188.2 MB)
2026-10-03T16:47:25.8515490Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 188.2/188.2 MB 85.6 MB/s  0:00:02
2026-10-03T16:47:25.8559109Z Downloading anyio-4.15.1-py3-none-any.whl (132 kB)
2026-10-03T16:47:25.8616534Z Downloading botocore-1.43.108-py3-none-any.whl (16.0 MB)
2026-10-03T16:47:25.9186748Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.0/16.0 MB 289.8 MB/s  0:00:00
2026-10-03T16:47:25.9226480Z Downloading click-8.5.0-py3-none-any.whl (125 kB)
2026-10-03T16:47:25.9290902Z Downloading ctranslate2-4.8.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (39.4 MB)
2026-10-03T16:47:26.2942309Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.4/39.4 MB 108.0 MB/s  0:00:00
2026-10-03T16:47:26.3049209Z Downloading cuda_bindings-13.4.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (7.2 MB)
2026-10-03T16:47:26.3450346Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 183.2 MB/s  0:00:00
2026-10-03T16:47:26.3498257Z Downloading distro-1.9.0-py3-none-any.whl (20 kB)
2026-10-03T16:47:26.3557474Z Downloading google_auth-2.59.1-py3-none-any.whl (263 kB)
2026-10-03T16:47:26.3615137Z Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-10-03T16:47:26.3665103Z Downloading jmespath-1.1.0-py3-none-any.whl (20 kB)
2026-10-03T16:47:26.3723771Z Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_x86_64.whl (423.1 MB)
2026-10-03T16:47:31.9595878Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.1/423.1 MB 57.5 MB/s  0:00:05
2026-10-03T16:47:31.9636337Z Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl (10.7 MB)
2026-10-03T16:47:32.0306487Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.7/10.7 MB 164.5 MB/s  0:00:00
2026-10-03T16:47:32.0352687Z Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (90.2 MB)
2026-10-03T16:47:32.3816088Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.2/90.2 MB 263.4 MB/s  0:00:00
2026-10-03T16:47:32.3853829Z Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (2.2 MB)
2026-10-03T16:47:32.3946668Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 283.1 MB/s  0:00:00
2026-10-03T16:47:32.3981357Z Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (214.1 MB)
2026-10-03T16:47:33.1561519Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 214.1/214.1 MB 283.1 MB/s  0:00:00
2026-10-03T16:47:33.1598764Z Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.2 MB)
2026-10-03T16:47:33.1664819Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 214.0 MB/s  0:00:00
2026-10-03T16:47:33.1706675Z Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl (59.5 MB)
2026-10-03T16:47:33.3635891Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.5/59.5 MB 311.6 MB/s  0:00:00
2026-10-03T16:47:33.3677389Z Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl (200.9 MB)
2026-10-03T16:47:34.1054542Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200.9/200.9 MB 273.3 MB/s  0:00:00
2026-10-03T16:47:34.1101199Z Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (145.9 MB)
2026-10-03T16:47:34.5832988Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 145.9/145.9 MB 309.6 MB/s  0:00:00
2026-10-03T16:47:34.5874098Z Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (40.7 MB)
2026-10-03T16:47:34.9415236Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.7/40.7 MB 116.4 MB/s  0:00:00
2026-10-03T16:47:34.9453947Z Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (148 kB)
2026-10-03T16:47:34.9508896Z Downloading onnxruntime-1.30.0-cp311-cp311-manylinux_2_28_x86_64.whl (23.6 MB)
2026-10-03T16:47:35.1360592Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.6/23.6 MB 128.7 MB/s  0:00:00
2026-10-03T16:47:35.1396120Z Downloading protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl (295 kB)
2026-10-03T16:47:35.1455913Z Downloading pydantic-2.13.5-py3-none-any.whl (472 kB)
2026-10-03T16:47:35.1517012Z Downloading pydantic_core-2.46.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-10-03T16:47:35.1599260Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 297.4 MB/s  0:00:00
2026-10-03T16:47:35.1633337Z Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2026-10-03T16:47:35.1688503Z Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
2026-10-03T16:47:35.1739761Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 180.0 MB/s  0:00:00
2026-10-03T16:47:35.1776300Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-10-03T16:47:35.1835027Z Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (269 kB)
2026-10-03T16:47:35.1921848Z Downloading idna-3.20-py3-none-any.whl (69 kB)
2026-10-03T16:47:35.1972301Z Downloading s3transfer-0.17.1-py3-none-any.whl (88 kB)
2026-10-03T16:47:35.2021739Z Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
2026-10-03T16:47:35.2072247Z Downloading tokenizers-0.23.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)
2026-10-03T16:47:35.2403086Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 102.2 MB/s  0:00:00
2026-10-03T16:47:35.2460792Z Downloading huggingface_hub-1.33.0-py3-none-any.whl (846 kB)
2026-10-03T16:47:35.2523127Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 846.4/846.4 kB 151.3 MB/s  0:00:00
2026-10-03T16:47:35.2561208Z Downloading hf_xet-1.6.0-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.5 MB)
2026-10-03T16:47:35.2729885Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 289.9 MB/s  0:00:00
2026-10-03T16:47:35.2766683Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-10-03T16:47:35.2821096Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
2026-10-03T16:47:35.2878606Z Downloading websockets-16.1.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (186 kB)
2026-10-03T16:47:35.2937320Z Downloading yt_dlp-2026.8.19-py3-none-any.whl (3.2 MB)
2026-10-03T16:47:35.3353506Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 84.6 MB/s  0:00:00
2026-10-03T16:47:35.3417475Z Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)
2026-10-03T16:47:35.3473968Z Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
2026-10-03T16:47:35.3527528Z Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
2026-10-03T16:47:35.3580212Z Downloading av-18.1.0-cp311-abi3-manylinux_2_28_x86_64.whl (35.8 MB)
2026-10-03T16:47:35.6111386Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.8/35.8 MB 142.1 MB/s  0:00:00
2026-10-03T16:47:35.6149990Z Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
2026-10-03T16:47:35.6206653Z Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl (4.8 MB)
2026-10-03T16:47:35.6370270Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 319.8 MB/s  0:00:00
2026-10-03T16:47:35.6405142Z Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (217 kB)
2026-10-03T16:47:35.6458546Z Downloading cuda_pathfinder-1.8.3-py3-none-any.whl (62 kB)
2026-10-03T16:47:35.6506808Z Downloading filelock-4.0.9-py3-none-any.whl (110 kB)
2026-10-03T16:47:35.6558698Z Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
2026-10-03T16:47:35.6612109Z Downloading fsspec-2026.9.0-py3-none-any.whl (221 kB)
2026-10-03T16:47:35.6672736Z Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-10-03T16:47:35.6720982Z Downloading matplotlib-3.11.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (9.9 MB)
2026-10-03T16:47:35.7364694Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 157.7 MB/s  0:00:00
2026-10-03T16:47:35.7411466Z Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (355 kB)
2026-10-03T16:47:35.7470135Z Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
2026-10-03T16:47:35.7525609Z Downloading fonttools-4.66.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.4 MB)
2026-10-03T16:47:35.7693839Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 360.2 MB/s  0:00:00
2026-10-03T16:47:35.7728974Z Downloading kiwisolver-1.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.4 MB)
2026-10-03T16:47:35.7866072Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 132.8 MB/s  0:00:00
2026-10-03T16:47:35.7901333Z Downloading networkx-3.6.1-py3-none-any.whl (2.1 MB)
2026-10-03T16:47:35.8015474Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 195.7 MB/s  0:00:00
2026-10-03T16:47:35.8049269Z Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
2026-10-03T16:47:35.8567029Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 337.1 MB/s  0:00:00
2026-10-03T16:47:35.8607485Z Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl (73.8 MB)
2026-10-03T16:47:36.9977695Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.8/73.8 MB 64.8 MB/s  0:00:01
2026-10-03T16:47:37.0019634Z Downloading packaging-26.3-py3-none-any.whl (129 kB)
2026-10-03T16:47:37.1365435Z Downloading polars-1.44.2-py3-none-any.whl (865 kB)
2026-10-03T16:47:37.1454310Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 865.8/865.8 kB 89.8 MB/s  0:00:00
2026-10-03T16:47:37.1493314Z Downloading polars_runtime_32-1.44.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (49.9 MB)
2026-10-03T16:47:37.6251466Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.9/49.9 MB 105.1 MB/s  0:00:00
2026-10-03T16:47:37.6291593Z Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl (155 kB)
2026-10-03T16:47:37.6352763Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
2026-10-03T16:47:37.6425436Z Downloading pyasn1-0.6.4-py3-none-any.whl (84 kB)
2026-10-03T16:47:37.6493340Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
2026-10-03T16:47:37.6605655Z Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
2026-10-03T16:47:37.7917748Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 278.2 MB/s  0:00:00
2026-10-03T16:47:37.7954069Z Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-10-03T16:47:37.8002786Z Downloading sounddevice-0.5.6-py3-none-any.whl (32 kB)
2026-10-03T16:47:37.8056408Z Downloading soupsieve-2.10-py3-none-any.whl (38 kB)
2026-10-03T16:47:37.8113246Z Downloading starlette-1.7.0-py3-none-any.whl (78 kB)
2026-10-03T16:47:37.8164034Z Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
2026-10-03T16:47:37.8356251Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 355.7 MB/s  0:00:00
2026-10-03T16:47:37.8395117Z Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
2026-10-03T16:47:37.8441448Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 108.2 MB/s  0:00:00
2026-10-03T16:47:37.8477284Z Downloading typing_inspection-0.4.4-py3-none-any.whl (14 kB)
2026-10-03T16:47:37.8530898Z Downloading ultralytics_thop-2.2.2-py3-none-any.whl (32 kB)
2026-10-03T16:47:37.8582685Z Downloading absl_py-2.5.0-py3-none-any.whl (137 kB)
2026-10-03T16:47:37.8635255Z Downloading ffmpeg_python-0.2.0-py3-none-any.whl (25 kB)
2026-10-03T16:47:37.8687751Z Downloading future-1.0.0-py3-none-any.whl (491 kB)
2026-10-03T16:47:37.8813055Z Downloading jax-0.10.2-py3-none-any.whl (3.2 MB)
2026-10-03T16:47:37.8965344Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 229.9 MB/s  0:00:00
2026-10-03T16:47:37.9012338Z Downloading jaxlib-0.10.2-cp311-cp311-manylinux_2_27_x86_64.whl (85.4 MB)
2026-10-03T16:47:38.4605291Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.4/85.4 MB 153.1 MB/s  0:00:00
2026-10-03T16:47:38.4683264Z Downloading ml_dtypes-0.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (412 kB)
2026-10-03T16:47:38.4753014Z Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
2026-10-03T16:47:38.4814876Z Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2026-10-03T16:47:38.4900242Z Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl (82.1 MB)
2026-10-03T16:47:39.1176446Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.1/82.1 MB 130.9 MB/s  0:00:00
2026-10-03T16:47:39.1213392Z Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
2026-10-03T16:47:39.1332779Z Downloading pandas-3.0.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.1 MB)
2026-10-03T16:47:39.1696335Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 322.8 MB/s  0:00:00
2026-10-03T16:47:39.1738422Z Downloading platformdirs-4.12.2-py3-none-any.whl (32 kB)
2026-10-03T16:47:39.1789672Z Downloading pycparser-3.0-py3-none-any.whl (48 kB)
2026-10-03T16:47:39.1856675Z Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
2026-10-03T16:47:42.2158162Z Installing collected packages: nvidia-cusparselt-cu13, mpmath, flatbuffers, cuda-toolkit, yt-dlp, websockets, urllib3, typing-extensions, triton, tqdm, tenacity, sympy, soupsieve, sniffio, six, pyyaml, python-multipart, python-dotenv, pyparsing, pycparser, pyasn1, psutil, protobuf, polars-runtime-32, platformdirs, Pillow, packaging, opt_einsum, nvidia-nvtx, nvidia-nvshmem-cu13, nvidia-nvjitlink, nvidia-nccl-cu13, nvidia-curand, nvidia-cufile, nvidia-cuda-runtime, nvidia-cuda-nvrtc, nvidia-cuda-cupti, nvidia-cublas, numpy, networkx, MarkupSafe, kiwisolver, jmespath, idna, hf-xet, h11, future, fsspec, fonttools, filelock, distro, cycler, cuda-pathfinder, click, charset_normalizer, certifi, av, attrs, annotated-types, annotated-doc, absl-py, uvicorn, typing-inspection, scipy, requests, python-dateutil, pydantic-core, pyasn1-modules, py3langid, polars, opencv-python, opencv-contrib-python, onnxruntime, nvidia-cusparse, nvidia-cufft, nvidia-cudnn-cu13, ml_dtypes, jinja2, httpcore, ffmpeg-python, cuda-bindings, ctranslate2, contourpy, cffi, beautifulsoup4, anyio, starlette, sounddevice, scenedetect, pydantic, pandas, nvidia-cusolver, matplotlib, jaxlib, httpx, cryptography, botocore, s3transfer, jax, huggingface-hub, google-auth, fastapi, torch, tokenizers, mediapipe, boto3, ultralytics-thop, transnetv2-pytorch, torchvision, google-genai, faster-whisper, ultralytics
2026-10-03T16:48:43.3118685Z 
2026-10-03T16:48:43.3165278Z Successfully installed MarkupSafe-3.0.4 Pillow-12.2.0 absl-py-2.5.0 annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 attrs-26.1.0 av-18.1.0 beautifulsoup4-4.14.3 boto3-1.43.4 botocore-1.43.108 certifi-2026.7.22 cffi-2.1.1 charset_normalizer-3.5.2 click-8.5.0 contourpy-1.3.3 cryptography-50.0.2 ctranslate2-4.8.2 cuda-bindings-13.4.3 cuda-pathfinder-1.8.3 cuda-toolkit-13.0.2 cycler-0.12.1 distro-1.9.0 fastapi-0.136.1 faster-whisper-1.2.1 ffmpeg-python-0.2.0 filelock-4.0.9 flatbuffers-25.12.19 fonttools-4.66.1 fsspec-2026.9.0 future-1.0.0 google-auth-2.59.1 google-genai-1.75.0 h11-0.16.0 hf-xet-1.6.0 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-1.33.0 idna-3.20 jax-0.10.2 jaxlib-0.10.2 jinja2-3.1.6 jmespath-1.1.0 kiwisolver-1.5.1 matplotlib-3.11.2 mediapipe-0.10.14 ml_dtypes-0.6.0 mpmath-1.3.0 networkx-3.6.1 numpy-2.4.6 nvidia-cublas-13.1.0.3 nvidia-cuda-cupti-13.0.85 nvidia-cuda-nvrtc-13.0.88 nvidia-cuda-runtime-13.0.96 nvidia-cudnn-cu13-9.19.0.56 nvidia-cufft-12.0.0.61 nvidia-cufile-1.15.1.6 nvidia-curand-10.4.0.35 nvidia-cusolver-12.0.4.66 nvidia-cusparse-12.6.3.3 nvidia-cusparselt-cu13-0.8.0 nvidia-nccl-cu13-2.28.9 nvidia-nvjitlink-13.0.88 nvidia-nvshmem-cu13-3.4.5 nvidia-nvtx-13.0.85 onnxruntime-1.30.0 opencv-contrib-python-5.0.0.93 opencv-python-5.0.0.93 opt_einsum-3.4.0 packaging-26.3 pandas-3.0.6 platformdirs-4.12.2 polars-1.44.2 polars-runtime-32-1.44.2 protobuf-4.25.9 psutil-7.2.2 py3langid-0.3.0 pyasn1-0.6.4 pyasn1-modules-0.4.2 pycparser-3.0 pydantic-2.13.5 pydantic-core-2.46.5 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 python-multipart-0.0.27 pyyaml-6.0.3 requests-2.34.2 s3transfer-0.17.1 scenedetect-0.7 scipy-1.17.1 six-1.17.0 sniffio-1.3.1 sounddevice-0.5.6 soupsieve-2.10 starlette-1.7.0 sympy-1.14.0 tenacity-9.1.4 tokenizers-0.23.2 torch-2.11.0 torchvision-0.26.0 tqdm-4.67.3 transnetv2-pytorch-1.0.5 triton-3.6.0 typing-extensions-4.16.0 typing-inspection-0.4.4 ultralytics-8.4.46 ultralytics-thop-2.2.2 urllib3-2.8.0 uvicorn-0.46.0 websockets-16.1.1 yt-dlp-2026.8.19
2026-10-03T16:48:43.8938388Z ##[group]Run python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
2026-10-03T16:48:43.8939016Z [36;1mpython main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"[0m
2026-10-03T16:48:43.9078455Z shell: /usr/bin/bash -e {0}
2026-10-03T16:48:43.9078739Z env:
2026-10-03T16:48:43.9079055Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:48:43.9079536Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-03T16:48:43.9080002Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:48:43.9080408Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:48:43.9080814Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-03T16:48:43.9081236Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-03T16:48:43.9081883Z   GEMINI_API_KEY: ***
2026-10-03T16:48:43.9082110Z ##[endgroup]
2026-10-03T16:48:46.3251459Z Creating new Ultralytics Settings v0.0.6 file ✅ 
2026-10-03T16:48:46.3252479Z View Ultralytics Settings with 'yolo settings' or at '/home/runner/.config/Ultralytics/settings.json'
2026-10-03T16:48:46.3253998Z Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/quickstart/#ultralytics-settings.
2026-10-03T16:48:50.8179452Z Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 227.6MB/s 0.0s
2026-10-03T16:48:50.8596901Z INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
2026-10-03T16:48:50.8666950Z [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
2026-10-03T16:48:50.8669117Z [debug] yt-dlp version stable@2026.08.19 from yt-dlp/yt-dlp [594bd50c2] (pip) API
2026-10-03T16:48:50.8675305Z [debug] params: {'quiet': False, 'verbose': True, 'no_warnings': False, 'cookiefile': None, 'proxy': None, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10, 'nocheckcertificate': True, 'cachedir': False, 'noplaylist': True, 'extractor_args': None, 'js_runtimes': {'node': {}}, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'remote_components': set(), 'compat_opts': set()}
2026-10-03T16:48:50.8745416Z WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
2026-10-03T16:48:50.8747508Z W0000 00:00:1791046130.874344    3912 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
2026-10-03T16:48:50.9247571Z [debug] Python 3.11.16 (CPython x86_64 64bit) - Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 (OpenSSL 3.0.13 30 Jan 2024, glibc 2.39)
2026-10-03T16:48:51.0219631Z [debug] exe versions: ffmpeg 6.1.1 (setts), ffprobe 6.1.1
2026-10-03T16:48:51.0221188Z [debug] Optional libraries: certifi-2026.07.22, requests-2.34.2, sqlite3-3.45.1, urllib3-2.8.0, websockets-16.1.1
2026-10-03T16:48:51.0753635Z [debug] JS runtimes: node-20.20.2 (unsupported)
2026-10-03T16:48:51.0756535Z [debug] Proxy map: {}
2026-10-03T16:48:51.0764824Z [debug] Request Handlers: urllib, requests, websockets
2026-10-03T16:48:51.0769179Z [debug] Plugin directories: none
2026-10-03T16:48:51.1169913Z [debug] Loaded 1744 extractors
2026-10-03T16:48:51.1543574Z Traceback (most recent call last):
2026-10-03T16:48:51.1544580Z 🔍 Debug: yt-dlp version: 2026.08.19
2026-10-03T16:48:51.1545516Z   File "/home/runner/work/openshorts/openshorts/main.py", line 567, in <module>
2026-10-03T16:48:51.1546616Z 📥 Downloading video from YouTube...
2026-10-03T16:48:51.1547442Z     input_video, video_title = download_youtube_video(args.url, output_dir)
2026-10-03T16:48:51.1548571Z                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1550132Z   File "/home/runner/work/openshorts/openshorts/main.py", line 443, in download_youtube_video
2026-10-03T16:48:51.1551330Z     info = ydl.extract_info(url, download=False, process=False)
2026-10-03T16:48:51.1552059Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1553337Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/YoutubeDL.py", line 1720, in extract_info
2026-10-03T16:48:51.1554873Z     return self.__extract_info(url, self.get_info_extractor(key), download, extra_info, process)
2026-10-03T16:48:51.1555898Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1557447Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/YoutubeDL.py", line 1731, in wrapper
2026-10-03T16:48:51.1558822Z     return func(self, *args, **kwargs)
2026-10-03T16:48:51.1559354Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1560557Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/YoutubeDL.py", line 1866, in __extract_info
2026-10-03T16:48:51.1561732Z     ie_result = ie.extract(url)
2026-10-03T16:48:51.1562223Z                 ^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1563374Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/extractor/common.py", line 762, in extract
2026-10-03T16:48:51.1564490Z     self.initialize()
2026-10-03T16:48:51.1565667Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/extractor/common.py", line 671, in initialize
2026-10-03T16:48:51.1566787Z     self._real_initialize()
2026-10-03T16:48:51.1568325Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/extractor/youtube/_video.py", line 1939, in _real_initialize
2026-10-03T16:48:51.1571857Z     self._pot_director = initialize_pot_director(self)
2026-10-03T16:48:51.1572549Z                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1574117Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/extractor/youtube/pot/_director.py", line 378, in initialize_pot_director
2026-10-03T16:48:51.1575757Z     logger, settings = get_provider_logger_and_settings(cache_provider, 'pot:cache')
2026-10-03T16:48:51.1576725Z                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1578535Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/extractor/youtube/pot/_director.py", line 374, in get_provider_logger_and_settings
2026-10-03T16:48:51.1579969Z     ie.get_param('extractor_args', {}).get(extractor_key, {}))
2026-10-03T16:48:51.1580614Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-03T16:48:51.1581322Z AttributeError: 'NoneType' object has no attribute 'get'
2026-10-03T16:48:52.0272191Z ##[error]Process completed with exit code 1.
2026-10-03T16:48:52.0434215Z Post job cleanup.
2026-10-03T16:48:52.1355611Z [command]/usr/bin/git version
2026-10-03T16:48:52.1403293Z git version 2.55.0
2026-10-03T16:48:52.1447919Z Temporarily overriding HOME='/home/runner/work/_temp/bfa47379-fcbf-4522-92d8-78e1dd443ce4' before making global git config changes
2026-10-03T16:48:52.1449393Z Adding repository directory to the temporary git global config as a safe directory
2026-10-03T16:48:52.1455558Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/openshorts/openshorts
2026-10-03T16:48:52.1496321Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-10-03T16:48:52.1534320Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-10-03T16:48:52.1817246Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-03T16:48:52.1851200Z http.https://github.com/.extraheader
2026-10-03T16:48:52.1864337Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-10-03T16:48:52.1906198Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-10-03T16:48:52.2183765Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-03T16:48:52.2229514Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-03T16:48:52.2686544Z Cleaning up orphan processes
2026-10-03T16:48:52.3097721Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-node@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
