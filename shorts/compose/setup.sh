#!/usr/bin/env bash
# 합성 도구를 처음 한 번 준비한다: bash shorts/compose/setup.sh
# ffmpeg, Python(numpy·Pillow), Node(playwright + 크로미움), 프리텐다드 글꼴
set -e
T=$(cd "$(dirname "$0")" && pwd)

command -v ffmpeg >/dev/null || { sudo apt-get update -q && sudo apt-get install -y -q ffmpeg; } || { echo "ffmpeg를 설치해 주세요"; exit 1; }
python3 -m pip install -q numpy pillow opencv-python-headless 2>/dev/null || python3 -m pip install -q --break-system-packages numpy pillow opencv-python-headless

# playwright: 이미 깔린 곳(PLAYWRIGHT_DIR 또는 /opt/node-tools)이 있으면 그대로 쓰고, 없으면 이 폴더에 설치
if ! node -e "require('${PLAYWRIGHT_DIR:-/opt/node-tools/node_modules}/playwright')" 2>/dev/null; then
  (cd "$T" && { [ -f package.json ] || npm init -y >/dev/null; } && npm i -s playwright@1.47.2 && npx playwright install chromium)
fi

# 프리텐다드(SIL OFL 1.1, 상업적 이용 가능)
mkdir -p "$T/fonts"
for w in Bold ExtraBold; do
  [ -s "$T/fonts/Pretendard-$w.woff2" ] || curl -sSfL -o "$T/fonts/Pretendard-$w.woff2" \
    "https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/web/static/woff2/Pretendard-$w.woff2"
done
ffmpeg -version | head -1; node --version; ls "$T/fonts"
echo "준비 끝"
