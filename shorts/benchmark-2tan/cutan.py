"""이탄생 컷 분석: 컷 목록 → 컷마다 움직임(확대·이동·시차), 전환 방식, 효과음·빨간 그래픽 위치.
사용: python -I cutan.py 영상.mp4 [영상2 ...]  → 영상마다 <id>_shots.csv, 요약 출력"""
import sys, subprocess, json, os
import numpy as np, cv2

FPS = 30; W, H = 180, 320

def frames(path):
    cap = cv2.VideoCapture(path); src = cap.get(cv2.CAP_PROP_FPS) or 30
    step = max(1, round(src / FPS)); out = []; col = []; i = 0
    while True:
        ok, f = cap.read()
        if not ok: break
        if i % step == 0:
            s = cv2.resize(f, (W, H), interpolation=cv2.INTER_AREA)
            out.append(cv2.cvtColor(s, cv2.COLOR_BGR2GRAY)); col.append(s)
        i += 1
    return np.array(out), col, src / step

def red_frac(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 0] < 8) | (hsv[..., 0] > 172)) & (hsv[..., 1] > 150) & (hsv[..., 2] > 120)
    return m.mean()

def affine_fit(flow):
    ys, xs = np.mgrid[8:H - 8:8, 8:W - 8:8]
    u = flow[ys, xs, 0].ravel(); v = flow[ys, xs, 1].ravel()
    x = (xs.ravel() - W / 2) / W; y = (ys.ravel() - H / 2) / W
    A = np.stack([x, y, np.ones_like(x)], 1)
    pu, *_ = np.linalg.lstsq(A, u, rcond=None); pv, *_ = np.linalg.lstsq(A, v, rcond=None)
    res = np.sqrt(np.mean((A @ pu - u) ** 2 + (A @ pv - v) ** 2))
    zoom = (pu[0] + pv[1]) / 2 / W            # 화면 폭 대비 배율 변화
    return zoom, pu[2] / W, pv[2] / W, res / W, np.sqrt(np.mean(u ** 2 + v ** 2)) / W

def audio_onsets(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    n, hop = 1024, 160
    if len(a) < n * 2: return np.array([])
    win = np.hanning(n); fr = np.lib.stride_tricks.sliding_window_view(a, n)[::hop] * win
    mag = np.abs(np.fft.rfft(fr, axis=1)); hf = mag[:, 256:]          # 4 kHz 위(효과음 쉭·딱)
    lm = np.log1p(hf * 50); flux = np.maximum(lm[1:] - lm[:-1], 0).sum(1)
    k = np.convolve(flux, np.ones(5) / 5, "same"); thr = k.mean() + 2.5 * k.std()
    t = []; last = -1
    for i in range(1, len(k) - 1):
        if k[i] > thr and k[i] >= k[i - 1] and k[i] >= k[i + 1] and (i - last) * hop / 16000 > 0.15:
            t.append((i + 1) * hop / 16000 + n / 32000); last = i
    return np.array(t)

def near(ts, xs, w):
    return np.mean([np.any(np.abs(ts - x) <= w) for x in xs]) if len(xs) else float("nan")

def analyze(path):
    g, col, fps = frames(path); N = len(g); dur = N / fps
    d = np.array([0] + [np.mean(cv2.absdiff(g[i], g[i - 1])) for i in range(1, N)])
    sharp = np.array([cv2.Laplacian(x, cv2.CV_64F).var() for x in g])
    hi = d > max(18, np.percentile(d, 99) * 0.6)                       # 장면이 크게 바뀐 프레임
    # 전환 묶기: 0.5초 안에 붙은 높은 프레임은 하나의 전환
    ev = []; i = 0
    while i < N:
        if hi[i]:
            j = i
            while j + 1 < N and (hi[j + 1] or (j + 2 < N and hi[j + 2]) or (j + 3 < N and hi[j + 3])) and (j - i) < fps * 0.8: j += 1
            ev.append((i, j)); i = j + 1
        else: i += 1
    trans = []
    for a0, b0 in ev:
        span = (b0 - a0 + 1) / fps
        lo, hi2 = max(0, a0 - 6), min(N - 1, b0 + 6)
        blur = sharp[a0:b0 + 1].min() / max(1, np.median(np.r_[sharp[lo:a0], sharp[b0 + 1:hi2 + 1]]) if b0 + 1 <= hi2 else 1)
        kind = "끊기" if span <= 2 / fps else ("휙(흐림)" if blur < 0.5 else "빠른 이동")
        trans.append(((a0 + b0) / 2 / fps, span, kind))
    cuts = [t for t, *_ in trans]
    bounds = [0] + [int(round(t * fps)) for t in cuts] + [N]
    shots = []
    for k in range(len(bounds) - 1):
        s0, s1 = bounds[k] + 3, bounds[k + 1] - 3
        if s1 - s0 < 8: continue
        st = max(3, int(fps * 0.2)); rec = []
        for f in range(s0, s1 - st, st):
            fl = cv2.calcOpticalFlowFarneback(g[f], g[f + st], None, 0.5, 3, 15, 3, 5, 1.2, 0)
            rec.append(affine_fit(fl))
        if not rec: continue
        r = np.array(rec); per = fps / st
        zoom = r[:, 0].mean() * per * 100; px = r[:, 1].mean() * per * 100; py = r[:, 2].mean() * per * 100
        res = np.median(r[:, 3]) * per * 100; mag = r[:, 4].mean() * per * 100
        shots.append(dict(t0=round(bounds[k] / fps, 2), t1=round(bounds[k + 1] / fps, 2), len=round((bounds[k + 1] - bounds[k]) / fps, 2),
                          zoom_pct_s=round(zoom, 2), panx_pct_s=round(px, 2), pany_pct_s=round(py, 2), resid_pct_s=round(res, 3), move_pct_s=round(mag, 2)))
    red = np.array([red_frac(c) for c in col])
    rs = np.convolve(red, np.ones(5) / 5, "same"); gup = []
    for i in range(int(fps * 0.3), N):
        if rs[i] - rs[i - int(fps * 0.3)] > 0.004 and (not gup or i / fps - gup[-1] > 0.8): gup.append(i / fps)
    on = audio_onsets(path)
    rng = np.random.default_rng(0); base = near(on, rng.uniform(0, dur, 300), 0.12)
    return dict(dur=round(dur, 1), shots=shots, trans=trans, gfx=gup, onsets=len(on),
                sfx_at_cut=round(near(on, cuts, 0.12), 2), sfx_at_gfx=round(near(on, gup, 0.15), 2), sfx_random=round(base, 2))

if __name__ == "__main__":
    allr = {}
    for p in sys.argv[1:]:
        r = analyze(p); allr[os.path.basename(p)] = r
        with open(os.path.splitext(p)[0] + "_shots.json", "w", encoding="utf-8") as f: json.dump(r, f, ensure_ascii=False, indent=0)
        print(os.path.basename(p), "길이", r["dur"], "컷", len(r["shots"]), "전환", {k: sum(1 for *_, x in r["trans"] if x == k) for k in ("끊기", "휙(흐림)", "빠른 이동")},
              "그래픽", len(r["gfx"]), "효과음: 컷 옆", r["sfx_at_cut"], "그래픽 옆", r["sfx_at_gfx"], "아무 데", r["sfx_random"], flush=True)
