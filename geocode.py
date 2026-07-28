# -*- coding: utf-8 -*-
"""주소 -> 좌표 (GSI 국토지리원 주소검색 API). 지역별 bbox로 타당성 검증."""
import json, time, urllib.parse, urllib.request
from candidates import PLACES, HOTEL, AREA_MIN

UA = "OsakaTripMap/1.0 (personal trip planning)"

def gsi(addr):
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch?" + urllib.parse.urlencode({"q": addr})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        js = json.loads(urllib.request.urlopen(req, timeout=40).read().decode())
    except Exception as e:
        return None, f"ERR {e}"
    if not js:
        return None, "NOHIT"
    lon, lat = js[0]["geometry"]["coordinates"]
    return (lat, lon), js[0]["properties"].get("title", "")

SANITY = {  # (lat_min, lat_max, lon_min, lon_max)
    "osaka":  (34.55, 34.82, 135.35, 135.62),
    "kyoto":  (34.85, 35.10, 135.60, 135.85),
    "nara":   (34.60, 34.75, 135.75, 135.90),
    "kobe":   (34.60, 34.83, 134.95, 135.30),
    "himeji": (34.75, 34.90, 134.60, 134.75),
    "uji":    (34.85, 34.95, 135.75, 135.85),
}
def region_of(area):
    if area in ("교토", "교토동부", "아라시야마", "후시미"): return "kyoto"
    if area == "우지":   return "uji"
    if area == "나라":   return "nara"
    if area in ("고베", "고베기타노", "고베베이", "아리마"): return "kobe"
    if area == "히메지": return "himeji"
    return "osaka"

out, bad = [], []
for p in [HOTEL] + PLACES:
    coord, note = gsi(p["addr"])
    lo_a, hi_a, lo_o, hi_o = SANITY[region_of(p.get("area", "미나미"))]
    ok = coord and lo_a <= coord[0] <= hi_a and lo_o <= coord[1] <= hi_o
    if ok:
        q = dict(p)
        q["lat"], q["lng"] = round(coord[0], 6), round(coord[1], 6)
        q["min"] = p.get("min", AREA_MIN.get(p.get("area", "미나미"), 60))
        out.append(q)
        print(f"OK   {p['id']:16s} {coord[0]:.5f},{coord[1]:.5f}  {note[:36]}")
    else:
        bad.append((p["id"], p["addr"], note))
        print(f"FAIL {p['id']:16s} {note}")
    time.sleep(0.35)

print(f"\n=== {len(out)} ok / {len(bad)} failed ===")
for x in bad: print("  FAILED:", x)
json.dump(out, open("places_geo.json", "w"), ensure_ascii=False, indent=1)
