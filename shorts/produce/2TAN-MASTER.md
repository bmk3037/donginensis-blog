# 이탄생식 한 편 만들기 — 새 세션용 마스터 (v2, 2026-11-03)

새 세션에서 이 파일 하나만 읽으면 주제 → 대본 → 음성 → 그림 → 클립 → 합성 → 업로드까지 만든다.
근거: 이탄생 릴스 조회수 상위 3편 실측(`shorts/benchmark-2tan-top3.md`), 김포골드라인 직접 분석(`shorts/benchmark-2tan_saeng.md`), Gemini 분석(`shorts/benchmark-gemini/2tan_*.md`), 57편 실제 제작(`shorts/produce/57.md`). 예전 판은 `2TAN-MASTER-v1.md`.
**베끼는 것은 구조·화면 짜임·리듬뿐.** 이탄생의 문장·주제·끝말("이렇게 탄생한 겁니다")은 쓰지 않는다. 우리 끝말은 "…이런 설비가 숨어 있었습니다".

## 0. 쓰는 법 (대표이사 → Claude)
```
2TAN-MASTER로 [주제] 만들어줘.            ← 대본 초안이 있으면 같이 붙여 넣기
2TAN-MASTER 2절로 다음 주제 5개 추천해줘.
```
Claude 순서: ① **편 번호 확인**(`ls shorts/produce shorts/media`, 다른 세션이 쓰는 번호면 다음 번호) ② 사실 확인 ③ 대본 ④ 음성 ⑤ 그림 프롬프트 + Aside 지시 ⑥ 그림 오면 검수 → 그림판 초안 ⑦ 클립 프롬프트 + Aside 지시 ⑧ 클립 오면 검수 → 완성본 ⑨ 업로드 카드. **묻지 말고 끝까지 한다**(대표이사 11/3 "몇번말해"). 정할 것만 끝에 한 줄로.

## 1. 이탄생 실측 (상위 3편: 삼성역 461만 · 롯데타워 320만 · 인천공항 238만)
| 항목 | 값 |
|---|---|
| 길이 | 88~105초 (우리 목표 96초 안팎) |
| 장면 | 14~18개, **평균 5.4~6.6초**. 컷을 자주 자르지 않고 한 장면을 5~10초 끈다 |
| 장면 안 변화 | 4~13번: 땅이 잘려 단면, 층이 차오름, 건물이 솟음, 낮→밤, 물이 참 |
| 끊김 없는 전환 | 2~4번: **카메라가 틈·지도 속으로 뚫고 들어감**, 또는 흐릿하게 확 도는 궤도 |
| 카메라 | 밀기(앞·아래), 정지(수직 부감·단면), **위로 솟기(뒤로 빠짐)**, 훑기, 궤도. 한 장면에 한두 동작 |
| 그림체 | 실내·통로도 밝고 따뜻하게(어둡고 거친 실사 아님), 앞뒤 흐린 틸트시프트. **실제 색의 3D 미니어처 도시**(회색 도로·유리 빌딩·초록 나무·보통 색 차·흙 단면, 밤 장면도 있음), 틸트시프트, 따뜻한 햇빛, 처음부터 끝까지 한 세계, **빨강은 그래픽에만**. ※ 11/3 실제 화면(삼성역·김포) 비교: 베이지·흰색 단색 모형이 아님 |
| 제목 | 0초 **위 가운데 지명 크게 2~4초**, 카메라가 움직이면 밀려남 |
| 숫자 | 전부 **빨간 도장·태그·핀·치수선**, 장면 속 물체 옆에 1~4초. 큰 글자 상자 없음 |
| 자막 | **화면 정가운데(세로 45~55%)**, 흰 굵은 글씨 + 검은 테두리, 1~2어절, 0.3~0.5초마다, 처음부터 끝까지 |
| 로고 | 왼쪽 위 작은 원형(1.5초부터 끝까지) |
| 소리 | 0.1~0.3초 만에 말 시작(음악 도입 없음), 배경음 아주 작게, **컷 직전 0.1~0.5초 거의 무음**, 빨간 그래픽 뜰 때 효과음 |
| 첫 문장 | **지명 + 다들 아는 장면**: "삼성역 코엑스 사거리 지날 때마다 보이는 그 공사장." |

