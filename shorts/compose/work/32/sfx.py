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
# ---- 32편 큐(지식컷식: 컷마다 휙, 라벨마다 톡) ----
S = lambda i: L[i]['start']; C = lambda i, k=0: L[i]['commas'][k]
T = lambda i, f: S(i) + (L[i]['end'] - S(i)) * f
MID = lambda i: C(i) if L[i]['commas'] else T(i, .5)
two = [1, 2, 3, 9, 10, 11, 12, 13, 15, 17, 18, 21, 22, 23, 24]
cuts = [S(i) for i in range(1, 28)] + [MID(i) for i in two] + [T(7, .34), T(7, .67), T(16, .34), T(16, .67), S(8) + 2.3]
for c in cuts: put(c - 0.12, whoosh(0.3), 0.10)
for c in [0.5, S(1) + .15, S(3) + .15, S(3) + .35, S(4) + .3, S(5) + .1, S(6) + .4, S(7) + .1, S(9) + .3, MID(10), S(11) + .2, MID(11) + .1,
          S(13) + .6, T(14, .45), S(15) + .2, MID(15) + .1, S(16) + .3, S(17) + .6, S(18) + .3, S(19) + .2, S(21) + .2, MID(21), S(22) + .4, S(23) + .6, S(24) + .3, MID(24), S(25) + .1]:
    put(c, pop(), 0.16)
put(S(8) + 0.7, boom(1.2), 0.42); put(S(8) + 0.2, rumble(2.0), 0.18)
put(S(12) + 0.75, riser(0.3), 0.12); put(S(12) + 1.0, thud(), 0.4)
put(S(20) + 0.05, shimmer(1.0), 0.14)
put(T(19, .8), thud(), 0.25)
out = out / max(1e-9, np.abs(out).max()) * 0.5
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
w = wave.open('sfx.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print(len(cuts), 'cuts')
