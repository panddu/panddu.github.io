---
layout: post
title: "프롬프트만 치는 건 끝났습니다. 저는 AI를 이렇게 씁니다"
date: 2026-07-25 16:22:00 +0900
category: tech
image: /assets/img/posts/2026-07-25/thumbnail.jpg
excerpt: "세션 저장, 자막 자동화, 로컬 LLM 태깅까지… 벤더 종속 없이 나에게 꼭 필요한 기능만 뚝딱 만들어 활용하는 실용적 AI 자동화 파이프라인과 JetBrains Koog 소개."
---

![대표 썸네일](/assets/img/posts/2026-07-25/thumbnail.jpg)

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#workspace-structure">1. 내 AI 워크스페이스의 4단 구조</a></li>
    <li><a href="#session-persistence">2. 토큰 난민을 구원한 '세션 영속화'</a></li>
    <li><a href="#caption-automation">3. 자막 지옥에서 탈출하기</a></li>
    <li><a href="#llm-integration">4. Kotlin 환경에서의 LLM 연동 (JetBrains Koog)</a></li>
    <li><a href="#conclusion">5. 결론: AI 시대를 똑똑하게 살아가는 법</a></li>
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
    color: var(--primary, #2563eb);
    text-decoration: none;
    font-weight: 500;
  }
  .toc-box a:hover {
    text-decoration: underline;
  }
</style>

안녕하세요, 판교뚜벅쵸입니다. 

요즘 AI 에이전트니 자동화니 하는 이야기들이 정말 많이 들려옵니다. 하지만 막상 남들이 구축해 놓은 거창한 프레임워크나 비싼 상용 툴을 쓰다 보면, 정작 내 업무 흐름에 딱 맞지 않아서 수동으로 보정하는 비효율이 생기거나 토큰 비용만 잔뜩 낭비하는 경우가 많습니다.

오늘 제가 소개해 드릴 내용은 대단하고 엄청난 최첨단 기술이 아닙니다. 이미 훌륭한 성능을 자랑하는 기존의 인공지능 모델들(GPT, Gemini, Whisper 등)을 **내 손으로 가볍게 엮어서 나한테 꼭 맞는 도구로 구축한 실용적인 AI 워크플로우**에 관한 이야기입니다.

![유행 vs 효율](/assets/img/posts/2026-07-25/efficiency_vs_waste.jpg)

---

## <span id="workspace-structure">🛠️ 내 AI 워크스페이스의 4단 구조</span>

제 개인 작업 공간은 다음과 같은 4단 레이어 구조로 탄탄히 엮여 있습니다.

1. **최하단 영속성 계층 (DB)**: **Bear Note**
   * 개인 workflow를 구성할 때 가장 먼저 결정해야 할 것이 바로 이 영속성 계층의 선택입니다. 저는 `bearcli` 명령어 인터페이스와 마크다운 문법을 완벽히 지원하는 Bear 노트를 메인 영속성으로 채택해 모든 기록의 싱글 소스오브트루스(Single Source of Truth)로 사용하고 있습니다.
2. **코어 연동 계층 (CORE)**: **`mingus-kit`**
   * 구글 시트, 캘린더, 유튜브 분석 등 제가 매일 반복해서 체크해야 하는 모든 API 스킬들을 묶어 둔 중심 프로젝트입니다. 
3. **영상 작업 보조 계층 (STUDIO)**: **`mingus-studio`**
   * 영상 더빙용 음성 합성(GPT-SoVITS)과 Whisper 기반의 파이널컷 XML 자막 생성 자동화를 담당합니다.
4. **LLM 제어 및 에이전트 계층 (AGENT)**: **`mingus-agent`**
   * JVM 환경에서 동작하며, 로컬 LLM을 엮어 복잡한 데이터 정제(블로그 상담소 질문 분류 및 HTML 변환 등)를 처리합니다.
5. **최상위 결과물 계층 (OUTPUT)**: **블로그(`panddu.github.io`) 및 유튜브 채널**

이 모든 레이어가 거대하고 복잡한 엔지니어링 덩어리가 아니라, 각자가 필요한 역할만 수행하며 유기적으로 연결됩니다.

![대표 썸네일](/assets/img/posts/2026-07-25/project_hierarchy_diagram.png)

---

## <span id="session-persistence">🔄 토큰 난민을 구원한 '세션 영속화' (`mingus-kit`)</span>

여러 대의 PC를 오가며 작업하거나, 상황에 따라 Claude Code, Codex, Antigravity를 넘나들며 작업하다 보면 컨텍스트(대화 기록)가 쪼개져 관리가 매우 어려워집니다. 

