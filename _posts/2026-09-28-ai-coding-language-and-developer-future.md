---
layout: post
title: "\"어차피 AI가 다 짤 텐데 코틀린이 뭔 상관? 님 밥통 5년 컷\" 댓글을 보고"
date: 2026-09-28 21:00:00 +0900
category: essay
excerpt: "\"AI 시대에 언어가 무의미하다\", \"자바에 널세이프티만 있으면 코틀린은 사족이다\"라는 유튜브 댓글에 부쳐, 현업 백엔드 시니어 개발자가 생각하는 언어의 엄격함과 AI 시대 개발자의 밥통에 대해 솔직하게 적어봅니다."
---

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#lang-comparison">1. "AI가 다 짜주는데 정적 언어 중에 뭔 상관?" (러스트·TS·자바 vs 코틀린)</a></li>
    <li><a href="#syntactic-sugar">2. "자바에 널세이프티만 있으면 충분하다?" (코틀린 '슈가'의 실체)</a></li>
    <li><a href="#developer-future">3. "AI 때문에 님 밥통 5년 컷?" (코더와 엔지니어의 차이)</a></li>
    <li><a href="#conclusion">4. 마치며: 밥통 걱정할 시간에 도구를 더 부려먹읍시다</a></li>
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
  .comment-btn {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #fff1f0;
    color: #e62117 !important;
    border: 1px solid #ffd6d6;
    border-radius: 20px;
    padding: 7px 16px;
    font-size: 13.5px;
    font-weight: 600;
    text-decoration: none !important;
    box-shadow: 0 1px 3px rgba(230, 33, 23, 0.08);
    transition: all 0.2s ease;
  }
  .comment-btn:hover {
    background: #ffe3e1;
    border-color: #ffb8b8;
    transform: translateY(-1px);
    box-shadow: 0 3px 8px rgba(230, 33, 23, 0.16);
  }
</style>

안녕하세요, 판교 뚜벅쵸입니다.

얼마 전 저희 아내가 복직을 앞두고 코틀린과 인텔리제이로 아기 식단표 웹앱(Baby Meal Planner)을 만든 이야기를 <a href="https://youtu.be/UItGOxVeKC4" target="_blank" rel="noopener noreferrer">영상</a>과 [블로그 글](/posts/2026/09/baby-meal-planner-kotlin/)로 공유해 드렸었는데요.

영상에 아주 흥미롭고, 또 한편으로는 많은 분들이 가질 법한 날카로운 의문이 담긴 댓글이 하나 달렸습니다.

![유튜브 시청자 댓글](/assets/img/posts/2026-09-28/comment.png)

<p style="margin: 8px 0 20px; text-align: center;">
  <a href="https://www.youtube.com/watch?v=UItGOxVeKC4&lc=Ugx_hls2AXLfr9FJgwh4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-btn">
    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0 2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span>YouTube에서 댓글 원문 보기</span>
    <span style="font-size: 11px; opacity: 0.6;">↗</span>
  </a>
</p>

> *"어짜피 ai 써서 코드짤탠데 코틀린이든 자바든 러스트든 타입스크립트든 뭔 상관임? 그리고 코틀린이 널세이프티 관련까진 좋은데 쓸데없는 syntactic sugar 너무 많아서 그냥 자바에 널세이프티만 해결한 버전 나오면 그냥 그게 더 낫겠다 느낌... 결론은 ai땜에 님 밥통 사라질날도 얼마 안남았단 말임 최대 5년??"*

댓글을 보고 피식 웃음이 났습니다.

우선 제 밥통 유효기간을 5년이나 넉넉하게 잡아주셔서 진심으로 감사하다는 말씀부터 드리고 싶습니다. 솔직히 요즘 AI 모델 발전 속도를 보면 5년이면 너무 관대하신 거 아닌가 싶거든요. 전 한 2년 봤는데 말이죠. 5년이면 저희 집 아들 은호 유치원 졸업하고 초등학교 들어갈 때까지는 먹여 살릴 수 있는 시간이라 오히려 안도감이 들 지경입니다.

이 댓글에는 사실 **현재 많은 개발자와 입문자분들이 AI 코딩을 바라보는 3가지 핵심 쟁점**이 모두 압축되어 있습니다.

