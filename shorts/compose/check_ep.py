"""편 점검표(11/7 대표이사 "왜 자꾸 까먹어"): 규칙을 기억에 맡기지 않고 기계로 확인한다.
사용: python check_ep.py NN [plan|render|upload]   (shorts/compose 에서)
  plan   : 녹음 전 — 대본 길이·"처음부터 보죠" 위치·숫자 개수·Codex 검수 기록
  render : 렌더 전 — 그림 20장 이상·같은 그림 2번 이하·클립 8개 이상·참고 사진 모양만·낮 맑은 하늘 문장·빨간 고리 금지
  upload : 업로드 전 — 배경음악 없음(문장 사이 소리)·음량 -14 LUFS 근처·커버·자막·업로드 카드 승인
FAIL이 하나라도 있으면 다음 단계로 가지 않는다(종료 코드 1)."""
import sys, os, re, json, subprocess
NN = sys.argv[1]; STAGE = sys.argv[2] if len(sys.argv) > 2 else 'all'
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
P = lambda *a: os.path.join(R, 'shorts', *a)
res = []
def chk(ok, name, detail=''): res.append((ok, name, detail))

def plan():
    disp = P('produce', f'{NN}_disp.txt')
    if not os.path.exists(disp): return chk(False, '대본 파일', disp)
    L = [l for l in open(disp, encoding='utf-8').read().splitlines() if l.strip()]
    # 11/8 대표이사 "100만 이상 터진 릴스 공통점을 대본에 적용시키려면 통과 기준이 있을 거 아냐" → 실측 기준을 기계로(MASTER §3, 스킬 §C 표)
    chars = [len(l.replace(' ', '')) for l in L]
    est = sum(chars) / 6.3
    at = [sum(chars[:i]) / 6.3 for i in range(len(L))]             # 문장 시작 초
    dur = [c / 6.3 for c in chars]; how = '예상'
    tl = P('compose', 'work', NN, 'timeline.js')                     # 11/8 64편: 예상 74초 → 실제 78.8초. 녹음 뒤엔 실제 시각으로
    if os.path.exists(tl):
        s = open(tl, encoding='utf-8').read(); d = json.loads(s[s.index('{'):s.rindex('}') + 1])
        if len(d['lines']) == len(L):
            at = [l['start'] for l in d['lines']]; dur = [l['end'] - l['start'] for l in d['lines']]; est = d['duration']; how = '녹음'
    chk(35 <= est <= 75, f'{how} 길이 {est:.1f}초', '채널 개선안: 생활 설비 35~50초, 큰 시설 60~75초')
    chk(not re.match(r'\s*(\d|지난|어제|오늘|그제)', L[0]), '첫 문장이 날짜·시각으로 시작 안 함', 'RULES-OPENING 4')
    q = next((i for i, l in enumerate(L) if '?' in l), None)
    chk(q is not None and at[q] <= 8, f'첫 질문 {at[q]:.1f}초' if q is not None else '첫 질문 없음', '8초 안(100만+ 4.6~7.7초)')
    k = next((i for i, l in enumerate(L) if '처음부터' in l), None)
    start = at[k] if k is not None else 99
    chk(start <= 14, f'"처음부터 보죠" 약 {start:.1f}초', '14초 안(100만+ 7.7~14.5초)')
    ans = k is not None and any(re.search(r'아니에요|아니라|거든요', l) for l in L[:k])
    chk(ans, '"처음부터" 앞에 답 한 줄', '"~가 아니에요/아니라 … ~거든요"')
    body = '\n'.join(L[k + 1:]) if k is not None else ''
    yrs = sorted(set(re.findall(r'(?:19|20)\d\d', body)))
    chk(len(yrs) >= 4, f'본문 연도 {len(yrs)}개 {yrs}', '연도순 사연: 4개 이상(100만+는 원리보다 누가 언제 왜)')
    tw = [i for i in range(k + 1, len(L)) if '?' in L[i]] if k is not None else []
    mid = [i for i in tw if 0.40 <= at[i] / est <= 0.60 or (i + 1 < len(L) and 0.40 <= at[i + 1] / est <= 0.60)]
    chk(bool(mid), '두 번째 반전 질문 40~60%', f'본문 질문 위치: {[round(100 * at[i] / est) for i in tw]}%')
    t = '\n'.join(L)
    nums = len(re.findall(r'\d[\d,.]*', t)) + len(re.findall(r'닷새|사흘|열흘|세 곳|두 곳', t))
    chk(12 <= nums <= 20, f'숫자 {nums}개', '줄기에 붙는 것만 12~20개(늘어놓기 금지)')
    long = [i + 1 for i, c in enumerate(dur) if c > 5]
    chk(not long, '한 문장 5초 이하(한 호흡)', f'긴 문장: {long}' if long else '')
    cm = [i + 1 for i, l in enumerate(L) if len(re.findall(r'(?<!\d),|,(?!\d)', l)) > 1]
    chk(not cm, '쉼표 문장당 1개 이하', f'{cm}' if cm else 'Typecast가 쉼표마다 쉼')
    ad = [i + 1 for i, l in enumerate(L) if re.search(r'구독|좋아요 눌|공유해|알림 설정', l)]
    chk(not ad, '나레이션에 구독·공유 유도 없음', f'{ad}' if ad else '')
    card = P('produce', f'{NN}.md')
    ct = open(card, encoding='utf-8').read() if os.path.exists(card) else ''
    chk('Codex' in ct, 'Codex 검수 기록', f'{NN}.md에 Codex 검수 결과')
    # 11/7 "저장하고 공유할 수 있게": 줄기 하나 + 저장·공유 줄을 대본 전에 정한다
    for key in ('줄기 질문:', '저장 줄:', '공유 줄:'):
        chk(key in ct, f'카드에 "{key}"', 'SKILL C — 대본 쓰기 전에 적고 대표이사 확인')
    chk('화면' in ct and '카메라' in ct, '대본 표에 화면·카메라 칸', '문장마다 무엇이 보이나·카메라')

