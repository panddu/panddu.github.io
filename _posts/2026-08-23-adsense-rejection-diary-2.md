---
layout: post
title: "애드고시 리젝당하다 2편 - 수동 색인도 씹는 구글 봇 깨우기"
date: 2026-08-23 18:30:00 +0900
category: tech
excerpt: "재신청한 지 2주 만에 다시 날아온 애드센스 리젝 메일. 수동 색인 요청도 무시하는 구글 봇의 멱살을 잡고 Google Indexing API로 강제 크롤링을 주입한 생생한 삽질기."
---

<div style="background: var(--answer-bg, #f6f8ff); border: 1px solid var(--answer-border, #e3e8ff); border-radius: 8px; padding: 16px 20px; margin: 24px 0 28px; font-size: 14.5px; line-height: 1.6; color: var(--ink);">
  <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; margin-bottom: 8px; font-size: 15.5px; color: var(--ink);">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="#D97706" style="flex-shrink: 0; display: inline-block; vertical-align: middle; margin-top: -2px;">
      <g>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5"/>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5" transform="rotate(60 12 12)"/>
        <rect x="10.5" y="1" width="3" height="22" rx="1.5" transform="rotate(120 12 12)"/>
      </g>
    </svg>
    <span style="display: inline-block; vertical-align: middle;">이 글은 Claude Sonnet 5와 함께 작성되었습니다</span>
  </div>
  재신청 이후 또 한 번의 애드센스 낙방 통보를 받고, 그 원인을 파악해 구글의 강제 색인 API(Google Indexing API)를 연동해 해결하기까지의 과정을 정리한 에세이입니다.
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
    <li><a href="#empty-site">2. 진짜 범인은 아직도 굳어있는 검색 색인</a></li>
    <li><a href="#bot-is-sleeping">3. 수동 요청도 씹어버리는 구글 봇의 위엄</a></li>
    <li><a href="#indexing-api">4. 치트키 발동: Google Indexing API 멱살잡이</a></li>
    <li><a href="#what-next">5. 다음 단계는?</a></li>
  </ul>
</div>

---

<h2 id="rejected-again">1. 2주 만에 돌아온 답장, 그리고 2차 리젝</h2>

2주 전, 구글 검색 인프라의 표준 이정표(Canonical)를 새 블로그 주소로 정확하게 돌려놓고, 브런치와 티스토리에 흩어져 있던 글들도 비공개(발행 취소)로 깔끔하게 정리했습니다. 중복 콘텐츠 페널티를 완벽히 해결했다고 자부하며 애드센스에 검토 요청 버튼을 누르고 결과를 기다렸습니다. 

그리고 정확히 2주가 지난 오늘, 구글 애드센스 팀으로부터 메일이 한 통 왔습니다.

![애드센스 정책 위반 발견 메일](/assets/img/posts/2026-08-23/adsense-rejection-again.png)
*가치가 별로 없는 콘텐츠로 2차 리젝당한 메일 화면.*

"정책 위반이 발견되었습니다. 가치가 별로 없는 콘텐츠." 

템플릿은 전과 100% 동일했습니다. "글 개수가 부족한가?" 싶어 제 블로그의 글들을 다시 세어봤습니다. 50개가 훌쩍 넘는 글이 발행되어 있으니 콘텐츠 절대량 부족은 결코 아니었습니다. 도대체 무엇이 문제였을까요?

---

<h2 id="empty-site">2. 진짜 범인은 아직도 굳어있는 검색 색인</h2>

구글 서치 콘솔에 접속해서 사이트의 실질적인 색인 상태를 조회해 보고 나서야 턱 하니 막혀있던 원인이 보였습니다.

구글 검색 데이터베이스에 정식 등록되어 검색 노출이 되고 있는 페이지가 **단 3개(홈 화면, 스팸체 생성기, 청첩장 페이지)**에 굳어있었던 것입니다. 

지난 2주간 예전 브런치와 티스토리 글들이 구글 인덱스에서 깨끗하게 지워진 것은 맞았습니다. 하지만 정작 새 블로그(`panddu.github.io`)의 나머지 50여 개 글들은 구글 봇이 긁어가지 않고 `색인이 생성되지 않음` 분류 속에 억류되어 있었습니다.

