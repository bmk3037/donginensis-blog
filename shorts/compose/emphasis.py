"""강조 문장만 느리고(1.03배) 3dB 크게, 앞에 짧은 쉼을 넣어 음성을 다시 짓는다. make.sh align 다음에 작업 폴더에서 실행.
   python3 ../../emphasis.py 배속 강조문장번호(0부터) 쉼
   예: python3 ../../emphasis.py 1.15 1,3,6,8,13 3:0.35,8:0.3,13:0.45   → narration.wav, timeline.js"""
import json, subprocess
import sys
BASE = float(sys.argv[1]) if len(sys.argv) > 1 else 1.15
EMPH_T, GAIN = 1.03, 3.0
EMPH = {int(x) for x in sys.argv[2].split(',')} if len(sys.argv) > 2 else set()
PAUSE = {int(k): float(v) for k, v in (p.split(':') for p in sys.argv[3].split(','))} if len(sys.argv) > 3 else {}
tl = json.loads(open('timeline_raw.js').read().split('=', 1)[1].strip().rstrip(';'))
L = tl['lines']; dur_raw = tl['duration']
cuts = [0.0] + [L[i]['b'] for i in range(len(L) - 1)] + [dur_raw]
parts, filt, t0 = [], [], 0.0
for i, l in enumerate(L):
    a, b = cuts[i], cuts[i + 1]
    tempo = EMPH_T if i in EMPH else BASE
    g = GAIN if i in EMPH else 0.0
    p = PAUSE.get(i, 0.0)
    filt.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,atempo={tempo},volume={g}dB" + (f",adelay={int(p*1000)}:all=1" if p else "") + f"[s{i}]")
    m = lambda x: round(t0 + p + (x - a) / tempo, 3)
    l['start'], l['end'] = m(l['start']), m(l['end'])
    l['commas'] = [m(c) for c in l['commas']]
    t0 = t0 + p + (b - a) / tempo
dur = round(t0, 2)
for i, l in enumerate(L):
    l['a'] = 0.0 if i == 0 else round((L[i - 1]['end'] + l['start']) / 2, 3)
    l['b'] = dur if i == len(L) - 1 else round((l['end'] + L[i + 1]['start']) / 2, 3)
fc = ';'.join(filt) + ';' + ''.join(f'[s{i}]' for i in range(len(L))) + f'concat=n={len(L)}:v=0:a=1[o]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'narration_raw.mp3', '-filter_complex', fc, '-map', '[o]', '-ar', '44100', 'narration.wav'], check=True)
open('timeline.js', 'w').write('window.TL = ' + json.dumps({'duration': dur, 'lines': L}, ensure_ascii=False) + ';\n')
print('길이', dur)
