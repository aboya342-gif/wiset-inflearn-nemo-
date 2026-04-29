---
marp: true
theme: default
paginate: true
header: "NEMO REAL ESTATE DATA"
footer: "© 2026 NEMO DATA LAB | V2.3 (LAYOUT FIXED)"
backgroundColor: #f5f500
style: |
  section {
    font-family: 'Courier New', Courier, monospace;
    padding: 40px 60px !important;
    display: flex !important;
    flex-direction: column !important;
    color: #000000 !important;
    background-color: #f5f500 !important;
    background-image: none !important;
  }
  h1 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    font-size: 2.2em !important; 
    margin: 0 0 20px 0 !important;
    background: #ffffff !important;
    padding: 10px 20px !important;
    border: 5px solid #000000 !important;
    box-shadow: 8px 8px 0px 0px #000000 !important;
    display: inline-block !important;
    text-transform: uppercase !important;
    line-height: 1.1 !important;
  }
  h2 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    color: #ffffff !important; 
    font-size: 1.3em !important; 
    margin: 0 0 25px 0 !important;
    background: #FF2D55 !important;
    padding: 8px 15px !important;
    border: 4px solid #000000 !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    display: inline-block !important;
    text-transform: uppercase !important;
  }
  h3 {
    font-family: 'Arial Black', Gadget, sans-serif !important;
    text-transform: uppercase !important;
    margin-bottom: 15px !important;
    font-size: 1.2em !important;
    border-bottom: 3px solid #000;
    display: inline-block;
  }
  .container {
    display: flex !important;
    flex: 1 !important;
    gap: 30px !important;
    min-height: 0 !important;
    width: 100% !important;
  }
  .visual-area, .text-area {
    background: #ffffff !important;
    border: 5px solid #000000 !important;
    box-shadow: 12px 12px 0px 0px #000000 !important;
    padding: 25px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    min-width: 0 !important;
  }
  .visual-area {
    flex: 1.2 !important;
    align-items: center !important;
  }
  .text-area {
    flex: 0.8 !important;
    align-items: flex-start !important;
  }
  .highlight-card {
    background: #f0f0f0 !important;
    border: 3px solid #000000 !important;
    padding: 10px 15px !important;
    margin-bottom: 15px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    font-weight: bold !important;
    width: 100%;
    box-sizing: border-box;
  }
  img { 
    max-width: 100% !important;
    max-height: 350px !important;
    object-fit: contain !important;
    border: 3px solid #000000 !important;
  }
  .badge {
    display: inline-block !important;
    padding: 5px 12px !important;
    background: #0000FF !important;
    color: white !important;
    border: 3px solid #000000 !important;
    font-weight: 900 !important;
    margin-bottom: 15px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    text-transform: uppercase !important;
    font-size: 0.8em !important;
  }
  footer, header {
    font-weight: 900 !important;
    color: #000000 !important;
    font-size: 0.75em !important;
    text-transform: uppercase !important;
  }
---

# 네모(Nemo) 매물 분석 리포트
## 데이터 기반 상업용 부동산 전략 가이드

<div class="container">
  <div class="visual-area">
    <div style="text-align: center;">
      <div style="font-size: 5em; margin-bottom: 15px; filter: drop-shadow(5px 5px 0px #000);">🏢</div>
      <div style="font-family: 'Arial Black'; font-size: 2em; background: #CCFF00; border: 4px solid #000; padding: 15px; box-shadow: 8px 8px 0px #000;">INTEL LAB</div>
    </div>
  </div>
  <div class="text-area">
    <div class="badge">V2.0 PRO</div>
    <div class="highlight-card">🎯 DATA: 677 SAMPLES</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">🛠 EDA & REGRESSION</div>
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">🚀 GOAL: MAX REVENUE</div>
  </div>
</div>

<!-- note
안녕하십니까. 지금부터 네모(Nemo) 플랫폼의 상가 및 사무실 매물 데이터를 분석한 2026년도 상반기 EDA 리포트 발표를 시작하겠습니다.
-->

---

## 1. 분석 개요 및 데이터 설계
<div class="container">
  <div class="visual-area">
    <div style="width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
      <div style="background: #CCFF00; padding: 25px; border: 4px solid #000; box-shadow: 8px 8px 0px #000; text-align: center;">
        <div style="font-size: 3em;">📊</div>
        <div style="font-family: 'Arial Black';">INDEX</div>
      </div>
      <div style="background: #FF2D55; padding: 25px; border: 4px solid #000; box-shadow: 8px 8px 0px #000; text-align: center; color: white;">
        <div style="font-size: 3em;">🎯</div>
        <div style="font-family: 'Arial Black';">MATCH</div>
      </div>
    </div>
  </div>
  <div class="text-area">
    <div class="badge">OBJECTIVES</div>
    <h3>데이터 거버넌스</h3>
    <p style="font-weight: bold; margin-top: 10px;">• PRICE STANDARD 수립</p>
    <p style="font-weight: bold;">• AREA ANALYSIS 데이터화</p>
    <p style="font-weight: bold;">• SEO LOGIC 분석</p>
  </div>
