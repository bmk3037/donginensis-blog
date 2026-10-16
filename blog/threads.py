"""쓰레드(Threads) 하루 3개 글: 검수 + 휴대폰에서 복사하기 좋은 미리보기.

사용법:
    python -m blog.threads threads/2026-10-17.json      # 검수 후 threads/2026-10-17.html 생성

threads/<날짜>.json 형식:
{
  "date": "2026-10-17",
  "posts": [
    {"slot": "아침", "type": "생각", "text": "...", "tag": "지능형제어반", "first_comment": "", "source": ""},
    {"slot": "점심", "type": "지식", ...}, {"slot": "저녁", "type": "질문", ...}
  ],
  "replies": [{"if": "예상 댓글", "reply": "답글 초안"}],
  "question": "대표에게 드리는 오늘의 질문"
}
source: 경험담이면 근거가 된 ceo_notes.md 날짜 (예: "ceo_notes 2026-10-16")
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

from blog import existing, quality

ROOT = Path(__file__).resolve().parent.parent
THREADS_DIR = ROOT / "threads"
SLOTS = ["아침", "점심", "저녁"]
TYPES = {"아침": "생각", "점심": "지식", "저녁": "질문"}
URL_RE = re.compile(r"https?://|www\.|\.com\b")
# 경험담처럼 읽히는 표현: 근거(source) 없이 쓰면 지어낸 이야기가 될 수 있음
STORY_RE = re.compile(r"어제|지난주|지난달|그날|그때 (저|제가|현장)|얼마 전|기억이 납니다|일이 있었|겪었")


def other_threads(date):
    docs = []
    for f in sorted(THREADS_DIR.glob("*.json")):
        if f.stem == date:
            continue
        for p in json.loads(f.read_text(encoding="utf-8")).get("posts", []):
            docs.append({"where": f"쓰레드 {f.stem} {p.get('slot', '')}", "title": "", "text": p["text"]})
    return docs


def recent_links(date, days=2):
    """바로 앞 며칠 동안 첫 댓글에 링크를 단 횟수"""
    files = sorted(f for f in THREADS_DIR.glob("*.json") if f.stem < date)[-days:]
    n = 0
    for f in files:
        n += sum(1 for p in json.loads(f.read_text(encoding="utf-8")).get("posts", []) if URL_RE.search(p.get("first_comment", "")))
    return n


def check(day, docs=None, links_before=0):
    out = []
    fail = lambda m: out.append(("FAIL", m))  # noqa: E731
    warn = lambda m: out.append(("WARN", m))  # noqa: E731
    posts = day.get("posts", [])
    if [p.get("slot") for p in posts] != SLOTS:
        fail("글은 아침·점심·저녁 3개, 이 순서로")
    corpus = docs if docs is not None else existing.corpus() + other_threads(day.get("date", ""))
    links = 0
    for p in posts:
        slot, text = p.get("slot", "?"), p.get("text", "")
        if p.get("type") != TYPES.get(slot):
            warn(f"{slot}: 종류는 '{TYPES.get(slot)}'로 (지금 '{p.get('type')}')")
        n = len(text)
        if n > 500:
            fail(f"{slot}: {n}자 — 쓰레드는 500자까지")
        elif n > 300:
            warn(f"{slot}: {n}자 — 쓰레드는 짧을수록 잘 읽힘 (80~250자)")
        elif n < 40:
            warn(f"{slot}: {n}자 — 너무 짧음")
        if URL_RE.search(text):
            fail(f"{slot}: 본문에 링크 — 링크는 첫 댓글(first_comment)에")
        if "#" in text:
            warn(f"{slot}: 본문에 # — 태그는 tag 칸에 1개만")
        if not p.get("tag") or " " in p["tag"] or "#" in p["tag"]:
            warn(f"{slot}: 태그(tag)는 띄어쓰기·# 없이 1개")
        for w in quality.BANNED:
            if w in text:
                fail(f"{slot}: 과장 표현 '{w}'")
        if STORY_RE.search(text) and not p.get("source"):
            warn(f"{slot}: 경험담처럼 읽힘 — 대표 답변(ceo_notes.md)이 근거면 source에 날짜를, 아니면 표현을 바꾸기")
        if URL_RE.search(p.get("first_comment", "")):
            links += 1
        for lv, m in existing.check({"title": "", "body_markdown": text}, docs=corpus):
            if "같은 문장" in m:
                out.append((lv, f"{slot}: {m}"))
    if links > 1:
        warn(f"링크 댓글 {links}개 — 하루 1개 이하")
    if links and links_before:
        warn("최근 이틀 안에 링크를 달았음 — 사흘에 한 번 정도로")
    if posts and posts[-1].get("slot") == "저녁" and len(day.get("replies", [])) < 2:
        warn("저녁 질문 글의 답글 초안(replies) 2~3개")
    if not day.get("question"):
        warn("대표에게 드릴 오늘의 질문(question)이 없음")
    return out


PAGE = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>쓰레드 {date}</title>
<style>
body{{margin:0;background:#f2f4f7;font-family:-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;color:#111;word-break:keep-all}}
.wrap{{max-width:560px;margin:0 auto;padding:18px 14px 60px}}
h1{{font-size:18px;margin:4px 0 14px}}
.card{{background:#fff;border:1px solid #dde2ea;border-radius:14px;padding:16px;margin-bottom:14px}}
.slot{{font-size:13px;font-weight:700;color:#1857A5;margin-bottom:8px}}
.text{{white-space:pre-wrap;font-size:16px;line-height:1.6}}
.meta{{font-size:13px;color:#5A6577;margin-top:10px}}
button{{border:0;background:#111;color:#fff;font-weight:700;padding:8px 12px;border-radius:8px;font-size:13px;margin:10px 6px 0 0}}
button.done{{background:#888}}
.q{{border-color:#E83E30}} .q .slot{{color:#E83E30}}
.review li{{font-size:13px;margin:3px 0}}
</style></head><body><div class="wrap">
<h1>쓰레드 · {date} · 동인엔시스 회사 계정</h1>
{review}{cards}{replies}{question}
</div><script>
document.querySelectorAll("button[data-t]").forEach(b=>b.onclick=async()=>{{
  const t=document.getElementById(b.dataset.t).innerText;
  try{{await navigator.clipboard.writeText(t)}}catch(e){{const a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();document.execCommand("copy");a.remove()}}
  b.textContent="복사됨 ✓";b.classList.add("done")}});
</script></body></html>"""


