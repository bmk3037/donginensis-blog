"""34편 긴 판 음성에서 문장을 골라 30초판 음성과 timeline.js를 만든다(새 녹음 없음).
   10/24 결정 2: 첫 1초에 큰 숫자(140집)를 보여 주므로 그 숫자가 나오는 19·20번을 넣고, 질문·어디로·받아 줄 열차·난로 문장은 뺌."""
import json, subprocess
PICK = [0, 6, 7, 9, 15, 17, 19, 20, 24]
# 문장 앞부분을 잘라 쓰는 곳: 15번은 앞의 "그래서 "(받아쓰기 단어 시각 50.48초)를 빼고 "예전엔"부터
TRIM = {15: (50.50, "예전엔 열차에 달린 저항기로, 그 전기를 열로 태워 버렸대요")}
R, EDGE, PAD = 1.1, 0.06, 0.8
tl = json.loads(open('../34/timeline_raw.js').read().split('=', 1)[1].strip().rstrip(';'))
src = json.load(open('../../episodes/34/lines.json', encoding='utf-8'))
filt, L, t0 = [], [], 0.0
for k, i in enumerate(PICK):
    l = dict(tl['lines'][i]); a, b = l['start'] - EDGE, l['end'] + EDGE
    text = src[i]['text']
    if i in TRIM: a, text = TRIM[i]; l['start'] = a
    filt.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,atempo={R}[s{k}]")
    m = lambda x: round(t0 + (x - a) / R, 3)
    L.append({"text": text, "src": i, "start": m(l['start']), "end": m(l['end']), "commas": [m(c) for c in l['commas']]})
    t0 += (b - a) / R
dur = round(t0 + PAD, 2)
for k, l in enumerate(L):
    l['a'] = 0.0 if k == 0 else round((L[k - 1]['end'] + l['start']) / 2, 3)
    l['b'] = dur if k == len(L) - 1 else round((l['end'] + L[k + 1]['start']) / 2, 3)
fc = ';'.join(filt) + ';' + ''.join(f'[s{k}]' for k in range(len(L))) + f'concat=n={len(L)}:v=0:a=1,apad=pad_dur={PAD}[o]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'narration_raw.mp3', '-filter_complex', fc, '-map', '[o]', '-ar', '44100', 'narration.wav'], check=True)
open('timeline.js', 'w').write('window.TL = ' + json.dumps({'duration': dur, 'lines': L}, ensure_ascii=False) + ';\n')
print('길이', dur, [(l['src'], l['start'], l['end']) for l in L])
