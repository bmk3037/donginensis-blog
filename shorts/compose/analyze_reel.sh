#!/usr/bin/env bash
# 남의 릴스(공개 게시물)를 받아 화면 짜임을 잰다. 어느 세션에서든 같은 결과.
#   bash shorts/compose/analyze_reel.sh <인스타 릴스 주소> <작업 폴더>
# 결과(작업 폴더): reel.mp4, reel.info.json, 1초 모아보기 sheet_*.jpg, cuts.txt(장면 전환), motion.txt(초당 화면 변화), transcript.txt(받아쓰기)
# 받아쓴 대본과 영상은 분석에만 쓰고 공개 저장소에 올리지 않는다(남의 대본).
set -euo pipefail
URL=$1; D=$2; mkdir -p "$D"; cd "$D"
command -v yt-dlp >/dev/null || pip install -q yt-dlp
python3 -c "import faster_whisper" 2>/dev/null || pip install -q faster-whisper
yt-dlp -q --no-warnings -o "reel.%(ext)s" --write-info-json "$URL"
ffprobe -v error -show_entries format=duration,bit_rate:stream=codec_type,width,height,r_frame_rate -of compact reel.mp4 | tee probe.txt
ffmpeg -v info -i reel.mp4 -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | tee -a probe.txt
# 장면 전환(큰 전환만). 빠른 드론 이동은 0.15 아래에서 잡히므로 0.3을 기준으로 센다
ffmpeg -v info -i reel.mp4 -vf "select='gt(scene,0.3)',showinfo" -an -f null - 2>&1 | grep -o "pts_time:[0-9.]*" | cut -d: -f2 > cuts.txt
echo "큰 장면 전환 $(wc -l < cuts.txt)번"
# 초당 화면 변화(낮으면 거의 멈춤): 12fps 흑백 축소 화면의 평균 차이
python3 -I - <<'PY' > motion.txt
import subprocess, numpy as np
fps, w, h = 12, 54, 96
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", "reel.mp4", "-vf", f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
a = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
print(" ".join(f"{d[i*fps:(i+1)*fps].mean():.0f}" for i in range(len(d) // fps)))
PY
# 1초마다 한 장, 52장씩 모아보기
ffmpeg -v error -y -i reel.mp4 -vf "fps=1,scale=160:-1,drawtext=text='%{eif\:t\:d}':fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.6:x=4:y=4" f%03d.jpg
n=$(ls f*.jpg | wc -l); s=1; k=1
while [ $s -le $n ]; do ffmpeg -v error -y -framerate 1 -start_number $s -i f%03d.jpg -vf "tile=13x4" -frames:v 1 sheet_$k.jpg; s=$((s+52)); k=$((k+1)); done
# 받아쓰기
ffmpeg -v error -y -i reel.mp4 -ar 16000 -ac 1 a16.wav
python3 -I - <<'PY' > transcript.txt 2>/dev/null
import numpy as np, wave
from faster_whisper import WhisperModel
w = wave.open("a16.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
for s in WhisperModel("small", device="cpu", compute_type="int8").transcribe(a, language="ko")[0]:
    print(f"{s.start:5.1f}-{s.end:5.1f} {s.text}")
PY
echo "끝: $D (sheet_*.jpg를 열어 보고, cuts.txt·motion.txt·transcript.txt로 구조를 적는다)"
