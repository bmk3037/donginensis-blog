# 편집 레시피 백업 (10/31)

컨테이너가 꺼지면 `work/` 안의 작업 파일이 사라져서, 편마다 **작은 텍스트 파일만** 여기에 `git add -f`로 보관한다(영상·프레임·음성 같은 큰 파일은 제외, 합계 약 3MB).

- `NN/scene_*.html` 합성 장면, `NN/scenes.json` 컷 목록, `NN/force.json` 문장 경계, `NN/lines.json` 대본 줄, `NN/sfx.py` 효과음, `NN/make60.sh` 정렬, `NN/thumb.html` 커버
- 다시 합성할 때: 이 폴더를 `shorts/compose/work/NN`에 두고, 클립·음성은 `shorts/media/NN/in/`에서 받아 `clipn/`로 프레임을 뽑는다(shorts-compose 스킬).
- 새 편을 합성한 뒤에는 같은 방식으로 레시피 파일을 올린다.
