# 오사카 3박4일 지도

숙소(오사카 주오구 시마노우치, 닛폰바시역 도보 5분) 기준 **편도 90분 이내**의
관광지 37곳 · 로컬 맛집 52곳 · 한국인 관광객 맛집 12곳을 담은 단일 HTML 지도 앱.

👉 https://jinpop.github.io/osaka-trip-map/

## 특징
- 외부 요청 없이 동작 — OSM 타일을 WebP로 압축해 파일에 내장(94장). 비행기 모드에서도 지도가 보임
- 필터: 카테고리 / 이동시간(≤15·30·60·90분) / 8·1(토)·8·2(일) 영업 여부 / 검색 / 즐겨찾기
- 좌표는 전 지점 일본 국토지리원(GSI) 주소검색 API로 조회
- 지도 © OpenStreetMap 기여자 (ODbL)

## 다시 빌드하려면
```
python3 geocode.py     # candidates.py 주소 -> 좌표
python3 build_data.py  # 이동시간·휴무·도보권 계산
python3 tiles.py       # OSM 타일 내려받아 압축 (Pillow 필요)
python3 build_html.py  # index.html 생성
```
장소를 추가하려면 `candidates.py`의 `PLACES`에 항목을 넣고 위를 다시 돌리면 됩니다.
