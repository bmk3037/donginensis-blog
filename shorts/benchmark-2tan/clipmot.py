"""클립마다 0.5초 칸별 움직임(화면 폭 %/초)과 장면 튐(프레임 차이) 출력"""
import sys, os, numpy as np, cv2
W, H = 180, 320
for p in sys.argv[1:]:
    cap = cv2.VideoCapture(p); fps = cap.get(cv2.CAP_PROP_FPS); g = []
    while True:
        ok, f = cap.read()
        if not ok: break
        g.append(cv2.cvtColor(cv2.resize(f, (W, H), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY))
    n = len(g); half = int(fps / 2); mv = []; jump = []
    for s in range(0, n - half, half):
        fl = cv2.calcOpticalFlowFarneback(g[s], g[min(s + 3, n - 1)], None, 0.5, 3, 15, 3, 5, 1.2, 0)
        m = np.sqrt((fl ** 2).sum(2)).mean() / W * fps / 3 * 100
        d = max(np.mean(cv2.absdiff(g[i], g[i - 1])) for i in range(s + 1, min(s + half, n)))
        mv.append(m); jump.append(d)
    print(f"{os.path.basename(p):9s} 움직임 " + " ".join(f"{m:3.0f}" for m in mv))
    print(f"{'':9s} 튐     " + " ".join(f"{d:3.0f}" for d in jump))
