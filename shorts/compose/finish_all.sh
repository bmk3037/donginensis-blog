#!/usr/bin/env bash
# 끊겨도 다시 돌리면 이어서 하는 마무리 스크립트(조각 렌더 + 단계별 건너뛰기). 49편 → jetfan v2b → v3 순서.
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd)
export SCENE=scene_v2.html

# ---- 49편 ----
cd "$T/work/49"
OUT49=$R/shorts/media/49/out/49_bathroom_fan.mp4
if [ ! -f "$OUT49" ]; then
  [ -s scenes.json ] || node "$T/dump_scenes.mjs" > scenes.json
  [ -f ambient.wav ] || python3 "$T/ambient_v2.py" scenes.json "$R/shorts/media/49/in/clip"
  [ -f sfx.wav ] || python3 sfx.py
  [ -f video_only_v2.mp4 ] || node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
  [ -f body_v2.mp4 ] || bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
  [ -f cover.jpg ] || { node /tmp/claude-0/-home-user/5ace3117-099c-50ca-a517-0e4abd6ef367/scratchpad/shot.js "$PWD/thumb.html" "$PWD/cover.png" && python3 -c "from PIL import Image; Image.open('cover.png').convert('RGB').save('cover.jpg',quality=92)"; }
  FPS=24 RATE=5000k CRF=20 bash "$T/append_cover.sh" body_v2.mp4 cover.jpg 49_bathroom_fan.mp4 > /dev/null && mkdir -p "$R/shorts/media/49/out" && cp 49_bathroom_fan.mp4 "$OUT49" && cp cover.jpg "$R/shorts/media/49/out/49_cover.jpg" && echo "49 ok"
fi

# ---- jetfan v2b / v3 (자막 중복 수정판) ----
cd "$T/work/jetfan"
[ -s scenes_v2.json ] || node "$T/dump_scenes.mjs" > scenes_v2.json
[ -f ambient_v2b.wav ] || { python3 "$T/ambient_v2.py" scenes_v2.json clipsrc && cp ambient.wav ambient_v2b.wav; }
if [ ! -f sub_v2b.done ]; then
  [ -f video_only_v2b.mp4.fixed ] || { rm -f video_only_v2b.mp4; SCENE=scene_v2.html node "$T/render.mjs" video video_only_v2b.mp4 24 > render_v2b.log 2>&1 && touch video_only_v2b.mp4.fixed; }
  cp ambient_v2b.wav ambient.wav && bash "$T/mixv2.sh" video_only_v2b.mp4 jetfan_body_v2b.mp4 > /dev/null && FPS=24 RATE=8000k CRF=19 bash "$T/append_cover.sh" jetfan_body_v2b.mp4 cover.jpg 48_jetfan_v2b.mp4 > /dev/null && cp 48_jetfan_v2b.mp4 "$R/shorts/media/jetfan/out/" && touch sub_v2b.done && echo "v2b ok"
fi
if [ ! -f sub_v3.done ]; then
  [ -f video_only_v3.mp4.fixed ] || { rm -f video_only_v3.mp4; SCENE=scene_v3.html node "$T/render.mjs" video video_only_v3.mp4 24 > render_v3.log 2>&1 && touch video_only_v3.mp4.fixed; }
  cp ambient_v3.wav ambient.wav && bash "$T/mixv2.sh" video_only_v3.mp4 jetfan_body_v3.mp4 > /dev/null && FPS=24 RATE=5000k CRF=20 bash "$T/append_cover.sh" jetfan_body_v3.mp4 cover.jpg 48_jetfan_v3.mp4 > /dev/null && cp 48_jetfan_v3.mp4 "$R/shorts/media/jetfan/out/" && touch sub_v3.done && echo "v3 ok"
fi
echo ALL_FINISHED
