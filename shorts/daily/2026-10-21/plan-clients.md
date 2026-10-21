# 우선 제작: 지금 진행 중인 현장 설비 시리즈 (2026-10-21)

대표이사 지시에 따라, 동인엔시스가 지금 하고 있는 현장의 설비부터 숏츠로 만듭니다. 첫 편들이 올라간 뒤 직원 공지를 보냅니다.

## 지킬 선

- **고객사 이름은 영상·커버·설명란에 넣지 않습니다.** 설비 이야기로만 풀고, 회사 이름도 영상에 넣지 않습니다(설명란에만).
- **진행 중인 일은 실적처럼 말하지 않습니다.** `knowledge/company.md`에 있는 실적만 설명란에 씁니다.
  - company.md에 있는 것: Atlas Copco BOG 압축기, 고려제강 신선기, 밥스트 포장기계, 액화수소충전소, 수소추진선박
  - 아직 없는 것(진행 중): 윌로, 테크로스, KTE, 현대중공업터보기계, 하이에어코리아, 한국해양대 MASTC
- **표현:** "AI가 고장을 예측한다"고 하지 않습니다. "기록하고, 기준을 넘으면 먼저 알린다"로만 씁니다.
- **경쟁사 숫자:** Grundfos의 "세계 전기의 10%가 펌프" 같은 숫자는 "업계 추정"으로 표기합니다.

## 편성과 추천 순서

| 순서 | 편 | 설비 (현장) | 훅 첫 문장 후보 | 상태 |
|---|---|---|---|---|
| 1 | 09 | 액화수소충전소 | 여기 남극 최저 기온보다 160도 더 차가운 연료를 보관하는 충전소가 있습니다. | 대본·프롬프트 완료. 음성·이미지 대기 |
| 2 | 10 | 수소추진선박 | 여기 달리는 동안, 연기 대신 물만 내보내는 배가 있습니다. | 대본·프롬프트 완료. 음성·이미지 대기 |
| 3 | 14 | 공장 압축공기 (Atlas Copco) | 여기, 공장이 만든 바람의 4분의 1이 새어 나가는 관이 있습니다. | 기획 |
| 4 | 15 | 빌딩·소방 펌프 (윌로) | 여기, 세계 전기의 10분의 1을 쓴다는 기계가 있습니다. 바로 펌프입니다. | 기획 |
| 5 | 16 | 포장기계 (밥스트) | 여기, 1초에 상자 14개를 접는 기계가 있습니다. | 기획 |
| 6 | 17 | 선박평형수 처리장치 (테크로스) | 여기, 1년에 바닷물 50억 톤을 싣고 다니는 것이 있습니다. | 기획 |
| 7 | 18 | 신선기 (고려제강) | 여기, 쇠를 당겨서 가늘게 뽑아내는 기계가 있습니다. | 기획(숫자 보강 필요) |
| 8 | 19 | 선박 주배전반 (KTE) | 여기, 배 한 척의 전기를 전부 나눠 주는 상자가 있습니다. | 기획 |
| 9 | 20 | LNG 극저온 펌프 (현대중공업터보기계) | 여기, 영하 160도 액체 속에 잠겨서 도는 모터가 있습니다. | 기획(11편과 겹침 주의) |
| 10 | 21 | 선박 공조 (하이에어코리아) | 여기, 배 전기의 3분의 1을 에어컨이 쓰는 배가 있습니다. | 기획(숫자 보강 필요) |
| 11 | 22 | 한국해양대 MASTC 통합제어 | 조사 중 | 조사 중 |

편 번호 14~22는 임시 번호입니다. 만드는 순서대로 붙입니다.

## 편마다 숫자와 출처

