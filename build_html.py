# -*- coding: utf-8 -*-
import json

PLAN = r"""
<div class="callout"><b>이 일정의 전제</b> 7/31(금) 18:00 KIX 도착 → 8/3(월) 오전 출국.
실제로 움직일 수 있는 시간은 <b>첫날 밤 3시간 + 8/1 하루 + 8/2 하루 + 마지막 날 아침</b>입니다.
그래서 근교는 한 곳만 넣었습니다. 항목을 누르면 지도로 이동합니다.</div>

<div class="day">
  <h3>D0 · 도착</h3><div class="when">7/31 (금) · 이동 반경 도보 1km</div>
  <div class="step key"><span class="tm">18:00</span><i class="kn"></i><div class="txt"><b>간사이공항 도착</b>
    <div class="note">입국심사 + 수하물까지 보통 40~60분. 도착층에서 난카이 간사이쿠코역까지 도보 5분.</div></div></div>
  <div class="step"><span class="tm">19:20</span><i class="kn"></i><div class="txt"><b>난카이선 난바행</b>
    <div class="note">공항급행 45분 ¥970 / 라피트 39분 ¥1,490. 이 시간대는 급행으로 충분합니다.
    ICOCA를 공항에서 사두면 이후 이틀이 편합니다.</div></div></div>
  <div class="step key"><span class="tm">20:20</span><i class="kn"></i><div class="txt"><b>숙소 체크인</b>
    <div class="note">난카이 난바역에서 도보 10분. 짐만 두고 바로 나와도 됩니다 — 아래는 전부 도보권입니다.</div></div></div>
  <div class="step key"><span class="tm">20:45</span><i class="kn"></i><div class="txt"><b>첫 저녁 · 우라난바</b>
    <div class="note">숙소 도보 5분. 관광객 동선 바로 뒤인데 손님은 거의 현지인입니다.
    <span class="go" data-go="kujira">쿠지라 · 무휴 · 24시까지</span> ·
    <span class="go" data-go="yakiton">야키톤 센터</span> ·
    <span class="go" data-go="tayutayu">타유타유</span></div></div></div>
  <div class="step"><span class="tm">22:15</span><i class="kn"></i><div class="txt"><b>도톤보리 야경</b>
    <div class="note">도보 10분. 밤에 간판 조명이 다 켜져서 낮보다 낫습니다.
    <span class="go" data-go="glico">글리코 간판</span> ·
    <span class="go" data-go="hozenji">호젠지 요코초</span> (한 블록 안인데 갑자기 조용해집니다)</div></div></div>
  <div class="step"><span class="tm">23:30</span><i class="kn"></i><div class="txt"><b>마무리 한 그릇 (선택)</b>
    <div class="note">둘 다 24시간이라 이 시간엔 오히려 줄이 짧습니다.
    <span class="go" data-go="kinryu">킨류라멘</span> · <span class="go" data-go="ichiran">이치란</span></div></div></div>
</div>

<div class="day">
  <h3>D1 · 근교 하루</h3><div class="when">8/1 (토) · 나라 안 (추천)</div>
  <div class="callout" style="margin:0 0 12px"><b>왜 나라인가</b> 킨테츠 닛폰바시역에서 <b>환승 없이 40분</b>.
  교토는 편도 55~70분에 볼거리가 흩어져 있어 하루로는 빠듯합니다. 아래에 교토 안도 같이 넣었습니다.</div>
  <div class="step key"><span class="tm">08:30</span><i class="kn"></i><div class="txt"><b>킨테츠 닛폰바시 → 킨테츠나라</b>
    <div class="note">급행 약 40분, ¥680. 숙소에서 역까지 도보 5분이라 부담이 없습니다.</div></div></div>
  <div class="step key"><span class="tm">09:30</span><i class="kn"></i><div class="txt"><b>나라 공원 · 사슴</b>
    <div class="note">역에서 도보 10분. 센베를 들면 몰려오니 살 거면 마지막에.
    <span class="go" data-go="narapark">지도에서 보기</span></div></div></div>
  <div class="step"><span class="tm">10:30</span><i class="kn"></i><div class="txt"><b>도다이지 대불</b>
    <div class="note">세계 최대급 목조 건축에 15m 대불. 나라에서 하나만 본다면 여기입니다.
    <span class="go" data-go="todaiji">도다이지</span></div></div></div>
  <div class="step"><span class="tm">12:00</span><i class="kn"></i><div class="txt"><b>카스가타이샤</b>
    <div class="note">도다이지에서 도보 15분. 석등롱 3,000기가 늘어선 참배길.
    <span class="go" data-go="kasuga">카스가타이샤</span></div></div></div>
  <div class="step"><span class="tm">13:30</span><i class="kn"></i><div class="txt"><b>나라마치 점심 · 산책</b>
    <div class="note">에도기 상가 마을. 사슴 인파에서 벗어나고 싶을 때.
    <span class="go" data-go="naramachi">나라마치</span></div></div></div>
  <div class="step key"><span class="tm">16:00</span><i class="kn"></i><div class="txt"><b>오사카 복귀 · 신세카이</b>
    <div class="note">쿠시카츠는 여기가 원조 동네입니다. 관광객 줄이 긴 다루마·야에카츠 대신
    <span class="go" data-go="yakko">얏코</span>(18시 마감·토 영업) 또는
    <span class="go" data-go="echigen">에치겐</span> ·
    <span class="go" data-go="tengu">텐구</span>가 현지 쪽입니다.</div></div></div>
  <div class="step"><span class="tm">19:00</span><i class="kn"></i><div class="txt"><b>츠텐카쿠 야경</b>
    <div class="note">쇼와 레트로 거리가 밤에 제일 삽니다. <span class="go" data-go="tsutenkaku">츠텐카쿠</span></div></div></div>
  <div class="step key"><span class="tm">20:30</span><i class="kn"></i><div class="txt"><b>텐마 술골목</b>
    <div class="note">오사카 사람들이 실제로 마시는 동네. 한 잔 몇백 엔, 한 접시 300~500엔.
    <span class="go" data-go="uosho">우오쇼</span>(토 16시부터) ·
    <span class="go" data-go="tamon">신타몬 사카구라</span> ·
    <span class="go" data-go="marcus">마커스</span></div></div></div>
  <div class="step"><span class="tm">대안</span><i class="kn"></i><div class="txt"><b>교토 안</b>
    <div class="note">이른 아침 <span class="go" data-go="fushimi">후시미이나리</span>(24시간, 7시 전이면 도리이가 텅 빕니다)
    → <span class="go" data-go="gion">기온</span> → <span class="go" data-go="kiyomizu">기요미즈데라</span>
    → <span class="go" data-go="nishiki">니시키 시장</span>(17시 마감) →
    교토역 <span class="go" data-go="shinpuku">신푸쿠사이칸</span> · <span class="go" data-go="daiichiasahi">다이이치 아사히</span> 라멘으로 마무리.</div></div></div>
</div>

<div class="day">
  <h3>D2 · 오사카 시내</h3><div class="when">8/2 (일) · 일요일 휴무 주의</div>
  <div class="callout" style="margin:0 0 12px"><b>일요일에 닫는 로컬집이 많습니다</b>
  우사미테이 마츠바야, 키지 본점, 우오쇼 텐마, 하코야, 제로쿠, 콜롬비아8, 리스본, 킹 오브 킹스, 탄포포, 커피센카 키도 —
  전부 8/2 휴무입니다. 위 <b>목록 탭 → "8/2 일 영업"</b> 필터를 켜면 갈 수 있는 곳만 남습니다.</div>
  <div class="step key"><span class="tm">08:00</span><i class="kn"></i><div class="txt"><b>나카자키초 모닝</b>
    <div class="note">공습을 피한 옛 목조 주택가가 통째로 카페 골목이 된 동네.
    <span class="go" data-go="marimo">킷사 마리모</span>(7시~15시, 8/2 영업) ·
    <span class="go" data-go="nakazakicho">나카자키초 골목</span></div></div></div>
  <div class="step"><span class="tm">10:30</span><i class="kn"></i><div class="txt"><b>오사카성</b>
    <div class="note">천수각까지 안 올라가도 공원 산책만으로 1시간. <span class="go" data-go="osakajo">오사카성</span></div></div></div>
  <div class="step key"><span class="tm">13:00</span><i class="kn"></i><div class="txt"><b>점심 · 니쿠스이</b>
    <div class="note"><span class="go" data-go="chitose">치토세 본점</span> — 우동 뺀 고기국물에 밥을 마는 오사카 고유 음식.
    14:30 마감이고 재료 떨어지면 조기 종료합니다. 문 닫았으면 NGK 1층 별관(11~20시 무휴)에 같은 게 있습니다.</div></div></div>
  <div class="step"><span class="tm">14:30</span><i class="kn"></i><div class="txt"><b>구로몬 · 덴덴타운</b>
    <div class="note">둘 다 숙소 도보권이라 체력 회복용으로 끼워 넣기 좋습니다.
    <span class="go" data-go="kuromon">구로몬 시장</span> · <span class="go" data-go="denden">덴덴타운</span></div></div></div>
  <div class="step key"><span class="tm">16:30</span><i class="kn"></i><div class="txt"><b>아베노 하루카스 300 · 해질녘</b>
    <div class="note">300m 전망대. 해 지는 시간에 맞춰 올라가면 주간·야경을 한 번에 봅니다.
    <span class="go" data-go="harukas">하루카스 300</span></div></div></div>
  <div class="step"><span class="tm">18:30</span><i class="kn"></i><div class="txt"><b>저녁 · 오코노미야키 또는 야키니쿠</b>
    <div class="note"><span class="go" data-go="fugetsu">츠루하시 후게츠 본점</span>(야키니쿠 골목과 붙어 있음) ·
    <span class="go" data-go="fukutaro">후쿠타로</span> · <span class="go" data-go="sanpei">호젠지 산페이</span></div></div></div>
  <div class="step key"><span class="tm">21:00</span><i class="kn"></i><div class="txt"><b>마지막 밤 · 우라난바</b>
    <div class="note">숙소 도보권이라 짐 정리하다 나가도 됩니다.
    <span class="go" data-go="ankeraso">안케라소</span>(화 휴무 → 8/2 영업) ·
    <span class="go" data-go="standajito">스탠드 아지토</span></div></div></div>
</div>

<div class="day">
  <h3>D3 · 출국</h3><div class="when">8/3 (월) 오전</div>
  <div class="step key"><span class="tm">역산</span><i class="kn"></i><div class="txt"><b>숙소에서 몇 시에 나가야 하나</b>
    <div class="note">난바역까지 도보 10분 + 난카이 공항급행 45분 + 국제선 2시간 전 도착 기준입니다.
    <table class="rev"><tr><th>출발편</th><th>숙소 출발</th><th>난바역 승차</th><th>KIX 도착</th></tr>
    <tr><td>09:00</td><td>05:50</td><td>06:05</td><td>06:55</td></tr>
    <tr><td>10:00</td><td>06:50</td><td>07:05</td><td>07:55</td></tr>
    <tr><td>11:00</td><td>07:50</td><td>08:05</td><td>08:55</td></tr>
    <tr><td>12:00</td><td>08:50</td><td>09:05</td><td>09:55</td></tr></table></div></div></div>
  <div class="step"><span class="tm">확인</span><i class="kn"></i><div class="txt"><b>첫차만 미리 보세요</b>
    <div class="note">난카이 난바역 공항급행 첫차는 평일 05:10 전후입니다.
    09시 이전 출발편이면 첫차로도 빠듯하니, 그 경우엔 전날 밤에 시각표를 한 번 확인해 두세요.
    라피트는 첫차가 더 늦습니다.</div></div></div>
  <div class="step"><span class="tm">선물</span><i class="kn"></i><div class="txt"><b>남는 시간이 있다면</b>
    <div class="note">난바역 근처에서 해결됩니다. <span class="go" data-go="horai">551 호라이</span>(부타만) ·
    <span class="go" data-go="rikuro">리쿠로 오지상</span>(치즈케이크). 둘 다 KIX 출국장에도 매장이 있습니다.</div></div></div>
</div>

<div class="callout"><b>이 지도에 대해</b> 관광지 37 · 로컬 맛집 52 · 한국인 관광객 맛집 12곳.
전부 숙소(닛폰바시)에서 <b>편도 90분 이내</b>만 담았습니다.
핀 위치는 주소 기준으로 찍혀 수십 m 오차가 있을 수 있으니, 실제 길찾기는 각 카드의 <b>길찾기</b> 버튼을 쓰세요.
영업시간·휴무는 2026년 7월 리서치 시점 기준입니다.</div>
"""

tpl = open("template.html", encoding="utf-8").read()
out = (tpl.replace("__TILES__", open("tiles.json", encoding="utf-8").read())
          .replace("__DATA__", open("app_data.json", encoding="utf-8").read())
          .replace("__PLAN__", json.dumps(PLAN, ensure_ascii=False)))
open("osaka-map.html", "w", encoding="utf-8").write(out)
print(f"osaka-map.html  {len(out.encode())/1024/1024:.2f} MB")
