"""타입캐스트 음성 한 파일을 문장별로 나눠 timeline.js를 만든다.
   python3 align.py narration.mp3 lines.json   (음성 없이 글자 수로 어림: python3 align.py - lines.json)"""
import json, re, subprocess, sys
audio, lines_path = sys.argv[1], sys.argv[2]
lines = json.load(open(lines_path))
n = len(lines)
# 숫자를 아라비아 숫자로 쓴 자막과 읽는 말의 길이가 다르면 "say"(타입캐스트 대본 문장)를 함께 적는다
spoken = [len(re.sub(r"[\s,.]", "", l.get("say", l["text"]))) + 2 * l["text"].count("%") for l in lines]

def commas(text, start, end, sil):
    # 쉼표 위치를 글자 비율로 어림하고, 가까운 문장 안 쉼이 있으면 그쪽에 붙인다
    out, pos = [], 0
    for part in text.split(",")[:-1]:
        pos += len(part.replace(" ", ""))
        guess = start + (end - start) * pos / max(1, len(text.replace(" ", "").replace(",", "")))
        near = [(abs((a + b) / 2 - guess), (a + b) / 2) for a, b in sil if start < a and b < end]
        out.append(min(near)[1] if near and min(near)[0] < 0.8 else guess)
    return out

if audio == "-":
    rate, gap, t, segs = 6.2, 0.42, 0.35, []
    for l, c in zip(lines, spoken):
        segs.append((t, t + c / rate)); t += c / rate + gap
    dur, sil = t + 0.8, []
else:
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio]))
    log = subprocess.run(["ffmpeg", "-i", audio, "-af", "silencedetect=noise=-38dB:d=0.16", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    sil = list(zip(st, en + [dur] * (len(st) - len(en))))
    s0 = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
    s1 = sil[-1][0] if sil and sil[-1][1] > dur - 0.05 else dur
    inner = [(a, b) for a, b in sil if s0 < a and b < s1]
    # 문장 경계 n-1개를 쉼 가운데서 고른다: 글자 수 비율로 어림한 시각에 가깝고, 긴 쉼일수록 좋다
    cum = [sum(spoken[:i + 1]) / sum(spoken) for i in range(n - 1)]
    exp = [s0 + (s1 - s0) * c for c in cum]
    m, INF = len(inner), float("inf")
    cost = [[INF] * m for _ in range(n - 1)]; back = [[-1] * m for _ in range(n - 1)]
    def c_(k, j):
        a, b = inner[j]; return ((a + b) / 2 - exp[k]) ** 2 - 6.0 * (b - a)
    for j in range(m): cost[0][j] = c_(0, j)
    for k in range(1, n - 1):
        best, bj = INF, -1
        for j in range(m):
            if j > 0 and cost[k - 1][j - 1] < best: best, bj = cost[k - 1][j - 1], j - 1
            if best < INF: cost[k][j], back[k][j] = best + c_(k, j), bj
    j = min(range(m), key=lambda j: cost[n - 2][j]); picks = []
    for k in range(n - 2, -1, -1): picks.append(j); j = back[k][j]
    picks = picks[::-1]
    # 말 속도가 튀는 곳은 들어 보고 경계를 직접 고정한다: {경계 앞 문장 번호: 쉼 시작 시각}
    force = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    for k, s in force.items():
        picks[int(k)] = min(range(m), key=lambda j: abs(inner[j][0] - s))
    assert picks == sorted(picks), picks
    bounds = [inner[j] for j in picks]
    segs = [(s0 if i == 0 else bounds[i - 1][1], s1 if i == n - 1 else bounds[i][0]) for i in range(n)]
out = []
for i, (l, (a, b)) in enumerate(zip(lines, segs)):
    A = 0.0 if i == 0 else (segs[i - 1][1] + a) / 2
    B = dur if i == n - 1 else (b + segs[i + 1][0]) / 2
    out.append({"beat": l["beat"], "text": l["text"], "start": round(a, 3), "end": round(b, 3),
                "commas": [round(x, 3) for x in commas(l["text"], a, b, sil)], "a": round(A, 3), "b": round(B, 3)})
tl = {"duration": round(dur, 2), "lines": out}
open("timeline.js", "w").write("window.TL = " + json.dumps(tl, ensure_ascii=False) + ";\n")
print(tl["duration"], [(round(o["start"], 1), o["text"][:12]) for o in out])
