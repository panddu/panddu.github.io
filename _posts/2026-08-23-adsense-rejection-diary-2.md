---
layout: post
title: "애드고시 리젝당하다 2편 - 수동 색인도 안 될 때의 또 다른 시도"
date: 2026-08-23 20:58:30 +0900
category: tech
excerpt: "재신청한 지 2주 만에 다시 날아온 애드센스 리젝 메일. 수동 색인 요청조차 씹는 구글 봇에게 Google Indexing API로 수집 신호를 보내며 조심스레 결과를 기다려봅니다."
---

<div style="background: var(--answer-bg, #f6f8ff); border: 1px solid var(--answer-border, #e3e8ff); border-radius: 8px; padding: 16px 20px; margin: 24px 0 28px; font-size: 14.5px; line-height: 1.6; color: var(--ink);">
  <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; margin-bottom: 8px; font-size: 15.5px; color: var(--ink);">
    <svg viewBox="0 0 24 24" width="20" height="20" style="flex-shrink: 0; display: inline-block; vertical-align: middle; margin-top: -2px;">
      <defs>
        <linearGradient id="gemini-grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#9168C0"/>
          <stop offset="50%" stop-color="#5684D1"/>
          <stop offset="100%" stop-color="#DE6B48"/>
        </linearGradient>
      </defs>
      <path fill="url(#gemini-grad)" d="M12 2a1 1 0 0 1 .968.756c.866 3.593 3.683 6.41 7.276 7.276a1 1 0 0 1 0 1.936c-3.593.866-6.41 3.683-7.276 7.276a1 1 0 0 1-1.936 0c-.866-3.593-3.683-6.41-7.276-7.276a1 1 0 0 1 0-1.936c3.593-.866 6.41-3.683 7.276-7.276A1 1 0 0 1 12 2z"/>
    </svg>
    <span style="display: inline-block; vertical-align: middle;">이 글은 Gemini와 함께 작성되었습니다</span>
  </div>
  2차 애드센스 낙방 통보를 받고, 여전히 풀리지 않는 색인 문제를 해결하기 위해 Google Indexing API라는 다소 낯선 방식을 적용해 본 시도에 대한 기록입니다.
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

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#rejected-again">1. 2주 만에 돌아온 답장, 그리고 2차 리젝</a></li>
    <li><a href="#empty-site">2. 어쩌면 원인은 아직도 정체된 검색 색인?</a></li>
    <li><a href="#bot-is-sleeping">3. 수동 요청도 씹어버리는 구글 봇</a></li>
    <li><a href="#indexing-api">4. 또 다른 시도: Google Indexing API 연동해 보기</a></li>
    <li><a href="#what-next">5. 이번엔 잘 될 수 있을까?</a></li>
  </ul>
</div>

---

<h2 id="rejected-again">1. 2주 만에 돌아온 답장, 그리고 2차 리젝</h2>

2주 전, 구글 검색 인프라의 표준 이정표(Canonical)를 새 블로그 주소로 돌려놓고, 브런치와 티스토리에 있던 기존 글들도 비공개(발행 취소)로 정리했습니다. 중복 콘텐츠 문제를 정석대로 다 처리했으니 이번엔 괜찮겠지 하는 마음으로 애드센스에 검토 요청을 넣었습니다.

그리고 2주가 지난 오늘, 구글 애드센스 팀으로부터 메일이 한 통 왔습니다.

![애드센스 정책 위반 발견 메일](/assets/img/posts/2026-08-23/adsense-rejection-again.png)
*가치가 별로 없는 콘텐츠로 2차 리젝당한 메일 화면.*

결과는 2주 전과 완전히 동일한 "정책 위반: 가치가 별로 없는 콘텐츠" 리젝이었습니다. 나름 고민하며 고쳤는데 똑같은 문구를 마주하니 허탈한 마음이 앞서더군요. 글의 개수는 50개가 넘는데 도대체 무엇이 부족한 건지 처음엔 이해하기 어려웠습니다.

---

<h2 id="empty-site">2. 어쩌면 원인은 아직도 정체된 검색 색인?</h2>

답답한 마음에 구글 서치 콘솔에 접속해 현재 색인 통계를 열어 보았습니다.

그런데 검색 데이터베이스에 등록되어 실제 검색 노출이 되고 있는 페이지가 여전히 **단 3개(홈 화면, 스팸체 생성기, 청첩장 페이지)**에 머물러 있었습니다. 

