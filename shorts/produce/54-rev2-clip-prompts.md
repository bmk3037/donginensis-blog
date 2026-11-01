# 숨은 설비도감 54편 크린넷 — 영상 제작 최종 프롬프트 Rev.2
작성일: 2026-11-01 / 기준: 사용자가 제공한 18문장 내레이션, 원본 검수 문서, 전체 이미지 시트

## 적용 범위와 사용법
- 기존 c01~c17 번호를 보존한다. 편집 순서는 c01→c02→c03→c04→c05→c06→c07→c08→c09→c10→c11→c12→c13→c14→c16→c17→c15.
- 아래 영어 블록은 공통 지시가 포함된 완전한 프롬프트다. 각 블록 하나만 해당 참조 이미지와 함께 입력한다. 이전 SYSTEM RULE을 덧붙이지 않는다.
- 8초 생성은 원본 제작안의 작업 조건이다. 도구에서 지원하는 길이·화면비·해상도·음향은 실제 화면에서 선택한다. 여기서는 새 영상 생성이나 크레딧 지출을 하지 않았다.
- _clean은 새 파일을 확보했다는 뜻이 아니라, 아래 수정사항을 적용해 준비할 참조 이미지 이름이다. 수정 전 원본으로 생성하면 기존 오류가 남을 수 있다.
- 생성 프롬프트가 구조·문자를 완벽히 고정한다고 보장하지 않는다. 출고 전 검수 기준을 적용한다.
- 기본 17개 편집 구간. c08은 2개 영상 소스, c10·c14는 각각 2개 고정 이미지 또는 정지 클립으로 구성한다. 모든 항목을 영상으로 생성하면 총 20개 소스가 되지만 c10·c14의 4개 소스는 이미지 편집으로 대체하는 것이 권장안이다.
- c10·c14 고정 비교를 이미지 편집으로 처리하면 생성할 영상 소스는 16개다. 영상 생성 128초 분량에서 필요한 부분만 골라 쓴다. 17구간 모두 8초씩 붙이지 않는다.
- 나레이션 타이밍은 실제 녹음에 맞춰 확정한다. 아래 93초는 편집 배분안이며 음성 측정값이 아니다.

## 검수 결과 — 원문의 충돌과 수정
| 원문 문제 | 최종 조치 |
|---|---|
| 모든 장면에 빠른 드론, 전체 8초 이동 | 설명 컷은 고정, 전경은 짧은 이동. 실내·관내 시점을 드론 비행이라고 부르지 않음 |
| 모든 클립에서 밸브만 움직임 vs 투입문·압축기·차량 동작 | 공통 규칙을 외형·축척 보존으로 축약하고 각 컷에서 허용 동작 지정 |
| 지하 관내 풍속인데 지상 모자·나무가 날림 | 지상은 평온하게, 관 속 봉투만 움직임 |
| 관은 형상 고정인데 벽이 닳고 구멍 생성 | c10은 두 고정 이미지 편집 비교, c11은 이미 있는 부식 관찰 |
| c09·c12 숫자판은 6~8초 등장, 다른 문장에서는 4초 내 통과 | 생성 문자 제거. 숫자 등장 시간은 편집에서 한 번만 지정 |
| c07 봉투는 카메라 쪽으로, 카메라는 추격·밝은 출구로 | 고정 관내 시점에서 먼 굴곡 방향으로 단일 이동, 밝은 외부 출구 삭제 |
| 분리·압축·컨테이너 상차를 회전 카메라로 한꺼번에 | c08a 분리와 c08b 압축을 편집으로 연결, 상차 생략 |
| 미가동을 건물 전체 폐허로 변환 | 동일한 온전한 건물의 비가동 상태로 비교 |
| 송도 철거 검토를 크레인 철거로 표현 | 설치 상태를 유지한 현장 점검으로 변경 |
| 정지 시설 엔딩인데 송풍기·기류 소리 | 도로·저녁 환경음만 사용 |
| 지정하지 않은 종료 이미지로 변화하라는 공통 문구 | 실제 종료 이미지를 쓰는 c04 외에는 삭제 |
| 영상 속 문자 보존·변경 요구를 동시에 사용 | 글자·숫자·장면 번호·로고를 참조 이미지에서 먼저 지우고 편집에서 합성 |

