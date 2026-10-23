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
# ---- 31편 큐 ----
S = lambda i: L[i]['start']; E = lambda i: L[i]['end']; C = lambda i, k=0: L[i]['commas'][k]
Aa = lambda i: L[i]['a']
# c01 클립 소리(발차기·석고 깨짐) 앞 2.2초만
import wave as _w
_c = _w.open('c01_audio.wav'); _x = np.frombuffer(_c.readframes(_c.getnframes()), np.int16).astype(float) / 32768
_x = _x[:int(2.2 * SR)] * np.linspace(1, 0, int(2.2 * SR)) ** 0.5
put(0.0, _x / max(1e-9, np.abs(_x).max()), 0.6)
put(0.35, thud(), 0.35)
for i in range(1, 20):
    if i not in (12,): put(Aa(i) - 0.18, whoosh(0.4), 0.08)
for c in [C(6), C(16)]: put(c - 0.18, whoosh(0.4), 0.08)
pops = [S(1) + .2, C(1) + .9, C(2) + .4, S(3) + .2, C(3) + .4, S(4) + .2, S(7) + .2, C(7) + .3, S(8) + .2, S(9) + .2,
        S(10) + .2, C(10, 0) + .2, C(10, 1) + .2, S(11) + .3, S(12) + .2, S(13) + 1.0, S(14) + .2, C(14) + 1.0, E(14) - 1.2,
        C(15) + .3, S(16) + .5, C(16) + .4, E(16) - 1.2, S(6) + 1.0, C(17) + .3, S(18) + .3, C(18) + .4, C(6) + .3]
for c in pops: put(c, pop(), 0.15)
# 발차기(엄마)와 강조
put(Aa(3) + 2.9, boom(1.0), 0.4)
for c in [S(5) + .9, S(6) + .3, C(4) + .3, C(13) + .3, C(19) + .2]: put(c, thud(), 0.3)
# 벽 두드리기 '통통' 3번
def knock():
    n = int(0.18 * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * 180 * tt) * np.exp(-tt * 30) + 0.4 * np.sin(2 * np.pi * 360 * tt) * np.exp(-tt * 40)
for k in range(3): put(E(12) - 1.4 + 0.35 * k, knock(), 0.5)
put(E(9) - 2.4, riser(0.9), 0.16); put(E(9) - 1.5, boom(), 0.4)
put(C(17) - 0.9, boom(), 0.4)
out = out / max(1e-9, np.abs(out).max()) * 0.5
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
w = wave.open('sfx.wav', 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print('sfx ok')
