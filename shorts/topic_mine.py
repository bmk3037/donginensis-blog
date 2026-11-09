"""주제 자동 채굴: 잘 터지는 같은 분야 채널의 최근 인기 영상 → 우리와 겹침 점검 → 후보 순위.
사용: (PowerShell) $env:YOUTUBE_API_KEY=[Environment]::GetEnvironmentVariable('YOUTUBE_API_KEY','User'); python shorts/topic_mine.py
결과: shorts/data/topic_candidates.json, shorts/TOPIC-CANDIDATES-AUTO.md
키는 환경 변수에서만 읽는다. 검색(search)은 100유닛이라 하루 한도에 주의, 채널 업로드 목록은 1유닛이라 가볍다."""
import os, re, json, sys, glob, datetime, urllib.request, urllib.parse, collections
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.environ['YOUTUBE_API_KEY']; API = 'https://www.googleapis.com/youtube/v3'
DAYS = 150; MIN_VIEWS = 150000
def get(path, **p):
    p['key'] = K
    return json.load(urllib.request.urlopen(API + path + '?' + urllib.parse.urlencode(p), timeout=40))
# 1) 채널 목록: 고정 목록 + (선택) 키워드 검색으로 찾은 신생 채널
SEED = ['신비한 건축사전', '건축해부도', '놀라운기술도감', '도시해부도', '세상을 바꾼 건축', '설계의 비밀', '월급루팡', '1분공구리', '돈의 구조물', '여기 놀랍게도', '건축비밀노트']
QUERIES = ['땅속 숨은 설비 쇼츠', '도시 인프라 해부 쇼츠', '이 건물이 안 무너지는 이유', '건축 해부도', '도로 아래 숨겨진 것', '서울 땅 밑에는', '지하철 역 숨은 구조']
after = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAYS)).strftime('%Y-%m-%dT00:00:00Z')
CH = os.path.join(HERE, 'data', 'channels.json'); os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
chan = json.load(open(CH, encoding='utf-8')) if os.path.exists(CH) else {}
def discover():
    for name in SEED:
        try:
            r = get('/search', part='snippet', q=name, type='channel', regionCode='KR', maxResults=1)
            it = r['items'][0]; chan[it['snippet']['channelId']] = it['snippet']['channelTitle']
        except Exception as e: print('검색 한도/오류(채널 목록은 저장본 사용):', str(e)[:50]); return
    for q in QUERIES:
        try:
            r = get('/search', part='snippet', q=q, type='video', videoDuration='short', regionCode='KR', relevanceLanguage='ko', order='viewCount', publishedAfter=after, maxResults=25)
            for it in r['items']: chan.setdefault(it['snippet']['channelId'], it['snippet']['channelTitle'])
        except Exception as e: print('검색 한도/오류:', q, str(e)[:50]); return
if os.environ.get('DISCOVER') == '1' or not chan: discover()
json.dump(chan, open(CH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('채널', len(chan))
# 2) 채널별 최근 업로드 → 조회수
vids = []
for cid, name in chan.items():
    pl = 'UU' + cid[2:]; ids = []
    try:
        tok = None
        for _ in range(3):
            p = dict(part='contentDetails', playlistId=pl, maxResults=50)
            if tok: p['pageToken'] = tok
            r = get('/playlistItems', **p)
            ids += [i['contentDetails']['videoId'] for i in r['items']]; tok = r.get('nextPageToken')
            if not tok: break
    except Exception as e: continue
    for i in range(0, len(ids), 50):
        r = get('/videos', part='statistics,snippet,contentDetails', id=','.join(ids[i:i+50]))
        for it in r['items']:
            d = it['snippet']['publishedAt'][:10]
            if d < after[:10]: continue
            v = int(it['statistics'].get('viewCount', 0))
            if v >= MIN_VIEWS: vids.append(dict(views=v, title=it['snippet']['title'], channel=name, date=d, id=it['id']))
vids.sort(key=lambda x: -x['views']); print('인기 영상', len(vids))
# 3) 우리 이미 만든 것 + 주제 은행과 겹침
def toks(s): return {w for w in re.findall(r'[가-힣A-Za-z0-9]{2,}', s) if w not in ('이유', '비밀', '어떻게', '대체', '무엇', '쇼츠')}
ours = []
for f in glob.glob(os.path.join(HERE, 'upload', '[0-9]*.md')): ours.append(open(f, encoding='utf-8').readline())
bank = open(os.path.join(HERE, 'TOPIC-BANK-2026-11.md'), encoding='utf-8').read() if os.path.exists(os.path.join(HERE, 'TOPIC-BANK-2026-11.md')) else ''
ourtoks = [toks(t) for t in ours]
SEASON = re.compile(r'눈|제설|결빙|한파|난방|보일러|단풍|수능|겨울|첫눈|난로|빙판|스케이트')
FACIL = re.compile(r'설비|배관|펌프|터널|환풍|지하|발전|수조|밸브|엘리베이터|에스컬레이터|보일러|하수|빗물|배수|필터|냉동|저수|댐|케이블|변전|변압')
NOISE = re.compile(r'눈동자|눈으로|척추|뉴스|MBC|SBS|KBS|JTBC|연설|폭탄|탈출')
out = []
for v in vids:
    if NOISE.search(v['title']) or NOISE.search(v['channel']): continue
    t = toks(v['title']); ov = max([len(t & o) / max(1, len(t)) for o in ourtoks] + [0])
    s_demand = 5 if v['views'] >= 1000000 else 4 if v['views'] >= 500000 else 3 if v['views'] >= 300000 else 2
    s_season = 5 if SEASON.search(v['title']) else 2
    s_facil = 5 if FACIL.search(v['title']) else 3
    s_overlap = 1 if ov >= 0.5 else 3 if ov >= 0.25 else 5
    v.update(score=round((s_demand + s_season + s_facil + s_overlap) / 4, 2), parts=dict(수요=s_demand, 시즌=s_season, 설비=s_facil, 겹침없음=s_overlap), overlap=round(ov, 2))
    out.append(v)
out.sort(key=lambda x: (-x['score'], -x['views']))
os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
json.dump(out, open(os.path.join(HERE, 'data', 'topic_candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
L = ['# 자동 주제 후보 (topic_mine.py, %s, 근거: 최근 %d일 %d만+ 조회 영상)' % (datetime.date.today(), DAYS, MIN_VIEWS // 10000),
     '남의 영상 주제를 베끼는 게 아니라 **수요 증거**이고, 만들 때는 우리 각도·겹침 점검을 다시 한다. 점수 = (수요+시즌+설비+겹침없음)/4 자동 추정(사람 판단 전).', '',
     '| 점수 | 조회수 | 채널 | 날짜 | 제목 | 수요/시즌/설비/겹침없음 |', '|---|---|---|---|---|---|']
for v in out[:40]:
    p = v['parts']; L.append('| %.2f | %d | %s | %s | %s | %d/%d/%d/%d |' % (v['score'], v['views'], v['channel'], v['date'], v['title'][:70].replace('|', '/'), p['수요'], p['시즌'], p['설비'], p['겹침없음']))
open(os.path.join(HERE, 'TOPIC-CANDIDATES-AUTO.md'), 'w', encoding='utf-8').write('\n'.join(L))
for v in out[:15]: print('%.2f %8d %s | %s' % (v['score'], v['views'], v['channel'][:10], v['title'][:50]))