## 참조 이미지 선행 수정
가능한 기존 이미지를 편집한다. 새로 그려야 하는 항목도 원본의 색감·축척·장소 배치를 기준으로 한다.

### 모든 이미지 공통 편집 지시
> Preserve the existing architecture, miniature scale, materials, camera angle and lighting. Remove green scene IDs, watermarks or star-shaped overlay marks, all letters, numbers, measurement labels and numeric signboards. Restore the background naturally where an overlay was removed. Do not invent replacement writing. Keep the same white unpainted figurines and model materials.

숫자판은 판과 글자 전체를 제거하고 빈 공간은 편집 합성에 사용한다. 화살표·점선·빨간 X도 생성 영상에서는 제거하고 필요할 때 편집 오버레이로 넣는다.

| 파일 | 추가 수정 |
|---|---|
| s01_clean | 246km판·붉은 흐름 화살표 제거. 관망은 고정, 한 갈래 이송만 보일 위치 확보 |
| s02_clean | 빨간 X 제거. 주민·투입구를 한 화면에 유지 |
| s03_clean | 같은 키 큰 우체통형 투입구, 사각 앞문은 이미 열린 상태. 주민 손의 봉투는 문 바깥에 한 개. 점선 박스 제거 |
| s04_clean | 대기 봉투와 닫힌 배출 밸브가 명확하게 보이도록 정리. 인물은 관 외부 발판에 고정. 화살표 제거 |
| e04_clean | s04_clean을 직접 편집. 카메라·밸브 하우징·관·인물·발판 고정, 밸브 요소만 열린 위치, 배출된 봉투는 관 입구 아래쪽. 관벽을 관통하지 않는 경로. 화면에 안 보이는 작동기구는 새로 발명하지 않음 |
| s05_clean | 덕트 화살표 제거. 케이싱은 불투명 고정. 존재하지 않는 회전 날개를 노출하지 않음 |
| s06_clean | 모자는 머리에, 나무는 정상. 지상 강풍 표현 제거. 관은 지하 단면 안에만 위치. 붉은 속도선·숫자판 제거 |
| s07_clean | 관 속 인물·난간·발판·전선처럼 보이는 붉은 선·터널등 제거. 봉투는 먼 방향으로 향하는 배치. 관내 질감만 유지 |
| s08a_clean | s08에서 분리기 구간을 같은 시설로 파생. 설명용 단면에 유입관·상부 공기 출구·하부 쓰레기 출구를 명확히 지정. 실제 배치 검증 전에는 원리 모형으로 표시 |
| s08b_clean | 같은 시설의 압축기 측면 단면. 동일 컨테이너, 수평 램과 가이드가 명확히 보이게. 램은 시작 위치. 트럭 고정 |
| s09_clean | 숫자판 제거. 지도가 지리적으로 틀리면 검증된 한국 지도 기반 편집 그래픽으로 대체. 핀 위치는 근거가 있는 위치만 편집에서 합성 |
| s10_clean·e10_clean | 구도·배관 외경·지지대·인물·조명 동일, 숫자·치수선 제거. e10은 내부 벽의 국부적 얇아짐·부식 상태만 비교. 원본처럼 외경·전체 엘보까지 바뀌면 다시 편집. 과장된 관통 구멍 제거 |
| s11_clean | 관 속 사람 제거, 점검 로봇만. 부식·찌꺼기는 이미 존재하는 상태. 활성 이송 장면과 분리 |
| s12_clean | 숫자판·서류 문자 제거. 동전 수량·높이 고정 |
| s13_clean | 동일 우체통형 투입구를 고정된 방수포로 덮은 상징 장면. 금액판 제거. 근거 없는 폐허·거미줄 과장 제거 |
| s14_clean | 2014표지·행사 군중·리본 제거. 준공된 온전한 비가동 건물 |
| e14_clean | s14_clean과 동일 구도·동일 건물, 같은 낮 조명으로 고정. 운영 활동 없음, 약한 표면 때만. 무너짐·파괴·폐허·과도한 잡초 제거 |
| s16_clean | 크레인·뽑힌 투입구·적재 트럭·빨간 X·굴착 제거. 온전히 설치된 투입구와 현장 점검자 둘. 실제 철거가 아닌 검토 장면 |
| s17_clean | 도로 위 차량과 지하 정지 봉투만 남기고 기류·화살표 제거 |
| s15_clean | 글자·흐름·경고 깜빡임 제거. 조용한 엔딩 전경 |

