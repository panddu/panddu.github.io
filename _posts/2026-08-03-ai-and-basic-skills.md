---
layout: post
title: "AI는 너무 빠른데 기본기는 조급하고.. 무엇을 더 해야 할까요?"
date: 2026-08-03 20:35:22 +0900
category: essay
image: /assets/img/posts/2026-08-03/thumbnail.jpg
excerpt: "기술 발전의 속도에 조급함을 느끼는 취준생분들을 위해, 시니어 개발자로서 생각하는 AI 시대의 기본기와 효율에 대한 솔직한 이야기."
---

![대표 썸네일](/assets/img/posts/2026-08-03/thumbnail.jpg)

<div style="background: var(--answer-bg, #f6f8ff); border: 1px solid var(--answer-border, #e3e8ff); border-radius: 8px; padding: 16px 20px; margin: 24px 0 28px; font-size: 14.5px; line-height: 1.6; color: var(--ink);">
  <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; margin-bottom: 8px; font-size: 15.5px; color: var(--ink);">
    <svg viewBox="0 0 24 24" width="20" height="20" style="flex-shrink: 0; display: inline-block; vertical-align: middle; margin-top: -2px;">
      <defs>
        <linearGradient id="gemini-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#1ba0fc" />
          <stop offset="40%" stop-color="#8a3ffc" />
          <stop offset="80%" stop-color="#e7347a" />
          <stop offset="100%" stop-color="#f99f1b" />
        </linearGradient>
      </defs>
      <path fill="url(#gemini-grad)" d="M12 2a1 1 0 0 1 .968.756c.866 3.593 3.683 6.41 7.276 7.276a1 1 0 0 1 0 1.936c-3.593.866-6.41 3.683-7.276 7.276a1 1 0 0 1-1.936 0c-.866-3.593-3.683-6.41-7.276-7.276a1 1 0 0 1 0-1.936c3.593-.866 6.41-3.683 7.276-7.276A1 1 0 0 1 12 2z"/>
    </svg>
    <span style="display: inline-block; vertical-align: middle;">이 글은 Gemini 3.5 Flash가 작성하였습니다</span>
  </div>
  이 포스팅은 판교 뚜벅쵸의 유튜브 댓글 및 대댓글을 바탕으로 <b>'판교 뚜벅쵸 페르소나'를 사전에 분석하여</b> 저 고유의 문체와 생각의 흐름을 반영해 작성되었습니다.
