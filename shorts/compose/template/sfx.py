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
# ---- 21편 큐 ----
S = lambda i: L[i]['start']; C = lambda i, k=0: L[i]['commas'][k]
T = lambda i, f: S(i) + (L[i]['end'] - S(i)) * f
cuts = [S(i) for i in range(1, 23)] + [C(1), C(2), C(4), C(5), C(6), C(8), C(9), C(10), C(11), C(12), C(14), C(18, 0), C(19), C(20), C(21), C(22)]
for c in cuts: put(c - 0.18, whoosh(), 0.12)
for c in [1.2, S(1) + .2, S(2) + .2, S(5) + .2, C(5) + .1, S(6) + .2, S(8) + .2, S(9) + .2, S(10) + .2, C(10) + .1, S(11) + .2, S(12), S(14) + .2, S(15) + .2, C(16) + .3, S(18) + .2, C(18, 1) + .1, C(19) + .1, S(20) + .2, S(21) + .2, S(22) + .3, C(22) + .1]:
    put(c, pop(), 0.18)
for k in range(3): put(S(7) + .3 + .35 * k, pop(), 0.2)
for k in range(3): put(S(12) + .6 + .8 * k, pop(), 0.2)
for k in range(3): put(C(14) + .1 + .6 * k, pop(), 0.22)
for c in [C(0) + .25, C(2) + .1, C(4) + .2, T(5, .85), C(9) + .1, T(16, .72), C(12) + .1, S(17) + .6, S(19) + .9, C(19) + .4, C(20) + .2, C(21) + .1, C(21) + .4, C(22) + .6]:
    put(c, thud(), 0.33)
# 강조 다섯 곳: 번쩍임과 함께 큰 쿵
for c in [C(1), S(3) - 0.05, C(6), C(8)]:
    put(c - 0.25, whoosh(0.3), 0.18); put(c, boom(1.0), 0.32)
put(S(13) - 0.9, riser(0.9), 0.18)
put(S(13), boom(), 0.5)
put(S(4) + .3, clicks(1.2), 0.2)
put(C(11) + .1, rumble(1.2), 0.15)
put(C(2) + .1, shimmer(), 0.15)
out = out / max(1e-9, np.abs(out).max()) * 0.5
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
w = wave.open('sfx.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print(len(cuts), 'cuts')
