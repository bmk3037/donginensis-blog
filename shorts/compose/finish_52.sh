#!/usr/bin/env bash
# 52편(형식 B v4 + 11절) 마무리: 끊겨도 다시 돌리면 이어서 한다(조각 렌더). 출력 1440×2560(lanczos), 24fps
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd); export SCENE=scene_52.html
cd "$T/work/52"
OUT=$R/shorts/media/52/out/52_maglev_empty.mp4
if [ ! -f "$OUT" ]; then
  [ -s scenes.json ] || node "$T/dump_scenes.mjs" > scenes.json
  [ -f ambient.wav ] || python3 "$T/ambient_v2.py" scenes.json "$R/shorts/media/52/in/clip"
  [ -f sfx.wav ] || python3 sfx.py
  [ -f video_only_v2.mp4 ] || node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
  [ -f body_v2.mp4 ] || bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
  W=1440 H=2560 FPS=24 RATE=9000k CRF=18 bash "$T/append_cover.sh" body_v2.mp4 cover.jpg 52_maglev_empty.mp4 > /dev/null && mkdir -p "$R/shorts/media/52/out" && cp 52_maglev_empty.mp4 "$OUT" && cp cover.jpg "$R/shorts/media/52/out/52_cover.jpg" && echo "52 ok"
fi
echo ALL_FINISHED_52
