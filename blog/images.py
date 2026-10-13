"""글 폴더의 images/*.html 조각을 PNG로 만듭니다.

각 조각 파일 첫 줄에 크기를 적습니다:  <!-- 1200x800 -->
조각은 assets/image.css의 클래스(.frame, .flow, .card ...)로 꾸밉니다.

사용법:
    python -m blog.images posts/2026-10-13-001
    python -m blog.images posts/2026-10-13-001 --cover "지능형 제어반이란?" --sub "설명" --kicker "제품 이야기" --tags 설비데이터 예지보전
"""
import argparse
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SIZE_RE = re.compile(r"<!--\s*(\d+)x(\d+)\s*-->")
FOOTER = '<div class="footer"><span>DONG-IN ENSIS · 지능형 제어반 블로그</span><span>donginensis.com</span></div>'
COVER_FOOTER = '<div class="footer"><span>donginensis.com</span><span>지능형 제어반 · 산업설비 데이터</span></div>'
FRAME_OPEN_RE = re.compile(r'(<div class="frame([^"]*)">)')

PAGE = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<style>
@font-face {{ font-family: "Pretendard"; font-weight: 400; src: url("{fonts}/Pretendard-Regular.woff2"); }}
@font-face {{ font-family: "Pretendard"; font-weight: 700; src: url("{fonts}/Pretendard-Bold.woff2"); }}
@font-face {{ font-family: "Pretendard"; font-weight: 800; src: url("{fonts}/Pretendard-ExtraBold.woff2"); }}
</style>
<link rel="stylesheet" href="{css}">
</head><body>{body}</body></html>"""


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for pattern in ("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell",
                    "/opt/pw-browsers/chromium-*/chrome-linux/chrome"):
        hits = sorted(glob.glob(pattern))
        if hits:
            return hits[-1]
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    sys.exit("크롬(Chromium)을 찾지 못했습니다. CHROME 환경변수로 경로를 알려 주세요.")


def wrap(fragment):
    """회사 로고(표지는 흰색, 나머지는 컬러)와 하단 표기를 자동으로 붙입니다."""
    m = FRAME_OPEN_RE.search(fragment)
    is_cover = bool(m and "cover" in m.group(2))
    if m and 'class="logo"' not in fragment:
        logo = (ASSETS / "logo" / ("logo_white.png" if is_cover else "logo_color.png")).as_uri()
        fragment = fragment.replace(m.group(1), f'{m.group(1)}<img class="logo" src="{logo}" alt="(주)동인엔시스">', 1)
    if 'class="footer"' not in fragment:
        footer = COVER_FOOTER if is_cover else FOOTER
        fragment = re.sub(r"</div>\s*$", footer + "</div>", fragment.strip(), count=1)
    return PAGE.format(fonts=(ASSETS / "fonts").as_uri(), css=(ASSETS / "image.css").as_uri(), body=fragment)


def render_file(src, chrome):
    text = src.read_text(encoding="utf-8")
    m = SIZE_RE.search(text)
    if not m:
        raise ValueError(f"{src.name}: 첫 줄에 <!-- 1200x800 --> 같은 크기 표시가 없습니다")
    w, h = m.groups()
    out = src.with_suffix(".png")
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(wrap(text), encoding="utf-8")
        subprocess.run(
            [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", f"--window-size={w},{h}",
             "--virtual-time-budget=3000", f"--screenshot={out}", page.as_uri()],
            check=True, capture_output=True, timeout=120,
        )
    return out


def cover_fragment(title, sub="", kicker="", tags=()):
    """정사각형 표지 (회사소개서 1쪽 서식). title 안의 *강조*에는 빨간 밑줄."""
    title_html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(title)).replace("\n", "<br>")
    tags_html = "".join(f"<span>#{html.escape(t)}</span>" for t in tags)
    return (
        "<!-- 1080x1080 -->\n"
        '<div class="frame cover"><div class="content">'
        f'{f"<div class=eyebrow>{html.escape(kicker)}</div>" if kicker else ""}'
        f"<h1>{title_html}</h1>"
        f'{f"<p class=lead>{html.escape(sub)}</p>" if sub else ""}'
        f'<div class="tags">{tags_html}</div>'
        "</div></div>\n"
    )


def render_dir(post_dir):
    chrome = find_chrome()
    outs = []
    for src in sorted((Path(post_dir) / "images").glob("*.html")):
        outs.append(render_file(src, chrome))
        print(f"  ✓ {outs[-1].relative_to(ROOT) if outs[-1].is_relative_to(ROOT) else outs[-1]}")
    return outs


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("post_dir")
    p.add_argument("--cover", help="표지 제목 (줄바꿈은 \\n, 강조는 *단어*)")
    p.add_argument("--sub", default="")
    p.add_argument("--kicker", default="")
    p.add_argument("--tags", nargs="*", default=[])
    args = p.parse_args(argv)
    img_dir = Path(args.post_dir) / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    if args.cover:
        (img_dir / "01-cover.html").write_text(
            cover_fragment(args.cover.replace("\\n", "\n"), args.sub, args.kicker, args.tags), encoding="utf-8")
    render_dir(args.post_dir)


if __name__ == "__main__":
    main()
