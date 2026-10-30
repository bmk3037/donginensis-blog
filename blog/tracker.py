"""초안 목록 이슈 본문 만들기: 블로그별로 발행 예정 초안을 한눈에 봅니다.

사용법:
    python -m blog.tracker              # 목록 마크다운을 출력 (GitHub 목록 이슈 본문에 붙여 넣기)
    python -m blog.tracker --mark       # 발행된 초안을 찾아 topics.csv에도 '발행됨'으로 기록

발행 여부는 existing/<블로그>.json(블로그 RSS로 받은 발행 글)에 같은 제목이 있는지로 판단합니다.
먼저 python -m blog.existing sync 를 실행해 두세요.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from blog import blogs, topics

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
EXISTING_DIR = ROOT / "existing"
DIR_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)-(\d{3})$")
REPO_URL = "https://github.com/bmk3037/donginensis-blog/tree/main/posts"


def _norm(title):
    return re.sub(r"[^0-9A-Za-z가-힣]", "", title)


def published_titles():
    """블로그별 발행된 글 제목 → 주소"""
    out = {}
    for f in EXISTING_DIR.glob("*.json"):
        out[f.stem] = {_norm(it["title"]): it["url"] for it in json.loads(f.read_text(encoding="utf-8"))}
    return out


def drafts():
    rows = []
    for f in sorted(POSTS_DIR.glob("*/post.json")):
        m = DIR_RE.match(f.parent.name)
        if not m:
            continue
        date, blog_id, tid = m.groups()
        post = json.loads(f.read_text(encoding="utf-8"))
        rows.append({"date": date, "blog": blog_id, "id": str(int(tid)), "dir": f.parent.name, "title": post["title"]})
    return rows


def build(rows, published, notes=None):
    notes = notes or {}
    lines = ["<!-- blog-tracker -->",
             "블로그별 초안 목록입니다. 매일 아침 루틴이 새 초안을 더하고, 블로그에 발행된 글은 자동으로 체크합니다.",
             "초안 파일(미리보기·이미지)은 각 줄의 폴더에 있습니다.", ""]
    done_n = 0
    for blog_id in blogs.ORDER:
        mine = [r for r in rows if r["blog"] == blog_id]
        if not mine:
            continue
        lines.append(f"## {blogs.get(blog_id)['name']}")
        lines.append("")
        for r in mine:
            url = published.get(blog_id, {}).get(_norm(r["title"]))
            done_n += bool(url)
            mark = "x" if url else " "
            tail = f" · 발행됨 {url}" if url else ""
            note = f" · ⚠ {notes[r['dir']]}" if r["dir"] in notes else ""
            lines.append(f"- [{mark}] {r['date'][5:]} · {r['title']} · [폴더]({REPO_URL}/{r['dir']}){tail}{note}")
        lines.append("")
    lines.insert(3, f"발행 {done_n} / 초안 {len(rows)}편")
    return "\n".join(lines).rstrip() + "\n"


def mark_published(rows, published):
    """발행된 초안의 주제를 topics.csv에서 published로 바꾸고, 바꾼 id 목록을 돌려줍니다."""
    status = {r["id"]: r["status"] for r in topics.load()}
    changed = []
    for r in rows:
        if published.get(r["blog"], {}).get(_norm(r["title"])) and status.get(r["id"]) != "published":
            topics.set_status(r["id"], "published")
            changed.append(r["id"])
    return changed


NOTES = {"2026-10-17-donginensis-011": "aside 'OPC UA Modbus TCP 차이'(10/25)와 같은 주제 — 발행 여부 판단 필요 (이슈 #8)"}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mark", action="store_true", help="발행된 초안을 topics.csv에 기록")
    a = ap.parse_args(argv)
    rows, pub = drafts(), published_titles()
    if a.mark:
        for tid in mark_published(rows, pub):
            print(f"주제 {tid} → published", file=sys.stderr)
    sys.stdout.write(build(rows, pub, NOTES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