애드센스 심사 봇이 제 블로그를 검사하러 들어왔을 때, 구글 인덱스 상에 올라와 있는 페이지는 단 2개(스팸체 생성기, 청첩장)뿐이었습니다. 그러니 애드센스 봇 입장에서는 **"글 2개밖에 없는 빈 껍데기 유령 사이트"**로 보여서 똑같이 "가치가 별로 없는 콘텐츠" 판정을 내린 것이었습니다. 

**검색 색인이 뚫리는 것이 애드센스 최종 합격의 가장 큰 열쇠**였습니다.

---

<h2 id="bot-is-sleeping">3. 수동 요청도 씹어버리는 구글 봇의 위엄</h2>

그동안 손을 놓고 있었던 것은 아닙니다. 퀄리티 있는 2026년 오리지널 신규 글들을 추려 서치 콘솔에서 하나하나 [색인 생성 요청]을 보냈고, 사이트맵도 등록해 보았습니다.

하지만 구글 봇은 요지부동이었습니다. 신생 도메인이라 그런지 크롤링 우선순위 대기열(Queue)의 맨 꽁무니로 밀려 있었고, 수동으로 콕 집어 등록 요청을 날려도 2주 동안 단 한 페이지도 수집해 가지 않았습니다. 사이트맵 상태도 구글 봇이 방문할 때 1~2초만 지연되면 빨갛게 띄우는 고질적인 `가져올 수 없음` 오류 캐시에 갇혀 있었습니다.

노크해도 열어주지 않는다면, 문을 부수고 강제로 들어가는 수밖에 없었습니다.

---

<h2 id="indexing-api">4. 치트키 발동: Google Indexing API 멱살잡이</h2>

구글은 채용 정보나 라이브 방송처럼 실시간 수집이 꼭 필요한 페이지들을 위해 **[Google Indexing API]**라는 강제 크롤링 API를 제공합니다. 일반적인 블로그에는 사용을 다소 지양하게끔 가이드라인을 두고 있지만, 지금처럼 수동 요청마저 씹히는 비정상적인 지연 상황에서는 봇을 멱살 잡고 끌고 올 수 있는 최상의 치트키가 됩니다.

AI 파트너(Claude)의 제안을 받아, 로컬 컴퓨터에 이미 설정해 두었던 GCP(Google Cloud Platform) 서비스 계정(`ga4-reader@ddu-family.iam.gserviceaccount.com`)을 활용해 작업을 세팅했습니다.

1. **API 활성화**: GCP 콘솔에서 `Web Search Indexing API`를 프로젝트에 사용 설정했습니다.
2. **서치 콘솔 소유자 권한 부여**: 구글의 클래식 관리자 페이지인 [웹마스터 센터](https://www.google.com/webmasters/verification/home)에 접속해, 해당 서비스 계정 이메일을 블로그의 **[소유자(Owner)]**로 정식 등록했습니다.
3. **API 자동화 스크립트 실행**: 블로그 사이트맵(`sitemap.xml`)을 자동으로 읽어 들여 모든 포스트 URL을 구글 API 서버로 직접 쏘아 올리는 파이썬 스크립트(`force_index.py`)를 돌렸습니다.

```bash
# 구글 봇에게 64개 URL을 실시간으로 강제 제출하는 파이썬 명령어
~/.config/mingus-kit/.venv/bin/python3 skills/blog-analytics/scripts/force_index.py --key-path ~/.config/mingus-kit/ga4_service_account.json
```

결과는 **64개 URL 전체 성공(SUCCESS)**! 

구글 API 서버에 직접 강제 수집 신호를 안전하게 밀어 넣는 데 성공했습니다.

---

<h2 id="what-next">5. 다음 단계는?</h2>

구글 Indexing API의 효과는 매우 강력합니다. 구글의 일반 크롤러와 달리 API 신호를 받은 구글 봇은 보통 수 시간 내, 길어도 24시간 내에 블로그를 차례대로 순방향 수집하기 시작합니다.

이제 구글 검색 결과에 50여 개의 포스트 글이 대량으로 한꺼번에 노출되는 것을 지켜보기만 하면 됩니다. 

며칠 동안 색인이 50개 이상으로 정상 갱신되어 검색 노출이 풀리는 시점에, 애드센스에 3번째 검토 요청을 날릴 계획입니다. 이번에야말로 초록색 승인 마크를 받아내고, 임시 비활성화해 둔 디스코드 게시판(`board.html`)과 오픈채팅방 링크(`chat.html`)를 기쁘게 원상 복구하여 3편(완결편)으로 돌아오겠습니다.
