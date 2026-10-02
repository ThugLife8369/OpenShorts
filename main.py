2026-10-02T05:03:28.8492003Z Current runner version: '2.337.0'
2026-10-02T05:03:28.8519958Z ##[group]Runner Image Provisioner
2026-10-02T05:03:28.8521235Z Hosted Compute Agent
2026-10-02T05:03:28.8521910Z Version: 20260901.588
2026-10-02T05:03:28.8522764Z Commit: f88ec8081b781fac6c440065ac7ff9e710ce3d0b
2026-10-02T05:03:28.8523619Z Build Date: 2026-09-01T19:56:44Z
2026-10-02T05:03:28.8524558Z Worker ID: {a9bc3409-f1d7-4475-afd4-9b4eb02b4d23}
2026-10-02T05:03:28.8525394Z Azure Region: westus
2026-10-02T05:03:28.8526147Z ##[endgroup]
2026-10-02T05:03:28.8528018Z ##[group]Operating System
2026-10-02T05:03:28.8529291Z Ubuntu
2026-10-02T05:03:28.8529964Z 24.04.5
2026-10-02T05:03:28.8530560Z LTS
2026-10-02T05:03:28.8531152Z ##[endgroup]
2026-10-02T05:03:28.8531780Z ##[group]Runner Image
2026-10-02T05:03:28.8532474Z Image: ubuntu-24.04
2026-10-02T05:03:28.8533140Z Version: 20260927.320.1
2026-10-02T05:03:28.8534947Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260927.320/images/ubuntu/Ubuntu2404-Readme.md
2026-10-02T05:03:28.8536730Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260927.320
2026-10-02T05:03:28.8537803Z ##[endgroup]
2026-10-02T05:03:28.8539329Z ##[group]GITHUB_TOKEN Permissions
2026-10-02T05:03:28.8541690Z Contents: read
2026-10-02T05:03:28.8542449Z Metadata: read
2026-10-02T05:03:28.8543060Z Packages: read
2026-10-02T05:03:28.8543663Z ##[endgroup]
2026-10-02T05:03:28.8546046Z Secret source: Actions
2026-10-02T05:03:28.8547083Z Cache mode: write
2026-10-02T05:03:28.8548270Z Prepare workflow directory
2026-10-02T05:03:28.8923818Z Prepare all required actions
2026-10-02T05:03:28.8976026Z Getting action download info
2026-10-02T05:03:29.2542785Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-10-02T05:03:29.3573089Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-10-02T05:03:29.5493290Z Complete job name: run-pipeline
2026-10-02T05:03:29.6327909Z ##[group]Run actions/checkout@v4
2026-10-02T05:03:29.6329135Z with:
2026-10-02T05:03:29.6329630Z   repository: ThugLife8369/openshorts
2026-10-02T05:03:29.6333478Z   token: ***
2026-10-02T05:03:29.6333949Z   ssh-strict: true
2026-10-02T05:03:29.6334426Z   ssh-user: git
2026-10-02T05:03:29.6334913Z   persist-credentials: true
2026-10-02T05:03:29.6335437Z   clean: true
2026-10-02T05:03:29.6335926Z   sparse-checkout-cone-mode: true
2026-10-02T05:03:29.6336489Z   fetch-depth: 1
2026-10-02T05:03:29.6336965Z   fetch-tags: false
2026-10-02T05:03:29.6337432Z   show-progress: true
2026-10-02T05:03:29.6337912Z   lfs: false
2026-10-02T05:03:29.6338522Z   submodules: false
2026-10-02T05:03:29.6339012Z   set-safe-directory: true
2026-10-02T05:03:29.6339551Z   allow-unsafe-pr-checkout: false
2026-10-02T05:03:29.6340397Z ##[endgroup]
2026-10-02T05:03:29.7440677Z Syncing repository: ThugLife8369/openshorts
2026-10-02T05:03:29.7443691Z ##[group]Getting Git version info
2026-10-02T05:03:29.7445110Z Working directory is '/home/runner/work/openshorts/openshorts'
2026-10-02T05:03:29.7447061Z [command]/usr/bin/git version
2026-10-02T05:03:29.7510378Z git version 2.55.0
2026-10-02T05:03:29.7537112Z ##[endgroup]
2026-10-02T05:03:29.7567497Z Temporarily overriding HOME='/home/runner/work/_temp/ddd89bf0-b247-4389-a593-8b10c2043109' before making global git config changes
2026-10-02T05:03:29.7570260Z Adding repository directory to the temporary git global config as a safe directory
2026-10-02T05:03:29.7572173Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/openshorts/openshorts
2026-10-02T05:03:29.7624390Z Deleting the contents of '/home/runner/work/openshorts/openshorts'
2026-10-02T05:03:29.7629535Z ##[group]Initializing the repository
2026-10-02T05:03:29.7635072Z [command]/usr/bin/git init /home/runner/work/openshorts/openshorts
2026-10-02T05:03:29.7757869Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-10-02T05:03:29.7759981Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-10-02T05:03:29.7768956Z hint: to use in all of your new repositories, which will suppress this warning,
2026-10-02T05:03:29.7781276Z hint: call:
2026-10-02T05:03:29.7789462Z hint:
2026-10-02T05:03:29.7790568Z hint: 	git config --global init.defaultBranch <name>
2026-10-02T05:03:29.7791674Z hint:
2026-10-02T05:03:29.7792703Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-10-02T05:03:29.7794448Z hint: 'development'. The just-created branch can be renamed via this command:
2026-10-02T05:03:29.7795869Z hint:
2026-10-02T05:03:29.7796620Z hint: 	git branch -m <name>
2026-10-02T05:03:29.7797488Z hint:
2026-10-02T05:03:29.7798841Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-10-02T05:03:29.7800671Z Initialized empty Git repository in /home/runner/work/openshorts/openshorts/.git/
2026-10-02T05:03:29.7803765Z [command]/usr/bin/git remote add origin https://github.com/ThugLife8369/openshorts
2026-10-02T05:03:29.7842394Z ##[endgroup]
2026-10-02T05:03:29.7843846Z ##[group]Disabling automatic garbage collection
2026-10-02T05:03:29.7846595Z [command]/usr/bin/git config --local gc.auto 0
2026-10-02T05:03:29.7887448Z ##[endgroup]
2026-10-02T05:03:29.7889361Z ##[group]Setting up auth
2026-10-02T05:03:29.7895680Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-10-02T05:03:29.7939622Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-10-02T05:03:29.8368899Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-02T05:03:29.8415506Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-10-02T05:03:29.8669479Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-02T05:03:29.8708645Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-02T05:03:29.8950972Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-10-02T05:03:29.8997487Z ##[endgroup]
2026-10-02T05:03:29.8999097Z ##[group]Fetching the repository
2026-10-02T05:03:29.9008597Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +d3679a867eaa004f01bc5d8b4560344fbfe504cb:refs/remotes/origin/main
2026-10-02T05:03:31.9967676Z From https://github.com/ThugLife8369/openshorts
2026-10-02T05:03:31.9970445Z  * [new ref]         d3679a867eaa004f01bc5d8b4560344fbfe504cb -> origin/main
2026-10-02T05:03:31.9975159Z ##[endgroup]
2026-10-02T05:03:31.9977247Z ##[group]Determining the checkout info
2026-10-02T05:03:31.9979798Z ##[endgroup]
2026-10-02T05:03:31.9983546Z [command]/usr/bin/git sparse-checkout disable
2026-10-02T05:03:32.0054339Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-10-02T05:03:32.0096934Z ##[group]Checking out the ref
2026-10-02T05:03:32.0102787Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-10-02T05:03:32.3891357Z Switched to a new branch 'main'
2026-10-02T05:03:32.3896668Z branch 'main' set up to track 'origin/main'.
2026-10-02T05:03:32.3920928Z ##[endgroup]
2026-10-02T05:03:32.3973802Z [command]/usr/bin/git log -1 --format=%H
2026-10-02T05:03:32.4006443Z d3679a867eaa004f01bc5d8b4560344fbfe504cb
2026-10-02T05:03:32.4454091Z ##[group]Run actions/setup-python@v5
2026-10-02T05:03:32.4455604Z with:
2026-10-02T05:03:32.4456640Z   python-version: 3.11
2026-10-02T05:03:32.4457762Z   cache: pip
2026-10-02T05:03:32.4459033Z   check-latest: false
2026-10-02T05:03:32.4469021Z   token: ***
2026-10-02T05:03:32.4470101Z   update-environment: true
2026-10-02T05:03:32.4471306Z   allow-prereleases: false
2026-10-02T05:03:32.4472764Z   freethreaded: false
2026-10-02T05:03:32.4473856Z ##[endgroup]
2026-10-02T05:03:32.5939950Z ##[group]Installed versions
2026-10-02T05:03:32.6050164Z (node:2314) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-10-02T05:03:32.6053730Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-10-02T05:03:32.6055649Z Successfully set up CPython (3.11.16)
2026-10-02T05:03:32.6058307Z ##[endgroup]
2026-10-02T05:03:32.7021597Z [command]/opt/hostedtoolcache/Python/3.11.16/x64/bin/pip cache dir
2026-10-02T05:03:33.0561739Z /home/runner/.cache/pip
2026-10-02T05:03:33.3810461Z pip cache is not found
2026-10-02T05:03:33.3975601Z ##[group]Run python -m pip install --upgrade pip
2026-10-02T05:03:33.3976235Z [36;1mpython -m pip install --upgrade pip[0m
2026-10-02T05:03:33.3976807Z [36;1mif [ -f requirements.txt ]; then pip install -r requirements.txt; fi[0m
2026-10-02T05:03:33.4264163Z shell: /usr/bin/bash -e {0}
2026-10-02T05:03:33.4264629Z env:
2026-10-02T05:03:33.4265040Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:03:33.4265644Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-02T05:03:33.4266241Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:03:33.4266766Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:03:33.4267299Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:03:33.4267826Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-02T05:03:33.4268668Z ##[endgroup]
2026-10-02T05:03:34.3391997Z Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages (26.2.1)
2026-10-02T05:03:35.6017884Z Collecting scenedetect==0.7 (from -r requirements.txt (line 1))
2026-10-02T05:03:35.7213242Z   Downloading scenedetect-0.7-py3-none-any.whl.metadata (3.9 kB)
2026-10-02T05:03:35.7439337Z Collecting transnetv2-pytorch==1.0.5 (from -r requirements.txt (line 2))
2026-10-02T05:03:35.7676896Z   Downloading transnetv2_pytorch-1.0.5-py3-none-any.whl.metadata (10 kB)
2026-10-02T05:03:35.9033783Z Collecting ultralytics==8.4.46 (from -r requirements.txt (line 3))
2026-10-02T05:03:35.9263759Z   Downloading ultralytics-8.4.46-py3-none-any.whl.metadata (39 kB)
2026-10-02T05:03:36.0158280Z Collecting torch==2.11.0 (from -r requirements.txt (line 4))
2026-10-02T05:03:36.0409627Z   Downloading torch-2.11.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (29 kB)
2026-10-02T05:03:36.1138353Z Collecting torchvision==0.26.0 (from -r requirements.txt (line 5))
2026-10-02T05:03:36.1359294Z   Downloading torchvision-0.26.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (5.5 kB)
2026-10-02T05:03:36.1726131Z Collecting tqdm==4.67.3 (from -r requirements.txt (line 6))
2026-10-02T05:03:36.1947013Z   Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
2026-10-02T05:03:36.3006278Z Collecting yt-dlp (from -r requirements.txt (line 7))
2026-10-02T05:03:36.3237847Z   Downloading yt_dlp-2026.8.19-py3-none-any.whl.metadata (183 kB)
2026-10-02T05:03:36.3829992Z Collecting faster-whisper==1.2.1 (from -r requirements.txt (line 8))
2026-10-02T05:03:36.4052662Z   Downloading faster_whisper-1.2.1-py3-none-any.whl.metadata (16 kB)
2026-10-02T05:03:36.5012159Z Collecting py3langid==0.3.0 (from -r requirements.txt (line 9))
2026-10-02T05:03:36.5244075Z   Downloading py3langid-0.3.0-py3-none-any.whl.metadata (13 kB)
2026-10-02T05:03:36.5573448Z Collecting google-genai==1.75.0 (from -r requirements.txt (line 10))
2026-10-02T05:03:36.5792439Z   Downloading google_genai-1.75.0-py3-none-any.whl.metadata (52 kB)
2026-10-02T05:03:36.6079419Z Collecting python-dotenv==1.2.2 (from -r requirements.txt (line 11))
2026-10-02T05:03:36.6300245Z   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
2026-10-02T05:03:36.6629387Z Collecting mediapipe==0.10.14 (from -r requirements.txt (line 12))
2026-10-02T05:03:36.6913295Z   Downloading mediapipe-0.10.14-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.7 kB)
2026-10-02T05:03:36.9396966Z Collecting boto3==1.43.4 (from -r requirements.txt (line 13))
2026-10-02T05:03:36.9627812Z   Downloading boto3-1.43.4-py3-none-any.whl.metadata (6.5 kB)
2026-10-02T05:03:37.0105786Z Collecting fastapi==0.136.1 (from -r requirements.txt (line 15))
2026-10-02T05:03:37.0331911Z   Downloading fastapi-0.136.1-py3-none-any.whl.metadata (28 kB)
2026-10-02T05:03:37.0694145Z Collecting uvicorn==0.46.0 (from -r requirements.txt (line 16))
2026-10-02T05:03:37.0929520Z   Downloading uvicorn-0.46.0-py3-none-any.whl.metadata (6.7 kB)
2026-10-02T05:03:37.1161684Z Collecting python-multipart==0.0.27 (from -r requirements.txt (line 17))
2026-10-02T05:03:37.1388930Z   Downloading python_multipart-0.0.27-py3-none-any.whl.metadata (2.1 kB)
2026-10-02T05:03:37.1637673Z Collecting httpx==0.28.1 (from -r requirements.txt (line 18))
2026-10-02T05:03:37.1862484Z   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-10-02T05:03:37.3731572Z Collecting Pillow==12.2.0 (from -r requirements.txt (line 19))
2026-10-02T05:03:37.3956835Z   Downloading pillow-12.2.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
2026-10-02T05:03:37.4224712Z Collecting beautifulsoup4==4.14.3 (from -r requirements.txt (line 20))
2026-10-02T05:03:37.4449942Z   Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
2026-10-02T05:03:37.4825194Z Collecting click!=8.3.0,~=8.0 (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-02T05:03:37.5049527Z   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
2026-10-02T05:03:37.7625292Z Collecting numpy (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-02T05:03:37.7847515Z   Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
2026-10-02T05:03:37.8546845Z Collecting opencv-python (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-02T05:03:37.8767619Z   Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (19 kB)
2026-10-02T05:03:37.9076111Z Collecting platformdirs (from scenedetect==0.7->-r requirements.txt (line 1))
2026-10-02T05:03:37.9303418Z   Downloading platformdirs-4.12.2-py3-none-any.whl.metadata (5.5 kB)
2026-10-02T05:03:37.9519687Z Collecting ffmpeg-python (from transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-02T05:03:37.9745968Z   Downloading ffmpeg_python-0.2.0-py3-none-any.whl.metadata (1.7 kB)
2026-10-02T05:03:38.1072262Z Collecting pandas (from transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-02T05:03:38.1331662Z   Downloading pandas-3.0.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
2026-10-02T05:03:38.3649059Z Collecting matplotlib>=3.3.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.3874471Z   Downloading matplotlib-3.11.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (80 kB)
2026-10-02T05:03:38.4501709Z Collecting pyyaml>=5.3.1 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.4722584Z   Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-10-02T05:03:38.5022294Z Collecting requests>=2.23.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.5239292Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-10-02T05:03:38.6665663Z Collecting scipy>=1.4.1 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.6891358Z   Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
2026-10-02T05:03:38.7864777Z Collecting psutil>=5.8.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.8082337Z   Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl.metadata (22 kB)
2026-10-02T05:03:38.9431899Z Collecting polars>=0.20.0 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:38.9656444Z   Downloading polars-1.44.2-py3-none-any.whl.metadata (11 kB)
2026-10-02T05:03:38.9937271Z Collecting ultralytics-thop>=2.0.18 (from ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:39.0174186Z   Downloading ultralytics_thop-2.2.2-py3-none-any.whl.metadata (14 kB)
2026-10-02T05:03:39.0518571Z Collecting filelock (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.0737003Z   Downloading filelock-4.0.9-py3-none-any.whl.metadata (2.0 kB)
2026-10-02T05:03:39.0990387Z Collecting typing-extensions>=4.10.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.1210588Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-10-02T05:03:39.1250840Z Requirement already satisfied: setuptools<82 in /opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages (from torch==2.11.0->-r requirements.txt (line 4)) (79.0.1)
2026-10-02T05:03:39.1463782Z Collecting sympy>=1.13.3 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.1686599Z   Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
2026-10-02T05:03:39.2033505Z Collecting networkx>=2.5.1 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.2265944Z   Downloading networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
2026-10-02T05:03:39.2551211Z Collecting jinja2 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.2771002Z   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2026-10-02T05:03:39.3077557Z Collecting fsspec>=0.8.5 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.3297499Z   Downloading fsspec-2026.9.0-py3-none-any.whl.metadata (10 kB)
2026-10-02T05:03:39.3680180Z Collecting cuda-toolkit==13.0.2 (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.3917242Z   Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl.metadata (9.4 kB)
2026-10-02T05:03:39.5091989Z Collecting cuda-bindings<14,>=13.0.3 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.5314161Z   Downloading cuda_bindings-13.4.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-10-02T05:03:39.5570698Z Collecting nvidia-cudnn-cu13==9.19.0.56 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.5906098Z   Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_x86_64.whl.metadata (1.9 kB)
2026-10-02T05:03:39.6122196Z Collecting nvidia-cusparselt-cu13==0.8.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.6377854Z   Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_x86_64.whl.metadata (12 kB)
2026-10-02T05:03:39.6604918Z Collecting nvidia-nccl-cu13==2.28.9 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.6948002Z   Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_x86_64.whl.metadata (2.0 kB)
2026-10-02T05:03:39.7164125Z Collecting nvidia-nvshmem-cu13==3.4.5 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.7383559Z   Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)
2026-10-02T05:03:39.7681703Z Collecting triton==3.6.0 (from torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:39.7929178Z   Downloading triton-3.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:39.8926515Z Collecting ctranslate2<5,>=4.0 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:39.9166205Z   Downloading ctranslate2-4.8.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
2026-10-02T05:03:39.9728801Z Collecting huggingface-hub>=0.21 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:39.9949484Z   Downloading huggingface_hub-2.1.1-py3-none-any.whl.metadata (16 kB)
2026-10-02T05:03:40.1573235Z Collecting tokenizers<1,>=0.13 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:40.1803377Z   Downloading tokenizers-0.23.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.8 kB)
2026-10-02T05:03:40.2536178Z Collecting onnxruntime<2,>=1.14 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:40.2760274Z   Downloading onnxruntime-1.30.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (5.7 kB)
2026-10-02T05:03:40.3320620Z Collecting av>=11 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:40.3557072Z   Downloading av-18.1.0-cp311-abi3-manylinux_2_28_x86_64.whl.metadata (5.0 kB)
2026-10-02T05:03:40.3857473Z Collecting anyio<5.0.0,>=4.8.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.4076814Z   Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
2026-10-02T05:03:40.4498754Z Collecting google-auth<3.0.0,>=2.48.1 (from google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.4718870Z   Downloading google_auth-2.59.1-py3-none-any.whl.metadata (6.0 kB)
2026-10-02T05:03:40.6538705Z Collecting pydantic<3.0.0,>=2.9.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.6759446Z   Downloading pydantic-2.13.5-py3-none-any.whl.metadata (110 kB)
2026-10-02T05:03:40.7082271Z Collecting tenacity<9.2.0,>=8.2.3 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.7303336Z   Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
2026-10-02T05:03:40.8474070Z Collecting websockets<17.0,>=13.0.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.8694120Z   Downloading websockets-16.1.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
2026-10-02T05:03:40.8915014Z Collecting distro<2,>=1.7.0 (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.9134196Z   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
2026-10-02T05:03:40.9340881Z Collecting sniffio (from google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:40.9562866Z   Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
2026-10-02T05:03:40.9855468Z Collecting certifi (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-02T05:03:41.0086609Z   Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
2026-10-02T05:03:41.0360073Z Collecting httpcore==1.* (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-02T05:03:41.0601987Z   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-10-02T05:03:41.0864422Z Collecting idna (from httpx==0.28.1->-r requirements.txt (line 18))
2026-10-02T05:03:41.1089855Z   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
2026-10-02T05:03:41.1344079Z Collecting absl-py (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.1573499Z   Downloading absl_py-2.5.0-py3-none-any.whl.metadata (3.3 kB)
2026-10-02T05:03:41.1799975Z Collecting attrs>=19.1.0 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.2017127Z   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
2026-10-02T05:03:41.2243742Z Collecting flatbuffers>=2.0 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.2479358Z   Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
2026-10-02T05:03:41.2786388Z Collecting jax (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.3023917Z   Downloading jax-0.10.2-py3-none-any.whl.metadata (13 kB)
2026-10-02T05:03:41.3624466Z Collecting jaxlib (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.3852043Z   Downloading jaxlib-0.10.2-cp311-cp311-manylinux_2_27_x86_64.whl.metadata (1.3 kB)
2026-10-02T05:03:41.4527175Z Collecting opencv-contrib-python (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.4746181Z   Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (19 kB)
2026-10-02T05:03:41.7068938Z Collecting protobuf<5,>=4.25.3 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.7293174Z   Downloading protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)
2026-10-02T05:03:41.7594834Z Collecting sounddevice>=0.4.4 (from mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:41.7824836Z   Downloading sounddevice-0.5.6-py3-none-any.whl.metadata (1.4 kB)
2026-10-02T05:03:42.0191727Z Collecting botocore<1.44.0,>=1.43.4 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:42.0410395Z   Downloading botocore-1.43.107-py3-none-any.whl.metadata (5.6 kB)
2026-10-02T05:03:42.0627237Z Collecting jmespath<2.0.0,>=0.7.1 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:42.0856983Z   Downloading jmespath-1.1.0-py3-none-any.whl.metadata (7.6 kB)
2026-10-02T05:03:42.1111490Z Collecting s3transfer<0.18.0,>=0.17.0 (from boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:42.1336321Z   Downloading s3transfer-0.17.1-py3-none-any.whl.metadata (1.7 kB)
2026-10-02T05:03:42.1669780Z Collecting starlette>=0.46.0 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-02T05:03:42.1887740Z   Downloading starlette-1.7.0-py3-none-any.whl.metadata (6.6 kB)
2026-10-02T05:03:42.2112254Z Collecting typing-inspection>=0.4.2 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-02T05:03:42.2352821Z   Downloading typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
2026-10-02T05:03:42.2556422Z Collecting annotated-doc>=0.0.2 (from fastapi==0.136.1->-r requirements.txt (line 15))
2026-10-02T05:03:42.2781613Z   Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)
2026-10-02T05:03:42.3025273Z Collecting h11>=0.8 (from uvicorn==0.46.0->-r requirements.txt (line 16))
2026-10-02T05:03:42.3244422Z   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-10-02T05:03:42.3554048Z Collecting soupsieve>=1.6.1 (from beautifulsoup4==4.14.3->-r requirements.txt (line 20))
2026-10-02T05:03:42.3773916Z   Downloading soupsieve-2.10-py3-none-any.whl.metadata (4.4 kB)
2026-10-02T05:03:42.4064442Z Collecting nvidia-cublas==13.1.0.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.4349406Z   Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.4574402Z Collecting nvidia-cuda-runtime==13.0.96.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.4806331Z   Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.5026705Z Collecting nvidia-cufft==12.0.0.61.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.5249069Z   Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-10-02T05:03:42.5464431Z Collecting nvidia-cufile==1.15.1.6.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.5685310Z   Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.5915668Z Collecting nvidia-cuda-cupti==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.6132994Z   Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.6364208Z Collecting nvidia-curand==10.4.0.35.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.6600170Z   Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.6828670Z Collecting nvidia-cusolver==12.0.4.66.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.7056040Z   Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
2026-10-02T05:03:42.7285735Z Collecting nvidia-cusparse==12.6.3.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.7509347Z   Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-10-02T05:03:42.7742024Z Collecting nvidia-nvjitlink==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.8011869Z   Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.8257766Z Collecting nvidia-cuda-nvrtc==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.8476471Z   Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-10-02T05:03:42.8695945Z Collecting nvidia-nvtx==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:42.8918592Z   Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl.metadata (1.8 kB)
2026-10-02T05:03:42.9261182Z Collecting python-dateutil<3.0.0,>=2.1 (from botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:42.9482185Z   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
2026-10-02T05:03:42.9811984Z Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:43.0031062Z   Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
2026-10-02T05:03:43.0304544Z Collecting cuda-pathfinder>=1.4.2 (from cuda-bindings<14,>=13.0.3->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:43.0527250Z   Downloading cuda_pathfinder-1.8.3-py3-none-any.whl.metadata (1.9 kB)
2026-10-02T05:03:43.0832497Z Collecting pyasn1-modules>=0.2.1 (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:43.1059236Z   Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
2026-10-02T05:03:43.3950033Z Collecting cryptography>=38.0.3 (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:43.4166991Z   Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.4 kB)
2026-10-02T05:03:43.4594160Z Collecting packaging (from onnxruntime<2,>=1.14->faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:43.4815304Z   Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
2026-10-02T05:03:43.5053717Z Collecting annotated-types>=0.6.0 (from pydantic<3.0.0,>=2.9.0->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:43.5273451Z   Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
2026-10-02T05:03:44.2610987Z Collecting pydantic-core==2.46.5 (from pydantic<3.0.0,>=2.9.0->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:44.2861889Z   Downloading pydantic_core-2.46.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
2026-10-02T05:03:44.3120341Z Collecting six>=1.5 (from python-dateutil<3.0.0,>=2.1->botocore<1.44.0,>=1.43.4->boto3==1.43.4->-r requirements.txt (line 13))
2026-10-02T05:03:44.3336429Z   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-10-02T05:03:44.4615585Z Collecting charset_normalizer<4,>=2 (from requests>=2.23.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:44.4849399Z   Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
2026-10-02T05:03:44.5345213Z Collecting huggingface-hub>=0.21 (from faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:44.5570411Z   Downloading huggingface_hub-1.33.0-py3-none-any.whl.metadata (16 kB)
2026-10-02T05:03:44.6179643Z Collecting hf-xet<2.0.0,>=1.6.0 (from huggingface-hub>=0.21->faster-whisper==1.2.1->-r requirements.txt (line 8))
2026-10-02T05:03:44.6431027Z   Downloading hf_xet-1.6.0-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-10-02T05:03:44.7656527Z Collecting cffi>=2.0.0 (from cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:44.7876763Z   Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
2026-10-02T05:03:44.8104805Z Collecting pycparser (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:44.8339416Z   Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
2026-10-02T05:03:44.9108350Z Collecting contourpy>=1.0.1 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:44.9327746Z   Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)
2026-10-02T05:03:44.9594166Z Collecting cycler>=0.10 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:44.9820062Z   Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
2026-10-02T05:03:45.2470379Z Collecting fonttools>=4.28.2 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:45.2700236Z   Downloading fonttools-4.66.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (130 kB)
2026-10-02T05:03:45.3556611Z Collecting kiwisolver>=1.3.1 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:45.3779287Z   Downloading kiwisolver-1.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (5.2 kB)
2026-10-02T05:03:45.4142578Z Collecting pyparsing>=3 (from matplotlib>=3.3.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:45.4431974Z   Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
2026-10-02T05:03:45.4837071Z Collecting polars-runtime-32==1.44.2 (from polars>=0.20.0->ultralytics==8.4.46->-r requirements.txt (line 3))
2026-10-02T05:03:45.5069366Z   Downloading polars_runtime_32-1.44.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
2026-10-02T05:03:45.5401697Z Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai==1.75.0->-r requirements.txt (line 10))
2026-10-02T05:03:45.5621206Z   Downloading pyasn1-0.6.4-py3-none-any.whl.metadata (8.4 kB)
2026-10-02T05:03:45.5967393Z Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:45.6184797Z   Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
2026-10-02T05:03:45.6479345Z Collecting future (from ffmpeg-python->transnetv2-pytorch==1.0.5->-r requirements.txt (line 2))
2026-10-02T05:03:45.6726095Z   Downloading future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
2026-10-02T05:03:45.7113537Z Collecting ml_dtypes>=0.5.0 (from jax->mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:45.7334213Z   Downloading ml_dtypes-0.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
2026-10-02T05:03:45.7549256Z Collecting opt_einsum (from jax->mediapipe==0.10.14->-r requirements.txt (line 12))
2026-10-02T05:03:45.7763509Z   Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
2026-10-02T05:03:45.8391652Z Collecting MarkupSafe>=2.0 (from jinja2->torch==2.11.0->-r requirements.txt (line 4))
2026-10-02T05:03:45.8622124Z   Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
2026-10-02T05:03:45.9004423Z Downloading scenedetect-0.7-py3-none-any.whl (134 kB)
2026-10-02T05:03:45.9296986Z Downloading transnetv2_pytorch-1.0.5-py3-none-any.whl (32.7 MB)
2026-10-02T05:03:46.3331469Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.7/32.7 MB 85.2 MB/s  0:00:00
2026-10-02T05:03:46.3567073Z Downloading ultralytics-8.4.46-py3-none-any.whl (1.2 MB)
2026-10-02T05:03:46.3707996Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 88.6 MB/s  0:00:00
2026-10-02T05:03:46.3944062Z Downloading torch-2.11.0-cp311-cp311-manylinux_2_28_x86_64.whl (530.6 MB)
2026-10-02T05:03:51.1141244Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 530.6/530.6 MB 85.4 MB/s  0:00:04
2026-10-02T05:03:51.1377819Z Downloading torchvision-0.26.0-cp311-cp311-manylinux_2_28_x86_64.whl (7.5 MB)
2026-10-02T05:03:51.1937706Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 136.1 MB/s  0:00:00
2026-10-02T05:03:51.2159651Z Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
2026-10-02T05:03:51.2402844Z Downloading faster_whisper-1.2.1-py3-none-any.whl (1.1 MB)
2026-10-02T05:03:51.2485574Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 148.8 MB/s  0:00:00
2026-10-02T05:03:51.2738613Z Downloading py3langid-0.3.0-py3-none-any.whl (746 kB)
2026-10-02T05:03:51.2795214Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 746.1/746.1 kB 151.5 MB/s  0:00:00
2026-10-02T05:03:51.3023017Z Downloading google_genai-1.75.0-py3-none-any.whl (793 kB)
2026-10-02T05:03:51.3106926Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 793.7/793.7 kB 95.4 MB/s  0:00:00
2026-10-02T05:03:51.3330895Z Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-10-02T05:03:51.3579953Z Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
2026-10-02T05:03:51.3844518Z Downloading mediapipe-0.10.14-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (35.7 MB)
2026-10-02T05:03:51.6745944Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.7/35.7 MB 123.2 MB/s  0:00:00
2026-10-02T05:03:51.6969037Z Downloading boto3-1.43.4-py3-none-any.whl (140 kB)
2026-10-02T05:03:51.7222641Z Downloading fastapi-0.136.1-py3-none-any.whl (117 kB)
2026-10-02T05:03:51.7469561Z Downloading uvicorn-0.46.0-py3-none-any.whl (70 kB)
2026-10-02T05:03:51.7771459Z Downloading python_multipart-0.0.27-py3-none-any.whl (29 kB)
2026-10-02T05:03:51.8025133Z Downloading pillow-12.2.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
2026-10-02T05:03:51.8466664Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 167.1 MB/s  0:00:00
2026-10-02T05:03:51.8686190Z Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
2026-10-02T05:03:51.8932909Z Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl (2.4 kB)
2026-10-02T05:03:51.9178773Z Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_x86_64.whl (366.1 MB)
2026-10-02T05:03:55.6037304Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 366.1/366.1 MB 89.5 MB/s  0:00:03
2026-10-02T05:03:55.6257483Z Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_x86_64.whl (169.9 MB)
2026-10-02T05:03:56.9041677Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 169.9/169.9 MB 133.0 MB/s  0:00:01
2026-10-02T05:03:56.9273508Z Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_x86_64.whl (196.5 MB)
2026-10-02T05:03:58.8966955Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 196.5/196.5 MB 99.9 MB/s  0:00:01
2026-10-02T05:03:58.9190239Z Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (60.4 MB)
2026-10-02T05:03:59.1751564Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.4/60.4 MB 237.7 MB/s  0:00:00
2026-10-02T05:03:59.2007911Z Downloading triton-3.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (188.2 MB)
2026-10-02T05:04:01.3062082Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 188.2/188.2 MB 89.5 MB/s  0:00:02
2026-10-02T05:04:01.3279382Z Downloading anyio-4.15.1-py3-none-any.whl (132 kB)
2026-10-02T05:04:01.3523665Z Downloading botocore-1.43.107-py3-none-any.whl (16.0 MB)
2026-10-02T05:04:01.4312830Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.0/16.0 MB 207.3 MB/s  0:00:00
2026-10-02T05:04:01.4534448Z Downloading click-8.5.0-py3-none-any.whl (125 kB)
2026-10-02T05:04:01.4836906Z Downloading ctranslate2-4.8.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (39.4 MB)
2026-10-02T05:04:01.8290894Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.4/39.4 MB 114.3 MB/s  0:00:00
2026-10-02T05:04:01.8511438Z Downloading cuda_bindings-13.4.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (7.2 MB)
2026-10-02T05:04:01.8890662Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 198.9 MB/s  0:00:00
2026-10-02T05:04:01.9226213Z Downloading distro-1.9.0-py3-none-any.whl (20 kB)
2026-10-02T05:04:01.9566057Z Downloading google_auth-2.59.1-py3-none-any.whl (263 kB)
2026-10-02T05:04:01.9842283Z Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-10-02T05:04:02.0087609Z Downloading jmespath-1.1.0-py3-none-any.whl (20 kB)
2026-10-02T05:04:02.0328491Z Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_x86_64.whl (423.1 MB)
2026-10-02T05:04:07.8644350Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.1/423.1 MB 57.0 MB/s  0:00:05
2026-10-02T05:04:07.8914530Z Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_x86_64.whl (10.7 MB)
2026-10-02T05:04:07.9344361Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.7/10.7 MB 261.5 MB/s  0:00:00
2026-10-02T05:04:07.9572774Z Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (90.2 MB)
2026-10-02T05:04:08.3581114Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.2/90.2 MB 227.4 MB/s  0:00:00
2026-10-02T05:04:08.3813285Z Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (2.2 MB)
2026-10-02T05:04:08.3931232Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 233.9 MB/s  0:00:00
2026-10-02T05:04:08.4161098Z Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (214.1 MB)
2026-10-02T05:04:09.3582012Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 214.1/214.1 MB 227.7 MB/s  0:00:00
2026-10-02T05:04:09.3816739Z Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.2 MB)
2026-10-02T05:04:09.3888559Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 206.6 MB/s  0:00:00
2026-10-02T05:04:09.4118568Z Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_x86_64.whl (59.5 MB)
2026-10-02T05:04:09.6981959Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.5/59.5 MB 210.0 MB/s  0:00:00
2026-10-02T05:04:09.7207524Z Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_x86_64.whl (200.9 MB)
2026-10-02T05:04:10.5999420Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200.9/200.9 MB 229.1 MB/s  0:00:00
2026-10-02T05:04:10.6226833Z Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (145.9 MB)
2026-10-02T05:04:12.2455662Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 145.9/145.9 MB 89.9 MB/s  0:00:01
2026-10-02T05:04:12.2702552Z Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (40.7 MB)
2026-10-02T05:04:12.6081824Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.7/40.7 MB 122.7 MB/s  0:00:00
2026-10-02T05:04:12.6306347Z Downloading nvidia_nvtx-13.0.85-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (148 kB)
2026-10-02T05:04:12.6617548Z Downloading onnxruntime-1.30.0-cp311-cp311-manylinux_2_28_x86_64.whl (23.6 MB)
2026-10-02T05:04:12.8966968Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.6/23.6 MB 101.7 MB/s  0:00:00
2026-10-02T05:04:12.9187457Z Downloading protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl (295 kB)
2026-10-02T05:04:12.9455046Z Downloading pydantic-2.13.5-py3-none-any.whl (472 kB)
2026-10-02T05:04:12.9715312Z Downloading pydantic_core-2.46.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-10-02T05:04:12.9882627Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 126.7 MB/s  0:00:00
2026-10-02T05:04:13.0104376Z Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2026-10-02T05:04:13.0370893Z Downloading pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
2026-10-02T05:04:13.0443853Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 806.6/806.6 kB 117.8 MB/s  0:00:00
2026-10-02T05:04:13.0663729Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-10-02T05:04:13.0912338Z Downloading charset_normalizer-3.5.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (269 kB)
2026-10-02T05:04:13.1159583Z Downloading idna-3.20-py3-none-any.whl (69 kB)
2026-10-02T05:04:13.1399300Z Downloading s3transfer-0.17.1-py3-none-any.whl (88 kB)
2026-10-02T05:04:13.1644045Z Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
2026-10-02T05:04:13.1893821Z Downloading tokenizers-0.23.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)
2026-10-02T05:04:13.2027588Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 301.5 MB/s  0:00:00
2026-10-02T05:04:13.2251578Z Downloading huggingface_hub-1.33.0-py3-none-any.whl (846 kB)
2026-10-02T05:04:13.2308347Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 846.4/846.4 kB 175.1 MB/s  0:00:00
2026-10-02T05:04:13.2549673Z Downloading hf_xet-1.6.0-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.5 MB)
2026-10-02T05:04:13.2721599Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 297.5 MB/s  0:00:00
2026-10-02T05:04:13.2943231Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-10-02T05:04:13.3186997Z Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
2026-10-02T05:04:13.3433100Z Downloading websockets-16.1.1-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (186 kB)
2026-10-02T05:04:13.3771582Z Downloading yt_dlp-2026.8.19-py3-none-any.whl (3.2 MB)
2026-10-02T05:04:13.3921801Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 248.9 MB/s  0:00:00
2026-10-02T05:04:13.4149723Z Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)
2026-10-02T05:04:13.4393861Z Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
2026-10-02T05:04:13.4643623Z Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
2026-10-02T05:04:13.4893888Z Downloading av-18.1.0-cp311-abi3-manylinux_2_28_x86_64.whl (35.8 MB)
2026-10-02T05:04:13.7828835Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.8/35.8 MB 129.9 MB/s  0:00:00
2026-10-02T05:04:13.8049969Z Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
2026-10-02T05:04:13.8305926Z Downloading cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl (4.8 MB)
2026-10-02T05:04:13.8480382Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 308.7 MB/s  0:00:00
2026-10-02T05:04:13.8705340Z Downloading cffi-2.1.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (217 kB)
2026-10-02T05:04:13.8956576Z Downloading cuda_pathfinder-1.8.3-py3-none-any.whl (62 kB)
2026-10-02T05:04:13.9204682Z Downloading filelock-4.0.9-py3-none-any.whl (110 kB)
2026-10-02T05:04:13.9456299Z Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
2026-10-02T05:04:13.9758690Z Downloading fsspec-2026.9.0-py3-none-any.whl (221 kB)
2026-10-02T05:04:14.0218325Z Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-10-02T05:04:14.0506483Z Downloading matplotlib-3.11.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (9.9 MB)
2026-10-02T05:04:14.1031483Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 211.7 MB/s  0:00:00
2026-10-02T05:04:14.1276138Z Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (355 kB)
2026-10-02T05:04:14.1527717Z Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
2026-10-02T05:04:14.1787533Z Downloading fonttools-4.66.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.4 MB)
2026-10-02T05:04:14.2052282Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 221.0 MB/s  0:00:00
2026-10-02T05:04:14.2285792Z Downloading kiwisolver-1.5.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.4 MB)
2026-10-02T05:04:14.2371531Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 201.7 MB/s  0:00:00
2026-10-02T05:04:14.2602539Z Downloading networkx-3.6.1-py3-none-any.whl (2.1 MB)
2026-10-02T05:04:14.2709309Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 229.5 MB/s  0:00:00
2026-10-02T05:04:14.2937455Z Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
2026-10-02T05:04:14.3608633Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 259.5 MB/s  0:00:00
2026-10-02T05:04:14.3962319Z Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl (73.8 MB)
2026-10-02T05:04:14.9437766Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.8/73.8 MB 136.4 MB/s  0:00:00
2026-10-02T05:04:14.9678286Z Downloading packaging-26.3-py3-none-any.whl (129 kB)
2026-10-02T05:04:14.9923460Z Downloading polars-1.44.2-py3-none-any.whl (865 kB)
2026-10-02T05:04:15.0003070Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 865.8/865.8 kB 130.0 MB/s  0:00:00
2026-10-02T05:04:15.0229976Z Downloading polars_runtime_32-1.44.2-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (49.9 MB)
2026-10-02T05:04:15.4312226Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.9/49.9 MB 122.6 MB/s  0:00:00
2026-10-02T05:04:15.4636615Z Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl (155 kB)
2026-10-02T05:04:15.4925659Z Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
2026-10-02T05:04:15.5178203Z Downloading pyasn1-0.6.4-py3-none-any.whl (84 kB)
2026-10-02T05:04:15.5431311Z Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
2026-10-02T05:04:15.5673340Z Downloading scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
2026-10-02T05:04:15.6991567Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 272.5 MB/s  0:00:00
2026-10-02T05:04:15.7209457Z Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-10-02T05:04:15.7450684Z Downloading sounddevice-0.5.6-py3-none-any.whl (32 kB)
2026-10-02T05:04:15.7693149Z Downloading soupsieve-2.10-py3-none-any.whl (38 kB)
2026-10-02T05:04:15.7946703Z Downloading starlette-1.7.0-py3-none-any.whl (78 kB)
2026-10-02T05:04:15.8196538Z Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
2026-10-02T05:04:15.8408720Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 326.5 MB/s  0:00:00
2026-10-02T05:04:15.8630332Z Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
2026-10-02T05:04:15.8684486Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 93.5 MB/s  0:00:00
2026-10-02T05:04:15.8925695Z Downloading typing_inspection-0.4.4-py3-none-any.whl (14 kB)
2026-10-02T05:04:15.9219162Z Downloading ultralytics_thop-2.2.2-py3-none-any.whl (32 kB)
2026-10-02T05:04:15.9476660Z Downloading absl_py-2.5.0-py3-none-any.whl (137 kB)
2026-10-02T05:04:15.9723625Z Downloading ffmpeg_python-0.2.0-py3-none-any.whl (25 kB)
2026-10-02T05:04:15.9965239Z Downloading future-1.0.0-py3-none-any.whl (491 kB)
2026-10-02T05:04:16.0293136Z Downloading jax-0.10.2-py3-none-any.whl (3.2 MB)
2026-10-02T05:04:16.0882311Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 52.6 MB/s  0:00:00
2026-10-02T05:04:16.1183842Z Downloading jaxlib-0.10.2-cp311-cp311-manylinux_2_27_x86_64.whl (85.4 MB)
2026-10-02T05:04:18.1375785Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.4/85.4 MB 42.2 MB/s  0:00:02
2026-10-02T05:04:18.1712092Z Downloading ml_dtypes-0.6.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (412 kB)
2026-10-02T05:04:18.1999202Z Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
2026-10-02T05:04:18.2283521Z Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2026-10-02T05:04:18.2590177Z Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl (82.1 MB)
2026-10-02T05:04:19.1666216Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.1/82.1 MB 90.6 MB/s  0:00:00
2026-10-02T05:04:19.1910170Z Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
2026-10-02T05:04:19.2149326Z Downloading pandas-3.0.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.1 MB)
2026-10-02T05:04:19.2599848Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 256.3 MB/s  0:00:00
2026-10-02T05:04:19.2819854Z Downloading platformdirs-4.12.2-py3-none-any.whl (32 kB)
2026-10-02T05:04:19.3065275Z Downloading pycparser-3.0-py3-none-any.whl (48 kB)
2026-10-02T05:04:19.3313404Z Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
2026-10-02T05:04:22.4002741Z Installing collected packages: nvidia-cusparselt-cu13, mpmath, flatbuffers, cuda-toolkit, yt-dlp, websockets, urllib3, typing-extensions, triton, tqdm, tenacity, sympy, soupsieve, sniffio, six, pyyaml, python-multipart, python-dotenv, pyparsing, pycparser, pyasn1, psutil, protobuf, polars-runtime-32, platformdirs, Pillow, packaging, opt_einsum, nvidia-nvtx, nvidia-nvshmem-cu13, nvidia-nvjitlink, nvidia-nccl-cu13, nvidia-curand, nvidia-cufile, nvidia-cuda-runtime, nvidia-cuda-nvrtc, nvidia-cuda-cupti, nvidia-cublas, numpy, networkx, MarkupSafe, kiwisolver, jmespath, idna, hf-xet, h11, future, fsspec, fonttools, filelock, distro, cycler, cuda-pathfinder, click, charset_normalizer, certifi, av, attrs, annotated-types, annotated-doc, absl-py, uvicorn, typing-inspection, scipy, requests, python-dateutil, pydantic-core, pyasn1-modules, py3langid, polars, opencv-python, opencv-contrib-python, onnxruntime, nvidia-cusparse, nvidia-cufft, nvidia-cudnn-cu13, ml_dtypes, jinja2, httpcore, ffmpeg-python, cuda-bindings, ctranslate2, contourpy, cffi, beautifulsoup4, anyio, starlette, sounddevice, scenedetect, pydantic, pandas, nvidia-cusolver, matplotlib, jaxlib, httpx, cryptography, botocore, s3transfer, jax, huggingface-hub, google-auth, fastapi, torch, tokenizers, mediapipe, boto3, ultralytics-thop, transnetv2-pytorch, torchvision, google-genai, faster-whisper, ultralytics
2026-10-02T05:05:22.2957008Z 
2026-10-02T05:05:22.3007503Z Successfully installed MarkupSafe-3.0.3 Pillow-12.2.0 absl-py-2.5.0 annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 attrs-26.1.0 av-18.1.0 beautifulsoup4-4.14.3 boto3-1.43.4 botocore-1.43.107 certifi-2026.7.22 cffi-2.1.1 charset_normalizer-3.5.2 click-8.5.0 contourpy-1.3.3 cryptography-50.0.2 ctranslate2-4.8.2 cuda-bindings-13.4.3 cuda-pathfinder-1.8.3 cuda-toolkit-13.0.2 cycler-0.12.1 distro-1.9.0 fastapi-0.136.1 faster-whisper-1.2.1 ffmpeg-python-0.2.0 filelock-4.0.9 flatbuffers-25.12.19 fonttools-4.66.1 fsspec-2026.9.0 future-1.0.0 google-auth-2.59.1 google-genai-1.75.0 h11-0.16.0 hf-xet-1.6.0 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-1.33.0 idna-3.20 jax-0.10.2 jaxlib-0.10.2 jinja2-3.1.6 jmespath-1.1.0 kiwisolver-1.5.1 matplotlib-3.11.2 mediapipe-0.10.14 ml_dtypes-0.6.0 mpmath-1.3.0 networkx-3.6.1 numpy-2.4.6 nvidia-cublas-13.1.0.3 nvidia-cuda-cupti-13.0.85 nvidia-cuda-nvrtc-13.0.88 nvidia-cuda-runtime-13.0.96 nvidia-cudnn-cu13-9.19.0.56 nvidia-cufft-12.0.0.61 nvidia-cufile-1.15.1.6 nvidia-curand-10.4.0.35 nvidia-cusolver-12.0.4.66 nvidia-cusparse-12.6.3.3 nvidia-cusparselt-cu13-0.8.0 nvidia-nccl-cu13-2.28.9 nvidia-nvjitlink-13.0.88 nvidia-nvshmem-cu13-3.4.5 nvidia-nvtx-13.0.85 onnxruntime-1.30.0 opencv-contrib-python-5.0.0.93 opencv-python-5.0.0.93 opt_einsum-3.4.0 packaging-26.3 pandas-3.0.6 platformdirs-4.12.2 polars-1.44.2 polars-runtime-32-1.44.2 protobuf-4.25.9 psutil-7.2.2 py3langid-0.3.0 pyasn1-0.6.4 pyasn1-modules-0.4.2 pycparser-3.0 pydantic-2.13.5 pydantic-core-2.46.5 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 python-multipart-0.0.27 pyyaml-6.0.3 requests-2.34.2 s3transfer-0.17.1 scenedetect-0.7 scipy-1.17.1 six-1.17.0 sniffio-1.3.1 sounddevice-0.5.6 soupsieve-2.10 starlette-1.7.0 sympy-1.14.0 tenacity-9.1.4 tokenizers-0.23.2 torch-2.11.0 torchvision-0.26.0 tqdm-4.67.3 transnetv2-pytorch-1.0.5 triton-3.6.0 typing-extensions-4.16.0 typing-inspection-0.4.4 ultralytics-8.4.46 ultralytics-thop-2.2.2 urllib3-2.8.0 uvicorn-0.46.0 websockets-16.1.1 yt-dlp-2026.8.19
2026-10-02T05:05:23.0067245Z ##[group]Run if [ -f "main.py" ]; then
2026-10-02T05:05:23.0067642Z [36;1mif [ -f "main.py" ]; then[0m
2026-10-02T05:05:23.0068398Z [36;1m  python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"[0m
2026-10-02T05:05:23.0068905Z [36;1melif [ -f "OpenShorts/main.py" ]; then[0m
2026-10-02T05:05:23.0069403Z [36;1m  python OpenShorts/main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"[0m
2026-10-02T05:05:23.0069884Z [36;1melse[0m
2026-10-02T05:05:23.0070239Z [36;1m  python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"[0m
2026-10-02T05:05:23.0070911Z [36;1mfi[0m
2026-10-02T05:05:23.0201514Z shell: /usr/bin/bash -e {0}
2026-10-02T05:05:23.0201845Z env:
2026-10-02T05:05:23.0202199Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:05:23.0202776Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib/pkgconfig
2026-10-02T05:05:23.0203345Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:05:23.0203893Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:05:23.0204398Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.16/x64
2026-10-02T05:05:23.0204898Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.16/x64/lib
2026-10-02T05:05:23.0205706Z   GEMINI_API_KEY: ***
2026-10-02T05:05:23.0206203Z   ELEVENLABS_API_KEY: ***
2026-10-02T05:05:23.0206669Z   FAL_KEY: ***
2026-10-02T05:05:23.0208555Z   UPLOAD_POST_API_KEY: ***
2026-10-02T05:05:23.0208890Z   AWS_ACCESS_KEY_ID: ***
2026-10-02T05:05:23.0209278Z   AWS_SECRET_ACCESS_KEY: ***
2026-10-02T05:05:23.0209563Z   AWS_S3_BUCKET: 
2026-10-02T05:05:23.0209846Z   AWS_REGION: us-east-1
2026-10-02T05:05:23.0210110Z ##[endgroup]
2026-10-02T05:05:25.5974431Z Creating new Ultralytics Settings v0.0.6 file ✅ 
2026-10-02T05:05:25.5975287Z View Ultralytics Settings with 'yolo settings' or at '/home/runner/.config/Ultralytics/settings.json'
2026-10-02T05:05:25.5976728Z Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/quickstart/#ultralytics-settings.
2026-10-02T05:05:31.5949130Z Downloading https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 323.4MB/s 0.0s
2026-10-02T05:05:31.6387905Z INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
2026-10-02T05:05:31.6482089Z [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
2026-10-02T05:05:31.6483552Z [debug] yt-dlp version stable@2026.08.19 from yt-dlp/yt-dlp [594bd50c2] (pip) API
2026-10-02T05:05:31.6488267Z [debug] params: {'quiet': False, 'verbose': True, 'no_warnings': False, 'cookiefile': None, 'proxy': None, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10, 'nocheckcertificate': True, 'cachedir': False, 'noplaylist': True, 'extractor_args': {'youtube': {'player_client': ['default', 'mweb']}}, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'js_runtimes': {'deno': {}}, 'remote_components': set(), 'compat_opts': set()}
2026-10-02T05:05:31.6536718Z WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
2026-10-02T05:05:31.6538734Z W0000 00:00:1790917531.653449    2491 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
2026-10-02T05:05:31.7229858Z [debug] Python 3.11.16 (CPython x86_64 64bit) - Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 (OpenSSL 3.0.13 30 Jan 2024, glibc 2.39)
2026-10-02T05:05:31.7255726Z [debug] exe versions: none
2026-10-02T05:05:31.7256775Z [debug] Optional libraries: certifi-2026.07.22, requests-2.34.2, sqlite3-3.45.1, urllib3-2.8.0, websockets-16.1.1
2026-10-02T05:05:31.7265200Z [debug] JS runtimes: none
2026-10-02T05:05:31.7268238Z [debug] Proxy map: {}
2026-10-02T05:05:31.7275327Z [debug] Request Handlers: urllib, requests, websockets
2026-10-02T05:05:31.7279453Z [debug] Plugin directories: none
2026-10-02T05:05:31.7687100Z [debug] Loaded 1744 extractors
2026-10-02T05:05:31.8067982Z [debug] [youtube] [pot] PO Token Providers: none
2026-10-02T05:05:31.8069028Z [debug] [youtube] [pot] PO Token Cache Providers: memory
2026-10-02T05:05:31.8069711Z [debug] [youtube] [pot] PO Token Cache Spec Providers: webpo
2026-10-02T05:05:31.8071803Z [debug] [youtube] [jsc] JS Challenge Providers: bun (unavailable), deno (unavailable), node (unavailable), quickjs (unavailable)
2026-10-02T05:05:31.8079165Z [youtube] Extracting URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
2026-10-02T05:05:31.8089464Z 🔍 Debug: yt-dlp version: 2026.08.19
2026-10-02T05:05:31.8090128Z 📥 Downloading video from YouTube...
2026-10-02T05:05:31.8092234Z [youtube] dQw4w9WgXcQ: Downloading webpage
2026-10-02T05:05:32.8591546Z [debug] [youtube] Forcing "main" player JS variant for player 8ab5c328
2026-10-02T05:05:32.8592501Z         original url = /s/player/8ab5c328/player_es6.vflset/en_US/base.js
2026-10-02T05:05:32.8621641Z [youtube] dQw4w9WgXcQ: Downloading visionos player API JSON
2026-10-02T05:05:32.9766547Z [youtube] dQw4w9WgXcQ: Downloading mweb client config
2026-10-02T05:05:33.2205489Z [debug] [youtube] dQw4w9WgXcQ: Detected experiment to bind GVS PO Token to video ID for mweb client
2026-10-02T05:05:33.2221082Z [youtube] dQw4w9WgXcQ: Downloading mweb player API JSON
2026-10-02T05:05:33.4279301Z [debug] [youtube] dQw4w9WgXcQ: Detected a 15s ad skippable after 5s for mweb
2026-10-02T05:05:33.4515747Z [youtube] dQw4w9WgXcQ: Downloading m3u8 information
2026-10-02T05:05:33.6340934Z WARNING: [youtube] dQw4w9WgXcQ: Signature solving failed: Some formats may be missing. Ensure you have a supported JavaScript runtime and challenge solver script distribution installed. Review any warnings presented before this message. For more details, refer to  https://github.com/yt-dlp/yt-dlp/wiki/EJS
2026-10-02T05:05:33.6344171Z WARNING: [youtube] dQw4w9WgXcQ: n challenge solving failed: Some formats may be missing. Ensure you have a supported JavaScript runtime and challenge solver script distribution installed. Review any warnings presented before this message. For more details, refer to  https://github.com/yt-dlp/yt-dlp/wiki/EJS
2026-10-02T05:05:33.6394715Z WARNING: [youtube] dQw4w9WgXcQ: mweb client https formats require a GVS PO Token which was not provided. They will be skipped as they may yield HTTP Error 403. You can manually pass a GVS PO Token for this client with --extractor-args "youtube:po_token=mweb.gvs+XXX". For more information, refer to  https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide
2026-10-02T05:05:33.7409437Z [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
2026-10-02T05:05:33.7410687Z [debug] yt-dlp version stable@2026.08.19 from yt-dlp/yt-dlp [594bd50c2] (pip) API
2026-10-02T05:05:33.7415852Z [debug] params: {'quiet': False, 'verbose': True, 'no_warnings': False, 'cookiefile': None, 'proxy': None, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10, 'nocheckcertificate': True, 'cachedir': False, 'noplaylist': True, 'extractor_args': {'youtube': {'player_client': ['default', 'mweb']}}, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'format': 'best[ext=mp4]/best', 'outtmpl': './Rick_Astley_-_Never_Gonna_Give_You_Up_(Official_Video)_(4K_Remaster).%(ext)s', 'merge_output_format': None, 'overwrites': True, 'ignoreerrors': False, 'progress_hooks': [<function download_youtube_video.<locals>._progress_hook at 0x7fc5ede78720>], 'js_runtimes': {'deno': {}}, 'remote_components': set(), 'compat_opts': set()}
2026-10-02T05:05:33.7422184Z [debug] Python 3.11.16 (CPython x86_64 64bit) - Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 (OpenSSL 3.0.13 30 Jan 2024, glibc 2.39)
2026-10-02T05:05:33.7423464Z [debug] exe versions: none
2026-10-02T05:05:33.7424803Z [debug] Optional libraries: certifi-2026.07.22, requests-2.34.2, sqlite3-3.45.1, urllib3-2.8.0, websockets-16.1.1
2026-10-02T05:05:33.7433068Z [debug] JS runtimes: none
2026-10-02T05:05:33.7436517Z [debug] Proxy map: {}
2026-10-02T05:05:33.7443207Z [debug] Request Handlers: urllib, requests, websockets
2026-10-02T05:05:33.7447238Z [debug] Plugin directories: none
2026-10-02T05:05:33.7849833Z [debug] Loaded 1744 extractors
2026-10-02T05:05:33.7924242Z [debug] Sort order given by extractor: quality, res, fps, hdr:12, source, vcodec, channels, acodec, lang, proto
2026-10-02T05:05:33.7925980Z [debug] Formats sorted by: hasvid, ie_pref, quality, res, fps, hdr:12(7), source, vcodec, channels, acodec, lang, proto, size, br, asr, vext, aext, hasaud, id
2026-10-02T05:05:36.8261454Z [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
2026-10-02T05:05:36.8262640Z [debug] yt-dlp version stable@2026.08.19 from yt-dlp/yt-dlp [594bd50c2] (pip) API
2026-10-02T05:05:36.8266717Z [debug] params: {'quiet': False, 'verbose': True, 'no_warnings': False, 'cookiefile': None, 'proxy': None, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10, 'nocheckcertificate': True, 'cachedir': False, 'noplaylist': True, 'extractor_args': {'youtube': {'player_client': ['default', 'mweb']}}, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'js_runtimes': {'deno': {}}, 'remote_components': set(), 'compat_opts': set()}
2026-10-02T05:05:36.8271000Z [debug] Python 3.11.16 (CPython x86_64 64bit) - Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 (OpenSSL 3.0.13 30 Jan 2024, glibc 2.39)
2026-10-02T05:05:36.8276527Z [debug] exe versions: none
2026-10-02T05:05:36.8277408Z [debug] Optional libraries: certifi-2026.07.22, requests-2.34.2, sqlite3-3.45.1, urllib3-2.8.0, websockets-16.1.1
2026-10-02T05:05:36.8284898Z [debug] JS runtimes: none
2026-10-02T05:05:36.8288295Z [debug] Proxy map: {}
2026-10-02T05:05:36.8294811Z [debug] Request Handlers: urllib, requests, websockets
2026-10-02T05:05:36.8298795Z [debug] Plugin directories: none
2026-10-02T05:05:36.8700656Z [debug] Loaded 1744 extractors
2026-10-02T05:05:36.8710012Z [debug] [youtube] [pot] PO Token Providers: none
2026-10-02T05:05:36.8710737Z [debug] [youtube] [pot] PO Token Cache Providers: memory
2026-10-02T05:05:36.8711501Z [debug] [youtube] [pot] PO Token Cache Spec Providers: webpo
2026-10-02T05:05:36.8714930Z [debug] [youtube] [jsc] JS Challenge Providers: bun (unavailable), deno (unavailable), node (unavailable), quickjs (unavailable)
2026-10-02T05:05:36.8715920Z [youtube] Extracting URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
2026-10-02T05:05:36.8718860Z [youtube] dQw4w9WgXcQ: Downloading webpage
2026-10-02T05:05:37.9540563Z [debug] [youtube] Forcing "main" player JS variant for player 8ab5c328
2026-10-02T05:05:37.9541978Z         original url = /s/player/8ab5c328/player_es6.vflset/en_US/base.js
2026-10-02T05:05:37.9566806Z [youtube] dQw4w9WgXcQ: Downloading visionos player API JSON
2026-10-02T05:05:38.0407570Z [youtube] dQw4w9WgXcQ: Downloading mweb client config
2026-10-02T05:05:38.2952312Z [debug] [youtube] dQw4w9WgXcQ: Detected experiment to bind GVS PO Token to video ID for mweb client
2026-10-02T05:05:38.2967986Z [youtube] dQw4w9WgXcQ: Downloading mweb player API JSON
2026-10-02T05:05:38.4970227Z [debug] [youtube] dQw4w9WgXcQ: Detected a 15s ad skippable after 5s for mweb
2026-10-02T05:05:38.5198021Z [youtube] dQw4w9WgXcQ: Downloading m3u8 information
2026-10-02T05:05:38.6831725Z WARNING: [youtube] dQw4w9WgXcQ: Signature solving failed: Some formats may be missing. Ensure you have a supported JavaScript runtime and challenge solver script distribution installed. Review any warnings presented before this message. For more details, refer to  https://github.com/yt-dlp/yt-dlp/wiki/EJS
2026-10-02T05:05:38.6835623Z WARNING: [youtube] dQw4w9WgXcQ: n challenge solving failed: Some formats may be missing. Ensure you have a supported JavaScript runtime and challenge solver script distribution installed. Review any warnings presented before this message. For more details, refer to  https://github.com/yt-dlp/yt-dlp/wiki/EJS
2026-10-02T05:05:38.6886554Z WARNING: [youtube] dQw4w9WgXcQ: mweb client https formats require a GVS PO Token which was not provided. They will be skipped as they may yield HTTP Error 403. You can manually pass a GVS PO Token for this client with --extractor-args "youtube:po_token=mweb.gvs+XXX". For more information, refer to  https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide
2026-10-02T05:05:38.7822005Z [debug] Encodings: locale UTF-8, fs utf-8, pref UTF-8, out utf-8 (No ANSI), error utf-8 (No ANSI), screen utf-8 (No ANSI)
2026-10-02T05:05:38.7823049Z [debug] yt-dlp version stable@2026.08.19 from yt-dlp/yt-dlp [594bd50c2] (pip) API
2026-10-02T05:05:38.7828826Z [debug] params: {'quiet': False, 'verbose': True, 'no_warnings': False, 'cookiefile': None, 'proxy': None, 'socket_timeout': 30, 'retries': 10, 'fragment_retries': 10, 'nocheckcertificate': True, 'cachedir': False, 'noplaylist': True, 'extractor_args': {'youtube': {'player_client': ['default', 'mweb']}}, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Sec-Fetch-Mode': 'navigate'}, 'format': 'best[ext=mp4]/best', 'outtmpl': './Rick_Astley_-_Never_Gonna_Give_You_Up_(Official_Video)_(4K_Remaster).%(ext)s', 'merge_output_format': None, 'overwrites': True, 'ignoreerrors': False, 'progress_hooks': [<function download_youtube_video.<locals>._progress_hook at 0x7fc5ede78720>], 'js_runtimes': {'deno': {}}, 'remote_components': set(), 'compat_opts': set()}
2026-10-02T05:05:38.7834079Z [debug] Python 3.11.16 (CPython x86_64 64bit) - Linux-6.17.0-1022-azure-x86_64-with-glibc2.39 (OpenSSL 3.0.13 30 Jan 2024, glibc 2.39)
2026-10-02T05:05:38.7836211Z [debug] exe versions: none
2026-10-02T05:05:38.7837260Z [debug] Optional libraries: certifi-2026.07.22, requests-2.34.2, sqlite3-3.45.1, urllib3-2.8.0, websockets-16.1.1
2026-10-02T05:05:38.7845355Z [debug] JS runtimes: none
2026-10-02T05:05:38.7848727Z [debug] Proxy map: {}
2026-10-02T05:05:38.7854589Z [debug] Request Handlers: urllib, requests, websockets
2026-10-02T05:05:38.7858495Z [debug] Plugin directories: none
2026-10-02T05:05:38.8261553Z [debug] Loaded 1744 extractors
2026-10-02T05:05:38.8322957Z [debug] Sort order given by extractor: quality, res, fps, hdr:12, source, vcodec, channels, acodec, lang, proto
2026-10-02T05:05:38.8324501Z [debug] Formats sorted by: hasvid, ie_pref, quality, res, fps, hdr:12(7), source, vcodec, channels, acodec, lang, proto, size, br, asr, vext, aext, hasaud, id
2026-10-02T05:05:38.8623295Z Traceback (most recent call last):
2026-10-02T05:05:38.8632899Z   File "/home/runner/work/openshorts/openshorts/main.py", line 981, in <module>
2026-10-02T05:05:38.8633970Z     input_video, video_title = download_youtube_video(args.url, output_dir)
2026-10-02T05:05:38.8634780Z                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-02T05:05:38.8635810Z   File "/home/runner/work/openshorts/openshorts/main.py", line 684, in download_youtube_video
2026-10-02T05:05:38.8637088Z     raise last_err
2026-10-02T05:05:38.8637914Z   File "/home/runner/work/openshorts/openshorts/main.py", line 664, in download_youtube_video
2026-10-02T05:05:38.8639122Z     sanitized_title = _attempt(ea, fmt, proxy, cookies)
2026-10-02T05:05:38.8639737Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-02T05:05:38.8640822Z   File "/home/runner/work/openshorts/openshorts/main.py", line 638, in _attempt
2026-10-02T05:05:38.8641723Z     ydl.process_ie_result(info, download=True)
2026-10-02T05:05:38.8642947Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/YoutubeDL.py", line 1946, in process_ie_result
2026-10-02T05:05:38.8644232Z     ie_result = self.process_video_result(ie_result, download=download)
2026-10-02T05:05:38.8644963Z                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-02T05:05:38.8646157Z   File "/opt/hostedtoolcache/Python/3.11.16/x64/lib/python3.11/site-packages/yt_dlp/YoutubeDL.py", line 3096, in process_video_result
2026-10-02T05:05:38.8648758Z     raise ExtractorError(
2026-10-02T05:05:38.8649776Z yt_dlp.utils.ExtractorError: [youtube] dQw4w9WgXcQ: Requested format is not available. Use --list-formats for a list of available formats
2026-10-02T05:05:39.7825564Z ##[error]Process completed with exit code 1.
2026-10-02T05:05:39.7973747Z Post job cleanup.
2026-10-02T05:05:39.8852362Z [command]/usr/bin/git version
2026-10-02T05:05:39.8899006Z git version 2.55.0
2026-10-02T05:05:39.8937153Z Temporarily overriding HOME='/home/runner/work/_temp/626c00cd-fe68-4475-8e37-57abd306827f' before making global git config changes
2026-10-02T05:05:39.8938972Z Adding repository directory to the temporary git global config as a safe directory
2026-10-02T05:05:39.8944392Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/openshorts/openshorts
2026-10-02T05:05:39.8983947Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-10-02T05:05:39.9021461Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-10-02T05:05:39.9297252Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-10-02T05:05:39.9328820Z http.https://github.com/.extraheader
2026-10-02T05:05:39.9340887Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-10-02T05:05:39.9376443Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-10-02T05:05:39.9640407Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-10-02T05:05:39.9686322Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-10-02T05:05:40.0159536Z Cleaning up orphan processes
2026-10-02T05:05:40.0465558Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
