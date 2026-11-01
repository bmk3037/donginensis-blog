"""주제 후보의 수요·경쟁을 유튜브 쇼츠 검색으로 잰다(2026-11-01). 키는 YOUTUBE_API_KEY.
   사용: python3 topic_check.py "후보1 검색어|후보1 다른 검색어" "후보2 검색어" ...
   판단: 같은 각도 국내 쇼츠 최고 조회수(top) < 30만이고, 관련 주제 최대(demand)가 크면 '빈자리'.
   검색어 하나에 할당량 101단위(하루 1만) → 한 번에 후보 20개 안쪽."""
import json, os, sys, urllib.request, urllib.parse
K = os.environ["YOUTUBE_API_KEY"]
def get(path, **q):
    q["key"] = K
    return json.load(urllib.request.urlopen("https://www.googleapis.com/youtube/v3/" + path + "?" + urllib.parse.urlencode(q), timeout=30))
for cand in sys.argv[1:]:
    rows = []
    for qy in cand.split("|"):
        r = get("search", part="snippet", q=qy, type="video", videoDuration="short", regionCode="KR", relevanceLanguage="ko", order="viewCount", maxResults=8)
        ids = [i["id"]["videoId"] for i in r["items"]]
        if not ids: continue
        for v in get("videos", part="snippet,statistics", id=",".join(ids))["items"]:
            rows.append((int(v["statistics"].get("viewCount", 0)), v["snippet"]["publishedAt"][:10], v["snippet"]["channelTitle"][:10], v["snippet"]["title"][:46]))
    rows = sorted(set(rows), reverse=True)
    top = rows[0][0] if rows else 0
    print(f"\n## {cand}  (최고 {top:,})")
    for x in rows[:5]: print(f"  {x[0]:>10,} {x[1]} {x[2]:<10} {x[3]}")
