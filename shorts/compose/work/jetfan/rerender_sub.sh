#!/usr/bin/env bash
# 자막 중복 수정판: v2b와 v3를 병렬 렌더 후 차례로 믹스·커버·복사
set -u
cd "$(dirname "$0")"
OUT=/home/user/donginensis-blog/shorts/media/jetfan/out
SCENE=scene_v2.html node ../../render.mjs video video_only_v2b.mp4 24 > render_v2b.log 2>&1 &
SCENE=scene_v3.html node ../../render.mjs video video_only_v3.mp4 24 > render_v3.log 2>&1 &
wait
cp ambient_v2b.wav ambient.wav && bash ../../mixv2.sh video_only_v2b.mp4 jetfan_body_v2b.mp4 > /dev/null && FPS=24 RATE=8000k CRF=19 bash ../../append_cover.sh jetfan_body_v2b.mp4 cover.jpg 48_jetfan_v2b.mp4 > /dev/null && cp 48_jetfan_v2b.mp4 $OUT/ && echo v2b ok
cp ambient_v3.wav ambient.wav && bash ../../mixv2.sh video_only_v3.mp4 jetfan_body_v3.mp4 > /dev/null && FPS=24 RATE=5000k CRF=20 bash ../../append_cover.sh jetfan_body_v3.mp4 cover.jpg 48_jetfan_v3.mp4 > /dev/null && cp 48_jetfan_v3.mp4 $OUT/ && echo v3 ok
echo SUB_DONE > sub.done
