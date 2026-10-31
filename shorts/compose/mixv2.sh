#!/usr/bin/env bash
# v2 소리 합성(10/30): 목소리 + 효과음 + 클립 환경음(ambient.wav) + 배경음, 환경음·배경음은 목소리가 나오면 줄어든다.
#   작업 폴더에서: bash ../../mixv2.sh video_only_v2.mp4 결과.mp4
set -euo pipefail
IN=$1; OUT=$2; T=$(cd "$(dirname "$0")" && pwd)
BGM=bgm.mp3; [ -f "$BGM" ] || BGM="$T/assets/bgm_calm.mp3"
ffmpeg -y -loglevel error -i narration.wav -i sfx.wav -i ambient.wav -stream_loop -1 -i "$BGM" -filter_complex \
 "[0:a]aformat=sample_rates=44100:channel_layouts=stereo[n];[1:a]volume=0.55,aformat=channel_layouts=stereo[s];[n][s]amix=inputs=2:duration=first:normalize=0[vs];\
[vs]asplit=3[v][c1][c2];\
[2:a]volume=${AMB:-1.0},aformat=channel_layouts=stereo[am];[am][c1]sidechaincompress=threshold=0.02:ratio=5:attack=20:release=400[amd];\
[3:a]volume=${BGMV:-0.22},aformat=channel_layouts=stereo[b];[b][c2]sidechaincompress=threshold=0.02:ratio=8:attack=30:release=500[bd];\
[v][amd][bd]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-3.0:LRA=11,alimiter=limit=0.72:level=false[a]" -map "[a]" -ar 44100 mix_v2.wav
ffmpeg -y -loglevel error -i "$IN" -i mix_v2.wav -c:v libx264 -crf 18 -preset slow -maxrate 8000k -bufsize 16000k -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart -shortest "$OUT"
ls -la "$OUT"; ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
