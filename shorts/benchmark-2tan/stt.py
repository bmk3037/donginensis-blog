"""벤치마킹 영상 나레이션 받아쓰기. python stt.py 영상.mp4 [모델=small] → 영상.stt.txt (시작-끝 문장)
ffmpeg로 소리를 직접 풀어 넘김: faster-whisper 1.2.1의 자체 디코더가 최신 PyAV와 안 맞음(metadata_errors 오류)."""
import subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

src = sys.argv[1]
pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True, check=True).stdout
segs, _ = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else 'small', device='cpu', compute_type='int8').transcribe(
    np.frombuffer(pcm, np.float32), language='ko', vad_filter=True)
out = src.rsplit('.', 1)[0] + '.stt.txt'
with open(out, 'w', encoding='utf-8') as f:
    for s in segs:
        f.write(f'{s.start:6.2f}-{s.end:6.2f} {s.text.strip()}\n')
print(out)