## 2. 주제 고르기
1. 바구니 셋: 매일 쓰거나 지나치는 **이름 있는 것**(노선·역·다리·공항·아파트 설비) + 최근 뉴스·계절 / **돈·안전 숫자** / **"왜 ~일까?"가 짐작 안 되는 것**.
2. `python3 shorts/compose/topic_check.py "검색어1|검색어2"` (환경 변수 YOUTUBE_API_KEY): 관련 영상 최고 30만 이상 = 수요, 같은 각도 설명형 쇼츠 최고 30만 미만 = 빈자리.
3. 원문(기사·공공자료)에서 숫자 5개 이상 + 질문의 답을 찾을 수 있는 것만.
4. 표로 5개: 주제 | 첫 문장(안) | 메인 질문 → 답 | 수요 | 경쟁 | 시기.

## 3. 대본 (24~27문장, 짧게, 원본 약 100초 → 1.06배 96초)
| 문장 | 할 일 | 57편 예 |
|---|---|---|
| 1 | **지명 + 다들 아는 장면** | "아파트 지하주차장, 차 댈 때마다 보이는 천장의 그 빨간 배관." |
| 2 | **결론부터** | "결론부터 말하면, 이 배관은 불이 나기 전까지 텅 비어 있습니다." |
| 3 | **결론 숫자**(사건·돈·사람) | "이 배관에 물이 끝내 오지 않아, 차 팔백칠십 대가 피해를 본 화재도 있었습니다." |
| 4 | **메인 질문**(13초 안) | "그런데 왜, 스프링클러 배관을 비워 둘까요?" |
| 5~10 | 답(원리), 한 문장 = 한 가지 | 찬바람 → 얼어 터짐 → 밸브 아래 물 → 감지기 두 개 → 물이 차오름 |
| 11~14 | **"그럼 ~하면 되지 않냐고요?"** → 막히는 이유 | "그럼 감지기만 울리면, 무조건 열리면 되지 않냐고요?" |
| 15~22 | 사연: **연도·장소·사람**, 날짜순 | 2024년 8월 청라 → 버튼 → 5분 → 87대·783대 → 두 달 뒤 전주 |
| 23~24 | 지금 | "그래서 올해 3월부터 … 습식이 원칙이 됐습니다." |
| 25 | 이름 밝히기 | "불이 나야 비로소 물이 차는 길, 준비작동식 스프링클러입니다." |
| 26 | 끝말 | "우리 아파트 땅 밑에는, 이런 설비가 숨어 있었습니다." |
- 나레이션에 구독·공유 유도 없음. 문장은 한 호흡(2~5초), 긴 문장은 둘로 나눈다.
- **사실 확인표 필수**: 말 | 원문 인용 | 출처(매체·날짜) | 상태. 원문에서 확인 안 된 말(동기·범위 등)은 빼거나 확인된 표현으로("오작동일까 봐" → "현장 확인 없이", "새로 짓는" → 뺌).
- say.txt(읽을 문장, 숫자는 한글) + disp.txt(자막, 숫자는 아라비아) 두 파일.

## 4. 음성 (타입캐스트 필재)
```
mkdir -p shorts/compose/work/NN && cd shorts/compose/work/NN   # say.txt, disp.txt 넣기
TYPECAST_API_KEY=… python3 ../../template-2tan/tts_lines.py say.txt piljae 1.06
```
- 문장마다 따로 만들어 0.3초 쉼으로 잇고 경계를 고정한다(한 파일로 만들면 문장 경계가 틀어짐, 57편에서 확인). 결과 timeline.js·narration.wav.
- 문장 하나 고치면 `lines/NN.mp3`만 지우고 다시 돌린다. 원본은 `shorts/media/NN/in/voice.mp3`로 올린다.
- 키는 환경 변수에서만. 채팅·저장소에 적지 않는다.

