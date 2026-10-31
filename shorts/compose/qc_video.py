"""올리기 전 영상 검사(STYLE-V4 8절). 사용: python3 -I qc_video.py 영상.mp4 [커버1초포함=1]
   길이, 소리 크기·최고 음량, 해상도, 컷 수(화면이 확 바뀌는 곳), 5초 넘게 느린 구간, 멈춘 프레임을 한 번에 잰다."""
import json, re, subprocess, sys
import numpy as np
p = sys.argv[1]; cover = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout.split()[0])
vs = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate", "-of", "csv=p=0", p]).stdout.strip()
e = run(["ffmpeg", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]; peak = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1]
fps, w, h = 12, 54, 96
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vf", f"fps={fps},scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
a = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
d = np.abs(np.diff(a, axis=0)).mean(axis=(1, 2))
body = dur - cover
cuts = []
for i in np.where(d > 16)[0]:
    if not cuts or i - cuts[-1] > 3: cuts.append(i)
# 느린 구간: 0.5초(6프레임) 이동 평균이 15 미만으로 이어지는 가장 긴 길이(컷 부분은 제외)
mv = np.convolve(np.minimum(d, 16), np.ones(6) / 6, mode="same")
slow, run_, worst = False, 0, 0
for x in mv:
    if x < 4.0: run_ += 1; worst = max(worst, run_)
    else: run_ = 0
print(f"길이 {dur:.1f}s (본편 {body:.1f}s)  해상도·프레임 {vs}")
print(f"소리 {lufs} LUFS  최고 음량 {peak} dBFS  {'OK' if float(peak) < 0 else '최고 음량 0 넘음'}")
print(f"컷 {len(cuts)}개  1분당 {len(cuts)/body*60:.1f}  평균 {body/max(1,len(cuts)+1):.1f}s  목표 22~28컷")
print(f"가장 긴 거의 정지 구간 {worst/fps:.1f}s (5초 넘으면 불합격)  멈춘 프레임 {(d < 0.25).sum()}개")
