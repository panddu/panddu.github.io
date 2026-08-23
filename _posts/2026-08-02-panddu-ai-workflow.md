---
layout: post
title: "Kotlin으로 LLM 연동부터 Whisper 자막 자동화, QnA 분류까지 나의 AI 활용 예시"
date: 2026-08-02 22:00:00 +0900
category: tech
image: /assets/img/posts/2026-07-25/thumbnail.jpg
excerpt: "Kotlin 기반 LLM 연동으로 Whisper 자막 제작을 자동화하고, 로컬 LLM으로 QnA 데이터 분류까지 해결한 판교 개발자의 벤더 종속 없는 실전 AI 파이프라인 구축기."
---

![대표 썸네일](/assets/img/posts/2026-07-25/thumbnail.jpg)

<p style="margin: 22px 0 30px;">
  <a href="https://youtu.be/uHRUcb_gXIQ" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 관련 영상 보기</span>
  </a>
</p>

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

요즘 AI 에이전트니 자동화니 하는 이야기들이 정말 많이 들려옵니다. 하지만 막상 남들이 구축해 놓은 거창한 프레임워크나 비싼 상용 툴을 쓰다 보면, 정작 내 업무 흐름에 딱 맞지 않아서 수동으로 보정하는 비효율이 생기거나 토큰 비용만 잔뜩 낭비하는 경우가 많습니다.

오늘 제가 소개해 드릴 내용은 대단하고 엄청난 최첨단 기술이 아닙니다. 이미 훌륭한 성능을 자랑하는 기존의 인공지능 모델들(GPT, Gemini, Whisper 등)을 **내 손으로 가볍게 엮어서 나한테 꼭 맞는 도구로 구축한 실용적인 AI 워크플로우**에 관한 이야기입니다.

![유행 vs 효율](/assets/img/posts/2026-07-25/efficiency_vs_waste.jpg)

---

## <span id="workspace-structure">🛠️ 내 AI 워크스페이스의 4단 구조</span>

제 개인 작업 공간은 다음과 같은 4단 레이어 구조로 탄탄히 엮여 있습니다.

1. **최하단 영속성 계층 (DB)**: **<a href="https://bear.app/" target="_blank" rel="noopener noreferrer">Bear Note</a>**
   * 개인 workflow를 구성할 때 가장 먼저 결정해야 할 것이 바로 이 영속성 계층의 선택입니다. 저는 <a href="https://blog.bear.app/2026/04/bear-2-8-bearcli-claude-connector-and-mcp-server/" target="_blank" rel="noopener noreferrer">bearcli</a> 명령어 인터페이스와 마크다운 문법을 완벽히 지원하는 Bear 노트를 메인 영속성으로 채택해 모든 기록의 싱글 소스오브트루스(Single Source of Truth)로 사용하고 있습니다.
2. **코어 연동 계층 (CORE)**: **`mingus-kit`**
   * 구글 시트, 캘린더, 유튜브 분석 등 제가 매일 반복해서 체크해야 하는 모든 API 스킬들을 묶어 둔 중심 프로젝트입니다. 
3. **영상 작업 보조 계층 (STUDIO)**: **`mingus-studio`**
   * 영상 더빙용 음성 합성(GPT-SoVITS)과 Whisper 기반의 파이널컷 XML 자막 생성 자동화를 담당합니다.
4. **LLM 제어 및 에이전트 계층 (AGENT)**: **`mingus-agent`**
   * JVM 환경에서 동작하며, 로컬 LLM을 엮어 복잡한 데이터 정제(블로그 상담소 질문 분류 및 HTML 변환 등)를 처리합니다.
5. **최상위 결과물 계층 (OUTPUT)**: **블로그 및 <a href="https://www.youtube.com/@pan-ddu" target="_blank" rel="noopener noreferrer">유튜브 채널</a>**

이 모든 레이어가 거대하고 복잡한 엔지니어링 덩어리가 아니라, 각자가 필요한 역할만 수행하며 유기적으로 연결됩니다.

![대표 썸네일](/assets/img/posts/2026-07-25/project_hierarchy_diagram.png)

---

## <span id="session-persistence">🔄 토큰 난민을 구원한 '세션 영속화' (`mingus-kit`)</span>