## 내레이션 연결 및 사실 표현
사용자가 제공한 18문장 순서를 유지한다. 문장 6의 ‘지붕 기와’는 비유이며 지상 강풍으로 묘사하지 않는다.
녹음 전 교체 권장 문장:
- 6: “관 속 공기 속도는 초속 이십에서 삼십 미터. 이 바람이 봉투를 집하장으로 옮깁니다.”
- 11: 단정적 원인이 출처에서 확인되지 않으면 “음식물 찌꺼기와 염분에 노출된 관은, 오랜 사용으로 부식과 마모를 겪었습니다.”
- 15: 지역·시설 범위를 확인한 다음 “송도 일부 구역은, 시설을 단계적으로 폐쇄하는 방안까지 검토하고 있어요.” 원문의 ‘송도’가 도시 전체로 읽히지 않도록 범위 확인.
- 16: 전국 전체 비가동으로 오해하지 않도록 “하지만 일부 지역에선, 그 꿈이 아직 땅속에 멈춰 있습니다.”

자료 확인 범위:
- 246km는 세종 관망 총연장으로 보도 확인. 단일 봉투의 이동거리로 표현하지 않는다.
- 영종은 2026-09-26 보도에서 2014년 준공, 1,530억원, 장기 미가동을 확인. 영상에서는 ‘약 1,500억원’을 사용할 수 있으나 게시 기준일 이후 운영상태 변경은 따로 확인할 항목이다.
- 20~30m/s, 약 2km, 전국 약 30곳·2조원, 20.9→1.94mm, 14년, 운영비 100억원대는 이번 확인에서 근거 원문을 확보하지 못했다. 원문 수치를 검증 완료로 간주하지 않으며 화면 합성 항목으로만 예약한다.
- ‘1.94mm’는 관 전체 균일 두께나 모든 시설 상태처럼 표현하지 않고 특정 측정부위의 사례로 제한한다.
- 송도 폐쇄 검토는 기존 자료와 최근 검색 단서가 있으나 이번에 원문 확인을 완료하지 못했다. 크레인 철거 장면은 근거가 없고 ‘검토’라는 대사와도 맞지 않아 제외한다.
- 모형 공정은 특정 도시의 설비 배치나 실제 운전 기록이 아니다. 관련 장면에 작게 ‘원리 모형’, ‘개념 재현’을 편집 표기한다.

참고 링크:
- https://www.fnnews.com/news/202504231559419400 (2025-04-23, 세종 246km·집하장 8곳·투입구 4,700개)
- https://m1.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02109046645584056 (2026-09-26, 영종 1,530억원·2014 준공·미가동)

## 93초 편집 배분안
c08a+b, c10a+b, c14a+b를 각각 하나의 편집 구간으로 묶는다. 아래 시간은 생성 소스의 실제 동작 완성 여부와 녹음 길이에 맞게 조정한다. 압축 행정처럼 동작이 더 길면 완결된 소스 구간을 골라 사용하며 기계 동작을 역재생하지 않는다.

