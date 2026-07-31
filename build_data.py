# -*- coding: utf-8 -*-
"""이동시간 보정 / 8·1·8·2 영업여부 / 핀 겹침 보정을 적용해 앱 데이터 생성."""
import json, math

d = json.load(open("places_geo.json"))

# 좌표를 이미 확보한 편의점(Overpass 좌표 + GSI reverse geocoder 지명)을 합류
from conv_stores import CONV_STORES
d.extend(CONV_STORES)

# 지역 기본값으로 안 맞는 개별 지점 (닛폰바시역 출발, 편도 도어투도어)
MIN_OVERRIDE = {"kinkakuji": 85, "kiyomizu": 70, "kasuga": 55, "meriken": 52, "kaiyukan": 30}

ROUTE = {
    "미나미": "닛폰바시역에서 도보권", "남센바": "지하철 신사이바시 경유 · 도보 포함",
    "혼마치": "미도스지선 혼마치역", "신세카이": "사카이스지선 닛폰바시→에비스초 3분",
    "텐노지": "타니마치선/미도스지선 텐노지역", "츠루하시": "센니치마에선 닛폰바시→츠루하시 6분",
    "우메다": "미도스지선 난바→우메다 8분", "텐마": "사카이스지선 닛폰바시→오기마치/텐진바시6",
    "나카자키초": "타니마치선 나카자키초역", "후쿠시마": "한신/JR 후쿠시마·노다역",
    "기타신치": "JR 도자이선 기타신치역", "키타하마": "사카이스지선 닛폰바시→키타하마 5분",
    "쿄바시": "JR/케이한 쿄바시역", "오사카성": "타니마치선 타니마치4초메역",
    "나카노시마": "케이한 나카노시마선", "나카츠": "미도스지선 나카츠역",
    "요도가와": "미도스지선 난바→니시나카지마미나미가타 12분",
    "스미요시": "난카이 난바→스미요시타이샤 10분", "스미노에": "요츠바시선",
    "니시나리": "미도스지선 난바→타마데 8분", "베이": "츄오선 오사카코역",
    "USJ": "JR 유메사키선 유니버설시티역", "아와자": "츄오선 아와자역",
    "가라호리": "나가호리츠루미료쿠치선 타니마치6초메역",
    "교토": "난바→우메다→JR 교토역 (또는 한큐 특급)",
    "교토동부": "케이한 기온시조역 하차", "아라시야마": "한큐/JR 사가아라시야마",
    "후시미": "케이한 후시미이나리역", "우지": "JR 나라선 우지역",
    "나라": "킨테츠 닛폰바시→킨테츠나라 급행 약 40분 (환승 없음)",
    "고베": "한신 오사카난바→고베산노미야 쾌속급행 40분 (환승 없음)",
    "고베기타노": "산노미야에서 도보 15분 언덕", "고베베이": "산노미야→포트라이너 10분", "아리마": "산노미야→신코베→기타신치선",
    "히메지": "우메다→JR 신쾌속 히메지 62분",
}

def open_days(closed):
    c = (closed or "").strip()
    if not c or c in ("점포별", "점포별 상이", "점포 확인 필요"): return None, None
    always = ("무휴", "없음", "연중무휴", "연말연시", "1/1", "12/28~1/1", "12/29~30", "부정기")
    sat = sun = True
    if "토" in c and "째 토" not in c: sat = False
    if "일요일" in c and "째 일" not in c: sun = False
    if "일·공휴일" in c: sun = False
    if "토·일" in c: sat = sun = False
    if any(a in c for a in always) and "요일" not in c: sat = sun = True
    return sat, sun

OPEN_OVERRIDE = {  # 규칙으로 안 잡히는 케이스 수동 확정 (8/1=첫째 토, 8/2=첫째 일)
    "zeroku": (True, False), "marimo": (True, True), "sunshine": (True, True),
    "horai": (True, True), "chitose": (True, True), "yakko": (True, True),
    "toraya": (True, True), "arima": (True, True), "nakanoshima": (True, True),
}

