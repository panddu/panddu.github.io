---
layout: post
title: "복직 앞두고 Kotlin한테 육아 도우미 시킨 개발자 엄마의 사연 (feat. JetBrains)"
date: 2026-09-27 22:00:00 +0900
category: essay
image: /assets/img/posts/2026-09-17/1.png
excerpt: "복직을 한 달 앞둔 개발자 아내가 아기 식단표를 짜기 위해 직접 웹앱을 개발했습니다. 100% AI 바이브 코딩 시대에 우리가 파이썬 대신 Kotlin과 IntelliJ IDEA를 선택한 이유를 정리해봅니다."
---

<p style="margin: 22px 0 26px;">
  <a href="https://youtu.be/UItGOxVeKC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 관련 영상 보기 (뚜데 39)</span>
  </a>
</p>

> 💡 *이 글은 JetBrains로부터 지원을 받아 제작된 영상을 요약하였습니다.*

<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 24px 0; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/UItGOxVeKC4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
</div>

얼마 전 유튜브 영상에서 말씀드렸듯이, 저는 AI 시대의 가장 큰 매력이 **"내가 필요한 도구를 내가 직접 빠르게 뚝딱 만들어 낼 수 있다는 점"**에 있다고 생각합니다.

이번에는 저희 집 뚜부인(아내)의 실제 사례를 소개해 보려고 합니다. 복직을 딱 한 달 앞두고, 본인이 매일 겪어야 할 아주 현실적인 문제를 해결하기 위해 직접 웹앱을 하나 만들었습니다.

---

### 매주 21끼 식단표, 보통 일이 아닙니다

이유식이나 유아식 챙겨보신 분들은 다 아실 겁니다. 이게 진짜 보통 일이 아니거든요.

- 매주 7일 3끼, 총 **21끼 식단표**를 짜야 하고
- 소고기, 닭고기, 생선, 달걀, 두부 등 필수 단백질 6가지를 매 끼니 겹치지 않게 분배해야 합니다.
- 거기에 냉장고 재고 파악, 장보기 스케줄, 전날 밤 손질 목록까지...

시간 누수 없이 챙기려면 체계적인 관리가 필수인데, 엑셀이나 메모장으로는 한계가 명확했습니다.

![Baby Meal Planner - 식단표 UI](/assets/img/posts/2026-09-17/2.png)

그래서 뚜부인이 직접 기획하고 구현했습니다. 이름하여 **Baby Meal Planner**.

엄마가 원하는 레시피와 식재료, 영양 성분을 처음에 yml로 한 번 싹 입력해 두면:
1. 서버가 영양소가 고루 분배되도록 겹치지 않게 식단표를 짜주고,
2. 전날 밤 밑작업 목록과 주말 장보기 리스트를 뽑아주며,
3. 요리 후 애매하게 남은 재료는 로컬 LLM(Ollama)이 **"지금 남은 재료로 만들 수 있는 대체 요리"**를 추천해 줍니다.

---

### "어차피 AI가 다 짜주는데 언어가 뭐가 중요해?"

솔직히 고백하자면, 이 프로젝트는 뚜부인이 100% **AI 바이브 코딩**으로 만들었습니다.

보통 가벼운 자동화나 개인 토이 프로젝트라고 하면 Python이나 Node.js 같은 스크립트 언어를 먼저 떠올리실 텐데요. 현업 개발자 입장에서 솔직히 스크립트 언어는... 환경설정하다가 화병 나는 경우가 많습니다.

가상환경(venv) 잡고 패키지 버전 충돌 해결하느라 시간 다 쓰고 나면 정작 코딩할 힘이 빠지죠. 반면 JVM 기반 Gradle 프로젝트는 JDK 하나만 있으면 `gradlew` 명령어 한 방으로 Mac이든 Windows든 100% 동일하게 빌드됩니다. 세팅 스트레스가 아예 없습니다.

그리고 역설적이게도 **AI가 코드를 짜주기 때문에 Kotlin이라는 언어가 훨씬 빛을 발합니다.**

![Java vs Kotlin 코드 비교](/assets/img/posts/2026-09-17/3.png)

