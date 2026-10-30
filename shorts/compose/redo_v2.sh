#!/usr/bin/env bash
# 기존 편을 v2 방식으로 다시 편집: 원본 24fps, 클립 안 확대 컷 없음, 클립 위 확대 약하게, 클립 환경음, 고화질.
#   bash redo_v2.sh 47        (work/47의 scene.html·narration.wav·sfx.wav·cover.jpg와 media/47/in/clip을 쓴다)
set -euo pipefail
N=$1
LOCK=/tmp/claude-0/redo/lock_$N
mkdir "$LOCK" 2>/dev/null || { echo "SKIP $N (이미 진행 중이거나 끝남)"; exit 0; }
trap 'rm -rf "$LOCK"' ERR
T=$(cd "$(dirname "$0")" && pwd); R=$(cd "$T/../.." && pwd); W=$T/work/$N; cd "$W"
SRC=$R/shorts/media/$N/in/clip
[ -d "$SRC" ] || SRC=$W/clipsrc
mkdir -p clipn
for f in "$SRC"/c*.mp4; do c=$(basename "$f" .mp4); mkdir -p clipn/$c; [ "$(ls clipn/$c | wc -l)" -ge 185 ] || ffmpeg -y -loglevel error -i "$f" -vf scale=720:1280 -q:v 3 clipn/$c/%03d.jpg; done
python3 - "$W" <<'PY'
import re, os, sys
w = sys.argv[1]
s = open(f"{w}/scene.html", encoding="utf8").read()
cnt = {c: len(os.listdir(f"{w}/clipn/{c}")) for c in sorted(os.listdir(f"{w}/clipn")) if os.path.isdir(f"{w}/clipn/{c}")}
used = set(re.findall(r'K\("(c\d+)"', s))
miss = [c for c in used if c not in cnt]
assert not miss, f"클립 원본 없음: {miss}"
s = re.sub(r"const CLIPS = \{.*?\}, CLIPIMG = \{\}, CFPS = 60;", "const CLIPS = { " + ", ".join(f"{c}: {n}" for c, n in cnt.items()) + " }, CLIPIMG = {}, CFPS = 24;", s, count=1, flags=re.S)
s = s.replace("clip/${c}/${String(k + 1)", "clipn/${c}/${String(k + 1)").replace("clip/${clip.id}/${String(fi)", "clipn/${clip.id}/${String(fi)")
old = 'Object.assign({ clip: { id, from: 1 + c0 * 60, rate, t0: a }, from: 1.04, to: 1.1 }, extra || {})'
assert old in s
s = s.replace(old, '(o => (o.to = Math.min(o.to, o.from + 0.06), o))(Object.assign({ clip: { id, from: 1 + c0 * 24, rate, t0: a }, from: 1.0, to: 1.03 }, extra || {}))')
lines = s.split("\n")
lines = [("// v2: 클립 안 2초마다 당겨 찍기 컷은 같은 화면 반복으로 보여 뺌" if l.startswith("SCENES.forEach(sc => { if (sc[3].clip && !sc[3].cuts") else l) for l in lines]
open(f"{w}/scene_v2.html", "w", encoding="utf8").write("\n".join(lines))
print("scene_v2 ok", cnt)
PY
SCENE=scene_v2.html node "$T/dump_scenes.mjs" > scenes.json
python3 "$T/ambient_v2.py" scenes.json "$SRC"
SCENE=scene_v2.html node "$T/render.mjs" video video_only_v2.mp4 24 > render_v2.log 2>&1
bash "$T/mixv2.sh" video_only_v2.mp4 body_v2.mp4 > /dev/null
OUTN=$(ls ${N}_*.mp4 | grep -v "_body\|_v2\|_upload\|_hq\|_old\|_v1" | head -1 | sed 's/\.mp4$//')
FPS=24 RATE=5000k CRF=20 bash "$T/append_cover.sh" body_v2.mp4 cover.jpg ${OUTN}_v2.mp4 | tail -2
mkdir -p "$R/shorts/media/$N/out"; cp ${OUTN}_v2.mp4 "$R/shorts/media/$N/out/"
echo "REDO_DONE $N ${OUTN}_v2.mp4"