여러 대의 PC를 오가며 작업하거나, 상황에 따라 Claude Code, Codex, Antigravity를 넘나들며 작업하다 보면 컨텍스트(대화 기록)가 쪼개져 관리가 매우 어려워집니다. 

저는 이를 해결하기 위해 `/mingus-kit:worklog`와 `/mingus-kit:resume` 스킬을 통해 현재의 세션 히스토리를 Bear에 동기화하고, 다른 디바이스나 에이전트에서 그대로 흡수하여 이전 작업을 즉시 이어 나갈 수 있도록 세션 영속화를 구축했습니다. 스마트폰을 통해서도 작업 상황을 완벽하게 모니터링할 수 있어 극단적인 효율을 발휘합니다.

![Bear 세션 영속화](/assets/img/posts/2026-07-25/session_persistence.jpg)

특히 이 워크플로우를 구축하며 유용했던 점은 에이전트가 사용할 상세 지침(`SKILL.md`)과 명령어 규칙(`commands/*.md`)을 **순수 마크다운 파일로 분리해 관리**한다는 것입니다. 소스코드 하드코딩을 최소화하고 텍스트 문서 위주로 에이전트 지침을 통제하니 기능 확장이 매우 간결해졌습니다.

여기에 적용된 세션 복구(`resume`) 동작 또한 단순히 대화록을 그대로 복사해 넣는 대신, 앞선 대화의 핵심 요약본(`worklog`)만 골라내 주입하기 때문에 **토큰 낭비를 줄이면서도 이전의 작업 컨텍스트를 아주 매끄럽게 복원**해 줍니다.

`mingus-kit`은 단순히 API 스크립트만 모아둔 것이 아닙니다. 각 기능(스킬)별 상세 지침서인 `SKILL.md`뿐만 아니라, `/worklog`, `/resume` 같이 에이전트의 작업 방식을 제어하는 명령어 사양서(`commands/*.md`)까지 한 곳에서 체계적으로 관리합니다.

실제 `mingus-kit`의 주요 디렉토리 구조는 다음과 같습니다:

<div class="code-block-container" markdown="1">
<div class="code-block-header">mingus-kit/</div>

```plaintext
mingus-kit/
├── commands/
│   ├── worklog.md            # 작업 로그(worklog) 기록 규칙 정의
│   └── resume.md             # 세션 복구(resume) 규칙 정의
├── skills/
│   ├── calendar/
│   │   ├── SKILL.md          # 캘린더 조회/변경 가이드라인
│   │   └── scripts/
│   │       └── calendar.py   # 실제 API 호출 스크립트
│   └── sheets/
│       ├── SKILL.md
│       └── scripts/
│           └── sheets.py
└── scripts/
```

</div>

여기에 들어가는 마크다운 문서들은 에이전트가 이 도구를 사용하는 "맥락과 규칙"을 명시합니다. 예를 들어, 대화 내역을 요약해 기록하도록 지시하는 `worklog.md` 명령어 사양서의 일부는 다음과 같습니다. 에이전트는 이 규칙을 읽고 도구 출력을 그대로 복사하는 대신 스스로 세션을 회고하며 중요한 트레이드오프와 의사결정만 정리해 Bear Note에 저장하게 됩니다:

<div class="code-block-container" markdown="1">
<div class="code-block-header">mingus-kit/commands/worklog.md</div>

{% raw %}
```markdown
---
description: 현재 세션에서 한 일을 정리해 Bear에 worklog 노트로 저장한다. 미리보기 후 사용자 확인을 거쳐 저장.
argument-hint: [제목 한 줄 요약 또는 추가 메모(선택)]
---

지금까지의 세션을 돌아보고 worklog 노트를 Bear에 저장하라.

## 절차

### 1. 컨텍스트 수집
- 오늘 날짜 수집
- 작업 디렉토리 및 프로젝트명 파악

### 2. 세션 회고 (도구 출력을 그대로 복붙하지 말 것)
- **컨텍스트**: 무엇을 하려고 했나, 왜 (요청·동기·제약)
- **한 일**: 실제로 변경한 것, 결정된 것 (단순 탐색·실패한 시도·중간 시행착오는 생략)
- **결정 / 배움**: 중요한 트레이드오프와 그 이유, 새로 알게 된 사실
- **다음 단계**: 미해결, 후속 작업, TODO
```
{% endraw %}

