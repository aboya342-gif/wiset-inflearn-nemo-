---
marp: true
theme: default
paginate: true
header: "NEMO REAL ESTATE DATA"
footer: "© 2026 NEMO DATA LAB | V2.2 (FIXED)"
backgroundColor: #f5f500
style: |
  section {
    font-family: 'Courier New', Courier, monospace;
    padding: 30px 50px !important;
    display: flex !important;
    flex-direction: column !important;
    color: #000000 !important;
    background-color: #f5f500 !important;
    background-image: none !important;
  }
  h1 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    font-size: 2.2em !important; 
    margin: 0 0 15px 0 !important;
    background: #ffffff !important;
    padding: 10px 20px !important;
    border: 5px solid #000000 !important;
    box-shadow: 8px 8px 0px 0px #000000 !important;
    display: inline-block !important;
    text-transform: uppercase !important;
  }
  h2 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    color: #ffffff !important; 
    font-size: 1.4em !important; 
    margin: 0 0 20px 0 !important;
    background: #FF2D55 !important;
    padding: 6px 12px !important;
    border: 4px solid #000000 !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    display: inline-block !important;
  }
  h3 {
    font-family: 'Arial Black', Gadget, sans-serif !important;
    text-transform: uppercase !important;
    margin-bottom: 10px !important;
    font-size: 1.1em !important;
  }
  .container {
    display: flex !important;
    flex: 1 !important;
    gap: 20px !important;
    min-height: 0 !important;
    overflow: hidden !important;
  }
  .visual-area {
    flex: 1 !important;
    background: #ffffff !important;
    border: 4px solid #000000 !important;
    box-shadow: 10px 10px 0px 0px #000000 !important;
    padding: 15px !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    min-width: 0 !important;
  }
  .text-area {
    flex: 0.8 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
  }
  .highlight-card {
    background: white !important;
    border: 3px solid #000000 !important;
    padding: 12px !important;
    margin-bottom: 12px !important;
    box-shadow: 6px 6px 0px 0px #000000 !important;
    font-weight: bold !important;
    font-size: 0.9em !important;
  }
  img { 
    max-width: 100% !important;
    max-height: 100% !important;
    object-fit: contain !important;
    border: 2px solid #000000 !important;
  }
  .badge {
    display: inline-block !important;
    padding: 4px 10px !important;
    background: #0000FF !important;
    color: white !important;
    border: 2px solid #000000 !important;
    font-weight: 900 !important;
    margin-bottom: 8px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    font-size: 0.8em !important;
  }
  footer {
    font-weight: 900 !important;
    color: #000000 !important;
    font-size: 0.7em !important;
    bottom: 10px !important;
    left: 20px !important;
  }
  header {
    font-weight: 900 !important;
    color: #000000 !important;
    font-size: 0.7em !important;
    top: 10px !important;
  }
---

# 네모(Nemo) 매물 분석 리포트
## 데이터 기반 상업용 부동산 전략 가이드

<div class="container">
  <div class="visual-area">
    <div style="text-align: center;">
      <div style="font-size: 4em; margin-bottom: 10px; filter: drop-shadow(5px 5px 0px #000);">🏢</div>
      <div style="font-family: 'Arial Black'; font-size: 2em; background: #CCFF00; border: 4px solid #000; padding: 10px; box-shadow: 8px 8px 0px #000;">INTEL LAB</div>
    </div>
  </div>
  <div class="text-area">
    <div class="badge">V2.0 PRO</div>
    <div class="highlight-card">🎯 DATA: 677 SAMPLES</div>
    <div class="highlight-card">🛠 METHOD: EDA & REGRESSION</div>
    <div class="highlight-card">🚀 GOAL: MAX REVENUE</div>
  </div>
</div>

<!-- note
안녕하십니까. 지금부터 네모(Nemo) 플랫폼의 상가 및 사무실 매물 데이터를 분석한 2026년도 상반기 EDA 리포트 발표를 시작하겠습니다. 본 리포트는 단순한 시장 조사를 넘어, 실제 현장에서 수집된 677건의 방대한 마이크로 데이터를 기반으로 작성되었습니다. 오늘 발표의 핵심은 '데이터가 어떻게 부동산 거래의 불확실성을 제거하고, 수익으로 연결되는 의사결정을 돕는가'에 있습니다.
-->

---

## 1. 분석 개요 및 데이터 설계
<div class="container">
  <div class="visual-area">
    <div style="width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 25px;">
      <div style="background: #CCFF00; padding: 30px; border: 4px solid #000; box-shadow: 8px 8px 0px #000; text-align: center;">
        <div style="font-size: 3em;">📊</div>
        <div style="font-family: 'Arial Black';">INDEX</div>
      </div>
      <div style="background: #FF2D55; padding: 30px; border: 4px solid #000; box-shadow: 8px 8px 0px #000; text-align: center; color: white;">
        <div style="font-size: 3em;">🎯</div>
        <div style="font-family: 'Arial Black';">MATCH</div>
      </div>
    </div>
  </div>
  <div class="text-area">
    <div class="badge">OBJECTIVES</div>
    <h3>데이터 거버넌스</h3>
    <ul style="font-weight: bold; line-height: 2; font-size: 0.8em;">
      <li>PRICE STANDARD 수립</li>
      <li>AREA ANALYSIS 데이터화</li>
      <li>SEO LOGIC 분석</li>
    </ul>
  </div>
</div>

<!-- note
첫 번째 슬라이드에서는 이번 분석의 설계 배경과 데이터 거버넌스에 대해 말씀드리겠습니다.
-->

---

