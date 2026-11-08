"""64편(보일러 없는 집 — 마곡, 대본 v4·녹음 74.1초) 그림판: 63편 scene_2tan.html·sfx.py 복사 후 바꿈. python patch64.py (work/64에서)
컷 카드 = produce/64.md '컷 카드 v4'. 시그니처 '땅 한 겹 벗기기'는 reveal mode "peel"(같은 구도 2장: bg=땅 위, name=단면).
그림 없는 이름은 엔진이 '이미지 대기' 회색으로 그려서, 그림을 받기 전에도 타이밍을 볼 수 있다."""
import re, shutil, json
shutil.copy('../63/scene_2tan.html', 'scene_2tan.html'); shutil.copy('../63/sfx.py', 'sfx.py')
p = 'scene_2tan.html'; s = open(p, encoding='utf-8').read()
s = re.sub(r'<title>.*?</title>', '<title>64 보일러 없는 집 마곡 그림판</title>', s, count=1)
s = re.sub(r'const NAMES = \[.*?\];', 'const NAMES = ["g01","g01n","g02","g03","g04","g04b","g05","g06","g07","g08","g09","t01","t01cut","t01night"];', s, count=1)

# 땅 한 겹 벗기기: 단면(name) 위에 땅 위 그림(bg)을 깔고, 구덩이 모양(poly, 그림 비율 좌표)만 판처럼 옆으로 밀어낸다(시험 컷 peel.py와 같은 움직임)
a = s.index('    const shape = rv.mode === "down"')
s = s[:a] + '''    if (rv.mode === "peel") {
      const pts = rv.poly.map(([x, y]) => `${(x * w).toFixed(1)},${(y * h).toFixed(1)}`).join(" ");
      const dxp = 0.9 * w * p2, dyp = -0.025 * h * Math.sin(Math.PI * p2), ln = prog(t, rv.t0 - 0.6, rv.t0);
      const edge = ln > 0 && p2 < 0.25 ? `<polygon points="${pts}" fill="none" stroke="#fff" stroke-width="${w / 220}" stroke-dasharray="${(w * 3 * ln).toFixed(0)} ${w * 3}" opacity="${1 - p2 * 4}"/>` : "";
      const inner = `<image href="img/${name}.webp" width="${w}" height="${h}"/><mask id="${id}"><rect width="${w}" height="${h}" fill="#fff"/><polygon points="${pts}" fill="#000"/></mask>`
        + `<image href="img/${rv.bg}.webp" width="${w}" height="${h}" mask="url(#${id})"/><clipPath id="${id}c"><polygon points="${pts}"/></clipPath>`
        + (p2 < 1 ? `<g transform="translate(${dxp},${dyp})"><polygon points="${pts}" fill="rgba(0,0,0,${0.35 * Math.sin(Math.PI * p2)})" transform="translate(${w / 50},${h / 70})"/><image href="img/${rv.bg}.webp" width="${w}" height="${h}" clip-path="url(#${id}c)"/></g>` : "") + edge;
      return `<g transform="translate(${dx + shake[0]},${dy + shake[1]}) translate(${cx},${cy}) rotate(${rot}) scale(${s}) translate(${-cx},${-cy})">
    <g transform="translate(${ox},${oy}) scale(${K})">${inner}${overlay}</g></g>`;
    }
''' + s[a:]

a = s.index('function hook(t) {'); b = s.index('const SIGNS = [];')
hud = r'''function hook(t) {
  const big = 1 - prog(t, 2.3, 2.7);
  const w = (y, sz, parts) => `<text x="540" y="${y}" text-anchor="middle" ${FONT} font-size="${sz}" fill="#fff" stroke="rgba(0,0,0,0.75)" stroke-width="${sz / 7}" paint-order="stroke" stroke-linejoin="round" letter-spacing="-2">${parts}</text>`;
  return big > 0 ? `<g opacity="${big}">${w(330, 140, "보일러")}${w(490, 140, "없는 집")}</g>` : "";
}
const M = n => (a_(n) + b_(n)) / 2;
function globalHud(t) {
  let g = badge();
  g += hook(t);
  g += tag(t, a_(2) + 0.6, b_(2) - 0.1, "지역난방 378만 호 (2023)", 540, 700, 56);
  g += stamp(t, a_(4) + 1.8, b_(4) - 0.05, "9천 세대", 540, 720, 120, -5);
  g += stamp(t, a_(6) + 0.2, b_(6) - 0.1, "2012", 540, 720, 130, -6);
  g += stamp(t, a_(8) + 0.3, b_(8) - 0.05, "공고 ×6", 540, 720, 120, -5);
  g += tag(t, a_(9) + 0.4, b_(9) - 0.1, "2024 · 5년째 첫 삽도 못 떠", 540, 700, 56);
  g += stamp(t, a_(10) + 0.2, b_(10) - 0.05, "?", 540, 760, 200, 0);
  g += stamp(t, a_(12) + 0.2, b_(12) - 0.1, "2014 · 20년", 540, 720, 110, -5);
  g += stamp(t, a_(14) + 0.3, b_(14) - 0.1, "11.6", 540, 720, 130, -6);
  g += stamp(t, a_(15) + 0.2, b_(15) - 0.05, "?", 540, 760, 200, 0);
  g += stamp(t, a_(16) + 0.6, b_(16) - 0.1, "23:00", 540, 720, 130, -5);
  g += stamp(t, a_(17) + 0.3, b_(17) - 0.1, "2026.9", 540, 720, 120, -5);
  g += stamp(t, a_(18) + 0.1, M(18), "2012", 540, 680, 110, -6);
  g += stamp(t, M(18), b_(18) - 0.05, "2032", 540, 860, 110, 5);
  g += tag(t, a_(21) + 0.4, b_(21) - 0.1, "첫 신고·누수 확인 → 10만 원", 540, 700, 54);
  return g;
}
'''
s = s[:a] + hud + s[b:]