## 5. 그림 (20~24장, Nano Banana, 9:16, x1)
- 문장 1~2개에 그림 1장. **지명이 나오면 3D 지도 그림**(빨간 핀 + 땅이 잘려 지하가 보이게, 나중에 "뚫고 들어가기" 시작 그림). 끝 그림 = 하늘에서 본 전체 + 땅 아래 단면(위로 솟기).
- 장면 안 변화가 필요한 곳은 **편집 그림**(예: 07 = 05를 열어 편집, 물이 차오름).
- **클립 끝 그림도 그림 단계에서 같이 만든다**(7-1의 1번): 같은 장면 다가가기는 `NNe.jpg`(NN을 열어 카메라만 가까이), 변화 장면은 결과 편집 그림. 그림 수는 약 1.6배가 되지만 크레딧 0.
- 프롬프트 = 장면 묘사(영어) + 아래 끝말 그대로. 주인공 설비도 실제 색 그대로(빨갛게 칠하지 않음), 빨간 소품을 그 옆에(고리·윤곽·화살표·핀·X·물음표). 글자·숫자는 그림에 넣지 않고 합성에서 얹는다.
```
Style: a hyper-detailed cinematic 3D render of the real place as a realistic miniature world, like a high-end architectural visualization seen through a tilt-shift lens: natural realistic colors and materials - grey asphalt and concrete, glass and stone buildings, green street trees, cars in ordinary everyday colors, brown soil and rock in the cut-away ground sections, black and grey cables - warm soft sunlight with gentle shadows unless the scene says otherwise, interiors and tunnels are lit just as brightly and warmly as a presentation model under soft studio light - clean, tidy and inviting, never dark, grimy or gritty; strong tilt-shift miniature look with the near foreground and far background softly blurred, shallow depth of field, the world continues to every edge of the frame with no table, base or backdrop. Bright red (#E53935) is used only for a few 3D infographic props placed next to objects (rings, outlines, arrows, pins, crosses, question marks, dimension lines); apart from those props, only things that are red in real life (a fire extinguisher, fire trucks) are red. Cars have no logos and no license plates. Any people are tiny plain white figurines without faces. Absolutely no letters or numbers anywhere; all signs, panels, screens and props are blank. Main subject in the lower two-thirds, upper third calmer for overlay text. Vertical 9:16.
```
- 이름: `~/Downloads/숨은설비/NN/01.jpg` …, GitHub `shorts/media/NN/in/img/` (ASIDE-MAKE 0-00). 카드 `shorts/produce/NN.md`, 한 번에 복사 `shorts/produce/NN_prompts.txt`.
- **회색 바탕 단면 블록 그림체(56편 00_기준)는 쓰지 않는다**(벤치마크 근거 없음, 11/3).

**Aside 지시(그림) 틀**
```
NN편 그림 MM장 만들어 줘(이탄생 그림체).
0. git pull. 프롬프트 shorts/produce/NN_prompts.txt ([01.jpg]~)
1. Flow 새 프로젝트 "숨은 설비 이야기 NN [주제] 이탄생", 이미지 · Nano Banana · 9:16 · x1, 참고 그림 없음
2. 01부터 순서대로, 프롬프트 한 글자도 바꾸지 말 것. 편집 그림(예 07)은 지정된 번호를 열어 편집(편집 전 큰 그림 번호 확인)
3. "1K 원본 크기"로 받자마자 ~/Downloads/숨은설비/NN/01.jpg … 로 이름 바꿈
4. 한 장마다 검사, 실패면 그 번호만 다시(최대 3번): 실제 색의 미니어처 도시 + 따뜻한 빛(온통 베이지·흰색이면 실패) / 빨강은 소품과 원래 빨간 것만 / 받침대·테이블 없음 / 사람은 얼굴 없는 흰 인형 / 글자·숫자 없음 / 차 상표·번호판 없음
5. 한 장 끝나면 바로 GitHub shorts/media/NN/in/img/ 에 올리고 커밋·푸시(모아서 올리지 말 것), NOTES.md(번호 | 다시 뽑은 횟수 | 이유 | 메모). 이메일·이름·계정 아이디 적지 말 것
6. 클립은 만들지 말 것. "NN: 그림 MM장 완료" 커밋하고 보고
```

## 6. 그림판 초안 (클립 없이 먼저)
```
cd shorts/compose
cp template-2tan/scene_2tan.html template-2tan/sfx_2tan.py work/NN/   # sfx_2tan.py → work/NN/sfx.py 로 이름 바꿈
# scene_2tan.html에서 "편마다 고칠 곳" 아래만 고침: globalHud(제목·도장·태그·핀), SCENES(P = 그림, Q = 클립)
bash template-2tan/finish_2tan.sh NN draft      # → shorts/media/NN/out/NN_draft.mp4
```
- 장면 20~23개(평균 4~6초). 문장 2~3개를 한 장면으로 묶는다. 같은 그림을 두 번 쓰면 배율·기준점을 달리한다.
- `P(그림, 시작, 끝, from, to, cx, cy, xin, dive)`: xin = 앞 장면과 겹쳐 바뀌는 초(장면 안 변화), dive = 끝 1.1초에 확 다가가 다음 장면으로 뚫고 들어감(지도 장면에). 끝 장면은 from > to(뒤로 빠짐).
- 숫자: `stamp`(도장), `tag`(꼬리 딱지), `pin`(핀). 0초 제목은 위 가운데(2.6초부터 밀려남). 자막은 가운데 흰 글자(자동).
- 정지 화면 먼저 확인: `SCENE=scene_2tan.html node ../../render.mjs stills 0.5,10,30,…` (work/NN에서).
- 대표이사에게 보내고 그림체·구성 확인받은 뒤 클립.

