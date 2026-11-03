#!/usr/bin/env bash
# 이탄생 그림판 마무리: bash template-2tan/finish_2tan.sh NN [이름]   (shorts/compose에서)
# 필요: work/NN/{scene_2tan.html, sfx.py, timeline.js, narration.wav}, shorts/media/NN/in/img/01.jpg… , 클립은 shorts/media/NN/in/clip/(있으면 clipn으로)
# 1440×2560 24fps, 조각 렌더(끊겨도 다시 돌리면 이어서), Flow 별 표시는 delogo로 지움
set -u
NN=$1; NAME=${2:-draft}; T=$(cd "$(dirname "$0")/.." && pwd); R=$(cd "$T/../.." && pwd); export SCENE=scene_2tan.html
W=$T/work/$NN; cd "$W"; SRC=$R/shorts/media/$NN/in
mkdir -p img; for f in "$SRC"/img/*.jpg; do n=$(basename "$f" .jpg); [ -f img/$n.webp ] || ffmpeg -v error -y -i "$f" -vf "delogo=x=640:y=1248:w=60:h=60" -quality 92 img/$n.webp; done
if [ -d "$SRC/clip" ]; then mkdir -p clipn; for f in "$SRC"/clip/c*.mp4; do c=$(basename "$f" .mp4); [ -d clipn/$c ] || { mkdir -p clipn/$c; ffmpeg -v error -y -i "$f" -vf "fps=24,scale=720:1280" -q:v 3 clipn/$c/%03d.jpg; }; done; fi
DUR=$(python3 -c "import json;print(json.loads(open('timeline.js').read().split('=',1)[1].strip().rstrip(';'))['duration'])")
[ -f ambient.wav ] || ffmpeg -y -loglevel error -f lavfi -t "$DUR" -i anullsrc=r=44100:cl=stereo ambient.wav
[ -f sfx.wav ] || python3 sfx.py
rm -rf chunks_video_only_v2; node "$T/render.mjs" video video_only_v2.mp4 24 > render.log 2>&1
bash "$T/mixv2.sh" video_only_v2.mp4 body.mp4 > /dev/null
O=$R/shorts/media/$NN/out; mkdir -p "$O"
if [ -f cover.jpg ]; then W=1440 H=2560 FPS=24 RATE=7500k CRF=19 bash "$T/append_cover.sh" body.mp4 cover.jpg "$O/${NN}_$NAME.mp4" > /dev/null; else cp body.mp4 "$O/${NN}_$NAME.mp4"; fi
echo "$NN $NAME ok"