a = s.index('].forEach(x => SCENES.push(x));'); a0 = s.rindex('\n[\n', 0, a) + 1
PEEL = '[[0.2305, 0.7587], [0.7695, 0.7587], [0.9603, 1], [0.0508, 1]]'   # t01·t01cut 구덩이(11/8 시험 컷에서 잰 값)
sc = f'''const RV = (img, a, b, f, to, cx, cy, rv, cx2, cy2) => [img + "@" + Math.round(a * 100), a, b, {{ img, from: f, to, cx, cy, cx2, cy2, cuts: 1, lin: true, reveal: rv }}, null, null];
[
  P("g01", 0, a_(2), 1.0, 1.45, 540, 1100),
  P("g02", a_(2), a_(3), 1.05, 1.35, 540, 1000),
  RV("t01cut", a_(3), a_(4), 1.0, 1.55, 540, 1650, {{ mode: "peel", bg: "t01", t0: a_(3) + 0.7, dur: 0.9, poly: {PEEL} }}),
  RV("g01n", a_(4), a_(5), 1.35, 1.05, 540, 1000, {{ bg: "g01", t0: a_(4) + 1.6, dur: 1.2, x: 540, y: 1000 }}),
  P("g03", a_(5), a_(6), 1.4, 1.05, 540, 1000),
  P("g04b", a_(6), a_(7), 1.0, 1.3, 540, 1100),
  RV("g04", a_(7), a_(8), 1.3, 1.3, 300, 1100, {{ bg: "g04b", t0: a_(7) + 0.8, dur: 1.4, x: 760, y: 1100 }}, 780, 1100),
  P("g04", a_(8), a_(9), 1.35, 1.2, 760, 1150),
  P("g04", a_(9), a_(10), 1.45, 1.05, 760, 1150),
  P("g01n", a_(10), a_(11), 1.3, 1.3, 300, 1000, 0, 0, 780, 1000),
  P("g03", a_(11), a_(12), 1.35, 1.35, 300, 1100, 0, 0, 780, 1100),
  P("g05", a_(12), a_(13), 1.0, 1.3, 540, 1300),
  P("g06", a_(13), a_(14), 1.4, 1.4, 260, 1200, 0, 0, 820, 1200),
  P("g07", a_(14), a_(15), 1.0, 1.3, 540, 1100),
  P("t01night", a_(15), a_(16), 1.45, 1.5, 540, 1500),
  P("g08", a_(16), a_(17), 1.3, 1.05, 540, 1100),
  RV("g04b", a_(17), a_(18), 1.05, 1.25, 760, 1150, {{ bg: "g04", t0: a_(17) + 0.5, dur: 1.4, x: 760, y: 1150 }}),
  P("g04b", a_(18), a_(19), 1.25, 1.1, 760, 1100),
  RV("t01cut", a_(19), a_(20), 1.05, 1.5, 540, 1650, {{ mode: "peel", bg: "t01", t0: a_(19) + 0.3, dur: 0.6, poly: {PEEL} }}),
  P("g09", a_(20), a_(21), 1.3, 1.3, 540, 800, 0, 0, 540, 1300),
  P("g09", a_(21), a_(22), 1.4, 1.05, 540, 1100),
  P("t01night", a_(22), D, 1.5, 1.0, 540, 1500),
'''
s = s[:a0] + sc + s[a:]

def split(l):
    out, cur = [], ''
    for x in l.split(' '):
        if cur and len((cur + ' ' + x).strip()) > 12: out.append(cur); cur = x
        else: cur = (cur + ' ' + x).strip()
    out.append(cur); return ' / '.join(out)
L = [l for l in open('../../../produce/64_disp.txt', encoding='utf-8').read().splitlines() if l.strip()]
a = s.index('const SPLIT = ['); b = s.index('];', a)
s = s[:a] + 'const SPLIT = [\n' + ''.join(f'  {json.dumps(split(l), ensure_ascii=False)},\n' for l in L) + s[b:]
open(p, 'w', encoding='utf-8').write(s)

p = 'sfx.py'; t = open(p, encoding='utf-8').read()
a = t.index('# ---- 63편'); b = t.index('out = out / max')
cue = '''# ---- 64편 v4 큐: 효과음은 그래픽이 찍힐 때만, 땅 벗기기는 스윽 ----
A = lambda n: 0 if n == 1 else L[n - 1]['a']
B = lambda n: L[n - 1]['b']
Mi = lambda n: (A(n) + B(n)) / 2
for t0 in (A(4) + 1.8, A(6) + 0.2, A(8) + 0.3, A(10) + 0.2, A(12) + 0.2, A(14) + 0.3, A(15) + 0.2, A(16) + 0.6, A(17) + 0.3, A(18) + 0.1, Mi(18)): put(t0, thud(), 0.16)
for t0 in (A(2) + 0.6, A(9) + 0.4, A(21) + 0.4): put(t0, pop(), 0.08)
for t0 in (A(3) + 0.7, A(19) + 0.3): put(t0, whoosh(), 0.14) if 'whoosh' in globals() else put(t0, thud(), 0.12)
'''
t = t[:a] + cue + t[b:]
open(p, 'w', encoding='utf-8').write(t)
print('patched', len(L), 'lines')