| 순서 | 소스 | 대사 | 편집 길이 | 누적 시간 |
|---|---|---|---:|---|
| 1 | c01 | 문장 1 · 세종 관로 전경 | 4.5초 | 0.0–4.5초 |
| 2 | c02 | 문장 2 · 지하 이송으로 배출 | 3.8초 | 4.5–8.3초 |
| 3 | c03 | 문장 3 · 투입구 소개 | 3.5초 | 8.3–11.8초 |
| 4 | c04 | 문장 4 · 저장 후 배출 | 6.5초 | 11.8–18.3초 |
| 5 | c05 | 문장 5 · 송풍기 운전 | 4.5초 | 18.3–22.8초 |
| 6 | c06 | 문장 6 · 관내 고속 기류 | 5.5초 | 22.8–28.3초 |
| 7 | c07 | 문장 7 · 집하장 방향 이송 | 5.8초 | 28.3–34.1초 |
| 8 | c08a | 문장 8 전반 · 공기와 쓰레기 분리 | 3.0초 | 34.1–37.1초 |
| 9 | c08b | 문장 8 후반 · 압축·컨테이너 | 3.8초 | 37.1–40.9초 |
| 10 | c09 | 문장 9 · 전국 규모 | 5.5초 | 40.9–46.4초 |
| 11 | c10a | 문장 10 전반 · 두께 비교 시작 | 3.0초 | 46.4–49.4초 |
| 12 | c10b | 문장 10 후반 · 얇아진 부위 비교 | 3.5초 | 49.4–52.9초 |
| 13 | c11 | 문장 11 · 부식 상태 점검 | 5.5초 | 52.9–58.4초 |
| 14 | c12 | 문장 12 · 운영비 | 4.5초 | 58.4–62.9초 |
| 15 | c13 | 문장 13 · 영종 시설 | 4.8초 | 62.9–67.7초 |
| 16 | c14a | 문장 14 전반 · 준공 시점 | 3.0초 | 67.7–70.7초 |
| 17 | c14b | 문장 14 후반 · 장기 미가동 | 3.5초 | 70.7–74.2초 |
| 18 | c16 | 문장 15 · 송도 폐쇄 검토 | 4.8초 | 74.2–79.0초 |
| 19 | c17 | 문장 16 · 멈춘 설비의 상징 | 4.8초 | 79.0–83.8초 |
| 20 | c15 | 문장 17·18 · 공유 및 엔딩 | 9.2초 | 83.8–93.0초 |

## 장면별 완성 프롬프트

### c01 — 문장 1 · 세종 관로 전경
- 참조: s01_clean
- 편집 배분: 4.5초. 관망은 실제 배치 재현이 아닌 개념도. 246km는 총 관로 길이로 표기.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes one short, smooth forward move, less than ten percent of the starting framing, toward the already visible underground cutaway. From the first second, one visible bag travels along one existing exposed pipe branch toward the collection side; keep its direction unchanged. Other branches remain static. Buildings, soil layers and buried pipes stay fixed. Never dive through the ground or reveal new pipe branches. Pipes remain below the street; the cutaway is a model display, not an open trench. Audio: quiet street ambience and a restrained enclosed airflow sound.
```

### c02 — 문장 2 · 지하 이송으로 배출
- 참조: s02_clean
- 편집 배분: 3.8초. 아파트에서 집하장까지의 구간을 설명한다. 이후 컨테이너 운반 트럭과 모순되지 않게 쓰레기차 전면 폐지로 표현하지 않는다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a short lateral slide parallel to the sidewalk. One resident takes two small steps toward the existing waste inlet while carrying one bag. The parked garbage truck stays parked and unchanged. The inlet remains visible throughout; do not invent a second inlet behind the camera. All other figurines remain still. No opening doors and no underground action in this shot. Audio: soft footsteps and quiet residential ambience.
```

### c03 — 문장 3 · 투입구 소개
- 참조: s03_clean
- 편집 배분: 3.5초. 이미 열린 사각 투입문과 봉투 투입 한 동작만 사용. 문 열기·투입·닫기 3동작을 요구하지 않는다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked camera at the supplied three-quarter close view. The inlet door is already open in the reference and stays open. During the first three seconds, the resident slowly moves one hand and the single bag through the existing opening, then releases the bag so it disappears inside the inlet. The arm withdraws slightly and rests. Only the bag and that arm move. Preserve the exact mailbox-shaped inlet and the original door hinge. Do not create a lid, duplicate the bag or show the underground chamber. Audio: one soft bag rustle and a muted contact sound.
```

### c04 — 문장 4 · 저장 후 배출
- 참조: s04_clean → e04_clean
- 편집 배분: 6.5초. 카메라 완전 고정. 시작·종료 이미지의 관·인물·발판 위치와 밸브 형상이 일치해야 한다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked camera matching both supplied keyframes exactly. 0–2 seconds: the bags remain above the closed discharge valve. 2–3 seconds: only the valve element visible in the approved keyframes moves to its open position. 3–5 seconds: the lowest two bags descend through that opening into the connected transport pipe, following the path shown by the end reference. 5–8 seconds: hold the end state. Technician, pipe shell, supports and chamber stay still. Bags never cross a solid wall. Do not add an imagined valve mechanism or move the camera. Audio: one restrained valve sound and short bag rustles.
```

