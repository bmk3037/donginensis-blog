#!/usr/bin/env bash
# 50편(형식 B) 마무리: 끊겨도 다시 돌리면 이어서 한다(조각 렌더, 단계별 건너뛰기)
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd); export SCENE=scene_51.html
cd "$T/work/51"
OUT=$R/shorts/media/51/out/51_museum_vault_v41.mp4
if [ ! -f "$OUT" ]; then
  [ -s scenes.json ] || node "$T/dump_scenes.mjs" > scenes.json
  [ -f ambient.wav ] || python3 "$T/ambient_v2.py" scenes.json "$R/shorts/media/51/in/clip"
  [ -f sfx.wav ] || python3 sfx.py
  [ -f video_only_v2.mp4 ] || node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
  [ -f body_v2.mp4 ] || bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
  [ -f cover.jpg ] || { node /tmp/claude-0/-home-user/5ace3117-099c-50ca-a517-0e4abd6ef367/scratchpad/shot.js "$PWD/thumb.html" "$PWD/cover.png" && python3 -c "from PIL import Image; Image.open('cover.png').convert('RGB').save('cover.jpg',quality=92)"; }
  FPS=24 RATE=5000k CRF=20 bash "$T/append_cover.sh" body_v2.mp4 cover.jpg 51_museum_vault_v41.mp4 > /dev/null && mkdir -p "$R/shorts/media/51/out" && cp 51_museum_vault_v41.mp4 "$OUT" && cp cover.jpg "$R/shorts/media/51/out/51_cover.jpg" && echo "51 ok"
fi
echo ALL_FINISHED_51