# ── 폭염 대응: 실내(in) / 지붕·아케이드(cov) / 실외(out) ──────────────
ENV = {
    # 실외 — 한낮(11~16시)에 오래 있으면 위험
    "glico": "out", "hozenji": "out", "amemura": "out", "nambayasaka": "out",
    "osakajo": "out", "shitennoji": "out", "nakazakicho": "out", "tenmangu": "out",
    "sumiyoshi": "out", "koreatown": "out", "usj": "out", "karahori": "out",
    "fushimi": "out", "kiyomizu": "out", "gion": "out", "arashiyama": "out",
    "kinkakuji": "out", "todaiji": "out", "narapark": "out", "kasuga": "out",
    "naramachi": "out", "kitano": "out", "nankinmachi": "out", "meriken": "out",
    "himeji": "out", "byodoin": "out",
    # 지붕 있는 아케이드 — 한낮에도 걸을 만함 (오사카의 큰 이점)
    "kuromon": "cov", "shinsaibashi": "cov", "denden": "cov",
    "tenjinbashi": "cov", "nishiki": "cov",
    # 냉방 실내 — 한낮 피난처
    "nekorepublic":"in","gurugurudo":"in","nekoeniwa":"in","mipig":"in","harrywood":"in",
    "rockstar":"in","kawauso":"in","reptile":"in","animeal":"in","raptorland":"in",
    "whiterabbit":"in","mameshiba":"in","savecat":"in","nifrel":"in","kobeanimal":"in",
    "harukas": "in", "umedasky": "in", "nakanoshima": "in", "kaiyukan": "in",
    "tsutenkaku": "in", "arima": "in",
    # 마트·편의점·100엔샵 — 전부 실내
    "donki_dotonbori": "in", "tamade_nihonbashi": "in", "daiso_kuromon": "in",
    "daiso_ebisubashi": "in", "lawson_shimanouchi": "in", "famima_shimanouchi": "in",
}
# 실외 줄서기가 긴 집 — 폭염엔 오픈런 아니면 피할 것
QUEUE = {"mizuno", "ichiran", "moeyo", "roshoki", "yaekatsu", "daruma",
         "rikuro", "horai", "chitose", "jinrui", "kiji", "kyuyamutei"}

hotel = [x for x in d if x["cat"] == "hotel"][0]
def dist_km(a, b):
    R = 6371; p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = p2 - p1; dl = math.radians(b[1] - a[1])
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * R * math.asin(math.sqrt(h))

for p in d:
    p["min"] = MIN_OVERRIDE.get(p["id"], p["min"])
    p["route"] = ROUTE.get(p.get("area", ""), "")
    if p["cat"] == "hotel":
        p["sat"], p["sun"], p["km"] = True, True, 0.0
        continue
    p["sat"], p["sun"] = OPEN_OVERRIDE.get(p["id"], open_days(p.get("closed")))
    p["km"] = round(dist_km((hotel["lat"], hotel["lng"]), (p["lat"], p["lng"])), 2)
    p["walk"] = p["km"] <= 1.3
    p["env"] = ENV.get(p["id"], "in")   # 식당·카페는 기본 실내
    if p["id"] in QUEUE: p["queue"] = True
    if p["id"] == "chitose":
        p["warn"] = ("본점은 10:30~14:30 · 화/금 휴무. 문 닫았으면 난바 그랜드 카게츠 1층 "
                     "「千とせ べっかん」이 11:00~20:00 무휴로 같은 니쿠스이를 판다.")

# 좌표가 겹치는 핀 미세 분리 (실제로 옆집인 경우)
seen = {}
for p in d:
    k = (round(p["lat"], 5), round(p["lng"], 5))
    if k in seen:
        seen[k] += 1
        p["lat"] += 0.00016 * (seen[k] - 1); p["lng"] += 0.00019 * (seen[k] - 1)
    else:
        seen[k] = 1

json.dump(d, open("app_data.json", "w"), ensure_ascii=False, separators=(",", ":"))
n = lambda c: sum(1 for x in d if x["cat"] == c)
print(f"관광지 {n('spot')} · 로컬 {n('local')} · 한국인 {n('tourist')} · 총 {len(d)}")
print("도보권(1.3km 내):", sum(1 for x in d if x.get("walk")))
print("8/1(토) 영업:", sum(1 for x in d if x.get("sat")), "/ 8/2(일) 영업:", sum(1 for x in d if x.get("sun")))
print("90분 초과:", [x["id"] for x in d if x["min"] > 90])