#### 1. 간결한 문법과 토큰 절약
Java에 익숙한 분들이라면 다 아는 그 지긋지긋한 보일러플레이트 코드. Kotlin은 군더더기를 싹 걷어냈습니다. 코드가 짧고 직관적이니 가독성도 좋죠. 

여기서 토큰이 절약된다는 건 구현에 발생하는 토큰 소모가 무조건 적다는 의미가 아니라, AI에게 기존 코드를 읽히고 맥락(Context)을 전달할 때 **입력에 소모되는 토큰 수가 Java에 비해 훨씬 적을 수 있다는 의미**입니다. 같은 비즈니스 로직이라도 코드가 훨씬 압축되어 있으니까요.

#### 2. NPE를 원천 차단하는 Null Safety
AI가 짜든 사람이 짜든 백엔드에서 제일 많이 터지는 게 바로 `NullPointerException`입니다. Kotlin은 언어 타입 레벨에서 `Type`과 `Type?`을 엄격히 구분합니다. AI가 깜빡하고 null 처리를 놓치더라도, **런타임 크래시가 나기 전에 컴파일 타임에 빨간 줄로 싹 잡아냅니다.**

#### 3. 이미 완성된 탄탄한 생태계
- **Spring Boot & JPA**: 기존 프로덕션 검증 환경 그대로 사용
- **Ktor**: Node.js보다 훨씬 빠르고 가벼운 코틀린 순정 비동기 웹 프레임워크 (제 10년 된 토이 프로젝트도 최근 Ktor로 성공적으로 포팅했습니다)
- **Exposed**: 복잡한 JPA 대신 Kotlin DSL 기반으로 타입 세이프하게 쿼리를 작성하는 SQL 프레임워크
- **Koog**: 지저분한 JSON 파싱 노가다 없이 순정 코틀린 객체로 LLM Inference를 호출하는 AI 연동 도구

---

### AI 시대에 IDE? 구시대의 유물 아닌가요?

요즘은 "터미널에서 Cursor나 Claude Code CLI만 쓰면 되지, 무거운 IDE를 굳이 왜 켜냐"고 하시는 분들도 많습니다. 실제로 제 주변에도 IDE를 아예 지워버린 동료들이 꽤 있습니다.

하지만 개발 입문자나 취준생일수록, 그리고 복잡한 아키텍처를 다루는 실무자일수록 **코드가 내부에서 어떻게 유기적으로 도는지 직접 눈으로 확인할 수 있는 도구**가 반드시 필요합니다. 구조를 모른 채 AI에 100% 의존하다 보면 생각보다 그 한계가 금방 찾아오거든요.

저희 부부가 여전히 **IntelliJ IDEA**를 숨 쉬듯이 켜두는 5가지 이유입니다:

#### 1. 바이브 코딩 극대화 (하단 터미널 분할 뷰 & MCP)
![IntelliJ IDEA 하단 터미널 분할 뷰와 Claude CLI](/assets/img/posts/2026-09-17/4-1.png)
터미널만 있으면 어디서든 CLI로 개발이 가능하긴 하지만, 큰 작업을 할 때는 구조와 코드를 실시간으로 보면서 해야 실수가 없습니다. 
IntelliJ IDEA에서는 하단에 터미널을 분할 뷰로 띄워두고 명령을 던지면, 얘가 일을 똑바로 하고 있는지 에디터에서 바로바로 눈으로 확인하며 바이브 코딩이 가능합니다. 
에디터에서 코드를 슥 긁으면 위치와 맥락이 그대로 프롬프트로 들어가며, 최신 버전에서는 MCP 도구를 통해 에이전트에게 단순 텍스트 검색을 넘어 함수 호출 계층 구조나 심볼 참조 추적 같은 강력한 IDE 코드 인텔리전스를 직접 쥐어줍니다.

#### 2. 날려먹은 코드도 살려내는 Local History
![IntelliJ IDEA Local History 변경 이력 추적](/assets/img/posts/2026-09-17/4-2.png)
바이브 코딩하다 보면 코드를 이상하게 덮어쓰거나 통째로 날려먹는 순간이 한 번씩 찾아옵니다. 세션을 꺼버렸거나 Git에 커밋을 안 해뒀다면 멘붕에 빠지기 십상인데요. 
IntelliJ IDEA는 자체적으로 파일 변경 스냅샷을 촘촘하게 떠두기 때문에, Git과 무관하게 과거 시점의 코드를 언제든 비교하고 완벽하게 되살릴 수 있습니다.

