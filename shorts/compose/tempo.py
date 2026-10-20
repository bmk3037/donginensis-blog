"""원래 속도 음성으로 만든 timeline_raw.js를 배속에 맞춰 timeline.js로 바꾼다.
   python3 tempo.py timeline_raw.js 1.12"""
import json, sys
src, R = sys.argv[1], float(sys.argv[2])
tl = json.loads(open(src).read().split("=", 1)[1].strip().rstrip(";"))
m = lambda x: round(x / R, 3)
L = tl["lines"]
for l in L:
    l["start"], l["end"] = m(l["start"]), m(l["end"])
    l["commas"] = [m(c) for c in l["commas"]]
dur = round(m(tl["duration"]), 2)
for i, l in enumerate(L):
    l["a"] = 0.0 if i == 0 else round((L[i - 1]["end"] + l["start"]) / 2, 3)
    l["b"] = dur if i == len(L) - 1 else round((l["end"] + L[i + 1]["start"]) / 2, 3)
open("timeline.js", "w").write("window.TL = " + json.dumps({"duration": dur, "lines": L}, ensure_ascii=False) + ";\n")
print(dur)
