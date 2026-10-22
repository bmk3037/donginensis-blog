"""숨은 설비 도감 배경음(직접 만든 음원, 저작권 걱정 없음). 잔잔한 다큐 느낌: 느린 화음 패드 + 부드러운 피아노 아르페지오 + 낮은 베이스.
   python3 make_bgm.py → bgm_calm.wav(120초, 앞뒤 페이드)"""
import numpy as np, wave
SR = 44100; BPM = 76; beat = 60 / BPM; bar = beat * 4; DUR = 120
t_all = np.arange(int(SR * DUR)) / SR
out = np.zeros_like(t_all); outR = np.zeros_like(t_all)
rng = np.random.default_rng(3)
def note(f): return 440 * 2 ** ((f - 69) / 12)
# Am - F - C - G (자연스러운 다큐 진행), 각 2마디
prog = [[57, 60, 64], [53, 57, 60], [48, 55, 60], [55, 59, 62]]
bass = [45, 41, 48, 43]
def add(buf, start, sig, gain):
    i = int(start * SR); j = min(len(buf), i + len(sig))
    if j > i: buf[i:j] += gain * sig[:j - i]
def pad(freqs, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) + 0.35 * np.sin(2 * np.pi * f * 2.003 * t) + 0.15 * np.sin(2 * np.pi * f * 0.998 * t) for f in freqs)
    env = np.minimum(1, t / 1.6) * np.minimum(1, (dur - t) / 1.6)
    return s * env / len(freqs)
def pluck(f, dur=2.5):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * k * t) * (0.6 ** (k - 1)) * np.exp(-t * (2.2 + k)) for k in range(1, 5))
    return s * np.minimum(1, t / 0.005)
def low(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * np.minimum(1, t / 0.4) * np.minimum(1, (dur - t) / 0.6)
pos, k = 0.0, 0
while pos < DUR:
    ch = prog[k % 4]; seg = bar * 2
    p = pad([note(m) for m in ch] + [note(ch[0] + 12)], seg + 1.2)
    add(out, pos, p, 0.22); add(outR, pos + 0.012, p, 0.22)
    add(out, pos, low(note(bass[k % 4] - 12), seg), 0.18); add(outR, pos, low(note(bass[k % 4] - 12), seg), 0.18)
    if pos > bar * 4:  # 처음 4마디 뒤부터 아르페지오
        arp = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[1] + 12, ch[0] + 24, ch[2] + 12, ch[1] + 12, ch[2] + 12]
        for i, m in enumerate(arp):
            st = pos + i * beat
            if rng.random() < 0.85:
                g = 0.10 * (0.8 + 0.4 * rng.random())
                add(out, st, pluck(note(m)), g * (1.1 if i % 2 else 0.9)); add(outR, st + 0.008, pluck(note(m)), g * (0.9 if i % 2 else 1.1))
    pos += seg; k += 1
# 간단한 잔향
ir = rng.standard_normal(int(SR * 1.8)) * np.exp(-np.arange(int(SR * 1.8)) / SR * 3.2) * 0.02
def rev(x): return x + np.convolve(x, ir)[:len(x)]
L, R = rev(out), rev(outR)
fade = np.minimum(1, t_all / 3) * np.minimum(1, (DUR - t_all) / 4)
L, R = L * fade, R * fade
m = max(np.abs(L).max(), np.abs(R).max()); L, R = L / m * 0.7, R / m * 0.7
pcm = (np.stack([L, R], 1) * 32767).astype(np.int16)
w = wave.open('bgm_calm.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print('bgm_calm.wav', DUR, 's')