### c05 — 문장 5 · 송풍기 운전
- 참조: s05_clean
- 편집 배분: 4.5초. 케이싱을 회전시키거나 불투명 덕트를 투명하게 만들지 않는다. 버튼을 누르는 동작은 생략.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a gentle short slide across the existing blower row. All blower housings, ducts and guards remain stationary and opaque. If an exposed shaft coupling is clearly visible in the reference, rotate only that coupling smoothly; otherwise keep the machine visually static. One existing small status light illuminates softly in the first second, then stays steady. The engineer remains in place. Airflow stays enclosed inside the connected ducts; no dust cloud is sucked from the room. Audio: a steady low industrial blower hum, no start-up surge, no button click.
```

### c06 — 문장 6 · 관내 고속 기류
- 참조: s06_clean
- 편집 배분: 5.5초. 지상은 평온하게. 속도는 관내에만 표현. 실제 속도 계측 재현 영상이 아닌 원리 모형.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked side cutaway view with the sidewalk above and the buried transport pipe below. One small group of bags moves briskly from the inlet side to the collection side inside the visible pipe; preserve that single direction throughout. Use light motion blur only on the moving bags. Keep the pipe rim and soil sharp. The surface trees, people's hats and street objects remain still. Nothing blows out of the model cutaway; it is a viewing section, not a physical leak. Do not add red cables, speed lines or dust outdoors. Audio: a short enclosed air rush with quiet street ambience.
```

### c07 — 문장 7 · 집하장 방향 이송
- 참조: s07_clean
- 편집 배분: 5.8초. 내부 터널이 아니라 소구경 관의 설명용 내부 시점. 실제 배치·실제 이송거리의 영상 재현이 아님.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked virtual camera inside the miniature pipe. Existing bags travel from the near foreground away from the camera toward the dark distant bend, continuously in one direction. Keep each bag's shape identifiable with restrained motion blur. The circular pipe stays rigid. No people, walkway, railings, tunnel lamps, cables or bright exit to a street. Do not reveal the collection plant or create a new building at the far end. Audio: enclosed rushing air. All waste motion is away from the camera; no bag reverses or passes toward the lens.
```

### c08a — 문장 8 전반 · 공기와 쓰레기 분리
- 참조: s08a_clean
- 편집 배분: 3.0초. 기존 s08을 편집한 분리기 단면. 흡입관→분리기→하부 배출 경로를 참조 이미지에 먼저 확정.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked explanatory cutaway view of the approved separator. A small batch of bags enters only through the existing inlet duct, curves downward within the separator and drops toward the already visible bottom discharge. The fixed separator shell and upper air outlet stay rigid. Waste never enters the upper air outlet. Show only this separation action; the downstream compactor and truck remain still. No rotating shell, magical suction funnel or new duct. Audio: steady enclosed airflow and a light material landing sound.
```