1. **AI가 짜는데 언어가 정말 상관없을까?**
2. **코틀린의 문법적 설탕(Syntactic Sugar)은 정말 쓸데없는 사족일까?**
3. **진짜로 5년 뒤면 개발자 밥통이 깨질까?**

현업에서 매일 AI 에이전트를 끼고 백엔드 레거시와 씨름하는 시니어 개발자 입장에서, 솔직한 제 생각을 차근차근 정리해 보았습니다.

---

## <span id="lang-comparison">1. "AI가 다 짜주는데 정적 언어들(자바, 러스트, TS, 코틀린) 중에 뭔 상관?"</span>  
👉 **정적 언어의 중요성을 짚은 건 맞습니다. 하지만 그중에서도 '코틀린'이어야 했던 이유가 있습니다.**

우선 인정할 건 쿨하게 인정하고 넘어가야 합니다.

댓글 작성자분께서 예시로 든 언어들(자바, 러스트, 타입스크립트, 코틀린)은 모두 **타입을 정적으로 다루는 언어들**입니다. 이 점에서 댓글 작성자분의 통찰은 아주 날카롭습니다.

AI 코딩 시대에 파이썬이나 순수 자바스크립트 같은 동적 언어는, AI가 환각(Hallucination)으로 잘못된 속성을 참조하거나 타입을 삐끗해도 컴파일 시점에 아무런 경고도 주지 않습니다. 결국 새벽에 런타임 에러(`AttributeError`, `TypeError`)가 터지면서 사람이 디버깅 지옥에 빠지죠. 반면 정적 타입 언어들은 컴파일러가 AI의 멱살을 잡고 즉각적인 기계적 피드백(Feedback Loop)을 주기 때문에, AI와의 협업 효율이 차원이 다릅니다.

그렇다면 **"정적 언어들끼리 비교했을 때도 정말 아무거나 써도 상관없을까?"**  
아닙니다. AI 바이브 코딩으로 주말에 빠르고 안전하게 프로덕트를 뽑아내야 하는 상황이라면, 이 네 언어의 체감 난이도와 생산성은 완전히 갈립니다.

#### ① vs Rust (러스트): 강력하지만 바이브 코딩의 템포를 끊는 컴파일러
러스트는 메모리 안전성과 성능에서 의심할 여지 없는 최고의 언어입니다. 하지만 AI에게 러스트 코드를 맡겨보면 곧바로 **소유권(Ownership), Borrow Checker, 그리고 라이프타임(Lifetime) 지옥**을 맛보게 됩니다.  
AI는 조금만 로직이 복잡해져도 소유권 에러를 해결하지 못해 `clone()`을 코드 전체에 남발하거나, 컴파일 에러를 고치려다 다른 라이프타임 에러를 뿜는 핑퐁 루프에 갇히기 십상입니다. 주말에 식단표 앱 하나 뚝딱 만들어야 하는데, 러스트 컴파일러와 기싸움하다가 주말이 다 끝납니다.

#### ② vs TypeScript (타입스크립트): 화려한 컴파일 타임, 그러나 허술한 런타임
타입스크립트는 웹 프론트엔드와 풀스택에서 최고의 언어입니다. 하지만 백엔드로 들어오면 본질은 결국 '런타임 자바스크립트'입니다.  
TS의 타입 시스템은 컴파일이 끝나면 런타임에 완전히 증발(Type Erasure)합니다. DB에서 넘어오는 데이터나 외부 API 응답 경계면에서 Zod 같은 런타임 스키마 검증 라이브러리를 덕지덕지 바르지 않으면, AI가 만든 코드에서 여전히 `undefined is not a function` 같은 런타임 폭탄이 터집니다. 게다가 매번 발목을 잡는 Node.js 생태계의 의존성 설정(ESM vs CommonJS 충돌, 빌드 설정 지옥)은 바이브 코딩의 흐름을 뚝뚝 끊어놓습니다.

