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


def char_count(body_md):
    """네이버 에디터 기준에 가깝게 본문 글자 수를 셉니다: (공백 포함, 공백 제외)"""
    text = PHOTO_RE.sub("", IMAGE_RE.sub("", body_md))
    text = re.sub(r"\]\(https?://[^)]*\)", "", text)  # 링크 주소
    text = re.sub(r"[#*\[\]>]", "", text).strip()
    return len(text), len(re.sub(r"\s", "", text))


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


# 사진 파일이 아직 없을 때: ChatGPT 등에서 만들 수 있게 프롬프트와 복사 버튼을 보여 줍니다
PROMPT_BOX = (
    '<div data-photo="{name}" style="border:2px dashed #e0a100;background:#fff8e1;color:#7a5a00;'
    'padding:18px;margin:0 0 18px;font-size:15px">'
    '<div style="font-weight:700;margin-bottom:6px">📷 사진 넣을 자리: {caption} <span style="font-weight:400">(파일 이름: {name})</span></div>'
    '<div style="font-size:13px;margin-bottom:6px">아래 프롬프트를 ChatGPT에 붙여넣어 사진을 만든 뒤 이 자리에 넣으세요. '
    '생성 사진 아래에는 "연출 이미지"라고 적어 주세요.</div>'
    '<pre class="prompt" style="white-space:pre-wrap;background:#fff;border:1px solid #f0d58a;padding:10px;margin:0 0 8px;'
    'font-size:13px;color:#333">{prompt}</pre>'
    '<button type="button" data-prompt style="background:#1857A5">프롬프트 복사</button></div>'
)


def photo_map(photos):
    return {p["file"]: p for p in (photos or [])}


def _photo_html(value, photos, have):
    photo = photos.get(value)
    if photo is None:  # 예전 형식: [사진: 설명]
        return PHOTO_BOX.format(html.escape(value))
    if value in have:
        return IMAGE_BOX.format(name=html.escape(value))
    return PROMPT_BOX.format(name=html.escape(value), caption=html.escape(photo.get("caption", "")),
                             prompt=html.escape(photo.get("prompt", "")))


def to_html(body_md, photos=None, have=()):
    """마크다운 본문 → 인라인 스타일 HTML.
    photos: [{"file", "caption", "prompt"}], have: images/ 폴더에 실제로 있는 파일 이름들"""
    photos, have = photo_map(photos), set(have)
    body_md = PHOTO_RE.sub(lambda m: "\n" + _photo_html(m.group(1), photos, have) + "\n", body_md)
    body_md = IMAGE_RE.sub(lambda m: "\n" + IMAGE_BOX.format(name=html.escape(m.group(1))) + "\n", body_md)
    out = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
    for tag, style in STYLES.items():
        out = re.sub(rf"<{tag}(?=[\s>])", f'<{tag} style="{style}"', out)
    return out


def to_issue_markdown(body_md, photos=None, have=()):
    """GitHub 이슈에서 읽기 좋게: 사진 자리를 눈에 띄는 인용문으로"""
    photos, have = photo_map(photos), set(have)

    def photo(m):
        value = m.group(1)
        if value not in photos:
            return f"> 📷 **사진 넣을 자리:** {value} (실제 사진이 없으면 생략)"
        if value in have:
            return f"> 🖼 **사진 넣기 (연출 이미지):** `images/{value}`"
        return (f"> 📷 **사진 넣을 자리:** {photos[value].get('caption', '')} — `{value}`\n"
                f">\n> ChatGPT 프롬프트:\n> ```\n> {photos[value].get('prompt', '')}\n> ```")

    body_md = IMAGE_RE.sub(lambda m: f"> 🖼 **이미지 넣기:** `images/{m.group(1)}`", body_md)
    return PHOTO_RE.sub(photo, body_md)


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
<div class="panel"><h2>② 본문 — [본문 복사] 후 스마트에디터에 붙여넣고, 파란 상자 자리에 images 폴더의 그림을 끌어다 놓으세요. 노란 상자가 있으면 [프롬프트 복사] → ChatGPT로 사진을 만들어 그 자리에 넣으세요</h2>
<button data-copy="post">본문 복사</button></div>
<div id="post">{body_html}</div>
{personal}<div class="panel" style="margin-top:16px"><h2>③ 태그</h2><div class="row"><div class="val" id="tags">{tags_esc}</div>
<button data-copy="tags">태그 복사</button></div></div>
<div class="panel"><h2>발행 전 확인</h2><ol class="check">{checklist}</ol></div>
</div>
<script>
const TAGS = {tags_json};
async function copy(id, btn) {{
  let el = document.getElementById(id);
  if (id === "post") {{
    el = el.cloneNode(true);
    el.querySelectorAll("[data-photo]").forEach(box => {{
      const p = document.createElement("p");
      p.setAttribute("style", "border:2px dashed #e0a100;background:#fff8e1;color:#7a5a00;padding:16px;text-align:center;font-size:15px");
      p.textContent = "📷 사진 넣기: " + box.dataset.photo;
      box.replaceWith(p);
    }});
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
document.querySelectorAll("button[data-prompt]").forEach(b => b.onclick = async () => {{
  const text = b.parentElement.querySelector("pre.prompt").innerText;
  try {{ await navigator.clipboard.writeText(text); }} catch (e) {{
    const t = document.createElement("textarea"); t.value = text; document.body.appendChild(t);
    t.select(); document.execCommand("copy"); t.remove();
  }}
  b.textContent = "복사됨 ✓"; b.classList.add("done");
}});
</script></body></html>
"""


def personal_panel(prompts):
    if not prompts:
        return ""
    items = "".join(f"<li>{html.escape(q)}</li>" for q in prompts)
    return ('<div class="panel" style="margin-top:16px;border-color:#1857A5"><h2>✍ 직접 한두 문장 덧붙이기 (권장)</h2>'
            '<p style="font-size:14px;margin:0 0 8px;color:#444">아래 질문 중 하나에 실제 경험으로 답해 본문 적당한 곳에 넣어 주세요. '
            '사람이 직접 쓴 문장이 들어가면 네이버에서 저품질 위험이 줄고 노출에 도움이 됩니다.</p>'
            f'<ol class="check">{items}</ol></div>')


def preview_page(title, tags, body_html, checklist, personal_prompts=()):
    return PREVIEW_TEMPLATE.format(
        personal=personal_panel(personal_prompts),
        title_esc=html.escape(title),
        tags_esc=html.escape(" ".join("#" + t for t in tags)),
        tags_json=json.dumps(tags, ensure_ascii=False),
        body_html=body_html,
        checklist="".join(f"<li>{html.escape(c)}</li>" for c in checklist),
    )
