#!/usr/bin/env bash
# 영상 끝에 커버(섬네일)를 1초 붙인다. 시작은 움직이는 장면 그대로 두고, 인스타·유튜브에서 마지막 장면을 표지로 고를 수 있게.
#   bash append_cover.sh 입력.mp4 cover.jpg 결과.mp4
set -euo pipefail
IN=$1; COVER=$2; OUT=$3
ffmpeg -y -loglevel error -i "$IN" -loop 1 -t 1.0 -framerate 30 -i "$COVER" -f lavfi -t 1.0 -i anullsrc=r=44100:cl=stereo -filter_complex \
  "[0:v]fps=30,format=yuv420p,setsar=1[v0];[1:v]scale=1080:1920,format=yuv420p,setsar=1[v1];[0:a]afade=t=out:st=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN" | awk '{print $1-0.4}'):d=0.4,aresample=44100,aformat=channel_layouts=stereo[a0];[v0][a0][v1][2:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 29 -preset slow -tune stillimage -maxrate 1300k -bufsize 2600k -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$OUT.tmp.mp4"
ffmpeg -y -loglevel error -i "$OUT.tmp.mp4" -i "$COVER" -map 0 -map 1 -c copy -c:v:1 mjpeg -disposition:v:1 attached_pic -movflags +faststart "$OUT"
rm -f "$OUT.tmp.mp4"
ls -la "$OUT"; ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