#### ③ vs Java (자바): 안정적이지만 AI의 컨텍스트를 갉아먹는 보일러플레이트
자바는 30년 프로덕션 역사를 자랑하는 백엔드의 절대 강자입니다. 하지만 코드가 너무 장황합니다.  
같은 비즈니스 로직을 구현해도 자바는 코틀린보다 코드 라인 수가 2~3배는 길어집니다. 타이핑이야 AI가 해준다 쳐도, 이게 왜 문제일까요? **AI에게 기존 코드를 읽히고 수정할 때 먹여야 하는 컨텍스트(Context Window)가 불필요하게 뚱뚱해지기 때문입니다.** 긴 보일러플레이트 코드는 토큰 비용을 낭비시킬 뿐만 아니라, LLM 모델의 주의력(Attention)을 분산시켜 정작 중요한 비즈니스 로직에서 실수를 유발합니다. 게다가 타입 레벨의 원천적 Null Safety가 없다는 치명적인 약점도 여전하죠.

#### ④ 코틀린이 가진 완벽한 '스위트 스팟 (Sweet Spot)'
코틀린은 바로 이 정적 언어들 사이에서 가장 실용적인 **균형점**을 찾아낸 언어입니다:

- 러스트처럼 컴파일러가 사납지 않아서 **AI가 막힘없이 빠른 템포로 코드를 쳐낼 수 있고**,
- 타입스크립트와 달리 JVM 바이트코드 레벨에서 **런타임 타입과 Null Safety(`Type?`)를 엄격하게 보장**하며,
- 자바 대비 훨씬 압축되고 간결한 문법 덕분에 **AI에게 전달하는 컨텍스트 밀도가 극대화(토큰 절약)**됩니다.
- 그러면서도 자바의 30년 오픈소스 생태계와 Gradle 기반의 무결한 빌드 환경을 100% 그대로 흡수합니다.

결국 "정적 언어니까 아무거나 써도 그게 그거"가 아니라, **"AI의 빠른 생산성을 갉아먹지 않으면서도 가장 단단한 안정성을 주는 스위트 스팟"**에 코틀린이 있었기 때문에 선택한 것입니다.

---

## <span id="syntactic-sugar">2. "코틀린 문법적 설탕(Syntactic Sugar) 많다? 자바에 널세이프티만 있으면 충분하다?"</span>  
👉 **그 '슈가'가 걷어내 준 수만 줄의 버그 유발 코드를 생각해보면요.**

댓글 작성자분께서는 코틀린의 다양한 문법 요소들을 "쓸데없는 장식(Sugar)"으로 보셨고, "차라리 자바에 Null Safety만 들어간 버전이 나오면 낫겠다"고 하셨습니다.

자바 진영도 최근 눈부시게 발전하고 있습니다. `record`, 패턴 매칭, 가상 스레드(Virtual Threads) 등 코틀린의 좋은 점들을 흡수하며 빠르게 현대화되고 있죠. 저 역시 자바를 10년 넘게 써온 입장에서 자바의 진화를 진심으로 응원합니다.

하지만 **"자바에 널세이프티만 추가하면 코틀린보다 낫다"**는 기술적으로 불가능에 가까운 희망사항입니다.

자바의 가장 위대한 자산이자 동시에 가장 무거운 족쇄는 바로 **'30년 묵은 하위 호환성(Backward Compatibility)'**입니다.  
자바는 1995년에 짠 코드도 최신 JDK에서 돌아가는 걸 지향하는 언어입니다. 그런 자바가 이제 와서 언어 타입 시스템 밑바닥을 갈아엎어 `String`과 `String?`을 언어 차원에서 구분한다? 기존의 수십억 줄짜리 오픈소스 생태계와 기업들의 레거시 코드가 전부 깨집니다. 

그래서 자바는 고육지책으로 `@Nullable`, `@NotNull` 같은 어노테이션이나 `Optional<T>` 같은 래퍼 객체를 도입했지만, 써보신 분들은 아실 겁니다. 강제력도 약하고 코드만 더 장황해진다는 걸요.

그리고 코틀린의 '문법적 설탕'들은 단순히 겉멋 부리려고 넣은 화장품이 아닙니다.
- **Smart Cast**: `if (obj is String)` 체크하면 개발자가 굳이 `(String) obj` 캐스팅 안 해도 알아서 처리
- **Data Class & 불변성**: 게터, 세터, `equals()`, `hashCode()`, `copy()` 손수 짜다 생기던 버그 원천 차단
- **Extension Functions & Scope Functions**: 의미 없는 유틸 클래스 남발 없이 비즈니스 로직을 물 흐르듯 읽히게 만드는 힘

