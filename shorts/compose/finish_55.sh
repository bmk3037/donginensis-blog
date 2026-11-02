#!/usr/bin/env bash
# 55편 KTX 유리창: B판(본판)·A판(첫 6초 다름) 마무리. 끊겨도 다시 돌리면 이어서 한다(조각 렌더). 1440×2560, 24fps
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd)
CLIP=$R/shorts/media/55/in/clip; O=$R/shorts/media/55/out; mkdir -p "$O"
for V in B A; do
  cd "$T/work/55/ab/$V"; export SCENE=scene_55$V.html
  OUT=$O/55${V}_ktx_glass.mp4
  [ -f "$OUT" ] && continue
  [ -s scenes.json ] || node "$T/dump_scenes.mjs" > scenes.json
  [ -f ambient.wav ] || python3 "$T/ambient_v2.py" scenes.json "$CLIP"
  [ -f sfx.wav ] || python3 sfx.py
  [ -f video_only_v2.mp4 ] || node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
  [ -f body_v2.mp4 ] || bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
  W=1440 H=2560 FPS=24 RATE=9000k CRF=18 bash "$T/append_cover.sh" body_v2.mp4 ../cov/cover.jpg out.mp4 > /dev/null && cp out.mp4 "$OUT" && echo "55$V ok"
done
cp "$T/work/55/ab/cov/cover.jpg" "$O/55_cover.jpg"
echo ALL_FINISHED_55