### 14. 공장 압축공기
- "Energy consumption accounts for up to 70% of the lifecycle cost of a compressed air installation." [Atlas Copco](https://www.atlascopco.com/en-uk/compressors/air-compressor-blog/reduce-compressor-operating-costs)
- "sometimes wasting 20-30% of a compressor's output … leak rate equal to 20%" [미국 DOE 팩트시트(2026 개정)](https://www.compressedairchallenge.org/data/sites/1/media/library/factsheets2026/fact-sheet-7-compressed-air-system-leaks_updated2026.pdf)
- 압축공기가 EU 산업 전력의 약 10% (Fraunhofer ISI, 요약만 확인. 대본 전에 원문 확인)
- 뼈대: 압축기가 멈추면 공압 라인 전체가 멈춤 → 돌리기만 하는 제어반은 압축기 모터가 지쳐 가는 걸 말해 주지 않음 → 지능형 제어반이 권선·베어링 온도, 진동, 전류 기록

### 15. 빌딩·소방 펌프
- "It is estimated that ten per cent of the world's electricity consumption is spent on pumps." [Grundfos 2014](https://www.grundfos.com/media/latest-news/annual-result-2013-growth-and-profit-at-grundfos) → "업계 추정"
- 부스터 시스템 하나가 수직 펌프를 최대 8대까지 병렬 운전 [이투데이 2017](https://www.etoday.co.kr/news/view/1509658)
- 04편(아파트 급수 펌프)과 겹치지 않게 소방 펌프·빌딩 부스터로 각을 바꿉니다.

### 16. 포장기계
- "Operating speed up to 700 m/min", "50,000 boxes per hour" [BOBST MASTERFOLD 75|110](https://www.bobst.com/eu/en/products/folding-gluing/masterfold-75-110) → 시속 42km, 1초에 약 14개(계산)
- "speeds up to 9,500 sheets per hour" [BOBST MASTERCUT 145 PER](https://www.bobst.com/usen/products/flatbed-die-cutting/die-cutters/overview/machine/mastercut-145-per)
- 13편(드럼 동기)과 같은 "고속 동기" 계열이므로 이야기는 접기·붙이기 공정 쪽으로 잡습니다.

### 17. 선박평형수 처리장치
- 연간 "an estimated 5 billion tonnes of ballast water", 침입종 피해 "USD 100 billion per year" [IMO·GloBallast 2016](https://archive.iwlearn.net/globallast.imo.org/global-treaty-halt-invasive-aquatic-species-enter-force-2017/index.html)
- BWM 협약 2004년 채택, 2017년 9월 8일 발효 [IMO](https://www.imo.org/en/mediacentre/hottopics/pages/bwm-default.aspx)
- 전기분해 방식. "세계 최대"는 회사 주장이라 쓰지 않습니다.

### 18. 신선기
- 신선: 굵은 철선을 점점 작은 다이스 구멍으로 연속해서 당겨 가늘게 늘리는 공정
- 주의: 타이어코드(0.15~0.40mm)는 머리카락(약 0.085mm)보다 굵습니다. "머리카락보다 가늘다"는 쓰지 않거나 쏘와이어로 한정합니다.
- 속도 숫자는 요약만 확인돼서 대본 전에 원문을 찾습니다.

### 19. 선박 주배전반
- 진동으로 접속부가 풀리고, "one quarter of the switchgear failures is caused by loose joint or hot spot" [ABB 기술자료](https://library.e.abb.com/public/9cec6142465543c0956bccf2033626ff/LE_STM(EN)-_1VCD000641.pdf)
- 주배전반이 꺼지면 배 전체가 블랙아웃
- 모터 설비 자체가 아니라서 "온도·접속부 감시" 쪽으로 뼈대를 바꿉니다.

### 20. LNG 극저온 펌프
- 영하 160℃ 이하에서 LNG 이송, 평택기지에서 7개월 실증, 2025-12-29 국산화 발표 [시사경제 2025](https://sateconomy.co.kr/news/view/1065596978038020)
- 11편(BOG)과 같은 LNG 계열이라 간격을 두고 올립니다.

### 21. 선박 공조
- 여객선 HVAC가 "consume up to a third of total energy demand" [Riviera 2026](https://www.rivieramm.com/news-content-hub/news-content-hub/why-passenger-ships-cannot-afford-to-ignore-this-hidden-power-drain-88782)
- 하이에어코리아는 1988년 설립된 김해의 선박·해양플랜트·군함용 공조기·냉동기·송풍기 회사입니다(요약만 확인).
