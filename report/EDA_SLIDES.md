---
marp: true
theme: default
paginate: true
header: "NEMO REAL ESTATE DATA"
footer: "© 2026 NEMO DATA LAB | V2.4 (FINAL LAYOUT)"
backgroundColor: #f5f500
style: |
  section {
    font-family: 'Courier New', Courier, monospace;
    padding: 50px 60px !important;
    display: flex !important;
    flex-direction: column !important;
    color: #000000 !important;
    background-color: #f5f500 !important;
    background-image: none !important;
  }
  h1 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    font-size: 2.1em !important; 
    margin: 0 0 15px 0 !important;
    background: #ffffff !important;
    padding: 8px 18px !important;
    border: 5px solid #000000 !important;
    box-shadow: 7px 7px 0px 0px #000000 !important;
    display: inline-block !important;
    text-transform: uppercase !important;
    line-height: 1.1 !important;
  }
  h2 { 
    font-family: 'Arial Black', Gadget, sans-serif !important;
    color: #ffffff !important; 
    font-size: 1.25em !important; 
    margin: 0 0 20px 0 !important;
    background: #FF2D55 !important;
    padding: 6px 12px !important;
    border: 4px solid #000000 !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    display: inline-block !important;
    text-transform: uppercase !important;
  }
  h3 {
    font-family: 'Arial Black', Gadget, sans-serif !important;
    text-transform: uppercase !important;
    margin-bottom: 12px !important;
    font-size: 1.05em !important;
    border-bottom: 3px solid #000;
    display: inline-block;
  }
  .container {
    display: flex !important;
    flex: 1 !important;
    gap: 25px !important;
    min-height: 0 !important;
    width: 100% !important;
    margin-top: 5px !important;
  }
  .visual-area, .text-area {
    background: #ffffff !important;
    border: 5px solid #000000 !important;
    box-shadow: 10px 10px 0px 0px #000000 !important;
    padding: 20px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    min-width: 0 !important;
  }
  .visual-area {
    flex: 1.1 !important;
    align-items: center !important;
  }
  .text-area {
    flex: 0.9 !important;
    align-items: flex-start !important;
  }
  .highlight-card {
    background: #f0f0f0 !important;
    border: 3px solid #000000 !important;
    padding: 8px 12px !important;
    margin-bottom: 10px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    font-weight: bold !important;
    width: 100%;
    box-sizing: border-box;
    font-size: 0.85em;
  }
  img { 
    max-width: 100% !important;
    max-height: 240px !important;
    object-fit: contain !important;
    border: 3px solid #000000 !important;
  }
  .badge {
    display: inline-block !important;
    padding: 4px 10px !important;
    background: #0000FF !important;
    color: white !important;
    border: 3px solid #000000 !important;
    font-weight: 900 !important;
    margin-bottom: 12px !important;
    box-shadow: 3px 3px 0px 0px #000000 !important;
    text-transform: uppercase !important;
    font-size: 0.75em !important;
  }
  footer {
    font-weight: 900 !important;
    color: #000000 !important;
    font-size: 0.7em !important;
    bottom: 15px !important;
  }
  header {
    font-weight: 900 !important;
    color: #000000 !important;
    font-size: 0.7em !important;
    top: 15px !important;
  }
---

# 네모(Nemo) 매물 분석 리포트
## 데이터 기반 상업용 부동산 전략 가이드

<div class="container">
  <div class="visual-area">
    <div style="text-align: center;">
      <div style="font-size: 3em; margin-bottom: 10px; filter: drop-shadow(4px 4px 0px #000);">🏢</div>
      <div style="font-family: 'Arial Black'; font-size: 1.8em; background: #CCFF00; border: 4px solid #000; padding: 10px; box-shadow: 6px 6px 0px #000;">INTEL LAB</div>
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
안녕하십니까. 지금부터 네모(Nemo) 플랫폼의 상가 및 사무실 매물 데이터를 분석한 2026년도 상반기 EDA 리포트 발표를 시작하겠습니다. 본 리포트는 단순한 시장 조사를 넘어, 실제 현장에서 수집된 677건의 방대한 마이크로 데이터를 기반으로 작성되었습니다. 오늘 발표의 핵심은 '데이터가 어떻게 부동산 거래의 불확실성을 제거하고, 수익으로 연결되는 의사결정을 돕는가'에 있습니다.
-->