</div>

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#intro">1. 조급함을 부르는 질문 하나</a></li>
    <li><a href="#ai-is-tool">2. AI는 작업 효율을 올리는 '도구'일 뿐입니다</a></li>
    <li><a href="#why-basic-skills">3. 왜 기본기가 AI 활용 능력의 뼈대가 될까요?</a></li>
    <li><a href="#how-to-deal-anxiety">4. 기술의 속도 앞에서 조급함을 다스리는 법</a></li>
    <li><a href="#conclusion">5. 결론: 결국은 묵묵히 쌓아가는 힘</a></li>
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
    padding-left: 0 !important;
    list-style: none !important;
    list-style-type: none !important;
  }
  .toc-box li {
    margin-bottom: 6px;
    list-style: none !important;
  }
  .toc-box a {
    color: var(--accent, #5b6cff);
    text-decoration: none;
    font-weight: 500;
  }
  .toc-box a:hover {
    text-decoration: underline;
  }
  [id] {
    scroll-margin-top: 90px;
  }
</style>

안녕하세요, 판교 뚜벅쵸입니다.

얼마 전에 유튜브에 <a href="https://youtu.be/uHRUcb_gXIQ" target="_blank" rel="noopener noreferrer">AI 워크플로우 영상</a>을 하나 올렸습니다. 제가 매일 작업하면서 생산성을 높이기 위해 구축해 둔 도구들을 소개하는 영상이었는데요. 감사하게도 많은 분이 관심을 가져주셨습니다. 

그런데 그 영상의 댓글을 보다가 유독 마음이 쓰이는 질문이 하나 있더라고요. 한 취준생 분이 남겨주신 댓글이었는데, 대략 요런 내용이었습니다.

> "Java, Spring, JPA, MySQL 같은 공부할 기술들은 이미 너무 많은데, AI의 발전 속도는 눈부시게 빠릅니다. 개념들을 제대로 알아야 AI도 잘 쓰겠다 싶다가도, 잘 모르더라도 일단 AI 사용법을 먼저 배워야 하는 건가 싶어서 마음이 갈수록 조급해지네요..😥"

이 고민, 아마 요즘 개발을 시작하거나 준비하시는 분들이라면 한 번쯤은 머릿속을 스쳐 지나갔을 이야기인 거 같아요. 저 역시 매일 쏟아지는 새로운 기술과 도구들을 보면서 머쓱해지거나 조급해질 때가 있거든요. 

짧은 댓글로만 답을 드리기엔 아쉬움이 남아서, 제 생각을 블로그에 조금 더 진솔하게 정리해 보려고 합니다.

---

## <span id="intro">❓ 조급함을 부르는 질문 하나</span>

앞서 말씀드린 시청자분의 질문처럼, 요즘 학습 속도에 조급함을 느끼시는 분들이 정말 많은 거 같습니다. 

"내가 이 두꺼운 기본서들을 언제 다 보고 기본기를 닦지? 그 시간에 최신 AI 툴 사용법을 익히는 게 트렌드에 더 맞는 거 아닌가?"

이런 생각이 드는 건 너무나 자연스러운 현상입니다. 특히 취업 시장의 문턱이 점점 더 높아지고, AI가 개발자를 대체할 거라는 자극적인 뉴스들이 쏟아지는 환경 속에서는 더욱더 그렇겠죠. 하지만 이럴 때일수록 시선을 밖이 아니라 나의 기본기로 돌릴 필요가 있습니다.

---

## <span id="ai-is-tool">🔨 AI는 작업 효율을 올리는 '도구'일 뿐입니다</span>

결론부터 말씀드리자면, 제 대답은 **"무조건 기본 실력 다지기가 먼저다"** 입니다. 

제가 올린 영상 속의 화려한(?) AI 자동화 파이프라인이나 워크플로우를 보셨다면 오해하기 쉬운데요. 자세히 뜯어보면 거기에는 개발에 대한 로직이나 심오한 설계 같은 게 들어있지 않습니다. 그저 제가 머릿속으로 '이렇게 짜야지'라고 구성해 둔 설계를 AI가 더 빠르게 타이핑하게 돕고, 귀찮은 자막 파일 검수나 포스팅 포맷팅 같은 작업을 대신해 주는 것뿐입니다.

즉, AI는 작업의 효율을 극적으로 끌어올리는 도구이지, 개발 그 자체를 대신해 주는 해결사가 아니라는 점입니다. 도구를 쥐여줘도 도구가 만들어 낸 결과물이 맞는지 틀린지 검수할 능력이 없다면 아무런 의미가 없지 않을까 싶습니다.

---

## <span id="why-basic-skills">🧠 왜 기본기가 AI 활용 능력의 뼈대가 될까요?</span>

우리가 흔히 공부하는 Java, Spring Framework, JPA, MySQL 같은 백엔드 기술들은 단순히 취업을 위한 스택을 넘어 개발의 '기본기'에 속합니다. 

AI에게 코딩을 시켜보신 분들은 다들 공감하실 텐데요. 질문을 구체적으로 잘 던질수록 AI는 더 좋은 코드를 뱉어냅니다. 그런데 그 질문(프롬프트)을 잘 던지려면 내가 무엇을 모르는지, 그리고 지금 시스템의 병목이 어디서 발생하는지 명확히 알고 있어야 합니다.

예를 들어, 데이터베이스 조회 쿼리가 너무 느려서 AI에게 최적화를 부탁한다고 해볼게요. 
JPA의 동작 원리와 영속성 컨텍스트, 그리고 인덱스(Index)의 작동 원리를 모르는 상태라면 AI가 던져주는 `N+1 문제` 해결책이나 `Fetch Join` 혹은 `QueryDSL` 리팩토링 코드를 마주했을 때 눈앞이 캄캄해질 수밖에 없습니다. 이게 왜 최적화가 되는지 모른 채 그저 복사해서 붙여넣기만 한다면, 당장은 돌아갈지 몰라도 언젠가 더 큰 장애나 유지보수 지옥으로 돌아오게 되더라고요.

결국 기술의 밑바닥에 흐르는 개념과 원리를 아는 것과, AI라는 도구를 다루는 건 완전히 별개의 문제입니다. AI를 진짜 내 무기로 활용하기 위해서라도 개념을 확실하게 내 것으로 만드는 노력이 선행되어야 한다고 저는 생각합니다.

---

## <span id="how-to-deal-anxiety">⏳ 기술의 속도 앞에서 조급함을 다스리는 법</span>

발전 속도가 너무 빨라서 도무지 따라갈 수 없을 것 같다는 불안감, 당연합니다. 하지만 조금만 냉정하게 생각해보면, 지금 쏟아지는 수많은 AI 툴들도 결국 우리가 만드는 소프트웨어의 한 종류일 뿐입니다.

프레임워크나 툴의 트렌드는 1~2년 만에 확확 바뀌기도 하지만, 그 아래에 있는 본질적인 컴퓨터 사이언스(CS) 지식이나 데이터베이스 모델링, 네트워크 동작 방식, 그리고 좋은 객체지향 설계 원칙 같은 것들은 10년이 지나도 쉽게 변하지 않습니다. 

저 역시 시니어 개발자로서 현업에서 개발을 계속해 오고 있지만, 매번 새로운 라이브러리가 나올 때마다 밤새워 공부하지는 않습니다. 대신 '이 툴은 내부적으로 어떤 구조로 돌까?'를 먼저 봅니다. 기본기가 단단하게 잡혀 있으면 새로운 라이브러리나 AI 도구가 등장해도 며칠 슥 훑어보면 금방 적응하게 되기 때문입니다.

지금 당장 옆자리에서 누군가 챗GPT를 써서 멋진 프로그램을 뚝딱 만들었다고 해서 조급해하실 필요 전혀 없습니다. 묵묵히 책을 펴고, 기본 개념을 한 장씩 이해하며 나아가는 사람이 결국 끝까지 살아남고 더 멀리 가게 됩니다.

---

## <span id="conclusion">✨ 결론: 결국은 묵묵히 쌓아가는 힘</span>

조급한 마음이 들 때마다 스스로에게 이렇게 질문해 보시면 좋을 거 같아요. 

*"내가 AI에게 코딩을 대신 시켜놓고, 그 코드가 맞는지 검증할 수 있는 눈을 가지고 있는가?"*

만약 그 대답이 망설여진다면, 지금은 AI 트렌드를 쫓아다니기보다 스프링의 빈 생명주기를 공부하고, MySQL의 실행 계획을 뜯어보고, Java의 메모리 구조를 한 번 더 이해하는 데 시간을 쏟는 게 맞습니다. 

불안하고 지치는 취업 준비 기간이겠지만, 스스로의 속도를 믿고 묵묵히 뼈대를 세워가시기를 응원합니다. 저도 제 자리에서 제 코드를 짜며 계속 응원하겠습니다. 

감사합니다.
