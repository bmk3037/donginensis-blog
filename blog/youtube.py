"""개인 유튜브 쇼츠: 클립 프롬프트 페이지 + 클립 10개를 쇼츠 1편으로 붙이기.

하루 무료 50크레딧 → 클립 5개 → 쇼츠 1편 (장면 5개, 장면마다 클립 1개).
json 하나에 5편(5일치)을 담아 두고 하루에 1편씩 만든다.

사용법:
    python -m blog.youtube page youtube/2026-10-27.json
        # youtube/2026-10-27.html 생성 (휴대폰에서 프롬프트·제목·설명 복사)

    python -m blog.youtube stitch youtube/2026-10-27.json 1 clips/1
        # clips/1 폴더의 클립 5개를 파일 이름순으로 붙이고 자막을 입혀
        # youtube/out/2026-10-27-1.mp4 생성 (ffmpeg 필요)
        # --voice 폴더: 장면별 내레이션 01.mp3~05.mp3 (있는 장면만 깔림, 길면 그 장면을 늘림)
        # --bgm 파일: 배경음악 (반복 재생, 작게)

youtube/<날짜>.json 형식:
{
  "date": "2026-10-27",
  "style": "모든 클립 프롬프트 앞에 붙는 공통 화풍·캐릭터 설명 (영어)",
  "episodes": [
    {"no": 1, "format": "궁금증", "hook": "화면 위 고정 제목", "title": "유튜브 제목",
     "description": "설명", "tags": ["..."], "check": ["올리기 전 확인할 사실"], "notes": ["훅·구조 메모"],
     "scenes": [{"caption": ["자막1", "자막2"], "prompt": "클립 프롬프트 (영어)"}, ... 5개]}
  ]
}
caption: 문자열 하나 또는 목록. 목록이면 그 장면 시간을 똑같이 나눠 차례로 보여줌. 줄바꿈 \\n, 2줄까지
"""
import argparse
import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS_DIR = ROOT / "assets" / "fonts"
OUT_DIR = ROOT / "youtube" / "out"
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv"}
AUDIO_EXT = [".mp3", ".wav", ".m4a"]
W, H, FPS = 1080, 1920, 30
SHORTS_MAX = 180  # 쇼츠 최대 길이(초)

# 쇼츠 화면은 위(검색·채널)와 아래(제목·버튼)를 앱 UI가 가리므로 그 사이에 둔다
ASS_HEAD = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,Pretendard ExtraBold,76,&H00FFFFFF,&H00FFFFFF,&H00A55718,&H00A55718,0,0,0,0,100,100,0,0,3,18,0,8,70,70,250,1
Style: Cap,Pretendard ExtraBold,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,2,2,70,70,560,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def episode(data, no):
    for ep in data["episodes"]:
        if ep["no"] == no:
            return ep
    sys.exit(f"{no}번 편이 없습니다 (있는 편: {[e['no'] for e in data['episodes']]})")


# ---------- 프롬프트 페이지 ----------

