#!/usr/bin/env bash
# 한 편 합성. 작업 폴더(예: shorts/compose/work/09)에 아래가 있어야 한다.
#   narration_raw.mp3  타입캐스트 음성(속도 1.0, 한 파일)
#   lines.json         [{"beat": 1, "text": "문장"}, ...] 타입캐스트 대본과 문장이 똑같아야 함
#   img/NN.webp        prep_images.py로 만든 플로우 이미지
#   scene.html         example-08/scene.html을 복사해 SCENES·KEYS·NAMES를 이 편에 맞게 고친 것
#   sfx.py             example-08/sfx.py를 복사해 맨 아래 효과음 위치(큐)를 이 편에 맞게 고친 것
#
#   bash make.sh align  작업폴더 [배속=1.12] ['{"10":48.9}']   음성 배속 + 문장별 시각(timeline.js)
#   bash make.sh stills 작업폴더 2,12,20                         정지 화면 확인
#   bash make.sh video  작업폴더 결과.mp4                         효과음 섞고 최종 영상
#   bash make.sh cover  작업폴더                                  cover.json으로 커버 이미지(cover.jpg)
set -euo pipefail
T=/home/user/donginensis-blog/shorts/compose
cmd=$1; W=$(cd "$2" && pwd); cd "$W"
[ -e fonts ] || ln -s "$T/fonts" fonts

case $cmd in
align)
  R=${3:-1.12}; FORCE=${4:-}
  # 문장 경계를 원래 속도 음성에서 찾고(쉼이 길어 잘 잡힌다), 배속에 맞춰 시각을 나눈다
  if [ -n "$FORCE" ]; then python3 "$T/align.py" narration_raw.mp3 lines.json "$FORCE"; else python3 "$T/align.py" narration_raw.mp3 lines.json; fi
  mv timeline.js timeline_raw.js
  ffmpeg -y -loglevel error -i narration_raw.mp3 -af "atempo=$R" -ar 44100 narration.wav
  echo -n "배속 뒤 길이(초): "; python3 "$T/tempo.py" timeline_raw.js "$R"
  ;;
stills)
  node "$T/render.mjs" stills "$3"; ls still_*.png | tail -5
  ;;
video)
  OUT=$3
  node "$T/render.mjs" video video_only.mp4 60
  if [ -f sfx.py ]; then
    python3 sfx.py
    ffmpeg -y -loglevel error -i narration.wav -i sfx.wav -filter_complex \
      "[1:a]volume=0.55[s];[0:a][s]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map "[a]" -ar 44100 mix.wav
  else
    ffmpeg -y -loglevel error -i narration.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 44100 mix.wav
  fi
  # 배경음악: 작업 폴더의 bgm.mp3, 없으면 공통 배경음(assets/bgm_calm.mp3). 목소리가 나올 때는 자동으로 줄인다(덕킹). NOBGM=1이면 뺀다
  BGM=bgm.mp3; [ -f "$BGM" ] || BGM="$T/assets/bgm_calm.mp3"
  if [ -z "${NOBGM:-}" ] && [ -f "$BGM" ]; then
    ffmpeg -y -loglevel error -i mix.wav -stream_loop -1 -i "$BGM" -filter_complex \
      "[0:a]asplit=2[v][sc];[1:a]volume=0.30,aformat=channel_layouts=stereo[b];[b][sc]sidechaincompress=threshold=0.02:ratio=8:attack=30:release=500[bd];[v][bd]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map "[a]" -ar 44100 mix_bgm.wav
    mv mix_bgm.wav mix.wav
  fi
  # 20MB 안쪽: 휴대폰으로 받기 쉬운 크기
  ffmpeg -y -loglevel error -i video_only.mp4 -i mix.wav -c:v libx264 -crf 29 -preset slow \
    -maxrate 1600k -bufsize 3200k -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart -shortest "$OUT"
  ls -la "$OUT"; ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
  ;;
cover)
  node "$T/cover.mjs"; ls -la cover.jpg
  ;;
*) echo "align | stills | video | cover"; exit 1;;
esac