## 2. 입지 및 업종 마켓 맵
<div class="container">
  <div class="visual-area" style="flex-direction: column; gap: 15px;">
    <div style="display: flex; gap: 15px; width: 100%; height: 100%;">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_0.png" style="width: 48%;" alt="업종">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_1.png" style="width: 48%;" alt="역세권">
    </div>
  </div>
  <div class="text-area">
    <div class="highlight-card" style="background: #CCFF00;">TOP: 기타판매(39%)</div>
    <div class="highlight-card" style="background: #0000FF; color: white;">HOT: 강남/역삼/선릉</div>
    <p style="font-weight: 900; text-transform: uppercase; margin-top: 10px; font-size: 0.7em;">강남권 오피스 배후 수요<br>공급 밀집 현상 뚜렷</p>
  </div>
</div>

<!-- note
이번 슬라이드는 현재 우리 플랫폼에 등록된 매물들이 어디에, 그리고 어떤 모습으로 분포하고 있는지를 보여주는 '마켓 맵'입니다.
-->

---

## 3. 매칭률 키워드 전략 (TF-IDF)
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/tfidf_keywords.png" alt="TF-IDF">
  </div>
  <div class="text-area">
    <div class="badge">SEMANTIC</div>
    <div class="highlight-card">#역세권 (입지 중심)</div>
    <div class="highlight-card" style="background: #CCFF00;">#무권리 (비용 절감)</div>
    <div class="highlight-card" style="background: #FF2D55; color: white;">#테라스 (공간 가치)</div>
  </div>
</div>

<!-- note
임대인들이 매물을 올릴 때 가장 고민하는 것은 "어떻게 제목을 지어야 임차인이 클릭할까?"입니다.
-->

---

## 4. 임대차 가격 '스윗스팟'
<div class="container">
  <div class="visual-area" style="flex-direction: column; gap: 10px;">
    <div style="display: flex; gap: 10px; width: 100%; height: 100%;">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_dist_deposit.png" style="width: 48%;" alt="보증금">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_dist_rent.png" style="width: 48%;" alt="월세">
    </div>
  </div>
  <div class="text-area">
    <div class="badge">PRICE TREND</div>
    <div class="highlight-card" style="background: #FF2D55; color: white;">월세: 200~500만</div>
    <div class="highlight-card" style="background: #CCFF00;">보증금: 3천~1억</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">전체 매물의 62% 집중</p>
  </div>
</div>

---

## 5. 이상치 및 프리미엄 전략
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_scatter_dep_rent.png" alt="산점도">
  </div>
  <div class="text-area">
    <div class="badge">VIP ONLY</div>
    <div class="highlight-card">TOP 5% PREMIUM</div>
    <div class="highlight-card" style="background: #000; color: white;">월세 2,000만+</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">기업사옥 / 플래그십</p>
  </div>
</div>

---

## 6. 업종별 공간 수요
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_bar_size_by_biz.png" alt="업종별 면적">
  </div>
  <div class="text-area">
    <div class="badge">SPACE</div>
    <div class="highlight-card" style="background: #FF2D55; color: white;">병원: 100평+</div>
    <div class="highlight-card" style="background: #CCFF00;">사무실/카페: 20~40평</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">지능형 검색 필터링</p>
  </div>
</div>

---

## 7. 층별 가격 프리미엄
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_box_floor_rent.png" alt="층별 분석">
  </div>
  <div class="text-area">
    <div class="badge">FLOOR</div>
    <div class="highlight-card" style="background: #000; color: white;">1층: 초고가 양극화</div>
    <div class="highlight-card" style="background: #ffffff;">지하/고층: 가성비</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">목적형 임차인 타겟팅</p>
  </div>
</div>

---

## 8. 회귀분석 가성비 알고리즘
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_reg_size_price.png" alt="회귀분석">
  </div>
  <div class="text-area">
    <div class="badge">ENGINE</div>
    <div class="highlight-card" style="background: #CCFF00;">STANDARD LINE</div>
    <div class="highlight-card" style="border: 4px dashed #FF2D55;">UNDERVALUED PICK</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">과학적 가성비 추천</p>
  </div>
</div>

---

## 9. 역세권 히트맵 수익 전략
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_station_price.png" alt="히트맵">
  </div>
  <div class="text-area">
    <div class="badge">REVENUE</div>
    <div class="highlight-card" style="background: #FF2D55; color: white;">HOTSPOT: 광고상향</div>
    <div class="highlight-card" style="background: #CCFF00;">COLDSPOT: 매물확보</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">동적 광고 상품 도입</p>
  </div>
</div>

---

## 10. 마케팅 골든 타임
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_day_activity.png" alt="활동 패턴">
  </div>
  <div class="text-area">
    <div class="badge">TIMING</div>
    <div class="highlight-card" style="background: #0000FF; color: white;">화/수요일 오전 PEAK</div>
    <div class="highlight-card">WED 10:30 AM PUSH</div>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.7em;">전환율 2.5배 상승</p>
  </div>
</div>

---

## 11. 결론: 네모의 내일
<div class="container">
  <div class="text-area" style="flex: 1;">
    <div class="highlight-card" style="background: #CCFF00;">1. AI 추천 시스템</div>
    <div class="highlight-card" style="background: #FF2D55; color: white;">2. VIP 프리미엄 케어</div>
  </div>
  <div class="text-area" style="flex: 1;">
    <div class="highlight-card" style="background: #0000FF; color: white;">3. 시장 투명성 강화</div>
    <div class="highlight-card" style="background: #ffffff;">4. 정밀 타겟 마케팅</div>
  </div>
</div>

---

# Q&A
## 감사합니다!
