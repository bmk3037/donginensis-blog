"""이탄생 5편 vs 59편: 화면(밝기·채도·대비), 소리(크기·무음), 대본(말 빠르기·첫 문장·질문 위치)"""
import sys, os, re, json, subprocess, numpy as np, cv2
S = sys.argv[1]; OURS = sys.argv[2]; SRT = sys.argv[3]
IDS = ["2qDiJtzDua0", "5HdmlQ4LLUw", "Fv-Kat1ysDQ", "KMBdQdjqTyE", "id7aXpGvx8s"]

def vis(p):
    cap = cv2.VideoCapture(p); fps = cap.get(cv2.CAP_PROP_FPS); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); V = []; Sa = []; C = []
    for i in range(0, n, int(fps)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, f = cap.read()
        if not ok: break
        f = cv2.resize(f, (180, 320)); h = cv2.cvtColor(f, cv2.COLOR_BGR2HSV); g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        V.append(h[..., 2].mean()); Sa.append(h[..., 1].mean()); C.append(g.std())
    return np.mean(V), np.mean(Sa), np.mean(C)

def aud(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True, errors="ignore").stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); LRA = float(re.findall(r"LRA:\s+([\d.]+) LU", e)[-1])
    sd = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", f"silencedetect=noise={I-20}dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True, errors="ignore").stderr
    return I, LRA, len(re.findall("silence_end", sd))

def ts(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)

def vtt(p):  # 자동 자막: 줄마다 (시작, 끝, 글)
    out = []; txt = open(p, encoding="utf-8").read()
    for m in re.finditer(r"(\d\d:\d\d:\d\d\.\d+) --> (\d\d:\d\d:\d\d\.\d+)[^\n]*\n(.+?)(?:\n\n|\Z)", txt, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(3)).strip().split("\n")[-1].strip()
        if t and (not out or t != out[-1][2]): out.append((ts(m.group(1)), ts(m.group(2)), t))
    return out

def srt(p):
    out = []
    for b in open(p, encoding="utf-8").read().strip().split("\n\n"):
        l = b.split("\n"); a, c = l[1].split(" --> "); out.append((ts(a), ts(c), " ".join(l[2:])))
    return out

def script(rows, dur):
    text = " ".join(r[2] for r in rows); ch = len(re.sub(r"[^가-힣0-9A-Za-z]", "", text))
    speech = sum(r[1] - r[0] for r in rows)
    first = rows[0][2] if rows else ""
    q = [r[0] for r in rows if "?" in r[2] or re.search(r"(까요|나요|을까|ㄹ까|일까|왜)", r[2])]
    nums = len(re.findall(r"\d[\d,.]*", text))
    return ch, ch / dur, q[:3], nums, first[:40], text

res = {}
for i in IDS:
    p = f"{S}/train/{i}.mp4"; dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
    res[i] = (dur, vis(p), aud(p), script(vtt(f"{S}/subs/{i}.ko.vtt"), dur))
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", OURS], capture_output=True, text=True).stdout)
res["59편"] = (dur, vis(OURS), aud(OURS), script(srt(SRT), dur - 1))
print("영상        길이  밝기 채도 대비 | LUFS  LRA 무음(0.25s↑) | 글자 글자/초 숫자 | 질문 시각 | 첫 문장")
for k, (d, v, a, s) in res.items():
    print(f"{k:11s} {d:5.1f} {v[0]:4.0f} {v[1]:4.0f} {v[2]:4.0f} | {a[0]:5.1f} {a[1]:4.1f} {a[2]:3d} | {s[0]:4d} {s[1]:4.1f} {s[3]:3d} | {[round(x,1) for x in s[2]]} | {s[4]}")
json.dump({k: v[3][5] for k, v in res.items()}, open(f"{S}/scripts.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
