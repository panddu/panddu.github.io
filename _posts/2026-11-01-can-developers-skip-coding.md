---
layout: post
title: "\"개발 지식은 높은데 코딩을 아예 못 한다?\" 뽑는다 vs 안 뽑는다"
date: 2026-11-01 22:00:16 +0900
category: essay
excerpt: "데이터 분산과 아키텍처 설계는 시니어급인데, 자바든 뭐든 코드는 한 줄도 못 읽는다는 지원자. '이 사람 뽑을 것인가?'라는 가상의 딜레마 하나에 판교 개발팀 회의실에서 불붙은 찬반 난상토론을 기록해 봅니다."
---

<p style="margin: 0 0 24px;">
  <a href="https://youtu.be/SDbYbAoKoC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">▶ YouTube에서 영상으로 보기: “뽑는다? 안 뽑는다?”.. 판뚜네 개발팀 콜로세움 열렸습니다</span>
  </a>
</p>

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#prologue">1. 발단: “이런 지원자 오면 뽑으실 건가요?”</a></li>
    <li><a href="#pro-view">2. 찬성파 (탈 코딩파): "기술의 레이어가 올라갔듯, 필요한 역량이 바뀐 거다"</a></li>
    <li><a href="#con-view">3. 반대파 (친 코딩파): "누더기 코드와 장애의 굴레, 어쩔 건데?"</a></li>
    <li><a href="#real-dilemma">4. 회의실의 딜레마: 코드 에디터를 닫아버린 시니어들</a></li>
    <li><a href="#epilogue">5. 마치며: 결국 6개월 뒤엔 어떻게 될지 모른다</a></li>
    <li><a href="#youtube-section">🎬 토론 풀영상 보기</a></li>
  </ul>
</div>

