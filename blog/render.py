"""초안(마크다운)을 네이버 스마트에디터에 붙여넣기 좋은 HTML로 바꿉니다.

스마트에디터는 붙여넣을 때 CSS 클래스를 버리므로 모든 서식을 style 속성으로 직접 넣습니다.
"""
import html
import json
import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

import markdown

SITE_HOST = "donginensis.com"
PHOTO_RE = re.compile(r"^\[사진:\s*(.+?)\][ \t]*$", re.MULTILINE)
IMAGE_RE = re.compile(r"^\[이미지:\s*(.+?)\][ \t]*$", re.MULTILINE)
SITE_URL_RE = re.compile(r"https?://(?:www\.)?donginensis\.com[^\s)\"'<>\]]*")

STYLES = {
    "h2": "word-break:keep-all;font-size:22px;font-weight:700;color:#111;margin:36px 0 14px;line-height:1.4",
    "h3": "word-break:keep-all;font-size:18px;font-weight:700;color:#111;margin:28px 0 10px;line-height:1.4",
    "p": "word-break:keep-all;font-size:16px;line-height:1.85;color:#333;margin:0 0 18px",
    "ul": "margin:0 0 18px;padding-left:22px",
    "ol": "margin:0 0 18px;padding-left:22px",
    "li": "word-break:keep-all;font-size:16px;line-height:1.85;color:#333;margin:0 0 6px",
    "strong": "font-weight:700;color:#111",
    "blockquote": "margin:0 0 18px;padding:12px 16px;border-left:4px solid #1857A5;background:#EAF1FA;color:#333",
    "table": "border-collapse:collapse;width:100%;margin:0 0 18px;font-size:15px",
    "th": "border:1px solid #c9d1dc;background:#eef2f7;padding:8px 10px;text-align:left",
    "td": "border:1px solid #c9d1dc;padding:8px 10px",
    "a": "color:#1857A5;text-decoration:underline",
}
PHOTO_BOX = (
    '<div style="border:2px dashed #e0a100;background:#fff8e1;color:#7a5a00;'
    'padding:20px;margin:0 0 18px;text-align:center;font-size:15px">'
    "📷 사진 넣을 자리: {}</div>"
)
# 미리보기에서는 그림을 보여 주고, [본문 복사] 때는 "이미지 넣기" 표시로 바뀝니다 (preview 스크립트)
IMAGE_BOX = (
    '<div data-img="{name}" style="margin:0 0 18px;text-align:center">'
    '<img src="images/{name}" alt="{name}" style="max-width:100%;border:1px solid #e3e8ef;border-radius:6px">'
    '<div style="font-size:13px;color:#7a5a00;margin-top:4px">⬆ 이 자리에 images/{name} 넣기</div></div>'
)


def add_utm(url, campaign):
    """홈페이지 링크에 유입 추적용 UTM을 붙입니다. #앵커는 뒤에 그대로 둡니다."""
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query.setdefault("utm_source", "naver_blog")
    query.setdefault("utm_medium", "blog")
    query.setdefault("utm_campaign", campaign)
    return urlunsplit(parts._replace(query=urlencode(query)))


def tag_site_links(text, campaign):
    return SITE_URL_RE.sub(lambda m: add_utm(m.group(0), campaign), text)


def to_html(body_md):
    """마크다운 본문 → 인라인 스타일 HTML"""
    body_md = PHOTO_RE.sub(lambda m: "\n" + PHOTO_BOX.format(html.escape(m.group(1))) + "\n", body_md)
    body_md = IMAGE_RE.sub(lambda m: "\n" + IMAGE_BOX.format(name=html.escape(m.group(1))) + "\n", body_md)
    out = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
    for tag, style in STYLES.items():
        out = re.sub(rf"<{tag}(?=[\s>])", f'<{tag} style="{style}"', out)
    return out