### c08b — 문장 8 후반 · 압축·컨테이너
- 참조: s08b_clean
- 편집 배분: 3.8초. s08과 같은 시설에서 파생한 압축기 측면 단면. 램·가이드·컨테이너를 명확히 보여준다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked side cutaway camera. The approved compactor ram makes one slow straight stroke along its existing guide toward the connected stationary container, pushing the visible waste into that container. The ram starts moving in the first second and completes the stroke by five seconds, then holds. Compaction happens only where the ram contacts the waste. The frame, separator, container and truck remain stationary. Do not fill the container spontaneously or hook it to the truck. No people enter the machine. Audio: one restrained hydraulic compression sound.
```

### c09 — 문장 9 · 전국 규모
- 참조: s09_clean
- 편집 배분: 5.5초. 정확한 지도와 위치 핀은 편집에서 작성. 현재 생성 지도는 정확한 지리자료로 간주하지 않는다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a shallow forward move across the supplied physical terrain model without rotating or changing its outline. The terrain, coastline and all existing fixed props stay completely unchanged. No pins grow, appear, multiply or move. Keep the central region in focus and preserve the composition throughout the shot. This is a scale model presentation shot, not a new map reveal. Audio: quiet neutral ambience only, no blower or pipe sounds.
```

### c10a — 문장 10 전반 · 두께 비교 시작
- 참조: s10_clean
- 편집 배분: 3.0초. e10으로 생성 전환하지 않는다. 두 장을 별도로 만든 뒤 같은 구도에서 편집으로 비교.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked close-up matching the source frame. The pipe wall, measuring tool, inspector and all supports remain completely still for the entire shot. Preserve the exact visible cross-section and its thickness. No corrosion growth, thinning, melting, cracking or new hole. No camera motion or focus shift. This is a static inspection comparison plate. Audio: quiet maintenance-room ambience only.
```

### c10b — 문장 10 후반 · 얇아진 부위 비교
- 참조: e10_clean
- 편집 배분: 3.5초. 수치가 확인되면 20.9mm→1.94mm를 편집 오버레이. 실제 사진이 아닌 개념 비교 표기.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked close-up matching the source frame. Keep the already corroded cross-section, measuring tool, inspector and supports perfectly still. Do not increase the existing damage, grow a hole, collapse the pipe or animate the wall. No camera motion or focus shift. This is the second static inspection comparison plate, with the same framing as the earlier plate. Audio: quiet maintenance-room ambience only.
```

### c11 — 문장 11 · 부식 상태 점검
- 참조: s11_clean
- 편집 배분: 5.5초. 즉석 부식·천공 대신 이미 존재하는 흔적을 관찰. 로봇은 설명용 모형.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked low camera inside the offline inspection pipe. Only the small inspection robot moves slowly forward by roughly one body length during the first four seconds. Its attached headlight moves with it and reveals the already existing corrosion and residue. The rust, residue, wet surface and existing wall damage do not spread, dissolve or change. No active waste transport and no people. The pipe remains rigid and enclosed. Audio: a soft wheel motor and quiet enclosed-room tone, no blower or rushing air.
```

### c12 — 문장 12 · 운영비
- 참조: s12_clean
- 편집 배분: 4.5초. 연 100억 원대라는 표현과 특정 연도 수치의 차이를 유지. 동전이 무한히 증가하지 않는다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes one short, slow slide along the existing meeting table, keeping the coin stacks in focus. The coin stacks keep the same count, height and position. One seated figurine makes a small downward head movement toward the existing blank paper; all other figures remain still. Papers stay blank and do not flip. No growing money pile or new sign. Audio: quiet indoor room tone and a faint chair movement.
```

### c13 — 문장 13 · 영종 시설
- 참조: s13_clean
- 편집 배분: 4.8초. 근거가 없는 거미줄·잡초·추가 폐허화는 제거. 방수포는 상징 표현임을 편집에 명시.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a short lateral slide along the existing covered waste inlets on the seaside sidewalk. The secured covers keep their shape and position, with only a barely noticeable edge flutter. The figurine remains beside the inlet without pulling the cover away. Buildings, pavement and inlet bodies stay unchanged. No revealing an invented machine, airborne dust cloud, new cobwebs or growing weeds. Audio: soft seaside street ambience, no machinery.
```

### c14a — 문장 14 전반 · 준공 시점
- 참조: s14_clean
- 편집 배분: 3.0초. 개소식 군중·리본·운전 조명 제거. 준공을 실제 정상 가동 행사로 보여주지 않는다.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked elevated camera of the completed collection plant in the approved reference. Preserve the clean completed building, road and equipment exactly. All machinery stays inactive. No cheering crowd, ribbon ceremony, new flags, moving waste or operating lights. No time-lapse and no building decay. Only a very slight movement of existing tree leaves. Audio: quiet outdoor ambience.
```

