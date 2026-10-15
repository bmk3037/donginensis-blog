"""발행 전 자동 검수: 저품질 신호, 회사명 노출, 홈페이지 유입 장치를 확인합니다.

사용법:
    python -m blog.quality posts/<글>/post.json --blog donginensis --keyword "설비 데이터 수집"

결과: FAIL(고친 뒤 발행) / WARN(확인 후 판단)
"""
import argparse
import json
import re
import sys
from pathlib import Path

from blog import blogs, render

FORMATS = {"해설형", "Q&A형", "체크리스트형", "사례형", "비교형", "단계형", "용어형", "현장일지형"}
BANNED = ["혁신적인", "최고의", "완벽한", "업계 유일", "국내 유일", "국내 최초", "세계 최초", "100% 보장", "무조건"]
SITE_LINK_RE = re.compile(r"\]\((https?://(?:www\.)?donginensis\.com[^)]*)\)")
OTHER_LINK_RE = re.compile(r"\]\((https?://(?!(?:www\.)?donginensis\.com)[^)]*)\)")
BRAND = "동인엔시스"
# 동인엔시스가 무슨 회사인지 알려 주는 문장의 단서
INTRO_WORDS = ["제어반", "설계", "제작", "1991", "부산"]


def _plain(body_md):
    text = re.sub(r"^\[(?:이미지|사진):.*$", "", body_md, flags=re.M)
    return re.sub(r"\]\([^)]*\)", "]", text)


def _kw_re(word):
    """키워드 낱말 사이에 조사 1~2글자가 끼어도 같은 키워드로 봅니다 (예: 'OPC UA와 Modbus TCP', '설비 데이터를 수집')"""
    return re.compile(".{0,2}".join(re.escape(t) for t in word.split()))


def _count(text, word):
    return len(_kw_re(word).findall(re.sub(r"\s", "", text)))


