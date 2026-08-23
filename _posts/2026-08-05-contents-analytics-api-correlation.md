---
layout: post
title: "뇌피셜 대신 구글 API로: 유튜브와 블로그 지표의 숨겨진 상관관계 분석"
date: 2026-08-05 20:13:59 +0900
category: tech
excerpt: "유튜브와 블로그 API를 파이썬으로 연결해 데이터를 통째로 긁어보았습니다. 테크 영상의 패키징 딜레마와 블로그 교차 유입 시너지를 수치로 증명한 데이터 분석기입니다."
---

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#dilemma">1. 파워 영세 유튜버이자 초보 블로거의 딜레마</a></li>
    <li><a href="#youtube-skill">2. 데이터 수집의 실체: 플랫폼별 스킬 및 API 아키텍처</a></li>
    <li><a href="#youtube-analysis">3. 유튜브 지표 분석: 범인은 아기 영상이 아니었다?</a></li>
    <li><a href="#blog-analysis">4. 블로그 지표 분석: 롱테일과 크로스 채널 시너지의 발견</a></li>
    <li><a href="#action-item">5. 결론 및 향후 채널 + 블로그 운영 전략</a></li>
  </ul>
</div>

<h2 id="dilemma">1. 파워 영세 유튜버이자 초보 블로거의 딜레마</h2>

<p>
채널과 블로그를 동시에 운영하면서 항상 마음 한편에 풀리지 않는 딜레마가 하나 있었습니다. 바로 <b>'내가 올리고 싶은 콘텐츠'</b>와 <b>'구독자가 기대하는 콘텐츠'</b> 사이의 괴리입니다. 
</p>
<p>
저는 판교에서 일하는 개발자이자, 이제 갓 돌이 지난 아들(뚜기쿤)을 건사하는 아빠이기도 합니다. 그러다 보니 자연스레 회사에서 일하는 '테크/AI' 이야기뿐만 아니라, 집에서 뚜기와 부대끼는 '육아 일상'도 제 채널의 소중한 한 축입니다.
</p>
<p>
그런데 지표를 가만히 쳐다보고 있으면 왠지 모르게 아기나 가족 이야기를 전면에 내세운 영상은 테크 영상에 비해 조회수나 구독 증가폭이 힘을 못 쓰는 것처럼 느껴졌습니다. <i>'사람들은 내 찌질한 회사 얘기나 코딩하는 것만 보고 싶어 하고, 우리 뚜기 자라나는 모습은 덜 좋아하시나...?'</i> 하는 서운한 감정이 슬그머니 들기도 했죠.
</p>
<p>
여기에 깃허브 블로그(<code>panddu.github.io</code>)까지 신설해 글을 쓰기 시작하면서 딜레마는 두 배가 되었습니다. 과연 내 블로그에 글을 썼을 때 사람들이 실제로 얼마나 찾아오는지, 그리고 유튜브 영상이 블로그 유입으로 제대로 이어지고는 있는지 모든 것이 베일에 싸여 있었습니다.
</p>
<p>
하지만 개발자는 느낌이나 뇌피셜로 말하면 안 되는 법입니다. 진짜로 아기 영상이 외면받고 있는 건지, 그리고 유튜브와 블로그가 어떤 유기적 상관관계를 맺고 있는지 알아보기 위해 API로 수집한 실 데이터를 뜯어보기로 결심했습니다.
</p>

---

<h2 id="youtube-skill">2. 데이터 수집의 실체: 플랫폼별 스킬 및 API 아키텍처</h2>

<p>
먼저 이 귀찮은 데이터 수집 작업을 어떻게 자동화해 두었는지 가볍게 기술적으로 짚고 넘어가겠습니다. 제 AI 에이전트 세션에는 두 가지 분석 전용 스킬이 구축되어 있습니다. (참고로 이 데이터 수집 도구들이 포함된 전체적인 AI 자동화 파이프라인의 큰 구조에 대해서는 이전에 작성한 <a href="/posts/2026/08/panddu-ai-workflow/">Kotlin으로 LLM 연동부터 Whisper 자막 자동화, QnA 분류까지 나의 AI 활용 예시</a> 글에서 가볍게 소개해 드린 적이 있습니다.)
</p>