2주간 예전 브런치와 티스토리 글들이 구글 검색에서 다 빠진 것은 확인했지만, 정작 이 새 블로그(`panddu.github.io`)의 나머지 50여 개 글들은 구글 봇이 긁어가지 않은 채 `색인이 생성되지 않음` 카테고리에 방치되어 있었습니다.

애드센스 심사 봇이 제 블로그를 검사하러 들어왔을 때, 구글 인덱스 장부상에 이 사이트는 글이 단 2개(스팸체 생성기, 청첩장)뿐인 사이트로 보였을 가능성이 큽니다. 그러다 보니 애드센스 봇 입장에서는 여전히 콘텐츠가 빈약한 사이트로 분류해서 똑같이 리젝을 내린 게 아닌가 하는 조심스러운 추측이 들었습니다.

---

<h2 id="bot-is-sleeping">3. 수동 요청도 씹어버리는 구글 봇</h2>

그동안 신규로 썼던 글 9개를 골라 서치 콘솔에서 수동으로 [색인 생성 요청]을 일일이 보냈고, 사이트맵도 삭제 후 재등록을 거듭해 보았습니다.

하지만 구글 봇은 반응이 없었습니다. 신생 도메인이라 우선순위에서 밀려 있는 탓인지, 수동 등록 요청 신호를 보냈음에도 2주째 단 한 페이지도 긁어가지 않았습니다. 사이트맵 상태 역시 구글 봇이 첫 수집 때 접근하지 못해 띄워둔 `가져올 수 없음` 오류 상태에서 갱신되지 않고 있었습니다.

그냥 일반 대기열을 쳐다보며 마냥 기다리기에는 기약이 없어 보였습니다.

---

<h2 id="indexing-api">4. 또 다른 시도: Google Indexing API 연동해 보기</h2>

구글은 채용 정보나 라이브 방송처럼 빠른 수집이 필요한 페이지들을 위해 **[Google Indexing API]**라는 색인 수집 API를 따로 열어두고 있습니다. 개인 블로그 글을 등록하는 용도로는 권장되지 않는 편이라고 하지만, 지금처럼 일반 수동 요청이 전혀 작동하지 않을 때는 지푸라기라도 잡는 심정으로 적용해 볼 만한 대안이었습니다.

로컬 환경에 세팅되어 있던 GCP(Google Cloud Platform) 서비스 계정(`ga4-reader@ddu-family.iam.gserviceaccount.com`)을 활용해 설정을 시도해 보았습니다.

1. **API 활성화**: GCP 콘솔에서 `Web Search Indexing API`를 사용 설정했습니다.
2. **소유자 권한 부여**: 구글의 이전 관리자 페이지인 [웹마스터 센터](https://www.google.com/webmasters/verification/home)로 접속해, 서비스 계정 이메일을 블로그의 **[소유자(Owner)]**로 등록했습니다.
3. **스크립트 실행**: 블로그 사이트맵(`sitemap.xml`)에서 모든 포스트 URL을 읽어와 구글 API 서버로 다이렉트 전송하는 파이썬 스크립트(`force_index.py`)를 돌려 보았습니다.

```bash
# 구글 봇에게 64개 URL을 실시간으로 강제 제출하는 파이썬 명령어
~/.config/mingus-kit/.venv/bin/python3 skills/blog-analytics/scripts/force_index.py --key-path ~/.config/mingus-kit/ga4_service_account.json
```

다행히 64개 URL 전체에 대해 전송 성공(`SUCCESS`) 응답이 떨어졌고, 구글 서버로 직접 색인 갱신 신호를 밀어 넣는 데까지는 완료했습니다.

---

<h2 id="what-next">5. 이번엔 잘 될 수 있을까?</h2>

API를 활용해 수집 신호를 전송하긴 했지만, 이것을 쓴다고 해서 굳어있던 색인이 정말 다 풀릴지는 아직 반신반의하는 심정입니다. 다만 마냥 대기열에 서서 구글 봇이 오기만을 바라보는 것보다는 할 수 있는 최소한의 기술적인 시도는 다 해보았다는 점에서 의미를 두려고 합니다.

이 방법마저 통하지 않는다면 정말 텍스트 자체의 퀄리티나 사이트 전체의 구조를 근본적으로 다시 점검해야 할 것 같습니다. 

일단은 구글 봇이 며칠 내로 사이트를 드나들며 색인을 갱신해 주기를 조용히 바라볼 뿐입니다. 며칠 뒤 검색 결과에 변화가 생기면 다시 그 결과를 정리해 보겠습니다. 이번엔 제발 좋은 소식으로 이어지기를 기대해 봅니다.
