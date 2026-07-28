# -*- coding: utf-8 -*-
"""OSM 타일을 받아 톤다운 + WebP 압축, base64 data URI 딕셔너리로 저장.
   개인 여행용 소량(~95장). 저작권 표기: (c) OpenStreetMap contributors (ODbL)."""
import math, os, time, json, base64, io, urllib.request
from PIL import Image, ImageEnhance

UA = "OsakaTripMap/1.0 (personal one-off trip map)"

def deg2num(lat, lon, z):
    n = 2 ** z
    return (int((lon + 180) / 360 * n),
            int((1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n))

LAYERS = [
    (10, 34.50, 35.15, 134.55, 136.10),      # 간사이 광역 (히메지·아리마까지)
    (13, 34.60, 34.75, 135.42, 135.56),      # 오사카 메트로
    (13, 34.95, 35.02, 135.74, 135.80),      # 교토 관광 중심
    (13, 34.67, 34.70, 135.81, 135.85),      # 나라 공원 일대
    (13, 34.68, 34.71, 135.17, 135.21),      # 고베 산노미야~모토마치
    (14, 34.640, 34.720, 135.460, 135.535),  # 오사카 중심축
    (15, 34.654, 34.686, 135.490, 135.520),  # 미나미 도보권 (숙소 중심)
]

want = set()
for z, la1, la2, lo1, lo2 in LAYERS:
    x1, y2 = deg2num(la1, lo1, z)
    x2, y1 = deg2num(la2, lo2, z)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            want.add((z, x, y))
want = sorted(want)
print("tiles to fetch:", len(want))

os.makedirs("tilecache", exist_ok=True)
out, total = {}, 0
for i, (z, x, y) in enumerate(want):
    cache = f"tilecache/{z}_{x}_{y}.png"
    if not os.path.exists(cache):
        req = urllib.request.Request(f"https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                     headers={"User-Agent": UA})
        try:
            open(cache, "wb").write(urllib.request.urlopen(req, timeout=30).read())
        except Exception as e:
            print("  skip", z, x, y, e); continue
        time.sleep(0.25)
    im = Image.open(cache).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.32)       # 채도를 낮춰 핀이 도드라지게
    im = ImageEnhance.Brightness(im).enhance(1.08)
    buf = io.BytesIO(); im.save(buf, "WEBP", quality=32, method=6)
    b = buf.getvalue(); total += len(b)
    out[f"{z}/{x}/{y}"] = base64.b64encode(b).decode()
    if i % 20 == 0: print(f"  {i}/{len(want)}  cum={total/1024:.0f}KB")

json.dump(out, open("tiles.json", "w"))
print(f"DONE {len(out)} tiles, webp {total/1024:.0f}KB, base64 {total*4/3/1024:.0f}KB")