### c14b — 문장 14 후반 · 장기 미가동
- 참조: e14_clean
- 편집 배분: 3.5초. 동일 구도·동일 건물. 폐허가 아닌 조용한 비가동 상태. 2014→2026·12년은 편집 표기.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked elevated camera matching the approved end reference and the earlier plant view. The completed building remains intact and inactive, with the same roofline, equipment positions and surrounding streets. No crowd appears, no machine starts and no waste moves. Keep existing surface wear subtle and unchanged. No rapid decay, collapse, boarded ruins or spreading vegetation. Audio: quiet outdoor ambience with no blower hum.
```

### c16 — 문장 15 · 송도 폐쇄 검토
- 참조: s16_clean
- 편집 배분: 4.8초. 크레인·뽑힌 투입구·굴착·빨간 X 제거. 실제 철거 완료로 읽히는 장면 금지.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a slow short lateral slide along the intact existing waste inlets in the Songdo-style seaside street. Two small white maintenance figurines stand outside the equipment, one holding a blank clipboard and making one small pointing gesture toward an inlet. Inlets remain firmly installed and unchanged; the pavement is intact. No crane, lifting, demolition, excavation, removal truck or red X. Audio: quiet urban seaside ambience. The scene shows inspection and consideration, not a decided closure.
```

