"""주제를 골라 Claude로 네이버 블로그 초안을 만듭니다.

사용법:
    python -m blog.generate                 # 다음 주제 1편
    python -m blog.generate --count 2       # 다음 주제 2편
    python -m blog.generate --id 17         # 특정 주제
    python -m blog.generate --id 17 --dry-run   # API 호출 없이 보낼 프롬프트만 출력
    python -m blog.generate --id 17 --from-json post.json --date 2026-10-14
        # API 없이: 대화창에서 Claude가 쓴 글(JSON)로 미리보기·이미지 묶음 만들기

결과물: posts/<날짜>-<id>/ 아래 preview.html(붙여넣기용), post.md, meta.json, issue.md
"""
import argparse
import datetime as dt
import json
import sys
import zipfile
from pathlib import Path

import anthropic

from blog import render, topics

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"
KST = dt.timezone(dt.timedelta(hours=9))
MODEL = "claude-opus-5-5"

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "네이버 블로그 제목. 핵심 키워드를 앞쪽에, 25~40자"},
        "body_markdown": {
            "type": "string",
            "description": "본문 마크다운. 소제목은 ##, 사진 자리는 한 줄에 [사진: 설명] 형식",
        },
        "tags": {"type": "array", "items": {"type": "string"}, "description": "태그 8~12개, # 없이, 띄어쓰기 없이"},
        "fact_check": {
            "type": "array",
            "items": {"type": "string"},
            "description": "본문에 쓴 수치·고객사·인증 등 사람이 확인해야 할 사실 목록",
        },
    },
    "required": ["title", "body_markdown", "tags", "fact_check"],
    "additionalProperties": False,
}

BASE_CHECKLIST = [
    "수치·고객사·인증 표기가 회사 자료와 같은지 확인 (아래 사실 확인 목록)",
    "파란 상자 자리에 images 폴더의 그림 넣기 (01-cover.png가 대표 이미지)",
    "담당자 한마디: 실제 경험 1~2문장 직접 덧붙이기 (미리보기 하단 질문 참고, 저품질 방지에 가장 효과적)",
    "붙여넣은 뒤 모바일 미리보기로 줄바꿈·글자 크기 확인",
    "실제 현장·제작 사진이 있으면 연출 이미지 대신 넣기 (노출에 가장 좋음)",
    "고객사 이름·현장 사진 공개가 계약상 문제없는지 확인",
    "본문 끝 홈페이지 링크가 눌리는지 확인",
    "태그 입력 후 발행 (매일 비슷한 시간에, 예약 발행 활용)",
]


def build_system():
    knowledge = ROOT / "knowledge"
    return (
        "당신은 ㈜동인엔시스의 네이버 블로그 담당 작가입니다. "
        "아래 글쓰기 규칙과 회사 자료만 근거로 글을 씁니다. "
        "회사 자료에 없는 사실은 쓰지 말고, 확실하지 않으면 빼세요.\n\n"
        f"<style_guide>\n{(knowledge / 'style.md').read_text(encoding='utf-8')}\n</style_guide>\n\n"
        f"<company_facts>\n{(knowledge / 'company.md').read_text(encoding='utf-8')}\n</company_facts>"
    )


def build_request(topic):
    return (
        "다음 주제로 네이버 블로그 글 1편을 써 주세요.\n\n"
        f"- 분류: {topic['category']}\n"
        f"- 가제목: {topic['title']}\n"
        f"- 핵심 키워드: {topic['keyword']}\n"
        f"- 글 끝에서 연결할 홈페이지 페이지: {topic['landing_url']}\n"
        f"- 다룰 내용: {topic['brief']}\n\n"
        "가제목은 더 나은 제목이 있으면 바꿔도 됩니다. "
        "글 끝에는 글쓰기 규칙의 '글 마무리' 흐름대로 위 홈페이지 링크를 마크다운 링크로 넣어 주세요."
    )


def call_claude(client, topic):
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=32000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        cache_control={"type": "ephemeral"},
        system=build_system(),
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": POST_SCHEMA}},
        messages=[{"role": "user", "content": build_request(topic)}],
    ) as stream:
        message = stream.get_final_message()

    if message.stop_reason == "refusal":
        raise RuntimeError(f"Claude가 작성을 거절했습니다 (주제 {topic['id']}): {message.stop_details}")
    if message.stop_reason == "max_tokens":
        raise RuntimeError(f"글이 너무 길어 중간에 잘렸습니다 (주제 {topic['id']})")

    # 대체 모델로 넘어간 경우 마지막 fallback 블록 뒤의 텍스트만 씁니다
    blocks = list(message.content)
    last_fallback = max((i for i, b in enumerate(blocks) if b.type == "fallback"), default=-1)
    text = "".join(b.text for b in blocks[last_fallback + 1:] if b.type == "text")
    return json.loads(text)


