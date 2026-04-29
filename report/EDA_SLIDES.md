---
marp: true
theme: default
paginate: true
header: "네모(Nemo) 매물 데이터 분석 EDA 리포트"
footer: "2026-04-29 | 부동산 데이터 사이언스 팀"
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Malgun Gothic', 'Pretendard', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 40px;
  }
  h1 { color: #0052cc; font-size: 1.8em; margin-bottom: 20px; }
  h2 { color: #334155; border-left: 8px solid #0052cc; padding-left: 15px; font-size: 1.2em; margin-bottom: 20px; }
  .content { flex: 1; }
  .speaker-note {
    background: #f8fafc;
    border-top: 2px solid #e2e8f0;
    padding: 15px;
    margin-top: 20px;
    font-size: 0.6em;
    color: #475569;
    border-radius: 8px;
    line-height: 1.5;
  }
  .speaker-note::before {
    content: "🎤 발표자 노트 (2분 스크립트)";
    display: block;
    font-weight: bold;
    color: #0052cc;
    margin-bottom: 5px;
    font-size: 1.1em;
  }
  img { border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
---

# 네모(Nemo) 매물 데이터 분석
## 상가/사무실 매물 데이터 시각화 및 비즈니스 인사이트

<div class="content">
  <div style="text-align: center; margin-top: 50px;">
    <p style="font-size: 1.2em; color: #64748b;">Nemo Real Estate Analytics v1.0</p>
    <p>본 리포트는 네모 플랫폼의 매물 데이터를 기반으로<br>시장의 흐름과 데이터 기반의 가이드를 제공합니다.</p>
  </div>
</div>

<div class="speaker-note">
  안녕하십니까. 지금부터 네모 플랫폼의 상가 및 사무실 매물 데이터를 분석한 EDA 리포트 발표를 시작하겠습니다. 본 분석은 최근 수집된 677건의 실제 매물 데이터를 바탕으로 하며, 단순한 통계 수치를 넘어 데이터 속에 숨겨진 시장의 트렌드와 비즈니스 기회를 발굴하는 데 목적이 있습니다. 네모는 단순한 중개 플랫폼을 넘어 데이터 기반의 의사결정을 돕는 파트너로서, 이번 분석을 통해 임대인과 임차인 모두에게 가치 있는 인사이트를 제공하고자 합니다. 슬라이드를 통해 업종별 분포, 가격대별 스윗스팟, 그리고 역세권 시세 현황 등을 심도 있게 살펴보겠습니다.
</div>

---

## 1. 분석 개요
<div class="content">
  <ul>
    <li><b>목적</b>: 네모 플랫폼 매물 데이터 분석을 통한 시장 현황 파악 및 기회 발굴</li>
    <li><b>데이터 규모</b>: 총 677건의 상업용 매물 데이터</li>
    <li><b>주요 분석 항목</b>:
      <ul>
        <li>입지 분석 및 업종별 밀집도</li>
        <li>보증금/월세 가격 스윗스팟(Sweet Spot) 도출</li>
        <li>TF-IDF 기반 매물 제목 키워드 인사이트</li>
      </ul>
    </li>
  </ul>
</div>

<div class="speaker-note">
  첫 번째 슬라이드인 분석 개요입니다. 이번 프로젝트는 네모 플랫폼 내의 상업용 부동산 데이터를 체계적으로 분석하기 위해 기획되었습니다. 총 677건의 유효 데이터를 활용했으며, 크게 세 가지 관점에서 접근했습니다. 첫째로 매물의 기본적인 정보와 입지 조건을 분석하여 현재 시장의 공급 현황을 파악했습니다. 둘째로 보증금과 월세의 분포를 분석하여 시장에서 가장 활발하게 거래되는 가격대를 정의했습니다. 셋째로 매물 제목에서 추출한 키워드를 분석하여 사용자들이 어떤 가치에 반응하는지 확인했습니다. 마지막으로 층별, 업종별 가격 편차를 분석하여 데이터에 기반한 합리적인 임대료 가이드를 도출하고자 했습니다.
</div>

---

## 2. 업종 및 입지 현황 (Top Categories)
<div class="content">
  <div style="display: flex; justify-content: space-around; align-items: center; gap: 20px;">
    <div style="text-align: center;">
      <p style="font-size: 0.8em; font-weight: bold;">[업종별 분포]</p>
      <img src="../images/cat_freq_0.png" width="100%" alt="업종 분포">
    </div>
    <div style="text-align: center;">
      <p style="font-size: 0.8em; font-weight: bold;">[주요 역세권 현황]</p>
      <img src="../images/cat_freq_1.png" width="100%" alt="역세권 분포">
    </div>
  </div>
</div>

<div class="speaker-note">
  현재 시장에 나와 있는 매물들의 업종과 위치를 살펴보겠습니다. 왼쪽 차트를 보시면 기타판매시설과 단독용도점포가 가장 큰 비중을 차지하고 있으며, 카페와 같은 식음료 업종이 그 뒤를 잇고 있습니다. 이는 현재 시장 공급이 일반 판매업과 소규모 창업 아이템 위주로 형성되어 있음을 보여줍니다. 오른쪽 차트는 입지 분석 결과입니다. 예상대로 역삼, 강남, 선릉역으로 이어지는 테헤란로 중심권의 매물 밀도가 매우 높습니다. 이 지역들은 유동인구가 보장되는 핵심 상권으로, 높은 임대료에도 불구하고 수요와 공급이 모두 활발하게 일어나는 지점입니다. 이러한 입지 데이터는 향후 지역별 맞춤형 광고 상품을 설계할 때 기초 자료가 될 것입니다.
</div>

---

## 3. 매물 제목 키워드 분석 (TF-IDF)
<div class="content">
  <div style="display: flex; align-items: flex-start; gap: 30px;">
    <img src="../images/tfidf_keywords.png" width="55%" alt="TF-IDF 키워드">
    <div style="font-size: 0.9em;">
      <p><b>핵심 키워드</b></p>
      <ul style="color: #0052cc; font-weight: bold;">
        <li>#역세권 #무권리</li>
        <li>#테라스 #신축</li>
        <li>#강남역 #사무실</li>
      </ul>
      <p style="font-size: 0.8em; color: #64748b;">상업용 매물의 경쟁력은<br>입지와 부가 혜택에서 결정됨</p>
    </div>
  </div>
</div>

<div class="speaker-note">
  임대인들이 매물을 등록할 때 제목에 어떤 단어를 가장 많이 사용하는지 TF-IDF 방식으로 분석해 보았습니다. 가장 압도적인 키워드는 역시 '역세권'과 특정 지하철역 이름입니다. 상업용 부동산에서 입지가 가진 절대적인 중요성을 다시 한번 확인할 수 있습니다. 흥미로운 점은 '무권리'와 '테라스' 같은 키워드입니다. 초기 창업 비용을 절감할 수 있는 무권리 매물이나, 수요가 급증한 테라스 공간이 주요 셀링 포인트로 활용되고 있습니다. 이는 임차인이 단순히 면적만을 보는 것이 아니라, 실질적인 운영 혜택과 공간의 활용성을 중요하게 여긴다는 것을 의미합니다. 플랫폼 운영 측면에서는 이러한 키워드들을 태그화하여 검색 필터에 적용한다면 사용자 편의성을 크게 높일 수 있을 것입니다.
</div>

---

## 4. 가격 분포 분석 (보증금 & 월세)
<div class="content">
  <div style="display: flex; justify-content: space-around; gap: 20px;">
    <div style="text-align: center;">
      <img src="../images/v2_dist_deposit.png" width="100%" alt="보증금 분포">
      <p style="font-size: 0.7em;">보증금: 3천~1억 밀집</p>
    </div>
    <div style="text-align: center;">
      <img src="../images/v2_dist_rent.png" width="100%" alt="월세 분포">
      <p style="font-size: 0.7em; color: #ef4444;">월세 스윗스팟: 200~500만</p>
    </div>
  </div>
</div>

<div class="speaker-note">
  가장 중요한 가격 지표인 보증금과 월세의 분포입니다. 보증금 분포를 보면 3천만 원에서 1억 원 사이 구간에 대다수의 매물이 몰려 있습니다. 이는 일반적인 상가 임대차 시장의 표준적인 보증금 수준을 반영합니다. 월세 분포의 경우, 200만 원에서 500만 원 사이가 전체 매물의 핵심 구간인 'Sweet Spot'으로 나타났습니다. 이 구간은 소상공인이 감당할 수 있는 심리적 한계선과 임대인이 원하는 수익률이 맞물리는 지점입니다. 우리는 이 스윗스팟 구간의 매물을 집중적으로 큐레이션 하거나, 해당 가격대의 매물 등록 시 비교 견적 서비스를 제공함으로써 플랫폼의 매칭 효율을 극대화할 수 있습니다. 반면, 우측 끝에 위치한 초고가 매물들은 별도의 프리미엄 섹션으로 관리할 필요가 있습니다.
</div>

---

## 5. 보증금-월세 관계 및 이상치(Outlier)
<div class="content">
  <div style="text-align: center;">
    <img src="../images/v2_scatter_dep_rent.png" width="70%" alt="보증금-월세 산점도">
    <p style="font-size: 0.8em; margin-top: 10px; color: #0052cc;"><b>"시장 평균을 벗어난 특수 매물을 타겟팅하라"</b></p>
  </div>
</div>

<div class="speaker-note">
  보증금과 월세의 상관관계를 산점도로 나타낸 자료입니다. 일반적으로 보증금이 높으면 월세도 높아지는 양의 상관관계를 보이지만, 그래프 곳곳에서 튀는 데이터들, 즉 이상치들이 발견됩니다. 예를 들어, 보증금은 낮지만 월세가 매우 높은 매물은 단기 임대나 특정 사업을 위한 특수 매물일 가능성이 큽니다. 반대로 보증금은 높지만 월세가 낮은 매물은 임대인의 자금 회수 목적이 강한 매물일 수 있습니다. 이러한 이상치들을 분석하는 것은 매우 중요합니다. 평범한 범위를 벗어난 '초고가 프리미엄 매물'들을 따로 추출하여 'Premium Collection'이라는 이름으로 VIP 임차인들에게 제안할 수 있기 때문입니다. 데이터 분석을 통해 시장의 평균가격을 제시할 뿐만 아니라, 특수한 목적을 가진 매물들까지 선별해낼 수 있다는 점이 큰 수확입니다.
</div>

---

## 6. 업종별 매물 규모 및 가격
<div class="content">
  <div style="display: flex; justify-content: center;">
    <img src="../images/v2_bar_size_by_biz.png" width="85%" alt="업종별 규모">
  </div>
</div>

<div class="speaker-note">
  업종별로 매물의 규모와 가격이 어떻게 다른지 분석해 보았습니다. 막대그래프를 보시면 숙박시설이나 대형 병원 의원 부지들이 압도적인 평균 면적을 차지하고 있습니다. 반면 커피숍이나 소규모 공방, 일반 사무실은 상대적으로 작은 면적에 집중되어 있습니다. 업종에 따라 요구되는 공간의 크기가 확연히 다르다는 것을 알 수 있습니다. 이는 플랫폼의 검색 엔진이 단순히 '면적' 필터만 제공할 것이 아니라, 업종을 선택했을 때 해당 업종에 적합한 '추천 면적 범위'를 가이드해 줄 수 있어야 함을 시사합니다. 예를 들어 사용자가 '카페'를 선택하면, 15평에서 30평 사이의 매물을 우선적으로 보여주는 식의 데이터 기반 추천 시스템을 구축할 수 있습니다. 업종별 표준화된 데이터를 확보함으로써 고객에게 더 전문적인 컨설팅이 가능해집니다.
</div>

---

## 7. 층별 월세 분포 (Box Plot)
<div class="content">
  <div style="display: flex; justify-content: center;">
    <img src="../images/v2_box_floor_rent.png" width="85%" alt="층별 월세 분포">
  </div>
</div>

<div class="speaker-note">
  상가 매물에서 '층수'는 가격을 결정하는 가장 결정적인 요인 중 하나입니다. 박스 플롯을 통해 확인해 보겠습니다. 역시 1층 매물의 가격 중앙값과 상단 경계가 다른 층에 비해 월등히 높습니다. 접근성과 가시성이 매출과 직결되는 일반 판매업종에게 1층은 포기할 수 없는 위치이기 때문입니다. 반면, 지하층이나 고층부는 월세 수준이 현저히 낮고 가격 편차도 작습니다. 여기서 비즈니스 기회를 찾을 수 있습니다. 가시성보다는 공간의 크기나 합리적인 비용이 중요한 IT 사무실, 공유 주방, 스튜디오 업종 임차인들에게는 이러한 저층부나 고층부 매물을 '가성비 매물'로 적극 추천할 수 있습니다. 데이터는 각 층별로 적합한 업종이 무엇인지 명확히 알려주고 있으며, 이를 통해 타겟팅된 매칭 서비스를 제공할 수 있습니다.
</div>

---

## 8. 면적 대비 가격 분석 (Regression)
<div class="content">
  <div style="display: flex; align-items: center; gap: 30px;">
    <img src="../images/v2_reg_size_price.png" width="60%" alt="면적-가격 회귀분석">
    <div style="font-size: 0.9em; background: #f1f5f9; padding: 20px; border-radius: 10px;">
      <p><b>가성비 지수 도출</b></p>
      <p>회귀선 아래 매물 = <br><span style="color: #ef4444; font-weight: bold;">초강력 추천 가성비!</span></p>
    </div>
  </div>
</div>

<div class="speaker-note">
  면적과 월세의 관계를 회귀 분석 모델로 시각화했습니다. 가운데 파란색 직선이 면적에 따른 시장의 평균 가격선이라고 보시면 됩니다. 대다수의 매물이 이 선을 따라 분포하고 있습니다. 우리가 주목해야 할 것은 회귀선 아래쪽에 위치한 데이터 포인트들입니다. 이 매물들은 면적은 넓지만 월세는 시장 평균보다 낮게 책정된, 소위 '급매물' 혹은 '가성비 매물'들입니다. 데이터 분석을 활용하면 이런 매물들을 시스템적으로 자동 추출하여 사용자에게 '현재 시세 대비 저렴한 추천 매물' 리스트로 보여줄 수 있습니다. 단순히 저렴한 매물이 아니라, '데이터가 검증한 저렴한 매물'이라는 신뢰를 줄 수 있는 것입니다. 이러한 과학적 접근 방식은 네모 플랫폼이 타사 대비 가지는 기술적 우위와 전문성을 고객에게 각각 각인시키는 좋은 수단이 될 것입니다.
</div>

---

## 9. 지하철역별 시세 현황 (Heatmap)
<div class="content">
  <div style="text-align: center;">
    <img src="../images/v2_station_price.png" width="75%" alt="역별 시세">
  </div>
</div>

<div class="speaker-note">
  주요 지하철역별 시세를 히트맵으로 분석한 결과입니다. 강남역과 역삼역 주변이 가장 붉은색으로 표시되며 압도적인 시세를 형성하고 있습니다. 이는 단순한 유동인구를 넘어 기업들의 본사가 밀집된 경제 중심지로서의 가치가 반영된 결과입니다. 이 데이터를 활용하여 '네모 시세 지도' 서비스를 구축할 수 있습니다. 특정 지역에 매물을 내놓으려는 임대인에게는 주변 시세를 바탕으로 한 '적정 임대료 제안'을, 임차인에게는 예산에 맞는 '지역별 최적 입지 추천'을 제공할 수 있습니다. 부동산 거래에서 가장 큰 정보 비대칭은 바로 '시세 정보'입니다. 네모가 수집한 방대한 데이터를 정제하여 투명하게 공개함으로써, 우리는 시장의 표준을 만드는 데이터 플랫폼으로 거듭날 수 있습니다.
</div>

---

## 10. 요일별 등록 활동 패턴
<div class="content">
  <div style="display: flex; justify-content: center;">
    <img src="../images/v2_day_activity.png" width="85%" alt="요일별 활동">
  </div>
</div>

<div class="speaker-note">
  마지막으로 매물 데이터가 시스템에 등록되고 수정되는 시간적 패턴을 분석했습니다. 데이터 분석 결과, 화요일과 수요일 등 주 중반에 매물 활동이 가장 활발하게 일어납니다. 주말을 보낸 후 임대인과 공인중개사들이 본격적으로 업무에 복귀하여 매물을 관리하는 시점임을 알 수 있습니다. 이 데이터는 마케팅 부서에게 매우 중요한 단서가 됩니다. 사용자 알림(Push)이나 이메일 뉴스레터를 언제 발송해야 가장 효과적일까요? 바로 매물 업데이트가 가장 활발한 수요일 오전입니다. 새로운 정보가 가장 많이 쏟아지는 시점에 마케팅 화력을 집중함으로써, 사용자의 체류 시간과 앱 실행 횟수를 극적으로 높일 수 있습니다. 데이터는 우리가 언제 리소스를 집중해야 하는지에 대한 전략적인 방향을 제시해 줍니다.
</div>

---

## 11. 결론 및 향후 전략
<div class="content">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
    <div style="background: #e0f2fe; padding: 15px; border-radius: 10px;">
      <p style="font-weight: bold; color: #0369a1;">1. 타겟팅 고도화</p>
      <p style="font-size: 0.7em;">역세권/무권리 기반 SEO 강화</p>
    </div>
    <div style="background: #fef3c7; padding: 15px; border-radius: 10px;">
      <p style="font-weight: bold; color: #b45309;">2. 프리미엄 관리</p>
      <p style="font-size: 0.7em;">Outlier 데이터 기반 VIP 서비스</p>
    </div>
    <div style="background: #dcfce7; padding: 15px; border-radius: 10px;">
      <p style="font-weight: bold; color: #15803d;">3. 가성비 알고리즘</p>
      <p style="font-size: 0.7em;">회귀분석 기반 저평가 매물 추출</p>
    </div>
    <div style="background: #f3f4f6; padding: 15px; border-radius: 10px;">
      <p style="font-weight: bold; color: #374151;">4. 마케팅 최적화</p>
      <p style="font-size: 0.7em;">활동 피크 타임 푸시 마케팅</p>
    </div>
  </div>
</div>

<div class="speaker-note">
  지금까지 분석한 내용을 종합하여 향후 전략 네 가지를 제안하며 마무리하고자 합니다. 첫째, 키워드 분석 결과를 검색 엔진 최적화와 큐레이션에 즉각 반영하겠습니다. 고객이 원하는 가치를 태그로 구현하겠습니다. 둘째, 이상치 분석을 통해 하이엔드 시장을 공략할 수 있는 프리미엄 컬렉션 섹션을 신설하겠습니다. 셋째, 시세 및 회귀 분석 데이터를 제품 기능으로 녹여내어 '데이터가 추천하는 가성비 매물'과 '지역별 적정 시세 가이드'를 제공하겠습니다. 넷째, 활동 패턴 데이터를 기반으로 마케팅 자동화 시점을 최적화하여 운영 효율을 높이겠습니다. 데이터는 네모가 상업용 부동산 시장에서 가장 신뢰받는 플랫폼이 될 수 있는 유일한 증거입니다. 경청해 주셔서 감사합니다.
</div>

---

# Q&A
## 감사합니다!