def render_page(data):
    e = html.escape
    style = data["style"]
    cards = []
    k = 0
    for ep in data["episodes"]:
        rows = []
        prompts = []
        for i, sc in enumerate(ep["scenes"], 1):
            full = f"{style}\n\n{sc['prompt']}"
            prompts.append(full)
            k += 1
            rows.append(
                f'<li><div class="cap">{e(chr(10).join(captions(sc)))}</div>'
                f'<div class="pr">{e(sc["prompt"])}</div>'
                f'<pre hidden id="p{k}">{e(full)}</pre>'
                f'<button data-t="p{k}">{i:02d}번 프롬프트 복사</button></li>')
        k += 1
        all_id = f"p{k}"
        meta = f'{ep["description"]}\n\n' + " ".join("#" + t for t in ep["tags"])
        checks = "".join(f"<li>{e(c)}</li>" for c in ep.get("check", []))
        notes = "".join(f"<li>{e(n)}</li>" for n in ep.get("notes", []))
        cards.append(
            f'<div class="card"><div class="slot">{ep["no"]}편 · {e(ep["format"])}</div>'
            f'<h2>{e(ep["hook"])}</h2>'
            + (f'<div class="slot">훅·구조·반전</div><ul class="meta">{notes}</ul>' if notes else "")
            + f'<div class="meta">클립을 받으면 <b>01.mp4 ~ {len(ep["scenes"]):02d}.mp4</b>로 이름을 바꿔 '
            f'<b>clips/{ep["no"]}</b> 폴더에 넣으세요.</div>'
            f'<pre hidden id="{all_id}">{e(chr(10).join(prompts))}</pre>'
            f'<button data-t="{all_id}">{len(ep["scenes"])}개 한 번에 복사</button>'
            f'<ol>{"".join(rows)}</ol>'
            f'<div class="slot">업로드</div>'
            f'<div class="text" id="t{ep["no"]}">{e(ep["title"])}</div><button data-t="t{ep["no"]}">제목 복사</button>'
            f'<div class="text" id="d{ep["no"]}">{e(meta)}</div><button data-t="d{ep["no"]}">설명 복사</button>'
            + (f'<div class="slot" style="margin-top:12px">올리기 전 확인</div><ul class="meta">{checks}</ul>' if checks else "")
            + "</div>")
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>쇼츠 {e(data["date"])}</title>
<style>
body{{margin:0;background:#f2f4f7;font-family:-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;color:#111;word-break:keep-all}}
.wrap{{max-width:560px;margin:0 auto;padding:18px 14px 60px}}
h1{{font-size:18px;margin:4px 0 14px}} h2{{font-size:20px;margin:4px 0 8px}}
.card{{background:#fff;border:1px solid #dde2ea;border-radius:14px;padding:16px;margin-bottom:14px}}
.slot{{font-size:13px;font-weight:700;color:#1857A5;margin-bottom:6px}}
.text{{white-space:pre-wrap;font-size:15px;line-height:1.6;margin-top:10px}}
.meta{{font-size:13px;color:#5A6577;line-height:1.6}}
ol{{padding-left:22px}} li{{margin:12px 0}}
.cap{{white-space:pre-wrap;font-weight:700;font-size:15px}}
.pr{{font-size:12px;color:#5A6577;margin-top:4px}}
button{{border:0;background:#111;color:#fff;font-weight:700;padding:8px 12px;border-radius:8px;font-size:13px;margin:8px 6px 0 0}}
button.done{{background:#888}}
</style></head><body><div class="wrap">
<h1>쇼츠 · {e(data["date"])} · {e(data.get("channel", ""))} · {len(data["episodes"])}편</h1>
<div class="card meta">프롬프트 복사 버튼은 공통 화풍·캐릭터 설명이 앞에 붙은 채로 복사됩니다. 클립은 <b>세로 9:16</b>으로 만드세요.</div>
{"".join(cards)}
</div><script>
document.querySelectorAll("button[data-t]").forEach(b=>b.onclick=async()=>{{
  const t=document.getElementById(b.dataset.t).textContent;
  try{{await navigator.clipboard.writeText(t)}}catch(e){{const a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();document.execCommand("copy");a.remove()}}
  b.textContent="복사됨 ✓";b.classList.add("done")}});
</script></body></html>"""


def cmd_page(args):
    data = load(args.json)
    out = Path(args.json).with_suffix(".html")
    out.write_text(render_page(data), encoding="utf-8")
    print(f"✓ {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


# ---------- 클립 붙이기 ----------

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg 실패:\n{' '.join(map(str, cmd))}\n{r.stderr[-2000:]}")
    return r.stdout


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "default=nw=1:nk=1", str(path)]).strip())


def ass_time(t):
    cs = round(t * 100)
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def captions(sc):
    c = sc["caption"]
    return [c] if isinstance(c, str) else c


def ass_text(s):
    return s.replace("{", "(").replace("}", ")").replace("\n", "\\N")


def find_audio(folder, i):
    if not folder:
        return None
    for ext in AUDIO_EXT:
        p = Path(folder) / f"{i:02d}{ext}"
        if p.exists():
            return p
    return None


def cmd_stitch(args):
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        sys.exit("ffmpeg가 없습니다. https://ffmpeg.org 에서 설치하세요.")
    data = load(args.json)
    ep = episode(data, args.no)
    scenes = ep["scenes"]
    clips = sorted(p for p in Path(args.clips).iterdir() if p.suffix.lower() in VIDEO_EXT)
    if len(clips) != len(scenes):
        sys.exit(f"클립 {len(clips)}개, 장면 {len(scenes)}개 — 개수가 같아야 합니다 ({args.clips})")
    out = Path(args.out) if args.out else OUT_DIR / f"{data['date']}-{ep['no']}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "fonts").mkdir()
        for f in FONTS_DIR.glob("*.woff2"):
            shutil.copy(f, tmp / "fonts")

        # 1) 장면마다 세로 1080x1920·30fps로 맞추고, 내레이션이 더 길면 마지막 프레임으로 늘림
        starts, voices, t = [], [], 0.0
        for i, (clip, sc) in enumerate(zip(clips, scenes), 1):
            voice = find_audio(args.voice, i)
            target = duration(clip)
            if voice:
                target = max(target, duration(voice) + 0.4)
            seg = tmp / f"seg{i:02d}.mp4"
            run(["ffmpeg", "-y", "-i", str(clip), "-vf",
                 f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,"
                 f"tpad=stop_mode=clone:stop_duration={target:.2f}",
                 "-t", f"{target:.3f}", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                 "-pix_fmt", "yuv420p", str(seg)])
            starts.append(t)
            voices.append(voice)
            print(f"  {i:02d} {clip.name} → {target:.1f}초{' + 내레이션' if voice else ''}")
            t += duration(seg)
        total = t

        # 2) 이어 붙이기
        (tmp / "list.txt").write_text("".join(f"file 'seg{i:02d}.mp4'\n" for i in range(1, len(scenes) + 1)))
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "joined.mp4"], cwd=tmp)

        # 3) 자막: 위에 고정 제목, 아래쪽에 장면 자막
        ends = starts[1:] + [total]
        lines = [f"Dialogue: 0,{ass_time(0)},{ass_time(total)},Hook,,0,0,0,,{ass_text(ep['hook'])}"]
        for s, e, sc in zip(starts, ends, scenes):
            caps = captions(sc)
            step = (e - s) / len(caps)
            lines += [f"Dialogue: 0,{ass_time(s + j * step)},{ass_time(s + (j + 1) * step)},Cap,,0,0,0,,{ass_text(c)}"
                      for j, c in enumerate(caps)]
        (tmp / "subs.ass").write_text(ASS_HEAD + "\n".join(lines) + "\n", encoding="utf-8")

        # 4) 소리: 장면별 내레이션 + 배경음악 (없으면 무음 트랙)
        cmd = ["ffmpeg", "-y", "-i", "joined.mp4"]
        parts, n = [], 1
        for s, v in zip(starts, voices):
            if v:
                cmd += ["-i", str(Path(v).resolve())]
                ms = int(s * 1000)
                parts.append(f"[{n}:a]adelay={ms}|{ms},aresample=48000[a{n}]")
                n += 1
        if args.bgm:
            cmd += ["-stream_loop", "-1", "-i", str(Path(args.bgm).resolve())]
            vol = 0.12 if n > 1 else 0.35
            parts.append(f"[{n}:a]volume={vol},aresample=48000[a{n}]")
            n += 1
        if n == 1:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
            parts.append("[1:a]anull[a1]")
            n = 2
        mix = "".join(f"[a{j}]" for j in range(1, n))
        graph = ";".join(["[0:v]ass=subs.ass:fontsdir=fonts[v]"] + parts
                         + [f"{mix}amix=inputs={n - 1}:normalize=0:duration=longest[a]"])
        cmd += ["-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out.resolve())]
        run(cmd, cwd=tmp)

    print(f"✓ {out} ({total:.1f}초)")
    if total > SHORTS_MAX:
        print(f"  ⚠ {SHORTS_MAX}초를 넘어서 쇼츠가 아니라 일반 영상으로 올라갑니다")
    if not any(voices):
        print("  ※ 내레이션 없음 — 자막만 있는 영상입니다. 목소리를 넣으면 시청 유지율이 올라갑니다")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("page", help="프롬프트·업로드 정보 복사 페이지 만들기")
    p.add_argument("json")
    p.set_defaults(func=cmd_page)
    s = sub.add_parser("stitch", help="클립을 붙여 쇼츠 1편 만들기")
    s.add_argument("json")
    s.add_argument("no", type=int, help="편 번호")
    s.add_argument("clips", help="클립 폴더 (파일 이름순 = 장면 순서)")
    s.add_argument("--voice", help="장면별 내레이션 폴더 (01.mp3 ...)")
    s.add_argument("--bgm", help="배경음악 파일")
    s.add_argument("--out", help="저장 경로 (기본: youtube/out/<날짜>-<편>.mp4)")
    s.set_defaults(func=cmd_stitch)
    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