## 7. 클립 — "전부 아주 좋음"을 목표로 (11/4 개정, 57·58편 클립 25개 검수 결과)

### 7-0. 57·58편에서 배운 것
| 결과 | 클립 | 공통점 |
|---|---|---|
| **아주 좋음** | 57 c16(지도→땅속→스프링클러), 58 c13(지도→맨홀→불난 통로), 58 c19(불탄 통로→새 통로), 58 c10(맨홀 속으로), 57 c01(배관 속으로) | **시작 + 끝 그림을 둘 다 줌**(또는 한 방향으로 계속 내려가는 길), 카메라 길이 처음부터 끝까지 정해져 있음 |
| 망가짐 | 58 c01 드론 기체가 화면에 나옴 | 프롬프트에 "**drone**"이라는 낱말 → Veo가 드론을 그려 넣음 |
| 망가짐 | 58 c03 소화기에 "FIRE", 57 c13 판에 "CCCC" | 원래 글자가 있는 물건(소화기·제어반)에 **다가가면** 글자를 만들어 냄 |
| 망가짐 | 58 c03·c07·c09·c21, 57 c11 — 3~4초 뒤 장면이 다른 곳으로 바뀜 | **시작 그림 하나만** 주고 카메라를 멀리 보냄 → 끝을 Veo가 지어냄 |
| 망가짐 | 57 c17 불이 꺼져야 하는데 커짐 | 결과(꺼짐)를 **끝 그림으로 안 줌** |
| 망가짐 | 58 c09 화살표가 새로 생김, 고리가 둘 | 빨간 소품이 "그대로 있어야 한다"는 말이 없음 |

### 7-1. 규칙 (모든 클립)
1. **모든 클립에 시작 + 끝 그림.** 끝 그림이 없으면 만든다(그림 단계에서 같이):
   - 다른 장면으로 뚫고 들어가는 클립: 끝 = 다음 장면 그림(예 01 → 02).
   - 같은 장면 안에서 다가가기·훑기: 끝 = **시작 그림을 열어 편집**한 "카메라가 더 다가간/옆으로 간" 그림(이름 `NNe.jpg`, 예 03 → 03e). 편집 문장: `Keep exactly the same place, objects, props and light. Change only the camera: it is now closer to [대상], [대상] fills the middle third of the frame. No letters or numbers anywhere.`
   - 변화가 있는 클립(불이 꺼짐·불이 켜짐·물이 참·낮→밤): 끝 = **결과가 그려진 편집 그림**.