def write_post(topic, post, today=None):
    today = today or dt.datetime.now(KST).date()
    out_dir = POSTS_DIR / f"{today.isoformat()}-{int(topic['id']):03d}"
    out_dir.mkdir(parents=True, exist_ok=True)

    campaign = f"post{int(topic['id']):03d}"
    body_md = render.tag_site_links(post["body_markdown"], campaign)
    tags = [t.lstrip("#").replace(" ", "") for t in post["tags"]]
    checklist = BASE_CHECKLIST + [f"사실 확인: {c}" for c in post["fact_check"]]
    photos = post.get("photos", [])
    have = {p.name for p in (out_dir / "images").glob("*.png")}
    if any(p["file"] not in have for p in photos):
        checklist.insert(2, "사진 파일이 없는 자리는 프롬프트를 ChatGPT에 넣어 만든 뒤 넣기 (사진 아래 '연출 이미지' 표기)")

    (out_dir / "post.json").write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "post.md").write_text(f"# {post['title']}\n\n{body_md}\n", encoding="utf-8")
    (out_dir / "preview.html").write_text(
        render.preview_page(post["title"], tags, render.to_html(body_md, photos, have), checklist,
                            post.get("personal_prompts", [])), encoding="utf-8"
    )
    meta = {
        "topic_id": topic["id"],
        "title": post["title"],
        "tags": tags,
        "keyword": topic["keyword"],
        "landing_url": render.add_utm(topic["landing_url"], campaign),
        "fact_check": post["fact_check"],
        "created": today.isoformat(),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "issue.md").write_text(
        issue_body(topic, post["title"], tags, render.to_issue_markdown(body_md, photos, have), checklist, out_dir),
        encoding="utf-8")
    return out_dir


def pack(out_dir, dest_dir):
    """네이버에 올릴 때 필요한 파일(미리보기 + 이미지)을 zip 하나로 묶습니다."""
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    zip_path = dest_dir / f"{out_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(out_dir / "preview.html", f"{out_dir.name}/preview.html")
        for png in sorted((out_dir / "images").glob("*.png")):
            zf.write(png, f"{out_dir.name}/images/{png.name}")
    return zip_path


def issue_body(topic, title, tags, body_md, checklist, out_dir):
    rel = out_dir.relative_to(ROOT).as_posix()
    checks = "\n".join(f"- [ ] {c}" for c in checklist)
    return (
        f"<!-- topic-id: {topic['id']} -->\n"
        f"**제목:** {title}\n\n"
        f"**태그:** {' '.join('#' + t for t in tags)}\n\n"
        f"**붙여넣기용 미리보기:** `{rel}/preview.html` (내려받아 브라우저로 열고 '본문 복사')\n\n"
        f"### 발행 전 확인\n{checks}\n\n"
        "발행한 뒤 이 이슈에 네이버 글 주소를 댓글로 남기고 이슈를 닫으면 주제 목록에 '발행됨'으로 기록됩니다.\n\n"
        "---\n\n"
        f"{body_md}\n"
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="동인엔시스 네이버 블로그 초안 생성")
    parser.add_argument("--id", action="append", help="특정 주제 id (여러 번 지정 가능)")
    parser.add_argument("--count", type=int, default=1, help="다음 주제 몇 편 (--id가 없을 때)")
    parser.add_argument("--dry-run", action="store_true", help="API를 부르지 않고 프롬프트만 출력")
    parser.add_argument("--from-json", help="API 대신 이미 쓴 글(JSON: title, body_markdown, tags, fact_check)을 사용")
    parser.add_argument("--date", help="글 폴더 날짜 (YYYY-MM-DD, 기본: 오늘)")
    parser.add_argument("--pack", help="미리보기+이미지 zip을 만들 폴더")
    args = parser.parse_args(argv)
    day = dt.date.fromisoformat(args.date) if args.date else None

    rows = topics.load()
    if args.from_json:
        if not args.id or len(args.id) != 1:
            parser.error("--from-json은 --id 하나와 함께 써야 합니다")
        topic = topics.find(rows, args.id[0])
        post = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
        out_dir = write_post(topic, post, today=day)
        with_space, no_space = render.char_count(post["body_markdown"])
        warn = "  ⚠ 2,500자 미만 — 내용 보강 필요" if no_space < 2500 else ""
        print(f"  글자 수: 공백 제외 {no_space:,}자 / 공백 포함 {with_space:,}자{warn}")
        if topic["status"] == "todo":
            topics.set_status(topic["id"], "drafted")
        print(f"  → {out_dir.relative_to(ROOT).as_posix()}/preview.html")
        if args.pack:
            print(f"  → {pack(out_dir, args.pack)}")
        return 0

    chosen = [topics.find(rows, i) for i in args.id] if args.id else topics.next_todo(rows, args.count)
    if not chosen:
        print("쓸 주제가 남아 있지 않습니다. topics.csv에 새 주제를 추가해 주세요.")
        return 0

    if args.dry_run:
        print(build_system()[:600] + "\n...\n")
        for topic in chosen:
            print(build_request(topic) + "\n" + "-" * 40)
        return 0

    client = anthropic.Anthropic()
    made = []
    for topic in chosen:
        print(f"[{topic['id']}] {topic['title']} 작성 중...", flush=True)
        post = call_claude(client, topic)
        out_dir = write_post(topic, post)
        topics.set_status(topic["id"], "drafted")
        made.append(out_dir.relative_to(ROOT).as_posix())
        print(f"  → {made[-1]}/preview.html")

    # GitHub Actions에서 다음 단계(이슈 생성)가 읽을 목록
    (ROOT / ".last_drafts").write_text("\n".join(made) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
