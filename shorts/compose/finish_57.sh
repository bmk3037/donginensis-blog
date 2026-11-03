#!/usr/bin/env bash
# 57편 그림판 초안: bash finish_57.sh block|2tan  (그림: shorts/media/57/in/img_block 또는 img → work/57/img_<판>/NN.webp)
# 1.06배 음성 96.6초, 1440×2560 24fps, 조각 렌더(이어서 가능)
set -u
V=$1; T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd); export SCENE=scene_57.html
W=$T/work/57; cd "$W"; SRC=$R/shorts/media/57/in/$([ "$V" = block ] && echo img_block || echo img)
mkdir -p img_$V; for f in "$SRC"/*.jpg; do n=$(basename "$f" .jpg); [ -f img_$V/$n.webp ] || ffmpeg -v error -y -i "$f" -vf "delogo=x=640:y=1248:w=60:h=60" -quality 92 img_$V/$n.webp; done
ln -sfn img_$V img; D=draft_$V; mkdir -p $D
[ -f ambient.wav ] || ffmpeg -y -loglevel error -f lavfi -t 97 -i anullsrc=r=44100:cl=stereo ambient.wav
[ -f sfx.wav ] || python3 sfx.py
[ -f $D/video.mp4 ] || { rm -rf chunks_video_only_v2; node "$T/render.mjs" video video_only_v2.mp4 24 > $D/render.log 2>&1 && mv video_only_v2.mp4 $D/video.mp4; }
bash "$T/mixv2.sh" $D/video.mp4 $D/body.mp4 > /dev/null
O=$R/shorts/media/57/out; mkdir -p "$O"; cp $D/body.mp4 "$O/57_draft_$V.mp4" && echo "57 $V ok"
