# ASIDE-RESUME: 지금 어디까지 했나 (어느 컴퓨터에서든 여기서 이어감)

> **규칙(대표이사 11/1)**: 회사 PC가 꺼져도 집 노트북에서 바로 이어 할 수 있어야 한다. Aside는 **작업 단계 하나가 끝날 때마다 이 파일을 갱신**해 GitHub에 올린다. 노트북(또는 다른 PC)의 Aside는 시작하면 **이 파일부터 읽고 "다음 할 일" 1번부터** 한다. 계정 이메일·이름은 여기 쓰지 않는다(계정 짝은 Aside 스킬 shorts-v4-flow에 있음).
> 같은 Flow 프로젝트에 두 기기가 동시에 클립을 넣지 않는다. 이어받는 쪽은 먼저 Flow 프로젝트에서 "생성 중" 클립이 있는지 본다.

마지막 갱신: 2026. 11. 1. (회사 PC)

## 지금: 54편 크린넷 — 남은 클립 만들기

| 항목 | 상태 | 위치 |
|---|---|---|
| 카드·대본(17문장) | 완료 | `shorts/produce/54.md` 맨 위 "★★★★" 절이 기준 |
| 음성 | 완료 86.9초 | `shorts/media/54/in/voice.wav`, 문장별 `in/voice/`, 시각 `in/NOTES.md` |
| 그림 | 완료 | `shorts/media/54/in/img/` (*_clean, *_sign, s09_pins) |
| 클립 완료(9) | c01 c02 c03 c04 c04b (1080p), c14a c14b c15 c17 (720p) | `shorts/media/54/in/clip/`, 쓸 구간은 NOTES |
| 클립 생성 중(3) | c10a c10b c12 | Flow 계정 D, 프로젝트 "숨은 설비 이야기 54 클립 D" |
| 클립 남음(7) | c13 c16 c05 c07 c08a c08b c11 | 같은 프로젝트에서 |
| c09 지도 | 뺌(글자 깨짐) | - |
| 크레딧 | 계정 D로 이번 편 100까지만(대표이사 11/1). 다른 계정 A·B·C는 오늘 0 | |

## 다음 할 일
1. Flow 계정 D → 프로젝트 "숨은 설비 이야기 54 클립 D" 열기. c10a·c10b·c12가 완성됐으면 **1080p 업스케일링됨**으로 받는다.
2. 받은 클립마다 0.3·2·4·6·7.8초 화면을 보고 표지판 글자("20.9mm", "1.94mm", "105억 원")가 깨졌는지 본다. 깨졌으면 다시 만들기 전에 크레딧을 말하고 묻는다.
3. 같은 프로젝트에서 남은 7개를 아래 시작 그림·프롬프트로 생성(설정: 동영상 · 프레임 · 9:16 · Veo 3.1 - Lite · x1 · 10크레딧 확인). 시작 그림은 프로젝트에 이미 올려 둠(파일 이름으로 "애셋 검색").
   - c13 ← s13_sign.jpg, c16 ← s16_sign.jpg, c05 ← s05_clean.jpg, c07 ← s07_clean.jpg, c08a ← s08a_clean.jpg, c08b ← s08b_clean.jpg, c11 ← s11_clean.jpg
   - 프롬프트: `54.md` "★★★★" 절의 같은 이름 클립. c16만 아래 "c16(표지판)" 판을 쓴다.
4. 1080p로 받아 `shorts/media/54/in/clip/`에 2개씩 올리고 NOTES.md 표에 "쓸 구간"을 적는다.
5. 다 모이면 Claude Code에 합성 요청(카드 "★★★★" 절 말·화면 표 그대로, 연속 장면 c04 전체 + c04b 앞 5초, 각 클립 쓸 구간은 NOTES).
6. 이 파일을 갱신한다.

## 카드에 없는 프롬프트
### c10a (← s10_sign.jpg, 문장 10 앞)
```
One continuous drone shot, no cuts. STRUCTURE RULE: waste moves in one direction only, from the street inlet down its chute, through the buried steel pipe, to the collection plant; the pipes stay buried under the ground and are seen only inside model cut-away sections, never above the street; pipes, inlets, buildings and machines keep exactly the same shape; nobody is ever inside a pipe or machine. Camera: slow smooth drone push-in toward the cut steel pipe wall, moving steadily for the whole 8 seconds. 0-3s: the camera passes the red "20.9mm" sign on the ground. 3-6s: the inspector measures the thick wall with the caliper. 6-8s: the camera settles on the thick solid edge of the wall. The wall stays thick and unchanged; no corrosion growth, no hole, no melting. Same tilt-shift architectural miniature look, colors and warm golden light as the start frame; tiny plain white faceless figurines. Audio: quiet workshop ambience, no music, no speech. No on-screen text overlays. The red 3D text keeps exactly the same "20.9mm" on the sign. No new letters or numbers beyond "20.9mm" on the sign; no logos.
```
### c10b (← e10_sign.jpg, 문장 10 뒤)
```
One continuous drone shot, no cuts. STRUCTURE RULE: waste moves in one direction only, from the street inlet down its chute, through the buried steel pipe, to the collection plant; the pipes stay buried under the ground and are seen only inside model cut-away sections, never above the street; pipes, inlets, buildings and machines keep exactly the same shape; nobody is ever inside a pipe or machine. Camera: slow smooth drone push-in toward the same cut steel pipe wall, moving steadily for the whole 8 seconds. 0-3s: the camera passes the red "1.94mm" sign on the ground. 3-6s: the inspector measures the thin corroded part of the wall with the caliper. 6-8s: the camera settles on the thinned corroded section. The damage does not spread; no new hole; the outer pipe keeps its shape. Same tilt-shift architectural miniature look, colors and warm golden light as the start frame; tiny plain white faceless figurines. Audio: quiet workshop ambience, no music, no speech. No on-screen text overlays. The red 3D text keeps exactly the same "1.94mm" on the sign. No new letters or numbers beyond "1.94mm" on the sign; no logos.
```
### c16(표지판) (← s16_sign.jpg, 문장 14)
```
One continuous drone shot, no cuts. STRUCTURE RULE: waste moves in one direction only, from the street inlet down its chute, through the buried steel pipe, to the collection plant; the pipes stay buried under the ground and are seen only inside model cut-away sections, never above the street; pipes, inlets, buildings and machines keep exactly the same shape; nobody is ever inside a pipe or machine. Camera: fast smooth drone tracking shot along the intact waste inlets on the seaside Songdo-style street, moving steadily for the whole 8 seconds. 0-3s: the camera glides past the firmly installed inlets. 3-6s: two maintenance figurines, one holding a blank clipboard, point at an inlet. 6-8s: the camera rises toward the glass skyline and the sea. No crane, no lifting, no removal, no digging. Same tilt-shift architectural miniature look, colors and warm golden light as the start frame; tiny plain white faceless figurines. Audio: quiet urban seaside ambience, no music, no speech. The red 3D text keeps exactly the same "단계적 폐쇄"; the camera passes it within the first 4 seconds and moves on. No new letters or numbers beyond "단계적 폐쇄"; no logos.
```