---

## 1. 분석 개요 및 데이터 설계
<div class="container">
  <div class="visual-area">
    <div style="width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
      <div style="background: #CCFF00; padding: 20px; border: 4px solid #000; box-shadow: 6px 6px 0px #000; text-align: center;">
        <div style="font-size: 2.5em;">📊</div>
        <div style="font-family: 'Arial Black'; font-size: 0.9em;">INDEX</div>
      </div>
      <div style="background: #FF2D55; padding: 20px; border: 4px solid #000; box-shadow: 6px 6px 0px #000; text-align: center; color: white;">
        <div style="font-size: 2.5em;">🎯</div>
        <div style="font-family: 'Arial Black'; font-size: 0.9em;">MATCH</div>
      </div>
    </div>
  </div>
  <div class="text-area">
    <div class="badge">OBJECTIVES</div>
    <h3>데이터 거버넌스</h3>
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">• PRICE STANDARD 수립</p>
    <p style="font-weight: bold; font-size: 0.8em;">• AREA ANALYSIS 데이터화</p>
    <p style="font-weight: bold; font-size: 0.8em;">• SEO LOGIC 분석</p>
  </div>
</div>

<!-- note
첫 번째 슬라이드에서는 이번 분석의 설계 배경과 데이터 거버넌스에 대해 말씀드리겠습니다. 상업용 부동산 시장은 아파트와 같은 주거용 부동산에 비해 정보의 비대칭성이 매우 심각한 분야입니다. '부르는 게 값'이라는 인식이 강한 이 시장에서, 네모는 데이터라는 무기로 투명성을 확보하고자 합니다.
-->

---

## 2. 입지 및 업종 마켓 맵
<div class="container">
  <div class="visual-area">
    <div style="display: flex; gap: 10px; width: 100%; justify-content: center;">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_0.png" style="width: 48%;" alt="업종">
      <img src="https://aboya342-gif.github.io/wiset-inflearn-nemo-/images/cat_freq_1.png" style="width: 48%;" alt="역세권">
    </div>
  </div>
  <div class="text-area">
    <div class="badge">MARKET MAP</div>
    <div class="highlight-card" style="background: #CCFF00 !important;">TOP: 기타판매(39%)</div>
    <div class="highlight-card" style="background: #0000FF !important; color: white !important;">HOT: 강남/역삼/선릉</div>
    <p style="font-weight: 900; margin-top: 10px; font-size: 0.75em;">강남권 오피스 배후 수요 및 공급 밀집 현상 뚜렷</p>
  </div>
</div>

<!-- note
이번 슬라이드는 현재 우리 플랫폼에 등록된 매물들이 어디에, 그리고 어떤 모습으로 분포하고 있는지를 보여주는 '마켓 맵'입니다. 데이터 분석 결과, 매우 흥미로운 'T-라인 밀집 현상'이 포착되었습니다. 역삼역, 강남역, 선릉역으로 이어지는 이른바 테헤란로 중심축의 매물 점유율이 압도적입니다.
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
    <div class="highlight-card" style="background: #CCFF00 !important;">#무권리 (비용 절감)</div>
    <div class="highlight-card" style="background: #FF2D55 !important; color: white !important;">#테라스 (공간 가치)</div>
  </div>
</div>

<!-- note
우리는 질문에 대한 답을 찾기 위해 677건의 제목 텍스트를 TF-IDF 기법으로 분석했습니다. 1위는 역시 '역세권'입니다. 하지만 진짜 주목해야 할 단어는 2위와 3위에 포진한 '무권리'와 '테라스'입니다. 고금리와 불황이 지속되면서 예비 창업자들은 초기 투자 비용을 최소화할 수 있는 '무권리' 매물에 열광하고 있습니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">전체 매물의 62%가 해당 구간에 집중 분포</p>
  </div>