</div>

---

## 2. 입지 및 업종 마켓 맵
<div class="container">
  <div class="visual-area">
    <div style="display: flex; gap: 15px; width: 100%; justify-content: center;">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_0.png" style="width: 48%;" alt="업종">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_1.png" style="width: 48%;" alt="역세권">
    </div>
  </div>
  <div class="text-area">
    <div class="badge">MARKET MAP</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">TOP: 기타판매(39%)</div>
    <div class="highlight-card" style="background: #0000FF !important; color: white !important;">HOT: 강남/역삼/선릉</div>
    <p style="font-weight: 900; margin-top: 10px;">강남권 오피스 배후 수요 및 공급 밀집 현상 뚜렷</p>
  </div>
</div>

---

## 3. 매칭률 키워드 전략 (TF-IDF)
<div class="container">
  <div class="visual-area">
    <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/tfidf_keywords.png" alt="TF-IDF">
  </div>
  <div class="text-area">
    <div class="badge">SEMANTIC</div>
    <div class="highlight-card">#역세권 (입지 중심)</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">#무권리 (비용 절감)</div>
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">#테라스 (공간 가치)</div>
  </div>
</div>

---

## 4. 임대차 가격 '스윗스팟'
<div class="container">
  <div class="visual-area">
    <div style="display: flex; gap: 10px; width: 100%; justify-content: center;">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_dist_deposit.png" style="width: 48%;" alt="보증금">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/v2_dist_rent.png" style="width: 48%;" alt="월세">
    </div>
  </div>
  <div class="text-area">
    <div class="badge">PRICE TREND</div>
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">월세: 200~500만</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">보증금: 3천~1억</div>
    <p style="font-weight: bold; margin-top: 10px;">전체 매물의 62%가 해당 구간에 집중 분포</p>
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
    <div class="highlight-card" style="background: #000 !important; color: white !important;">TOP 5% PREMIUM</div>
    <div class="highlight-card">월세 2,000만 이상</div>
    <p style="font-weight: bold; margin-top: 10px;">대형 기업 사옥 및 플래그십 스토어 전략 매물</p>
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
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">병원: 100평 이상</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">사무실/카페: 20~40평</div>
    <p style="font-weight: bold; margin-top: 10px;">업종별 맞춤형 지능형 검색 필터링 로직 제안</p>
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
    <div class="highlight-card" style="background: #000 !important; color: white !important;">1층: 초고가 양극화</div>
    <div class="highlight-card">지하/고층: 가성비 우수</div>
    <p style="font-weight: bold; margin-top: 10px;">비즈니스 목적에 따른 층별 차별화 타겟팅</p>
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
    <div class="highlight-card" style="background: #CCFF00 !important;">STANDARD LINE</div>
    <div class="highlight-card" style="border: 4px dashed #FF2D55 !important;">UNDERVALUED PICK</div>
    <p style="font-weight: bold; margin-top: 10px;">데이터 모델링을 통한 객관적 가성비 지수 도출</p>
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
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">HOTSPOT: 광고 단가 상향</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">COLDSPOT: 신규 매물 확보</div>
    <p style="font-weight: bold; margin-top: 10px;">입지 경쟁 기반의 동적 광고 상품 도입 전략</p>
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
    <div class="highlight-card" style="background: #0000FF !important; color: white !important;">화/수요일 오전 피크</div>
    <div class="highlight-card">WED 10:30 AM PUSH</div>
    <p style="font-weight: bold; margin-top: 10px;">유저 활동 주기에 최적화된 마케팅 타이밍</p>
  </div>
</div>

---

## 11. 결론: 네모의 내일
<div class="container">
  <div class="text-area" style="flex: 1;">
    <div class="badge">STRATEGY A</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">1. AI 추천 시스템</div>
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">2. VIP 프리미엄 케어</div>
  </div>
  <div class="text-area" style="flex: 1;">
    <div class="badge">STRATEGY B</div>
    <div class="highlight-card" style="background: #0000FF !important; color: white !important;">3. 시장 투명성 강화</div>
    <div class="highlight-card" style="background: #ffffff !important;">4. 정밀 타겟 마케팅</div>
  </div>
</div>

---

# Q&A
## 감사합니다!