</div>

![mingus-kit 구조 및 지침](/assets/img/posts/2026-07-25/mingus_kit_structure.jpg)

---

## <span id="caption-automation">🎬 자막 지옥에서 탈출하기 (`mingus-studio`)</span>

유튜브 영상을 만들 때 가장 손이 많이 가고 지치는 작업은 단연 '자막 타이핑'입니다. 

![지옥의 자막 타이핑](/assets/img/posts/2026-07-25/exhausted_captioning.jpg)

기존 상용 앱(Vrew 등)들은 무료 한도가 있거나, 파이널컷으로 자막 스타일을 변경하면 자막 싱크가 살짝 밀려 직접 손으로 다시 맞춰야 하는 치명적인 단점이 있었습니다. 

이를 극복하기 위해 로컬 환경에서 **Whisper 기반 자막 생성 파이프라인**을 직접 구축했습니다. 이 도구는 기본적으로 오디오 파일만 주입해도 꽤 훌륭하게 받아쓰기를 해내며, 텍스트 스크립트 대본이 있을 경우 추가로 주입하여 정확도를 극대화할 수 있습니다. 템플릿과 싱크 보정을 순정 코드 단에서 처리하므로 타이밍 밀림 현상이 전혀 없습니다.

![Whisper 파이프라인](/assets/img/posts/2026-07-25/whisper_flow_diagram.jpg)

단순히 Whisper가 추출해 준 초(seconds) 단위 타임스탬프를 그대로 타임라인에 나열하면 프레임 오차가 누적되어 영상 뒤로 갈수록 자막 싱크가 미세하게 밀려나게 됩니다.

`mingus-studio`에서는 파이널컷이 네이티브로 인식하는 프레임 틱 단위(예: 29.97fps의 경우 `1001/30000s`)의 시간 구조로 정밀 변환하고, 자막 간의 무음 구간(Gap)을 감지하여 타이밍 오프셋을 보정하는 공식을 적용했습니다. 이 덕분에 컷 편집 완료 시점까지 자막 타이밍이 1프레임도 밀리지 않고 칼싱크를 유지하게 되었습니다.

---

## <span id="llm-integration">🤖 Kotlin 환경에서의 깔끔한 LLM 연동, JetBrains Koog (`mingus-agent`)</span>

자막이 1차로 추출되면 어색한 표현들을 LLM으로 후보정해야 하는데, 이 과정은 사람이 일일이 프롬프트를 치는 것이 아니라 **어플리케이션(코드) 내부에서 LLM API를 다이렉트로 호출**하여 유기적으로 동작해야 합니다.

![Application API 직접 호출](/assets/img/posts/2026-07-25/app_calls_llm.jpg)

저는 현업에서 주로 사용하는 JVM 환경의 강점을 살려 Kotlin 기반의 AI 에이전트 프레임워크인 **JetBrains Koog**를 사용했습니다. Koog는 Spring AI나 LangChain처럼 다양한 LLM(Gemini, Ollama 등)을 매끄럽게 교체할 수 있을 뿐만 아니라, Kotlin DSL을 통해 에이전트들의 오케스트레이션 및 데이터 흐름 상태를 코드로 명료하게 선언할 수 있습니다.

블로그에 게시한 [뚜쪽상담소]({{ '/series/comms/' | relative_url }})의 181개 QnA 카테고리 태깅 및 블로그용 HTML 마크업 생성 역시 로컬에서 Ollama로 `gemma4:e4b` 모델을 물려 안전하고 비용 걱정 없이 처리했습니다.

다만 소형 로컬 LLM의 특성상 출력 포맷(JSON)이 깨져서 파이프라인이 멈추는 고질적인 문제가 있었는데, 이를 해결하기 위해 Koog의 네이티브 스키마 생성 기능과 내장 자동 복구기(`StructureFixingParser`)를 이용해 아래와 같이 구조화 출력(Structured Output)을 위한 코틀린 확장 함수를 구현하여 극복했습니다.

<div class="code-block-container" markdown="1">
<div class="code-block-header">mingus-agent/src/main/kotlin/executeStructuredNative.kt</div>