</div>

<!-- note
모든 시장에는 가장 활발하게 거래가 일어나는 핵심 구간이 존재하며, 상업용 부동산 시장에서도 그 지점을 정확히 찾아냈습니다. 그래프를 보시면 보증금은 3천만 원에서 1억 원 사이, 월세는 200만 원에서 500만 원 사이 구간에 매물이 가장 두텁게 형성되어 있습니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">대형 기업 사옥 및 플래그십 스토어 전략 매물</p>
  </div>
</div>

<!-- note
통계 분석에서 '이상치(Outlier)'는 보통 제거의 대상이지만, 비즈니스 분석에서는 종종 '새로운 기회'가 됩니다. 월세가 2,000만 원을 넘어가거나 보증금이 수억 원에 달하는 이들은 전체의 약 5%에 불과하지만, 계약 한 건당 발생하는 수수료나 플랫폼 기여도는 매우 높습니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">업종별 맞춤형 지능형 검색 필터링 로직 제안</p>
  </div>
</div>

<!-- note
분석 결과, 숙박시설과 대형 병원은 평균 100평 이상의 대형 면적에 집중되어 있습니다. 시설 투자비가 높고 운영 효율을 위해 규모의 경제가 필수적인 업종들이기 때문입니다. 반면, 우리 플랫폼의 주력 매물인 사무실과 커피숍은 20평에서 40평 사이의 '컴팩트 효율 구간'에 밀집되어 있습니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">비즈니스 목적에 따른 층별 차별화 타겟팅</p>
  </div>
</div>

<!-- note
결과는 예상보다 훨씬 선명했습니다. 1층 매물은 월세 중앙값뿐만 아니라 가격의 편차도 가장 큽니다. 이는 1층 내에서도 가시성이나 골목 유무에 따라 가격 양극화가 매우 심하다는 것을 의미합니다. 반면 지하층이나 3층 이상의 고층부는 월세 수준이 매우 합리적입니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">데이터 모델링을 통한 객관적 가성비 지수 도출</p>
  </div>
</div>

<!-- note
이 슬라이드는 이번 분석 리포트의 기술적 정점인 '선형 회귀 분석' 결과입니다. 우리는 면적이 월세에 미치는 영향을 분석하여, 시장의 '적정 임대료 기준선'을 도출했습니다. 그래프 중앙의 파란색 선이 바로 그 기준입니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">입지 경쟁 기반의 동적 광고 상품 도입 전략</p>
  </div>
</div>

<!-- note
히트맵 데이터는 지도 위의 단순한 색깔이 아닙니다. 그것은 네모 플랫폼의 수익을 결정하는 '매출 대시보드'입니다. 강남역과 역삼역 인근이 붉게 타오르는 것을 보십시오. 이 지역은 매물 가치가 가장 높을 뿐만 아니라 노출 경쟁도 가장 치열한 곳입니다.
-->

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
    <p style="font-weight: bold; margin-top: 10px; font-size: 0.8em;">유저 활동 주기에 최적화된 마케팅 타이밍</p>
  </div>
</div>

<!-- note
분석 결과, 매물 등록과 정보 수정 활동은 화요일과 수요일 오전에 가장 폭발적으로 일어납니다. 주말 동안 고민한 공급자들이 평일 업무 복귀 후 본격적으로 데이터를 업데이트하기 때문입니다. 우리는 매주 수요일 오전 10시 30분을 푸시 알림 발송 시간으로 확정했습니다.
-->

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

<!-- note
발표를 마무리하며 네모의 데이터 기반 미래 비전을 정리해 드립니다. 우리는 AI 가성비 추천 엔진을 상용화하고, 하이엔드 시장을 공략하며, 시세 지도를 공개하여 정보 비대칭을 해소하겠습니다. 긴 시간 경청해 주셔서 감사합니다.
-->

---

# Q&A
## 감사합니다!
