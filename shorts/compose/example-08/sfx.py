"""효과음을 숫자로 직접 만들어 한 트랙으로 섞는다(외부 음원 없음). 작업 폴더에서 python3 sfx.py → sfx.wav
   소리 함수(whoosh 휙, pop 톡, thud 쿵, boom 큰 쿵, shimmer 반짝, rumble 바람, clicks 째깍, riser 긴장)는 그대로 두고,
   맨 아래 "편마다 고칠 곳"의 시각만 새 편의 장면에 맞게 바꾼다. S(i)=i번 문장 시작, C(i,k)=쉼표, At(i,f)=문장 안 비율."""
import json, numpy as np, wave
SR = 44100
tl = json.loads(open('timeline.js').read().split('=', 1)[1].strip().rstrip(';'))
L, dur = tl['lines'], tl['duration']
rng = np.random.default_rng(7)
out = np.zeros(int((dur + 1) * SR))
def env(n, a, d):
    e = np.ones(n); ai = int(a * SR); di = int(d * SR)
    e[:ai] = np.linspace(0, 1, ai) if ai else 1
    e[-di:] *= np.linspace(1, 0, di) ** 2
    return e
def lowpass(x, k):
    c = np.cumsum(np.insert(x, 0, 0)); return (c[k:] - c[:-k]) / k
def put(t, x, g):
    i = int(t * SR); j = min(len(out), i + len(x)); out[i:j] += g * x[:j - i]
def whoosh(d=0.45):
    n = int(d * SR); x = rng.standard_normal(n + 40); x = lowpass(x, 40)[:n]
    f = np.linspace(0.2, 1, n) ** 2; return x * env(n, d * 0.6, d * 0.4) * (0.5 + f)
def pop():
    n = int(0.09 * SR); tt = np.arange(n) / SR; fr = np.linspace(1100, 650, n)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-tt * 45)
def thud():
    n = int(0.5 * SR); tt = np.arange(n) / SR
    return (np.sin(2 * np.pi * 70 * tt) * np.exp(-tt * 9) + 0.25 * rng.standard_normal(n) * np.exp(-tt * 60))
def boom(d=1.6):
    n = int(d * SR); tt = np.arange(n) / SR
    rum = lowpass(rng.standard_normal(n + 200), 200)[:n] * 6
    return (np.sin(2 * np.pi * 45 * tt) * 0.8 + rum) * np.exp(-tt * 2.2)
def shimmer(d=1.6):
    n = int(d * SR); tt = np.arange(n) / SR
    return sum(np.sin(2 * np.pi * f * tt) for f in (1760, 2217, 2637)) / 3 * env(n, 0.05, d * 0.9) * 0.6
def rumble(d):
    n = int(d * SR); x = lowpass(rng.standard_normal(n + 300), 300)[:n] * 8
    return x * env(n, d * 0.7, 0.15)
def clicks(d, rate=14):
    n = int(d * SR); x = np.zeros(n); c = pop()[:600] * 0.5
    for k in range(int(d * rate)):
        i = int(k / rate * SR); x[i:i + len(c)] += c[:max(0, min(len(c), n - i))]
    return x
def riser(d=1.2):
    n = int(d * SR); tt = np.arange(n) / SR; fr = np.linspace(120, 480, n)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.linspace(0, 1, n) ** 2 * 0.6
# ---- 편마다 고칠 곳 (아래는 08편) ----
S = lambda i: L[i]['start']; C = lambda i, k=0: L[i]['commas'][k]; At = lambda i, f: S(i) + (L[i]['end'] - S(i)) * f
# 컷마다 휙(장면이 바뀌는 시각)
cuts = [C(0), S(1), S(2), S(3), C(3), S(4), At(5, .35), S(6), C(7), S(8), S(9), S(10), S(11), C(11), S(12), S(13), S(14), S(15), S(16), C(16), S(17), S(18), S(19), C(19, 1), S(20), S(21), S(22), S(23), S(24), C(24)]
for c in cuts: put(c - 0.18, whoosh(), 0.10)
# 라벨이 뜰 때 톡
for c in [S(1) + .1, S(2) + .2, S(3) + .2, S(8) + .1, C(8) + .1, S(10) + .1, C(11) + .2, S(12) + .1, S(16) + .2, At(17, .5), S(20) + .2, S(21) + .2, C(21) + .1, S(22) + .2, S(23) + .3, S(18) + .1, C(18, 0) + .1, C(18, 1) + .1]:
    put(c, pop(), 0.18)
# 큰 숫자·핵심어에 쿵
for c in [S(0) + .2, C(0) + .2, S(4) + .1, S(6) + .1, S(9) + .2, S(11) + .2, S(13) + .1, S(15) + .3, C(19, 0) + .2]:
    put(c, thud(), 0.35)
put(C(3) + .1, thud(), 0.3)
put(At(5, .35), rumble(C(5) - At(5, .35)), 0.12)   # 터널로 다가가는 바람 소리
put(C(5), boom(), 0.45)                              # 블랙홀: 쿵 하고 어두워짐
put(C(7), shimmer(), 0.25)                           # 화이트홀: 반짝
put(S(9) - 1.0, riser(1.0), 0.18)                    # 중간 훅 앞 긴장
put(C(11) + .1, clicks(L[11]['end'] - C(11)), 0.5)  # 계량기 도는 소리
put(C(19, 1) + .6, riser(1.2), 0.12)
out = out / max(1e-9, np.abs(out).max()) * 0.5
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
w = wave.open('sfx.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print(len(cuts), 'cuts')
