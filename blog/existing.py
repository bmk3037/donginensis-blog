"""세 블로그에 이미 올라간 글을 모아 두고, 새 글이 겹치는지 검사합니다.

사용법:
    python -m blog.existing sync                      # 세 블로그 RSS로 발행된 글 본문을 existing/에 저장
    python -m blog.existing check posts/<글>/post.json  # 새 글과 기존 글·다른 초안의 겹침 검사

겹침 판단
- 같은 문장: 20자 이상 문장이 다른 글에 그대로 있으면 (네이버 유사 문서의 가장 확실한 신호)
- 본문 유사도: 5글자 조각 기준으로 새 글의 몇 %가 다른 글에 있는지
- 제목 유사도: 제목 2글자 조각 기준
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from pathlib import Path

from blog.blogs import ORDER

ROOT = Path(__file__).resolve().parent.parent
EXISTING_DIR = ROOT / "existing"
POSTS_DIR = ROOT / "posts"
UA = {"User-Agent": "Mozilla/5.0 (compatible; donginensis-blog-check)"}

# 같은 회사 같은 분야 글이라 용어가 겹치는 건 자연스럽습니다. 아래 기준은 실제 글로 맞춘 값입니다.
BODY_WARN, BODY_FAIL = 0.15, 0.25
TITLE_WARN = 0.45
SENTENCE_MIN = 20


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="ignore")


def _clean(fragment):
    text = re.sub(r"<br\s*/?>", "\n", fragment)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).replace("​", "").strip()


def post_text(page):
    """네이버 글 페이지 HTML에서 본문 문단만 꺼냅니다 (스마트에디터 ONE, 예전 에디터 둘 다)."""
    paras = re.findall(r'<p class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>', page, re.S)
    if paras:
        lines = [_clean(p) for p in paras]
    else:
        m = re.search(r'id="postViewArea"[^>]*>(.*?)</div>\s*<!--', page, re.S)
        lines = _clean(m.group(1)).splitlines() if m else []
    return "\n".join(l for l in lines if l)


def fetch_blog(blog_id):
    rss = _get(f"https://rss.blog.naver.com/{blog_id}.xml")
    items = []
    for item in re.findall(r"<item>(.*?)</item>", rss, re.S):
        title = _clean(re.sub(r"<!\[CDATA\[|\]\]>", "", re.search(r"<title>(.*?)</title>", item, re.S).group(1)))
        link = re.search(r"<link>(.*?)</link>", item, re.S).group(1).strip()
        date = re.search(r"<pubDate>(.*?)</pubDate>", item, re.S)
        log_no = re.search(r"/(\d+)", link.split(blog_id, 1)[-1]).group(1)
        page = _get(f"https://blog.naver.com/PostView.naver?blogId={blog_id}&logNo={log_no}")
        items.append({"blog": blog_id, "log_no": log_no, "title": title, "url": f"https://blog.naver.com/{blog_id}/{log_no}",
                      "date": date.group(1).strip() if date else "", "text": post_text(page)})
    return items


def sync():
    EXISTING_DIR.mkdir(exist_ok=True)
    for blog_id in ORDER:
        items = fetch_blog(blog_id)
        (EXISTING_DIR / f"{blog_id}.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"  {blog_id}: 발행된 글 {len(items)}개")


# ── 겹침 계산 ──────────────────────────────────────────────

def _norm(text):
    text = re.sub(r"\[(?:이미지|사진):[^\]]*\]", "", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)  # 링크 주소
    return re.sub(r"[^0-9A-Za-z가-힣]", "", text)


def shingles(text, n=5):
    t = _norm(text)
    return {t[i:i + n] for i in range(max(len(t) - n + 1, 0))}


CONTACT_RE = re.compile(r"0\d{1,2}-\d{3,4}-\d{4}|[\w.]+@[\w.]+|https?://\S+|donginensis\.com\S*")


def sentences(text):
    """비교할 문장 목록. 전화·이메일·주소만 다른 연락처 줄은 빼고 셉니다."""
    text = re.sub(r"\[(?:이미지|사진):[^\]]*\]|\]\([^)]*\)|[#*>|`]", " ", text)
    parts = re.split(r"(?<=[.?!다요])\s+|\n+", text)
    return [s.strip() for s in parts
            if len(_norm(s)) >= SENTENCE_MIN and len(_norm(CONTACT_RE.sub("", s))) >= SENTENCE_MIN]


def title_sim(a, b):
    def grams(t):
        t = _norm(t)
        return {t[i:i + 2] for i in range(len(t) - 1)}
    ga, gb = grams(a), grams(b)
    return len(ga & gb) / max(len(ga | gb), 1)


def corpus(exclude_dir=None):
    """비교 대상: 발행된 글(existing/) + 다른 초안(posts/)"""
    docs = []
    for f in sorted(EXISTING_DIR.glob("*.json")):
        for it in json.loads(f.read_text(encoding="utf-8")):
            docs.append({"where": f"발행됨 {it['blog']} · {it['date'][5:16]}", "title": it["title"], "text": it["text"]})
    for f in sorted(POSTS_DIR.glob("*/post.json")):
        if exclude_dir and f.parent.resolve() == Path(exclude_dir).resolve():
            continue
        p = json.loads(f.read_text(encoding="utf-8"))
        docs.append({"where": f"초안 {f.parent.name}", "title": p["title"], "text": p["body_markdown"]})
    return docs


def check(post, post_dir=None, docs=None):
    """[(수준, 메시지)] 를 돌려줍니다. 수준: FAIL(고쳐야 함) / WARN(확인)"""
    docs = corpus(post_dir) if docs is None else docs
    mine = shingles(post["body_markdown"])
    my_sents = sentences(post["body_markdown"])
    results = []
    for d in docs:
        other = shingles(d["text"])
        body = len(mine & other) / max(len(mine), 1)
        other_norm = _norm(d["text"])
        same = [s for s in my_sents if _norm(s) in other_norm]
        tsim = title_sim(post["title"], d["title"])
        label = f"[{d['where']}] {d['title'][:40]}"
        if same:
            results.append(("FAIL", f"같은 문장 {len(same)}개 — {label}: “{same[0][:50]}…”"))
        if body >= BODY_FAIL:
            results.append(("FAIL", f"본문 {body:.0%} 겹침 — {label}"))
        elif body >= BODY_WARN:
            results.append(("WARN", f"본문 {body:.0%} 겹침 — {label}"))
        if tsim >= TITLE_WARN:
            results.append(("WARN", f"제목 비슷함 {tsim:.0%} — {label}"))
    return results


def main(argv=None):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sync")
    c = sub.add_parser("check")
    c.add_argument("post_json")
    args = p.parse_args(argv)
    if args.cmd == "sync":
        sync()
        return 0
    path = Path(args.post_json)
    results = check(json.loads(path.read_text(encoding="utf-8")), path.parent)
    for level, msg in results:
        print(f"  {'✗' if level == 'FAIL' else '⚠'} {msg}")
    if not results:
        print("  ✓ 겹치는 글 없음")
    return 1 if any(l == "FAIL" for l, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