2. **"drone", "FPV", "camera", "aircraft"라는 낱말을 쓰지 않는다.** 대신 "The view flies low and fast …", "The view glides …".
3. **글자가 있을 법한 물건(소화기·제어반·간판·버스)에는 다가가지 않는다.** 꼭 필요하면 그 물건은 화면의 1/4보다 작게 두고, 그림 단계에서 라벨을 빈 흰 사각형으로 편집해 둔다.
4. **카메라 이동은 시작 그림과 끝 그림 사이 거리만큼만.** "keeps flying along the tunnel"처럼 끝 없는 이동을 쓰지 않는다.
5. 동작은 하나, 변화도 하나. 사람 인형 동작은 "steps forward and stops" 정도로 작게.
6. **모델:** 뚫고 들어가기·첫 장면·변화 장면은 **Veo 3.1 정식**, 천천히 밀기는 Lite도 가능.
8. **첫 장면 클립(c01)은 가장 먼저, 정식 모델로, 2개 뽑아 더 나은 것.** 58편 c01은 드론 기체가 나와 앞 2초를 사진으로 대신함 → 첫 2초가 멈춰 보임. 첫 장면에 새 물체·글자가 하나라도 나오면 다른 클립보다 먼저 다시 만든다(최대 3번).
9. **클립 하나가 맡는 장면은 6초 이하로 기획.** 문장 묶음이 6초를 넘으면 클립을 둘로 나눈다(시작·끝 그림 쌍도 둘). 58편 c05·c16은 쓸 구간이 2~4초뿐이라 4~5초 장면에 0.5배로 느리게 깔려 어색했음.
10. **느리게 쓰기 한도 0.8배.** 합성에서 쓸 구간 ÷ 장면 길이가 0.8보다 작으면(더 느려지면) 그 클립은 다시 만들거나, 장면을 둘로 나눠 남는 시간에 다른 클립을 넣는다. 사진으로 메우지 않는다.
7. 끝말(아래)을 모든 클립에 그대로 붙인다:
```
Keep the same realistic miniature world, light and colors as the start and end images, and end exactly on the end image. Keep every object's shape, size and position stable for the whole shot; buildings, pipes, cars and figurines must not morph, mirror, split or change design. The red props stay exactly as in the start image; no new arrows, rings, pins or marks appear. No drone, aircraft, camera device or extra people appear. All labels and signs stay blank; no text, letters or numbers appear on anything. One single continuous move, no cuts, no scene change. Nothing breaks, shatters, explodes or falls apart. Audio: natural ambient sound only, no music, no voice.
```

### 7-2. 클립 종류 (이탄생 실측 카메라)
| 종류 | 시작 → 끝 | 프롬프트 예 |
|---|---|---|
| 첫 장면 통과 | 지도·거리 → 땅속 대상 | "The view flies low and fast along the avenue toward the building with the red pin, dives through the cut-away opening in the street and arrives at [대상], exactly matching the end image." |
| 지명 통과 | 지도 → 사건 장면 | 위와 같은 꼴 |
| 다가가기 | NN → NNe | "The view glides slowly forward toward [대상] and stops close to it, exactly matching the end image." |
| 장면 안 변화 | NN → 결과 편집 그림 | "[변화 하나] happens steadily while the view stays almost still." |
| 위로 솟기(끝) | 땅속 → 하늘에서 본 전체 | "The view rises smoothly straight up out of the tunnel to above the city, exactly matching the end image." |
- 카드 `shorts/produce/NN_clips.txt` ([cNN.mp4] 시작 NN.jpg / 끝 NNe.jpg · 쓰임).

**Aside 지시(클립) 틀**
```
NN편 클립 KK개 만들어 줘(이탄생 판). 계정 하나당 5개까지(A/B/C/D로만 적기).
0. git pull. 프롬프트 shorts/produce/NN_clips.txt (한 글자도 바꾸지 말 것), 그림 shorts/media/NN/in/img/ (끝 그림 NNe.jpg 포함)
1. 동영상 · 프레임 · Veo 3.1(카드에 "정식"이라 적힌 클립은 정식) · 9:16 · x1, 소리 켬, 8초. **모든 클립 시작·끝 두 칸 다.** 넣기 전 그림 번호 확인
2. 다른 계정은 새 프로젝트를 만들고 필요한 그림을 GitHub img에서 받아 올려 씀
3. 1080p. ~/Downloads/숨은설비/NN/clip/cNN.mp4
4. 검수: **8초 전부**를 0.5초 간격으로. 아래면 한 번 다시(최대 2번): 모양 바뀜·거울 겹침·장면 바뀜 / 글자·얼굴 / 새로 생긴 물체(드론·사람·화살표·고리) / 끝이 끝 그림과 다름 / 프롬프트와 반대
5. 클립 하나 끝나면 바로 GitHub shorts/media/NN/in/clip/ 에 올리고 커밋·푸시(모아서 올리지 말 것) + NOTES.md(클립 | 계정 | 모델 | 화질 | 쓸 구간 | 메모). 다 되면 보고
```