```kotlin
suspend fun <T> PromptExecutor.executeStructuredNative(
    prompt: Prompt,
    model: LLModel,
    serializer: KSerializer<T>,
): T {
    // 1. 소형 모델 친화적인 '평탄화된 JSON 스키마' 생성
    val structure = JsonStructure.create(
        serializer.descriptor.serialName,
        serializer,
        NATIVE_JSON,
        BasicJsonSchemaGenerator.Default,
    )
    val config = StructuredRequestConfig(StructuredRequest.Native(structure), emptyMap())
    
    // 2. 파싱 에러 발생 시, 깨진 출력과 스키마를 모델에 다시 보여주고 수정을 유도 (최대 2회)
    val fixer = StructureFixingParser(model, retries = 2)
    return executeStructured(prompt, model, config, fixer).getOrThrow().data
}
```

</div>

이 래퍼 함수 덕분에 소형 로컬 LLM을 연동하면서도 포맷 어긋남 걱정 없이 실제 업무 파이프라인에서 100%에 가까운 신뢰성으로 데이터 정제를 자동화할 수 있었습니다.

다만 소형 로컬 LLM(`gemma4:e4b`)의 한계로 인해 간혹 출력 포맷(JSON)이 깨져 파이프라인이 멈추는 문제가 골칫거리였는데, 이는 Kotlin 코드의 `StructureFixingParser`를 통해 극복했습니다. 

파싱 에러가 발생하면 **[에러 로그 + 깨진 결과물]을 모델에 다시 주입해 스스로 수정을 유도(최대 2회)하는 자율 교정 피드백 루프**를 얹어 둠으로써, 로컬 모델임에도 100%에 가까운 신뢰성으로 카테고리 분류 및 데이터 정제를 자동화할 수 있었습니다.

---

## <span id="conclusion">💡 결론: AI 시대를 똑똑하게 살아가는 법</span>

제가 구축한 이 일련의 흐름들은 겉보기에는 거창해 보일지 몰라도, 사실 제가 겪고 있던 실제 불편함(자막 타이핑, 디바이스 간 세션 단절 등)을 해소하기 위해 작은 도구들을 엮어 놓은 것뿐입니다.

![내가 필요한 건 직접 뚝딱](/assets/img/posts/2026-07-25/crafting_own_tools.jpg)

인공지능 모델들의 기본적인 지능은 이미 충분히 훌륭합니다. 중요한 것은 그 거대한 기술에 압도되는 것이 아니라, **나에게 필요한 형태로 가볍게 가공하여 스마트하게 활용하는 접근 방식**입니다.

굳이 남이 복잡하게 짜놓은 자동화 패키지나 맞지 않는 기성복 옷에 내 일하는 방식을 억지로 구겨 넣지 마세요. 내 몸에 꼭 맞는 최적화된 도구들을 직접 엮어 나가는 것, 그것이 현 시점 AI 시대를 살아가는 가장 실리적이고 현명한 전략이라고 생각합니다.

![나만의 방식 나만의 AI](/assets/img/posts/2026-07-25/ai_era_my_way.jpg)

<p style="margin: 32px 0 16px; text-align: center;">
  <a href="https://youtu.be/uHRUcb_gXIQ" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none; font-size: 16.5px;">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">YouTube에서 관련 영상 보기</span>
  </a>
</p>

---

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
    <span style="display: inline-block; vertical-align: middle;">이 글은 Gemini 3.5 Flash와 함께 작성되었습니다</span>
  </div>
  이 포스팅은 판뚜의 여러 행동 데이터를 분석한 기반으로 <b>'판교 뚜벅쵸 페르소나'를 사전에 분석하여</b> 저 고유의 문체와 생각의 흐름을 반영해 작성되었습니다. 제목 개선 피드백 반영, Kotlin 코드 삽입, 8.4MB 이미지의 300KB JPEG 최적화 압축, 그리고 로컬 서버 기동까지의 모든 다듬기 과정 역시 <code>mingus-workspace</code>의 AI 에이전트(<b>Gemini 3.5 Flash</b> 모델)가 단독으로 수행했습니다. AI를 나만의 도구로 엮어 쓴다는 것이 무엇인지, 이 글 자체로 증명합니다.
</div>