이 '슈가'들은 개발자가 **비즈니스 로직의 의도(Intent)**에만 집중할 수 있게 기계적인 노가다를 언어 차원에서 흡수한 결과물입니다. 그게 없던 시절, 자바 개발자들이 롬복(Lombok) 억지로 끼워 넣다가 IDE 깨지고 컴파일러 꼬이며 고통받았던 역사를 떠올려보면 코틀린의 설계가 얼마나 실용적인지 실감하게 됩니다.

---

## <span id="developer-future">3. "AI 때문에 님 밥통 5년 컷?"</span>  
👉 **단순히 '코드를 치는 사람'의 밥통은 이미 깨지고 있습니다. 하지만…**

마지막으로 가장 흥미진진했던 밥통 이야기입니다. 다시 생각해도 "최대 5년"은 참 따뜻한 전망입니다. 현업에 있다 보면 체감상 2년 뒤도 까마득하거든요.

냉정하게 인정할 건 인정해야 합니다. 만약 어떤 개발자의 업무가 기획서 보고 CRUD API 타이핑 치고, 화면 퍼블리싱 긁어다 붙이는 게 전부였다면? 5년은커녕 지금 당장 위험한 게 맞습니다. 그런 단순 노동은 지금의 AI도 이미 기가 막히게 잘하니까요.

하지만 현업에서 진짜 소프트웨어를 만드는 일은 '타이핑'이 10%도 안 됩니다.

- 기획자가 자기도 모르는 숨은 엣지 케이스를 집요하게 파고들어 요구사항을 정의하고,
- 회사의 10년 묵은 결제 DB와 정합성을 맞추기 위해 트랜잭션 격리 수준을 고민하며,
- AI가 그럴싸하게 짜놓은 코드 속에 숨어있는 동시성 버그나 슬로우 쿼리를 잡아내고,
- **시스템이 터졌을 때 "이건 AI가 짰는데요?"라고 핑계 댈 수 없으니 온전히 최종 책임을 지는 일.**

소프트웨어 개발의 본질은 **'책임'**과 **'의사결정'**입니다.  
AI가 코드를 10배 빨리 생성해 낼수록, 그 코드가 만들어낼 버그와 기술 부채를 감당하고 검증할 수 있는 사람의 가치는 오히려 더 올라갑니다.

AI가 발전해서 제 밥통이 2년 뒤에 깨질지, 5년 뒤에 깨질지는 저도 모릅니다. 미래는 아무도 장담할 수 없으니까요.  
하지만 한 가지 확실한 건 있습니다.

"어차피 AI가 다 해줄 텐데 공부해서 뭐 해?", "어차피 망할 텐데 언어가 뭐가 중요해?" 하고 냉소하며 손 놓고 있는 사람의 밥통이 제일 먼저 깨질 거라는 사실입니다.

---

## <span id="conclusion">마치며: 밥통 걱정할 시간에 도구를 더 부려먹읍시다</span>

2년이든 5년이든 제 밥통의 수명이 언제까지일지는 모르겠지만, 적어도 그 시간 동안 저는 AI라는 강력한 부사수를 옆에 끼고 예전 같으면 상상도 못 했을 속도로 문제를 해결해 나갈 생각입니다.

아내와 함께 주말에 식단표 앱을 뚝딱 만들고, 레거시 코드를 정리하고, 아낀 시간으로 아들 은호랑 놀이터에서 미끄럼틀 한 번 더 타는 것. 

AI 시대에 우리가 취해야 할 태도는 막연한 공포나 시니컬한 방관이 아니라, **"이 기가 막힌 도구로 오늘 내 삶의 어떤 문제를 더 빠르고 재밌게 풀 것인가"**에 집중하는 게 아닐까 싶습니다.

<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 30px 0 16px; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/UItGOxVeKC4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
</div>

<p style="margin: 0 0 28px;">
  <a href="https://youtu.be/UItGOxVeKC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0 2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 관련 영상 보기 (뚜데 39)</span>
  </a>
</p>

---

*이 글은 Gemini 3.8 Flash와 함께 작성되었습니다.*