<style>
  .toc-box {
    background: var(--surface, #f9fafb);
    border: 1px solid var(--line, #e5e7eb);
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 14.5px;
  }
  .toc-title {
    font-weight: bold;
    margin-top: 0 !important;
    margin-bottom: 10px !important;
    color: var(--ink, #1f2937);
  }
  .toc-box ul {
    margin: 0 !important;
    padding-left: 20px !important;
  }
  .toc-box li {
    margin-bottom: 6px;
  }
  .toc-box a {
    text-decoration: none;
    color: var(--primary, #0284c7);
  }
  .post-img-box {
    margin: 28px 0;
    text-align: center;
  }
  .post-img-box img {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    max-width: 100%;
    height: auto;
  }
  .post-img-caption {
    margin-top: 8px;
    font-size: 13.5px;
    color: #6b7280;
  }
</style>

<h2 id="prologue">1. 발단: “이런 지원자 오면 뽑으실 건가요?”</h2>

며칠 전, 뚜부인이 저한테 꽤나 흥미로운 면접 상황 하나를 불쑥 던져줬습니다.

서버 개발자 면접을 보는 **가상의 상황**을 하나 가정해 보죠.

어떤 지원자가 면접에 들어왔는데 대답을 기가 막히게 잘합니다. 데이터 분산 처리는 어떻게 할 건지, 로컬 캐시와 분산 캐시는 어떻게 나눌 건지, 아키텍처 설계와 문제 해결력 질문마다 막힘없이 술술 풀어내는 게 거의 시니어급 수준입니다.

‘오, 이 사람 진짜 일 잘하겠다’ 싶어서 뽑으려고 마지막 확인을 하는데, 지원자가 아주 담담하게 이런 가상의 폭탄선언을 던집니다.

<div class="post-img-box">
  <img src="/assets/img/posts/2026-11-01-can-developers-skip-coding/저코딩할줄모르는데요.png" alt="저 코딩 할 줄 모르는데요">
  <p class="post-img-caption">▲ 대답은 시니어급으로 완벽한데, 정작 코딩은 해본 적 없다는 가상의 면접자</p>
</div>

> **“근데 저, 자바든 파이썬이든 코딩을 한 번도 직접 해본 적은 없어요. 바이브 코딩으로 AI한테 시켜서 프로젝트를 다 만들었거든요. 코드를 꼭 읽고 쓸 줄 알아야 하나요?”**

개발 지식, 아키텍처 설계, 문제 해결 능력은 완벽한데, 정작 본인은 코드 한 줄을 스스로 읽거나 타이핑할 줄 모르는 상태.

이 기묘한 가상 시나리오를 두고 사무실에서 팀원들에게 툭 질문을 던져봤습니다.  
**“야, 만약 우리 팀 면접에 진짜 이런 지원자 오면 뽑을 거냐, 거를 거냐?”**

그 한마디에 회의실은 순식간에 난상토론장이 되어버렸습니다.

---

<h2 id="pro-view">2. 찬성파 (탈 코딩파): "기술의 레이어가 올라갔듯, 필요한 역량이 바뀐 거다"</h2>

우선 **찬성파(탈 코딩파)**, 즉 ‘뽑는다(혹은 긍정적으로 검토한다)’ 쪽에 선 팀원의 논리는 꽤나 파격적이면서도 설득력이 있었습니다.

비전공자로 개발을 시작했던 한 동료의 논리는 꽤 신선했습니다.

> *“소프트웨어 개발의 역사를 보면 늘 더 높은 추상화 레이어로 올라가는 과정이었잖아요. 예전엔 프레임워크나 라이브러리 없이 바닥부터 직접 짜는 게 기본기였지만, 지금은 잘 만들어진 도구를 레고 블록처럼 조합해서 비즈니스 문제를 빠르게 푸는 게 실력이 된 것처럼요. AI가 코드를 대신 짜주는 것도 결국 요구되는 역량의 층위가 바뀌어가는 자연스러운 흐름 아닐까요?”*

그 동료의 핵심 주장은 이거였습니다. **‘코드 자체를 짜는 능력’보다 ‘코드 바깥의 비즈니스 맥락을 AI에게 전달하는 능력’이 훨씬 중요해진 시대**라는 겁니다.

예를 들어, 10월 대규모 프로모션 때 어떤 종류의 트래픽이 몰릴지, 다른 부서와 협업할 때 어떤 예외 케이스를 고려해야 하는지 같은 맥락은 AI가 스스로 알 수 없습니다. 그런 거시적인 문제를 정의하고 AI에게 날카로운 질문을 던질 줄 안다면, 코드를 직접 타이핑하지 못하더라도 충분히 1인분 이상의 가치를 만들어낼 수 있지 않냐는 논리였죠.

문법만 달달 외워서 코드만 짤 줄 알고 설계는 엉망인 사람보다, 아키텍처와 문제 정의 능력이 탁월한 사람이 차라리 낫다는 의견이었습니다.

---

<h2 id="con-view">3. 반대파 (친 코딩파): "누더기 코드와 장애의 굴레, 어쩔 건데?"</h2>

하지만 **반대파(친 코딩파)**, 즉 ‘절대 안 된다’고 손사래를 치는 팀원들의 반격도 만만치 않았습니다. 현업에서 온갖 장애와 레거시를 겪어본 백엔드 엔지니어라면 절대 무시할 수 없는 현실적인 지적들이 터져 나왔죠.

반대파 동료들의 주장은 명확했습니다. **“AI가 짠 코드를 검증할 눈이 없으면 결국 대참사가 난다.”**

> *“A 버그 고쳐달라고 하고, B 버그 고쳐달라고 해서 나중에 코드 열어보면 완전 누더기 짜깁기 코드예요. AI는 당장 눈앞의 요구사항은 맞춰주지만, 전체 아키텍처의 정합성이나 비즈니스 예외 케이스를 입체적으로 보진 못하거든요.”*

또 다른 동료는 ‘장애 대응’의 공포를 꼬집었습니다.

> *“진짜 트래픽 터져서 장애 났을 때, AI한테 프롬프트 깎아서 물어볼 여유가 어디 있나요? 동시성 이슈나 멀티스레드 세이프 하지 않게 짜놓은 코드를 못 읽으면 ‘배포! 어? NPE 왜 나? 어? 수정해서 재배포!’ 하다가 끝없는 굴레에 갇히는 거죠.”*

데이터 타입에 대한 현실적인 예시도 나왔습니다.  
커머스 주문 수량 필드를 추가하는데, AI가 아무 생각 없이 `Int`로 박아둔 걸 보고 “어? 이거 대규모 트래픽이나 글로벌 확장 생각하면 `Long`으로 가야지”라고 제동을 걸어줄 수 있는 건 결국 코드를 읽을 줄 아는 엔지니어뿐이라는 이야기였습니다.

---

<h2 id="real-dilemma">4. 회의실의 딜레마: 코드 에디터를 닫아버린 시니어들</h2>

토론이 한참 이어지다 보니, 문득 재미있는 모순 하나가 회의실을 감돌았습니다.

**“근데 솔직히… 우리 요즘 코드 에디터 얼마나 열어보냐?”**

사실 저희 팀도 최근엔 PR을 올리면 사내 AI 리뷰 봇 두 개가 교차 검증을 해주고, 로컬 캐시 구조를 바꿀 때도 코드 한 줄 한 줄보다는 “이걸 한 번에 캐싱할지, 쪼갤지” 같은 구조와 전략 위주로 논의를 하거든요. 코드 파라미터나 디테일한 타이핑은 이미 AI에게 상당 부분 위임한 지 오래였습니다.

<div class="post-img-box">
  <img src="/assets/img/posts/2026-11-01-can-developers-skip-coding/1.jpg" alt="개발지식 설계 문제해결력은 완벽한데 코딩을 못함">
  <p class="post-img-caption">▲ 개발지식·설계·문제해결은 완벽한데 코딩을 못하는 지원자.. 회의실의 딜레마</p>
</div>

‘코드 에디터도 안 켜고 AI한테 일 시키는 우리가, 과연 면접자에게 코드를 읽을 줄 알아야 한다고 당당하게 말할 자격이 있는가?’

반대파 팀원에게 “만약 그 친구가 ‘코드는 못 읽지만, PR 봇과 테스트 코드를 다섯 겹으로 돌려서 무결성을 증명하겠다’고 하면 어떻게 할 거냐?”라고 물었을 때, 다들 쉽게 답을 내리지 못하고 머리를 긁적였습니다.

‘코드를 알아야 한다’는 당위는 분명한데, ‘왜 꼭 알아야 하는가?’를 따지고 들어가면 그 경계선이 6개월 전보다 훨씬 흐려져 있다는 사실을 모두가 체감하고 있었던 거죠.

---

<h2 id="epilogue">5. 마치며: 결국 6개월 뒤엔 어떻게 될지 모른다</h2>

한 시간 가까이 열띤 콜로세움이 펼쳐졌지만, 결국 결론은 **“모르겠다, 참 어렵다”**로 끝이 났습니다.

6개월 전의 저였다면 “코딩을 못하는 개발자가 대체 어디 있냐”며 1초 만에 탈락시켰을 겁니다. 하지만 지금은 그 질문을 듣고 선뜻 “당신은 그래서 안 됩니다”라고 단호하게 말하지 못하겠더라고요. 

어쩌면 우리는 ‘코딩(Implementation)’이라는 행위 자체가 개발자의 고유 영역에서 점차 도구의 영역으로 밀려나는 거대한 변곡점 한가운데를 지나고 있는지도 모르겠습니다.

6개월 뒤, 혹은 1년 뒤에는 또 어떤 괴물 같은 도구들이 나와서 우리의 이 진지한 고민을 우스꽝스럽게 만들어버릴지… 솔직히 잘 모르겠습니다.

<div class="post-img-box">
  <img src="/assets/img/posts/2026-11-01-can-developers-skip-coding/당신의선택.png" alt="당신의 선택">
  <p class="post-img-caption">▲ 여러분 회사 면접에 이런 지원자가 온다면, 당신의 선택은?</p>
</div>

여러분 회사 면접에 이런 지원자가 온다면,  
**여러분은 뽑으시겠습니까, 아니면 거르시겠습니까?**

---

<h2 id="youtube-section">🎬 토론 풀영상 보기</h2>

팀원들과 회의실에서 피 터지게(?) 나눈 실제 토론과 재현 영상은 아래 유튜브 채널에서 풀버전으로 시청하실 수 있습니다!

<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 24px 0 16px; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/SDbYbAoKoC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
</div>

<p style="margin: 0 0 28px;">
  <a href="https://youtu.be/SDbYbAoKoC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 영상으로 보기: “뽑는다? 안 뽑는다?”.. 판뚜네 개발팀 콜로세움 열렸습니다</span>
  </a>
</p>