def render():
    img = P('media', NN, 'in', 'img')
    imgs = [f for f in os.listdir(img) if f.endswith('.jpg')] if os.path.isdir(img) else []
    chk(len(imgs) >= 20, f'그림 {len(imgs)}장', '20장 이상')
    clips = [f for f in os.listdir(P('media', NN, 'in', 'clip')) if f.endswith('.mp4')] if os.path.isdir(P('media', NN, 'in', 'clip')) else []
    scene = P('compose', 'work', NN, 'scene_2tan.html')
    if os.path.exists(scene):
        s = open(scene, encoding='utf-8').read()
        Ps = re.findall(r'^\s+P\("(\w+)"', s, re.M); Qs = re.findall(r'^\s+Q\("(\w+)"', s, re.M)
        rep = {n: Ps.count(n) for n in set(Ps) if Ps.count(n) > 2}
        chk(not rep, '같은 그림 2번 이하', str(rep) if rep else '')
        chk(len(Qs) >= 8, f'클립 컷 {len(Qs)}개(파일 {len(clips)}개)', '8컷 이상(큰 움직임 27~42% 목표)')
    import glob
    files = [f for f in glob.glob(P('produce', f'{NN}_*.txt')) if re.search(r'_(prompts|more|redo)', f)]
    newest = max(files, key=os.path.getmtime) if files else None
    if newest:
        t = open(newest, encoding='utf-8').read()
        chk('haze-free' in t, f'낮 맑은 하늘 문장({os.path.basename(newest)})', 'Style에 haze-free')
        chk('reference photos' not in t or 'in shape only' in t, '참고 사진은 모양만', '"in shape only"')
        chk('never rings or circles' in t, '빨간 고리·동그라미 금지 문장')

def upload():
    out = P('media', NN, 'out')
    vids = sorted([f for f in os.listdir(out) if f.endswith('.mp4')], key=lambda f: os.path.getmtime(os.path.join(out, f))) if os.path.isdir(out) else []
    if not vids: return chk(False, '완성 영상', out)
    v = os.path.join(out, vids[-1])
    # 배경음악: 나레이션 문장 사이 빈틈에서 소리 크기를 잰다. 음악이 깔리면 -35dB 근처, 없으면 -45dB 아래
    nar = P('compose', 'work', NN, 'narration.wav'); gaps = []
    if os.path.exists(nar):   # 나레이션이 조용한 구간(문장 사이)을 찾아, 완성 영상의 같은 구간 소리를 잰다
        e = subprocess.run(['ffmpeg', '-v', 'info', '-i', nar, '-af', 'silencedetect=n=-45dB:d=0.12', '-f', 'null', '-'], capture_output=True, text=True, errors='ignore').stderr
        st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', e)]; en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', e)]
        gaps = [(a0 + 0.02, b0 - 0.02) for a0, b0 in zip(st, en) if b0 - a0 > 0.1]
    vals = []
    for g0, g1 in gaps:
        e = subprocess.run(['ffmpeg', '-v', 'info', '-ss', f'{g0:.2f}', '-t', f'{g1 - g0:.2f}', '-i', v, '-af', 'volumedetect', '-vn', '-f', 'null', '-'], capture_output=True, text=True, errors='ignore').stderr
        m = re.search(r'mean_volume: (-?[\d.]+) dB', e)
        if m: vals.append(float(m.group(1)))
    vals.sort(); db = vals[len(vals) // 2] if vals else 0
    chk(db < -40, f'배경음악 없음(문장 사이 가운데값 {db:.1f}dB)', '-40dB보다 조용')
    e = subprocess.run(['ffmpeg', '-v', 'info', '-i', v, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True, errors='ignore').stderr
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', e); lufs = float(m[-1]) if m else 0
    chk(-16 <= lufs <= -13, f'음량 {lufs} LUFS', '-14 근처')
    chk(os.path.exists(os.path.join(out, f'{NN}_cover.jpg')), '커버 이미지')
    chk(os.path.exists(P('upload', f'{NN}_ko.srt')), '한국어 자막')
    card = P('upload', f'{NN}.md')
    chk(os.path.exists(card) and re.search(r'승인 \| \*\*예\*\*', open(card, encoding='utf-8').read()), '업로드 카드 승인 예')
    chk(os.path.exists(card) and vids[-1] in open(card, encoding='utf-8').read(), f'카드에 최신 영상 이름({vids[-1]})')

for st, f in (('plan', plan), ('render', render), ('upload', upload)):
    if STAGE in (st, 'all'): f()
bad = 0
for ok, name, d in res:
    print(('PASS ' if ok else 'FAIL ') + name + (f'  — {d}' if d and not ok else ''))
    bad += not ok
print(f'\n{len(res) - bad}/{len(res)} 통과' + ('' if not bad else '  → FAIL을 고친 뒤 다음 단계로'))
sys.exit(1 if bad else 0)