def render(day, results):
    e = html.escape
    cards = []
    for i, p in enumerate(day["posts"]):
        fc = p.get("first_comment", "")
        cards.append(
            f'<div class="card"><div class="slot">{e(p["slot"])} · {e(p.get("type", ""))}</div>'
            f'<div class="text" id="t{i}">{e(p["text"])}</div>'
            f'<div class="meta">주제 태그: <b id="g{i}">{e(p.get("tag", ""))}</b>'
            f'{" · 근거: " + e(p["source"]) if p.get("source") else ""}</div>'
            f'<button data-t="t{i}">글 복사</button><button data-t="g{i}">태그 복사</button>'
            + (f'<div class="meta">첫 댓글로 달기:</div><div class="text" id="c{i}" style="font-size:14px">{e(fc)}</div>'
               f'<button data-t="c{i}">댓글 복사</button>' if fc else "")
            + "</div>")
    reps = "".join(f'<li><b>{e(r["if"])}</b><br><span id="r{i}">{e(r["reply"])}</span> '
                   f'<button data-t="r{i}">복사</button></li>' for i, r in enumerate(day.get("replies", [])))
    replies = f'<div class="card"><div class="slot">저녁 질문 글 · 답글 초안</div><ul style="padding-left:18px;font-size:14px;line-height:1.6">{reps}</ul></div>' if reps else ""
    question = (f'<div class="card q"><div class="slot">오늘의 질문 (대표님 답변 부탁드립니다)</div>'
                f'<div class="text">{e(day["question"])}</div>'
                '<div class="meta">대화창에 한두 줄로 답해 주시면 다음 쓰레드 \'생각\' 글에 씁니다.</div></div>') if day.get("question") else ""
    if results:
        items = "".join(f'<li style="color:{"#c62828" if lv == "FAIL" else "#8a6100"}">{"✗" if lv == "FAIL" else "⚠"} {e(m)}</li>' for lv, m in results)
        review = f'<div class="card review"><div class="slot">자동 검수</div><ul style="padding-left:18px">{items}</ul></div>'
    else:
        review = '<div class="card review"><div class="slot">자동 검수</div><div style="font-size:13px;color:#0a7a3a">✓ 겹침·길이·링크 점검 통과</div></div>'
    return PAGE.format(date=e(day["date"]), review=review, cards="".join(cards), replies=replies, question=question)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    a = ap.parse_args(argv)
    path = Path(a.json)
    day = json.loads(path.read_text(encoding="utf-8"))
    results = check(day, links_before=recent_links(day["date"]))
    path.with_suffix(".html").write_text(render(day, results), encoding="utf-8")
    for lv, m in results:
        print(f"  {'✗' if lv == 'FAIL' else '⚠'} {m}")
    if not results:
        print("  ✓ 쓰레드 검수 통과")
    print(f"  → {path.with_suffix('.html')}")
    return 1 if any(lv == "FAIL" for lv, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