def to_issue_markdown(body_md):
    """GitHub 이슈에서 읽기 좋게: 사진 자리를 눈에 띄는 인용문으로"""
    body_md = IMAGE_RE.sub(lambda m: f"> 🖼 **이미지 넣기:** `images/{m.group(1)}`", body_md)
    return PHOTO_RE.sub(lambda m: f"> 📷 **사진 넣을 자리:** {m.group(1)} (실제 사진이 없으면 생략)", body_md)


PREVIEW_TEMPLATE = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_esc}</title>
<style>
body{{margin:0;word-break:keep-all;background:#f2f4f7;font-family:-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;color:#222}}
.wrap{{max-width:760px;margin:0 auto;padding:24px 16px 80px}}
.panel{{background:#fff;border:1px solid #dde2ea;border-radius:10px;padding:18px 20px;margin-bottom:16px}}
.panel h2{{font-size:15px;margin:0 0 10px;color:#555}}
.row{{display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap}}
.val{{flex:1;min-width:0;font-size:16px;word-break:break-all}}
button{{border:0;background:#03c75a;color:#fff;font-weight:700;padding:9px 14px;border-radius:6px;cursor:pointer;font-size:14px}}
button.done{{background:#555}}
ol.check{{margin:0;padding-left:20px;line-height:1.8;font-size:14px}}
#post{{background:#fff;border:1px solid #dde2ea;border-radius:10px;padding:28px 24px}}
</style></head><body><div class="wrap">
<div class="panel"><h2>① 제목</h2><div class="row"><div class="val" id="title">{title_esc}</div>
<button data-copy="title">제목 복사</button></div></div>
<div class="panel"><h2>② 본문 — [본문 복사] 후 스마트에디터에 붙여넣고, 파란 상자 자리에 images 폴더의 그림을 끌어다 놓으세요. 노란 상자는 실제 사진 자리(없으면 지우기)</h2>
<button data-copy="post">본문 복사</button></div>
<div id="post">{body_html}</div>
<div class="panel" style="margin-top:16px"><h2>③ 태그</h2><div class="row"><div class="val" id="tags">{tags_esc}</div>
<button data-copy="tags">태그 복사</button></div></div>
<div class="panel"><h2>발행 전 확인</h2><ol class="check">{checklist}</ol></div>
</div>
<script>
const TAGS = {tags_json};
async function copy(id, btn) {{
  let el = document.getElementById(id);
  if (id === "post") {{
    el = el.cloneNode(true);
    el.querySelectorAll("[data-img]").forEach(box => {{
      const p = document.createElement("p");
      p.setAttribute("style", "border:2px dashed #1857A5;background:#EAF1FA;color:#1857A5;padding:16px;text-align:center;font-size:15px");
      p.textContent = "🖼 이미지 넣기: " + box.dataset.img;
      box.replaceWith(p);
    }});
  }}
  const text = id === "tags" ? TAGS.map(t => "#" + t).join(" ") : el.innerText;
  try {{
    if (id === "post" && window.ClipboardItem) {{
      await navigator.clipboard.write([new ClipboardItem({{
        "text/html": new Blob([el.innerHTML], {{type: "text/html"}}),
        "text/plain": new Blob([text], {{type: "text/plain"}})
      }})]);
    }} else {{
      await navigator.clipboard.writeText(text);
    }}
  }} catch (e) {{
    const src = id === "post" ? document.getElementById("post") : el;
    const range = document.createRange(); range.selectNodeContents(src);
    const sel = getSelection(); sel.removeAllRanges(); sel.addRange(range);
    document.execCommand("copy"); sel.removeAllRanges();
  }}
  btn.textContent = "복사됨 ✓"; btn.classList.add("done");
}}
document.querySelectorAll("button[data-copy]").forEach(b => b.onclick = () => copy(b.dataset.copy, b));
</script></body></html>
"""


def preview_page(title, tags, body_html, checklist):
    return PREVIEW_TEMPLATE.format(
        title_esc=html.escape(title),
        tags_esc=html.escape(" ".join("#" + t for t in tags)),
        tags_json=json.dumps(tags, ensure_ascii=False),
        body_html=body_html,
        checklist="".join(f"<li>{html.escape(c)}</li>" for c in checklist),
    )