def check(post, blog_id, keyword="", prev_format=None):
    out = []
    fail = lambda m: out.append(("FAIL", m))  # noqa: E731
    warn = lambda m: out.append(("WARN", m))  # noqa: E731
    body, title = post["body_markdown"], post["title"]
    plain = _plain(body)
    blog = blogs.get(blog_id)

    # 분량·구성
    _, chars = render.char_count(body)
    if chars < 2500:
        fail(f"본문 {chars:,}자 (공백 제외) — 2,500자 이상으로 보강")
    elif chars > 3800:
        warn(f"본문 {chars:,}자 — 너무 길면 끝까지 안 읽힘 (3,500자 안팎 권장)")
    h2 = len(re.findall(r"^## ", body, re.M))
    if not 5 <= h2 <= 8:
        warn(f"소제목 {h2}개 (5~8개 권장)")
    fmt = post.get("format", "")
    if fmt not in FORMATS:
        warn(f"post.json에 글 형식(format)을 적어 주세요: {', '.join(sorted(FORMATS))}")
    elif prev_format and fmt == prev_format:
        fail(f"같은 블로그 바로 전 글과 형식이 같음({fmt}) — 형식을 바꿔야 기계적인 글로 안 보임")
    if fmt != "Q&A형" and not re.search(r"자주 묻는|^\*\*Q", body, re.M):
        warn("자주 묻는 질문(FAQ) 3~5개가 없음")

    # 제목
    if not 18 <= len(title) <= 45:
        warn(f"제목 {len(title)}자 (25~40자 권장)")
    if keyword and not _kw_re(keyword).search(title.replace(" ", "")[:24]):
        warn(f"핵심 키워드 '{keyword}'가 제목 앞쪽에 없음")
    if keyword:
        n = _count(plain, keyword)
        if n < 3:
            warn(f"핵심 키워드 '{keyword}' 본문 {n}회 (4~8회 권장)")
        elif n > 12:
            fail(f"핵심 키워드 '{keyword}' 본문 {n}회 — 억지 반복은 저품질 신호 (4~8회)")
        elif n > 8:
            warn(f"핵심 키워드 '{keyword}' 본문 {n}회 — 일부는 '이 제어반'처럼 바꿔 쓰기 (4~8회)")

    # 회사명 노출 (관련 검색어로 동인엔시스가 검색되게)
    first = " ".join(l for l in plain.strip().splitlines()[:6] if l.strip())[:350]
    if BRAND not in first:
        warn("첫 문단에 '동인엔시스'가 없음 — 검색 결과 미리보기에 회사명이 보이게")
    brand_n = plain.count(BRAND)
    if brand_n < 3:
        warn(f"본문에 '동인엔시스' {brand_n}회 (3~6회 권장)")
    elif brand_n > 9:
        warn(f"본문에 '동인엔시스' {brand_n}회 — 광고처럼 보임 (3~6회)")
    sents = re.split(r"(?<=[.?!])\s+|\n+", plain)
    if not any(BRAND in s and sum(w in s for w in INTRO_WORDS) >= 2 for s in sents):
        warn("동인엔시스가 무슨 회사인지 알려 주는 문장이 없음 (예: 1991년부터 부산에서 제어반을 설계·제작)")

    # 홈페이지 유입
    site = SITE_LINK_RE.findall(body)
    if len(site) > 1:
        fail(f"홈페이지 링크 {len(site)}개 — 글당 1개")
    elif not site and "홈페이지" not in plain[-600:]:
        warn("글 끝에 홈페이지 안내(링크 또는 '블로그 상단 홈페이지 메뉴')가 없음")
    if OTHER_LINK_RE.findall(body):
        warn("다른 사이트 링크가 있음 — 빼는 것을 권장")

    # 태그
    tags = [t.lstrip("#").replace(" ", "") for t in post.get("tags", [])]
    if not 8 <= len(tags) <= 12:
        warn(f"태그 {len(tags)}개 (8~12개)")
    for t in blog["brand_tags"]:
        if t not in tags:
            fail(f"태그에 '{t}' 없음")
    if len(set(tags)) != len(tags):
        warn("같은 태그가 두 번 있음")

    # 금지 표현·사실
    for w in BANNED:
        if w in plain:
            fail(f"과장 표현 '{w}'")
    if re.search(r"고장을\s*(미리\s*)?예측(합니다|해 줍니다|한다)", plain):
        fail("AI가 고장을 예측한다고 단정함 — 'AI 이상탐지는 고도화 중'으로")
    for m in re.finditer(r"5\s*%", plain):
        if "목표" not in plain[max(m.start() - 60, 0):m.end() + 60]:
            fail("'5%' 절감 수치 옆에 '목표'라는 말이 없음 (실증 결과 아님)")
            break
    if "데이터센터" in plain and re.search(r"데이터센터[^.\n]{0,30}(납품|실적|구축했)", plain):
        warn("데이터센터 납품 실적처럼 읽히는 문장 — 실적 없음, 확인")

    # 글 안의 반복
    seen, dup = set(), set()
    for s in sents:
        k = re.sub(r"\W", "", s)
        if len(k) >= 20:
            (dup if k in seen else seen).add(k)
    if dup:
        warn(f"글 안에서 같은 문장이 {len(dup)}번 반복됨")

    # 이미지
    imgs = render.IMAGE_RE.findall(body)
    photos = render.PHOTO_RE.findall(body)
    if not imgs or imgs[0] != "01-cover.png":
        warn("본문 맨 위에 [이미지: 01-cover.png] 표지가 없음 (검색 썸네일)")
    if len(imgs) - 1 < 2:
        warn(f"설명 이미지 {max(len(imgs) - 1, 0)}장 (2~3장 권장)")
    if not photos:
        warn("사진 자리가 없음 (연출 이미지 또는 실제 현장 사진 2~3장 권장)")
    if len(post.get("personal_prompts", [])) < 2:
        warn("담당자 한마디 질문(personal_prompts) 2개 이상")
    return out


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("post_json")
    p.add_argument("--blog", required=True, choices=blogs.ORDER)
    p.add_argument("--keyword", default="")
    p.add_argument("--prev-format")
    a = p.parse_args(argv)
    res = check(json.loads(Path(a.post_json).read_text(encoding="utf-8")), a.blog, a.keyword, a.prev_format)
    for level, msg in res:
        print(f"  {'✗' if level == 'FAIL' else '⚠'} {msg}")
    if not res:
        print("  ✓ 검수 통과")
    return 1 if any(l == "FAIL" for l, _ in res) else 0


if __name__ == "__main__":
    sys.exit(main())
