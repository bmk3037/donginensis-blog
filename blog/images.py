"""글 폴더의 images/*.html 조각을 PNG로 만듭니다.

각 조각 파일 첫 줄에 크기를 적습니다:  <!-- 1200x800 -->
조각은 assets/image.css의 클래스(.frame, .flow, .card ...)로 꾸밉니다.

사용법:
    python -m blog.images posts/2026-10-13-001
    (생성 사진 원본은 posts/<글>/photos-src/*.png 에 두면 '연출 이미지' 표기를 붙여 images/로 저장)
    python -m blog.images posts/2026-10-13-001 --cover "지능형 제어반이란?" --sub "설명" --kicker "제품 이야기" --tags 설비데이터 예지보전
"""
import argparse
import glob
import html
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

from blog import blogs

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SIZE_RE = re.compile(r"<!--\s*(\d+)x(\d+)\s*-->")
FOOTER = '<div class="footer"><span>DONG-IN ENSIS · {label}</span><span>donginensis.com</span></div>'
COVER_FOOTER = '<div class="footer"><span>donginensis.com</span><span>{label}</span></div>'
DEFAULT_LABEL = "지능형 제어반 · 산업설비 데이터"
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


def blog_of(post_dir):
    """폴더 이름(날짜-블로그-번호)에서 블로그 id를 찾습니다"""
    return next((b for b in blogs.ORDER if f"-{b}-" in Path(post_dir).name), None)


def label_of(post_dir):
    b = blog_of(post_dir)
    return blogs.get(b)["name"] if b else DEFAULT_LABEL


def wrap(fragment, label=DEFAULT_LABEL):
    """회사 로고(표지는 흰색, 나머지는 컬러)와 하단 표기를 자동으로 붙입니다."""
    m = FRAME_OPEN_RE.search(fragment)
    is_cover = bool(m and "cover" in m.group(2))
    dark = is_cover and "t-field" not in m.group(2)
    if m and 'class="logo"' not in fragment:
        logo = (ASSETS / "logo" / ("logo_white.png" if dark else "logo_color.png")).as_uri()
        fragment = fragment.replace(m.group(1), f'{m.group(1)}<img class="logo" src="{logo}" alt="(주)동인엔시스">', 1)
    if 'class="footer"' not in fragment:
        footer = (COVER_FOOTER if is_cover else FOOTER).format(label=html.escape(label))
        fragment = re.sub(r"</div>\s*$", footer + "</div>", fragment.strip(), count=1)
    return PAGE.format(fonts=(ASSETS / "fonts").as_uri(), css=(ASSETS / "image.css").as_uri(), body=fragment)


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path.name}: PNG 파일만 지원합니다")
    return struct.unpack(">II", head[16:24])


def label_photo(src, out, chrome):
    """생성 사진에 '연출 이미지' 표기와 회사 로고를 붙여 images/로 저장합니다."""
    w, h = png_size(src)
    body = (f'<div class="photo"><img class="src" src="{src.resolve().as_uri()}">'
            '<span class="badge">연출 이미지</span>'
            f'<img class="wm" src="{(ASSETS / "logo" / "logo_white.png").as_uri()}"></div>')
    page_html = PAGE.format(fonts=(ASSETS / "fonts").as_uri(), css=(ASSETS / "image.css").as_uri(), body=body)
    _screenshot(page_html, out, w, h, chrome)
    return out


def _screenshot(page_html, out, w, h, chrome):
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(page_html, encoding="utf-8")
        subprocess.run(
            [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--default-background-color=00000000", f"--window-size={w},{h}",
             "--virtual-time-budget=3000", f"--screenshot={out}", page.as_uri()],
            check=True, capture_output=True, timeout=120,
        )


def render_file(src, chrome, label=DEFAULT_LABEL):
    text = src.read_text(encoding="utf-8")
    m = SIZE_RE.search(text)
    if not m:
        raise ValueError(f"{src.name}: 첫 줄에 <!-- 1200x800 --> 같은 크기 표시가 없습니다")
    w, h = m.groups()
    out = src.with_suffix(".png")
    _screenshot(wrap(text, label), out, w, h, chrome)
    return out


def cover_fragment(title, sub="", kicker="", tags=(), theme="panel"):
    """정사각형 표지 (회사소개서 1쪽 서식). title 안의 *강조*에는 빨간 밑줄. theme: 블로그별 표지 색 (blogs.py)"""
    title_html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(title)).replace("\n", "<br>")
    tags_html = "".join(f"<span>#{html.escape(t)}</span>" for t in tags)
    return (
        "<!-- 1080x1080 -->\n"
        f'<div class="frame cover t-{theme}"><div class="content">'
        f'{f"<div class=eyebrow>{html.escape(kicker)}</div>" if kicker else ""}'
        f"<h1>{title_html}</h1>"
        f'{f"<p class=lead>{html.escape(sub)}</p>" if sub else ""}'
        f'<div class="tags">{tags_html}</div>'
        "</div></div>\n"
    )


def render_dir(post_dir):
    """images/*.html → PNG, photos-src/*.png(생성 사진 원본) → images/ 에 '연출 이미지' 표기 후 저장"""
    chrome = find_chrome()
    post_dir = Path(post_dir)
    outs = []
    for src in sorted((post_dir / "images").glob("*.html")):
        outs.append(render_file(src, chrome, label_of(post_dir)))
    for src in sorted((post_dir / "photos-src").glob("*.png")):
        outs.append(label_photo(src, post_dir / "images" / src.name, chrome))
    for out in outs:
        print(f"  ✓ {out}")
    return outs


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("post_dir")
    p.add_argument("--cover", help="표지 제목 (줄바꿈은 \\n, 강조는 *단어*)")
    p.add_argument("--sub", default="")
    p.add_argument("--kicker", default="")
    p.add_argument("--tags", nargs="*", default=[])
    p.add_argument("--blog", choices=blogs.ORDER, help="표지 색을 이 블로그 서식으로 (폴더 이름에서 자동으로 찾음)")
    args = p.parse_args(argv)
    img_dir = Path(args.post_dir) / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    blog_id = args.blog or blog_of(args.post_dir)
    theme = blogs.get(blog_id)["theme"] if blog_id else "panel"
    if args.cover:
        (img_dir / "01-cover.html").write_text(
            cover_fragment(args.cover.replace("\\n", "\n"), args.sub, args.kicker, args.tags, theme), encoding="utf-8")
    render_dir(args.post_dir)


if __name__ == "__main__":
    main()
