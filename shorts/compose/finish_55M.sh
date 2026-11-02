#!/usr/bin/env bash
# 55M v3(미니어처 그림판): 그림 24장 + B판 음성. 1440×2560, 24fps, 조각 렌더(이어서 가능)
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd); export SCENE=scene_55M.html
cd "$T/work/55M"; O=$R/shorts/media/55M/out; mkdir -p "$O"
[ -f ambient.wav ] || ffmpeg -y -loglevel error -f lavfi -t "$(python3 -c "import json;print(json.loads(open('timeline.js').read().split('=',1)[1].strip().rstrip(';'))['duration'])")" -i anullsrc=r=44100:cl=stereo ambient.wav
[ -f sfx.wav ] || python3 sfx.py
[ -f video_only_v2.mp4 ] || node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
[ -f body_v2.mp4 ] || bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
W=1440 H=2560 FPS=24 RATE=7500k CRF=19 bash "$T/append_cover.sh" body_v2.mp4 cov/cover.jpg out.mp4 > /dev/null && cp out.mp4 "$O/55M_v3_miniature.mp4" && cp cov/cover.jpg "$O/55M_cover.jpg" && echo "55M ok"
echo ALL_FINISHED_55M