#### 3. Database 연계와 엔티티 점프
![JPA @Query와 Database 콘솔 연계](/assets/img/posts/2026-09-17/4-3.png)
단순히 DB 툴이 내장된 수준이 아닙니다. JPA를 쓸 때 엔티티 코드 옆 아이콘만 누르면 실제 DB 테이블의 데이터로 즉시 점프하고, `@Query` 어노테이션 옆 버튼을 누르면 콘솔에서 해당 쿼리가 바로 실행됩니다. 엔티티 정보를 기반으로 한 쿼리문 자동완성도 기본입니다.

#### 4. .http 파일 기반의 API 테스트 및 자동화
![IntelliJ IDEA 내장 HTTP Client (.http)](/assets/img/posts/2026-09-17/4-4.png)
Postman 같은 별도 툴을 켤 필요 없이 컨트롤러 메소드 옆에서 바로 HTTP 요청을 날릴 수 있습니다. 
요청 시나리오가 순수 텍스트 파일(`.http`)로 저장되기 때문에 Git으로 버전 관리도 되고, AI에게 "이 API 테스트 시나리오 좀 짜줘"라고 시키면 복잡한 쿼리 파라미터를 조합해 가며 통합 테스트 자동화를 뚝딱 만들어줍니다.

#### 5. 실시간 인라인 스마트 디버거
![스마트 디버거 실시간 인라인 값 및 Evaluation](/assets/img/posts/2026-09-17/4-5.png)
중간 변수값 하나 보겠다고 `println` 노가다를 하거나 별도 인스펙터 창을 두리번거릴 필요가 없습니다. 
코드 줄 바로 옆에 인라인으로 실시간 변수값이 예쁘게 찍히며, 브레이크포인트에서 복잡한 조건식을 즉시 평가(Evaluation)해 보거나 강제 리턴(Force Return), 강제 예외 발생(Throw Exception)까지 가능해 디버깅 생산성이 압도적입니다.

---

### 마치며

아무리 AI 시대가 왔다고 한들, IntelliJ IDEA와 Kotlin으로 이루어진 이 탄탄한 개발 환경은 실무자에게도, 기초를 다져야 하는 입문자에게도 여전히 최고의 조합이라고 생각합니다.

마침 JetBrains에서 **Kotlin 무료 강좌 프로모션**을 진행하고 있는데, 원래 2026년 9월 초까지였던 무료 수강 기간이 **2026년 10월 9일까지**로 연장되었다고 합니다. 

- 👉 **[JetBrains Kotlin 프로모션 & 강좌 링크](https://jb.gg/lm4an8)**

해당 링크 페이지 스크롤을 살짝 내리시면 Hyperskill(JetBrains Academy)에서 제공하는 기초 문법부터 실무 트랙(Ktor, 코루틴 등)까지의 공식 무료 코스들을 바로 수강하실 수 있습니다. 

영상만 시청하는 한국식 '인강' 느낌이라기보다는, 텍스트 이론을 읽고 브라우저나 IntelliJ IDEA에서 직접 코드를 짜며 퀘스트를 깨나가는 **체험형 인터랙티브 실습 강의**에 가깝습니다. 영어로 되어 있어 처음엔 낯설 수 있지만, 언어의 장벽만 살짝 넘기면 직접 만들어보면서 아주 재미있게 배우실 수 있습니다.

바이브 코딩을 제대로 받쳐줄 탄탄한 기본기를 다져보고 싶으셨던 분들이라면 이번 기회에 가볍게 입문해 보시는 걸 추천드립니다.

<p style="margin: 32px 0 20px;">
  <a href="https://youtu.be/UItGOxVeKC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 관련 영상 보기 (뚜데 39)</span>
  </a>
</p>

> 💡 *이 글은 JetBrains로부터 지원을 받아 제작된 영상을 요약하였습니다. #광고 #협찬*

---

*이 글은 Gemini 3.8 Flash와 함께 작성되었습니다.*