### 1) YouTube 분석 스킬 (<code>youtube</code>)
<p>
조회하고자 하는 데이터의 종류에 따라 <b>두 갈래 인증 방식(API Key / OAuth)을 영리하게 분기</b>하여 처리합니다.
</p>
<ul>
  <li><b>공개 메타 (<code>channel_meta.py</code>)</b>: 영구 API Key를 활용해 조회수, 좋아요, 댓글 수 등 공개된 수치 수집.</li>
  <li><b>Owner-Only 지표 (<code>analytics_report.py</code>)</b>: OAuth(<code>yt-analytics.readonly</code>) 인증을 거쳐 시청 지속시간, 평균 시청비율, 트래픽 소스, 일별 구독자 변동 수집.</li>
</ul>

### 2) 블로그 분석 스킬 (<code>blog-analytics</code>)
<p>
구글 애널리틱스 4(GA4)와 서치 콘솔(GSC) 데이터를 정밀 분석하기 위해 구축된 스킬입니다.
</p>
<ul>
  <li><b>GA4 (<code>ga4_report.py</code>)</b>: OAuth 소유 계정 인증을 통해 최근 인기 포스트, 유입 소스, 세션 수, 참여율 및 평균 세션 시간 분석.</li>
  <li><b>Search Console (<code>gsc_report.py</code>)</b>: 구글 검색 유입 키워드(검색어), 페이지별 클릭수, 평균 노출 순위 트래킹.</li>
</ul>

<p>
이 분석 도구들을 활용해 로컬 파이썬 스크립트에서 통계 연산 및 그룹핑 처리를 완료하고, 정제된 수치만 보고하는 분석 자동화 구조를 완성했습니다.
</p>

---

<h2 id="youtube-analysis">3. 유튜브 지표 분석: 범인은 아기 영상이 아니었다?</h2>

<p>
분석 대상 기간은 <b>2025년 10월 1일부터 2026년 6월 22일까지</b>로 잡았으며, 이 기간 업로드된 장편 본편 영상 32개를 모았습니다. 
</p>
<p>
단순히 '아기 영상', '테크 영상'으로 이분법적으로 나누지 않고, **첫인상인 '제목과 썸네일(패키징)'이 시청자에게 어떤 약속을 먼저 던지느냐**를 기준으로 4가지 패턴으로 촘촘히 분류해 D2, D7 조회수와 구독자 순증을 비교했습니다.
</p>

### 📊 유튜브 패키징 패턴별 지표 평균값

| 패키징 분류 | 평균 D2 조회수 | 평균 D7 조회수 | D7 평균 구독 순증 |
| :--- | :---: | :---: | :---: |
| **1. AI/회사 전면 (단독형)** | **6.9k** | **9.6k** | **+54.3명** |
| **3. AI 전면 (혼합형)** | **5.2k** | **6.6k** | **+15.0명** |
| **4. 아기 전면 (혼합형)** | **3.7k** | **4.5k** | **0명** |

<p>
지표상으로 확실히 테크 콘텐츠가 전면에 나설 때 조회수와 구독자 유입이 훨씬 강력했습니다. 반면 아기/가족을 전면에 앞세운 혼합형 영상은 평균 D7 조회수 <b>4.5k</b>에 구독 순증은 <b>0</b>에 수렴하는 수준이었습니다.
</p>

### 💡 숨겨진 반전: 클릭률 vs 평균 시청 비율
<p>
그런데 평균 시청 지속 비율(Average View Percentage) 데이터를 뜯어보았을 때 반전이 나타났습니다.
</p>
<p>
놀랍게도 <b>아기/가족 전면 단독형 영상의 평균 시청 비율이 테크 전면 영상보다 오히려 높거나 대등한 수준</b>이었습니다. 이는 영상이 재미없거나 품질이 떨어져서 시청자가 중간에 싫어서 나간 것이 아니라는 뜻입니다. 일단 영상을 누른 시청자들은 아기 이야기를 아주 몰입해서 끝까지 다 봐주셨던 겁니다.
</p>
<p>
결국 문제는 '콘텐츠 내용의 불만족'이 아니라, 클릭 이전의 <b>'첫인상(패키징)의 당김'</b>이 덜했다는 데 있었습니다. 채널 오디언스(구독자층)가 본질적으로 '개발, AI, 직장인' 훅에 가장 빠르게 반응하다 보니, 아기 중심 패키징은 기존 구독자들이 클릭을 주저하게 만들고, 이에 따라 알고리즘 노출도 조기에 마감되었던 것입니다.
</p>

