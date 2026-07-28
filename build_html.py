# -*- coding: utf-8 -*-
import json
from plan_data import PLAN

tpl = open("template.html", encoding="utf-8").read()
out = (tpl.replace("__TILES__", open("tiles.json", encoding="utf-8").read())
          .replace("__DATA__", open("app_data.json", encoding="utf-8").read())
          .replace("__PLAN__", json.dumps(PLAN, ensure_ascii=False)))
open("osaka-map.html", "w", encoding="utf-8").write(out)
open("index.html", "w", encoding="utf-8").write(out)
print(f"osaka-map.html  {len(out.encode())/1024/1024:.2f} MB")