## 8. 완성본
- **완성 전 확인(11/4):** 장면표의 클립 배속이 모두 0.8 이상인지, 사진(P)으로 남은 장면이 첫 장면이 아닌지 본다. 0.8 아래거나 첫 장면이 사진이면 해당 클립을 다시 주문하고 그다음에 완성본을 만든다.
- 클립을 0.5초 모아보기로 검수(`ffmpeg -vf "fps=2,scale=180:-1,tile=8x2"`) → 쓸 구간을 정해 SCENES의 해당 P를 `Q("cNN", 시작, 끝, 클립시작초, 클립끝초)`로 바꿈.
- 커버: 인스타 프로필 격자(3:4)에서 안 잘리게 글자는 세로 300~1500px 안. 그림 + "궁금증 문구"(55M "바닥의 이 얼음"). `work/NN/cover.jpg`가 있으면 끝에 1초 붙음.
- `bash template-2tan/finish_2tan.sh NN final` → 길이·소리(−14 LUFS, 최고 −1.5 dB 아래)·컷 수 확인 → 대표이사에게 보냄. 100MB 넘으면 다시 인코딩(GitHub 한도).
- 업로드는 대표이사 "올려" 뒤. 카드 `shorts/upload/NN.md`(TEMPLATE.md), 시험은 인스타 시험용 릴스(웹에 없음 → 앱).

## 9. 주의 (실수 기록)
- **편 번호 겹침**: 57편 만들 때 다른 세션의 56편 음성을 덮어씀(11/2). 시작 전에 번호가 비었는지 확인.
- `pkill`/`pgrep -f`는 자기 셸 명령과도 맞아 자기를 죽이거나 끝없이 기다림 → 쓰지 말고 로그 파일 끝 문구로 기다린다.
- 회사 이름·슬로건 넣지 않기. 남의 대본 전문은 저장소에 올리지 않기. 모델 이름은 저장소에 적지 않기.
- 영상 출력 폴더(out/)는 .gitignore — 올릴 때 `git add -f`.

## 10. 로컬(대표이사 컴퓨터)에서 쓰기
처음 한 번:
```
git clone https://github.com/bmk3037/donginensis-blog.git && cd donginensis-blog && git checkout claude/shorts-daily
brew install ffmpeg node python        # 맥(이미 있으면 건너뜀)
bash shorts/compose/setup.sh           # numpy·Pillow, playwright+크로미움(shorts/compose/node_modules), 프리텐다드 글꼴
```
키는 터미널 환경 변수로만(채팅·파일에 적지 않음):
```
export TYPECAST_API_KEY=…   # 음성
export YOUTUBE_API_KEY=…    # 주제 조사(topic_check.py)
export GEMINI_API_KEY=…     # 영상 분석(gemini_video.py, 선택)
```
매번: `git pull` → 로컬 Claude에게 "shorts/produce/2TAN-MASTER.md 읽고 [주제] 만들어줘". 경로는 모두 저장소 기준 상대 경로라 그대로 돈다.
- 그림·클립은 Aside가 GitHub에 올림 → 로컬에서 `git pull` 후 합성. 렌더는 맥에서 96초 기준 10~20분.
- **윈도우 PC**(11/3 58편에서 확인): `python3`가 스토어 바로가기라 안 돎 → `python`으로, `PYTHONUTF8=1`(안 하면 lines.json 글자가 깨짐). 새로 받은 크로미움은 실행이 막힘 → `export CHROMIUM_PATH="C:/Program Files/Google/Chrome/Application/chrome.exe"`. 바로가기(심볼릭 링크)는 권한 문제로 실패 → `fonts`는 복사(`cp -r ../../fonts .`). 키는 사용자 환경 변수에서 `powershell -c '[Environment]::GetEnvironmentVariable("TYPECAST_API_KEY","User")'`로 읽음.
- 결과 `shorts/media/NN/out/`(git에 안 올라감). Aside가 올려야 하면 `git add -f`.

## 11. 커버(섬네일) 채널 통일 (11/4)
```
python3 shorts/compose/template-2tan/cover_2tan.py NN 그림.jpg "위 작은 줄(장소·대상)" "가운데 노란 큰 줄(훅)" "아래 줄(궁금증)" shorts/compose/work/NN/cover.jpg [x% y% 확대%]
```
- 모든 편 같은 틀: 흰 줄(장소) → **노란 큰 줄(훅, 한 줄)** → 흰 줄(궁금증). 번호 도장은 넣지 않는다(11/4).
- 글자는 인스타 프로필 격자(3:4) 안(세로 300~1500px). 그림은 그 편에서 가장 센 장면(불·물·사람 행동).
- 예: 57 "아파트 지하주차장 천장 / 불나기 전엔 텅 빈 배관 / 차 870대 피해 화재의 이유", 58 "충정로 KT 아현지사 땅 밑 / 소화기 1대뿐이던 통로 / 서울 5개 구 통신이 멈춘 이유".