---

<h2 id="blog-analysis">4. 블로그 지표 분석: 롱테일과 크로스 채널 시너지의 발견</h2>

<p>
그렇다면 새로 만든 블로그(<code>panddu.github.io</code>)의 성과는 어땠을까요? 최근 28일 동안 GA4 데이터를 통해 수집된 지표를 열어 보았습니다.
</p>

### 📈 블로그 기본 지표 (최근 28일 기준)
* **총 페이지뷰 (Screen Page Views)**: 1,088회
* **총 방문 사용자 (Total Users)**: 244명
* **세션 수 (Sessions)**: 386회
* **평균 세션 시간 (Average Session Duration)**: **289초 (약 4.8분)**
* **사용자 참여율 (Engagement Rate)**: 38.1%

<p>
블로그를 개설한 지 얼마 안 된 지금, 일 평균 사용자는 약 10명 내외에 불과한 아주 작은 규모입니다. 그런데도 <b>평균 체류 시간 4.8분, 참여율 38%</b>라는 숫자를 보고 있으면, 아직 초기 단계인데도 텍스트를 진득하게 읽고 가는 사람들이 있다는 신호로 읽혀 내심 반가웠습니다.
</p>

### 🏆 최근 인기 포스트 순위 (Top Page Views)

<div style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0;">
<table style="width: 100%; min-width: 480px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid var(--answer-border, #e3e8ff); text-align: left;">
      <th style="padding: 10px;">순위</th>
      <th style="padding: 10px;">페이지 경로 (pagePath)</th>
      <th style="padding: 10px;">페이지 타이틀</th>
      <th style="padding: 10px; text-align: center;">조회수 (PV)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid var(--answer-border, #e3e8ff);">
      <td style="padding: 10px; text-align: center;">1</td>
      <td style="padding: 10px;"><code>/posts/2019/04/spammaker/</code></td>
      <td style="padding: 10px;">스팸체 생성기</td>
      <td style="padding: 10px; text-align: center; font-weight: bold; color: #4B9CD3;">182</td>
    </tr>
    <tr style="border-bottom: 1px solid var(--answer-border, #e3e8ff);">
      <td style="padding: 10px; text-align: center;">2</td>
      <td style="padding: 10px;"><code>/posts/2026/08/panddu-ai-workflow/</code></td>
      <td style="padding: 10px;">Kotlin으로 LLM 연동부터 자막 자동화까지..</td>
      <td style="padding: 10px; text-align: center; font-weight: bold; color: #4B9CD3;">115</td>
    </tr>
    <tr style="border-bottom: 1px solid var(--answer-border, #e3e8ff);">
      <td style="padding: 10px; text-align: center;">3</td>
      <td style="padding: 10px;"><code>/posts/2026/06/ai-analysis-comm-style/</code></td>
      <td style="padding: 10px;">매일 이 계정주 부탁 들어주는 AI인데 현타 온다</td>
      <td style="padding: 10px; text-align: center;">47</td>
    </tr>
  </tbody>
</table>
</div>

<p>
여기서 발견한 지표의 비밀과 시너지는 크게 두 가지입니다.
</p>

#### ① 이제 막 들어오기 시작한 검색 유입의 씨앗
<p>
가장 높은 조회수를 기록한 글은 뜻밖에도 2019년에 다른 곳에 끄적여두었다가 이번에 이 블로그로 옮겨온 <b>'스팸체 생성기'</b>였습니다. 블로그를 만든 지 얼마 되지도 않았는데 벌써 구글 검색 엔진을 타고 외부 트래픽이 들어오고 있다는 건, 앞으로 글이 쌓일수록 이런 롱테일 유입이 더 늘어날 수 있겠다는 기대를 갖게 하는 초기 신호였습니다.
</p>

#### ② 유튜브 📢 ➔ 블로그 소소한 보완 📝 시너지
<p>
가장 인상적인 사례는 최근 8월 2일에 업로드했던 유튜브 영상과 연계된 <b>'Kotlin으로 LLM 연동부터 자막 자동화까지...'</b> 포스트였습니다. 
</p>
<p>
유튜브 영상 설명란과 댓글에 상세 코드 구현과 로직이 적힌 블로그 링크를 걸어두었는데, 단 며칠 만에 **115회 이상의 순수 뷰(사용자 51명 이상)**를 기록하며 인기 페이지 2위에 랭크되었습니다. 
</p>
<p>
유튜브 영상은 시각적인 훅을 주며 트래픽을 모으고, 영상 밖에서 텍스트로 가볍게 보완된 추가 내용을 읽고 싶은 사용자들은 블로그로 넘어와 긴 시간(평균 4.8분) 체류하며 정독하는 <b>'크로스 채널 데이터 깔때기'</b> 구조가 잘 굴러가고 있음이 증명된 셈입니다.
</p>

---

<h2 id="action-item">5. 결론 및 향후 채널 + 블로그 운영 전략</h2>

<p>
유튜브와 블로그의 API 지표를 크로싱하여 내린 최종적인 채널 및 블로그 융합 전략은 다음과 같습니다.
</p>

<ul>
  <li><b>유튜브와 블로그의 상호 보완 구조</b><br>
    유튜브 영상은 많은 사람이 흥미를 느낄 수 있는 요약과 호흡이 빠른 훅에 집중하고, 블로그는 영상으로 길게 다루기엔 애매하거나 소소해서 영상화가 곤란했던 가벼운 주제들을 편하게 모아두는 텍스트 저장소로 활용합니다.
  </li>
  <li><b>유튜브 패키징과 타겟 매칭에 대한 고민</b><br>
    물론 육아나 가족 일상 자체가 영상의 메인 주인공이 될 수밖에 없는 에피소드도 많겠지만, 채널 유입 성장을 적극적으로 겨냥해야 하는 특정 영상에 한해서는 썸네일과 타이틀 훅을 'AI/회사' 이야기로 앞세우고 뚜기와 가족의 따뜻한 일상은 후반부에 자연스럽게 배치해 보는 등의 패키징 실험을 열어두고 고민해 보려 합니다.
  </li>
  <li><b>블로그를 통한 롱테일 트래픽 확장</b><br>
    유튜브 영상은 시간이 지나면 추천 알고리즘의 수명이 다하지만, 블로그 글은 <b>'스팸체 생성기'</b> 사례에서 엿본 것처럼 시간이 지날수록 검색 노출을 통한 롱테일 트래픽을 쌓아갈 잠재력이 있습니다. 이제 막 걸음마를 뗀 블로그이니만큼, 영상에 들어간 기획이나 스크립트 중 유용한 팁들은 검색 엔진 최적화(SEO)를 고려해 꾸준히 블로그 텍스트로 쌓아가 보려 합니다.
  </li>
</ul>

<p>
데이터를 분석하기 전에는 유튜브 조회수 하락에 섭섭해하고, 이제 막 문을 연 블로그에 사람이 오긴 오는 건지 막연하기만 했는데, API 데이터를 결합해 보니 두 플랫폼이 어떻게 톱니바퀴처럼 서로를 밀어주고 있는지, 그리고 블로그의 초기 유입이 어떤 모양으로 시작되고 있는지 명확하게 볼 수 있었습니다. 역시 느낌 대신 데이터에 질문을 던지는 것이 가장 확실한 성장의 열쇠인 것 같습니다.
</p>

---

<div style="background: var(--answer-bg, #f6f8ff); border: 1px solid var(--answer-border, #e3e8ff); border-radius: 8px; padding: 16px 20px; margin: 24px 0 28px; font-size: 14.5px; line-height: 1.6; color: var(--ink);">
  <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; margin-bottom: 8px; font-size: 15.5px; color: var(--ink);">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="#4B9CD3" style="flex-shrink: 0; display: inline-block; vertical-align: middle; margin-top: -2px;">
      <g>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5"/>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5" transform="rotate(60 12 12)"/>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5" transform="rotate(120 12 12)"/>
      </g>
    </svg>
    <span style="display: inline-block; vertical-align: middle;">이 글은 Gemini 3.5 Flash와 함께 작성되었습니다</span>
  </div>
  이 포스팅은 판교 뚜벅쵸의 유튜브 채널 분석 스킬(<code>youtube</code>)과 블로그 방문 지표 분석 스킬(<code>blog-analytics</code>)의 실 데이터를 바탕으로, AI가 분석 흐름과 문체를 자연스럽게 녹여내어 작성했습니다.
</div>