저는 이를 해결하기 위해 `/mingus-kit:worklog`와 `/mingus-kit:resume` 스킬을 통해 현재의 세션 히스토리를 Bear에 동기화하고, 다른 디바이스나 에이전트에서 그대로 흡수하여 이전 작업을 즉시 이어 나갈 수 있도록 세션 영속화를 구축했습니다. 스마트폰을 통해서도 작업 상황을 완벽하게 모니터링할 수 있어 극단적인 효율을 발휘합니다.

![Bear 세션 영속화](/assets/img/posts/2026-07-25/session_persistence.jpg)

---

## <span id="caption-automation">🎬 자막 지옥에서 탈출하기 (`mingus-studio`)</span>

유튜브 영상을 만들 때 가장 손이 많이 가고 지치는 작업은 단연 '자막 타이핑'입니다. 

![지옥의 자막 타이핑](/assets/img/posts/2026-07-25/exhausted_captioning.jpg)

기존 상용 앱(Vrew 등)들은 무료 한도가 있거나, 파이널컷으로 자막 스타일을 변경하면 자막 싱크가 살짝 밀려 직접 손으로 다시 맞춰야 하는 치명적인 단점이 있었습니다. 

이를 극복하기 위해 로컬 환경에서 **Whisper 기반 자막 생성 파이프라인**을 직접 구축했습니다. 이 도구는 기본적으로 오디오 파일만 주입해도 꽤 훌륭하게 받아쓰기를 해내며, 텍스트 스크립트 대본이 있을 경우 추가로 주입하여 정확도를 극대화할 수 있습니다. 템플릿과 싱크 보정을 순정 코드 단에서 처리하므로 타이밍 밀림 현상이 전혀 없습니다.

![Whisper 파이프라인](/assets/img/posts/2026-07-25/whisper_flow_diagram.jpg)

---

## <span id="llm-integration">🤖 Kotlin 환경에서의 깔끔한 LLM 연동, JetBrains Koog (`mingus-agent`)</span>

자막이 1차로 추출되면 어색한 표현들을 LLM으로 후보정해야 하는데, 이 과정은 사람이 일일이 프롬프트를 치는 것이 아니라 **어플리케이션(코드) 내부에서 LLM API를 다이렉트로 호출**하여 유기적으로 동작해야 합니다.

![Application API 직접 호출](/assets/img/posts/2026-07-25/app_calls_llm.jpg)

저는 현업에서 주로 사용하는 JVM 환경의 강점을 살려 Kotlin 기반의 AI 에이전트 프레임워크인 **JetBrains Koog**를 사용했습니다. Koog는 Spring AI나 LangChain처럼 다양한 LLM(Gemini, Ollama 등)을 매끄럽게 교체할 수 있을 뿐만 아니라, Kotlin DSL을 통해 에이전트들의 오케스트레이션 및 데이터 흐름 상태를 코드로 명료하게 선언할 수 있습니다.

블로그에 게시한 '뚜쪽상담소'의 181개 QnA 카테고리 태깅 및 블로그용 HTML 마크업 생성 역시 로컬에서 Ollama로 `gemma4:e4b` 모델을 물려 안전하고 비용 걱정 없이 처리했습니다. JSON 형태가 일그러질 때를 대비한 native schema 강제와 `StructureFixingParser`를 통한 automatic 복구까지 구현하여 실제 업무 파이프라인에서 신뢰성 높게 동작하도록 했습니다.

---

## <span id="conclusion">💡 결론: AI 시대를 똑똑하게 살아가는 법</span>

제가 구축한 이 일련의 흐름들은 겉보기에는 거창해 보일지 몰라도, 사실 제가 겪고 있던 실제 불편함(자막 타이핑, 디바이스 간 세션 단절 등)을 해소하기 위해 작은 도구들을 엮어 놓은 것뿐입니다.

![내가 필요한 건 직접 뚝딱](/assets/img/posts/2026-07-25/crafting_own_tools.jpg)

인공지능 모델들의 기본적인 지능은 이미 충분히 훌륭합니다. 중요한 것은 그 거대한 기술에 압도되는 것이 아니라, **나에게 필요한 형태로 가볍게 가공하여 스마트하게 활용하는 접근 방식**입니다.

굳이 남이 복잡하게 짜놓은 자동화 패키지나 맞지 않는 기성복 옷에 내 일하는 방식을 억지로 구겨 넣지 마세요. 내 몸에 꼭 맞는 최적화된 도구들을 직접 엮어 나가는 것, 그것이 현 시점 AI 시대를 살아가는 가장 실리적이고 현명한 전략이라고 생각합니다.

![나만의 방식 나만의 AI](/assets/img/posts/2026-07-25/ai_era_my_way.jpg)