### c17 — 문장 16 · 멈춘 설비의 상징
- 참조: s17_clean
- 편집 배분: 4.8초. 특정 비가동 구간의 개념 표현. 세종·송도·전국 전체가 정지했다는 화면 문구 금지.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Locked cross-section camera. Above ground, the existing small garbage truck moves slowly along its visible lane for the first five seconds. Below ground, the pipe, the single bag and the collection equipment remain completely still and dark. The truck never intersects the cutaway edge or creates a new road. Keep remaining figurines still. No glowing flow, moving arrows, airflow effects or pipe motion. Audio: a distant truck engine passing with quiet evening ambience; no underground machinery sound.
```

### c15 — 문장 17·18 · 공유 및 엔딩
- 참조: s15_clean
- 편집 배분: 9.2초. 8초 클립을 무리하게 늘리지 않고 엔딩 정지화면 추가. 음성 9.2초는 원문 기준 계획값.

```text
8-second vertical 9:16 image-to-video shot. Match the supplied reference: finely crafted architectural miniature, realistic model materials, plain white unpainted figurines, stable colors and lighting. Preserve the reference composition, scale and solid geometry. Animate only the stated action. No new objects, text, numbers, logos or speech; no music. Keep the main subject sharp with gentle background blur. Camera makes a slow, small pullback within the existing aerial composition, revealing no new streets or pipe branches. The model remains coherent and still. Existing city lights maintain their brightness; do not invent lights in the underground pipes. One or two already visible surface figurines may take a small step only. End on a steady composition for the last two seconds. No warning flash, waste movement, sign or scene transformation. Audio: soft evening city ambience only, no blower or rushing air.
```

## 문자·기호 합성 지시
- 원본의 빨간 포인트는 유지하되, 글자는 후반 편집에서 별도 레이어로 처리한다. 위치 추적이 어렵다면 장면에 붙어 움직이는 3D 글자 대신 고정 자막을 사용한다.
- c01: ‘세종 지하 관로 총연장 246km’. 첫 0.5초 안에 제시하고 대사 종료까지 유지.
- c02: 필요하면 쓰레기차에 작은 X를 편집 합성. ‘단지→집하장 구간’ 맥락을 유지.
- c03: 투입구 외곽선은 짧게 한 번 강조.
- c05~c08: 진행 방향 표시를 사용할 때만 얇은 붉은 화살표 한 개. c07의 소실점 방향과 맞출 것.
- c06: 수치 근거 확인 후 ‘관내 공기 속도 20~30m/s’. 단위 m가 아니라 m/s. 지상 풍속처럼 표현하지 않음.
- c07: 거리 출처 확인 후 ‘이송거리 약 2km · 시설별 상이’.
- c09: 지역 수·총사업비 출처와 기준연도를 확인해 표기. 지도 핀은 실제 위치를 검증한 항목만.
- c10: 같은 위치에서 ‘초기 두께 20.9mm’→‘측정부위 1.94mm’로 편집 교체. 출처·측정시점 확인 필수. 두 고정 이미지는 0.2초 내외 디졸브 또는 동일 위치 컷 전환으로 비교. 실제 부식 진행을 촬영한 것처럼 연출하지 않음.
- c12: ‘연간 운영비 100억원대’는 확인한 연도·회계범위와 함께. ‘매년 정확히 100억원’으로 바꾸지 않음.
- c13: ‘영종 · 약 1,500억원’, 보도일 2026-09-26. 필요하면 실제 1,530억원을 사용하되 음성과 맞출 것.
- c14: 두 이미지 동일 위치에 ‘2014 준공’→‘2026 · 장기 미가동’ 편집. 소스에 과장된 폐허 이미지 사용 금지.
- c16: 지역 범위와 자료 기준일 확인 후 ‘일부 구역 · 단계적 폐쇄 검토’. 결정·완료로 표기하지 않음.
- c17: ‘일부 미가동 시설 개념 재현’.
- c15: 마지막 1.2초는 끝 프레임을 유지해 CTA와 채널명 배치. UI에 가리는지 실제 세로 미리보기로 확인.

## 연결과 음향
- c01~c08: 단지→투입구→지하 저장→송풍기→이송→집하장. 서로 다른 공간을 생성형 연속 줌으로 이어 붙이지 않고 컷 전환한다.
- c06의 횡방향 이송에서 c07의 깊이방향 시점으로는 컷을 사용한다. 한 숏 안에서 방향 반전으로 만들지 않는다.
- c08a→c08b: 쓰레기가 하부로 내려가는 동작 뒤 압축기로 컷. 장비 형상과 재질은 같은 시설이어야 한다.
- c09~c14: 통계·상태 비교 구간. 공간 이동 효과를 과하게 쓰지 않고 숫자가 읽힐 시간을 확보한다.
- c16은 검토, c17은 일부 비가동의 상징, c15는 채널 엔딩이다.
- 내레이션은 별도 음원. 생성 음향은 필요 부분만 골라 낮춘다. 송풍기음은 운전 설명 구간에만, 회의실·미가동 시설·엔딩에는 넣지 않는다.
- 장면마다 효과음을 처음부터 다시 크게 터뜨리지 않는다. c05~c08은 필요한 경우 낮은 기류음을 편집에서 연결하고, c09에서 끊는다.
- c15 9.2초는 원문의 예상 대사 길이에 대응한 배분이다. 실제 녹음이 다르면 엔딩 정지시간을 조정한다.

## 생성 결과 승인 기준
1. 관·건물·밸브 하우징·장비가 휘거나 새로 생기지 않는가.
2. 허용 동작 이외 부분이 움직이거나 복제되지 않는가.
3. 쓰레기가 관벽을 뚫거나 역주행하지 않는가.
4. 관 내부에 사람·보행 통로가 생기지 않는가.
5. 지하 이송이 지상 강풍·열린 도로 관구로 바뀌지 않는가.
6. 문자·숫자·가짜 브랜드가 생기지 않는가.
7. c10·c14 비교 이미지가 동일 구도이며 건물·관 외경까지 달라지지 않는가.
8. c16에 실제 철거, c17·c15에 기류·송풍기 운전이 생기지 않는가.
9. 영상만 보아도 내레이션보다 더 강한 사실을 단정하지 않는가.
10. 실제 녹음 기준으로 맞췄고, 문장 중간에서 대응 장면이 끝나지 않는가.

재생성은 ‘아주 자연스럽게’라는 문구를 덧붙이기보다 실패한 동작 하나를 줄이고 참조 이미지를 먼저 수정한다. 고정 구도로 바꿔도 안 되면 원본 이미지의 편집 확대·이동으로 대체한다.

