---
layout: post
title: "애드고시 리젝당하다 1편"
category: tech
excerpt: "애드센스 심사에서 '가치가 별로 없는 콘텐츠'로 리젝당한 뒤, 브런치·티스토리·구 깃헙 블로그에 흩어져 있던 흔적을 정리하고 재도전한 과정. 아직 결론은 안 났습니다."
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
  Claude Code로 애드센스 리젝 원인을 실시간으로 진단(robots.txt, 사이트맵, 서치 콘솔 URL 검사 API 조회)하던 세션 로그와, 그 과정에서 나온 작업 워크로그를 바탕으로 정리한 글입니다.
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
    <li><a href="#rejected">1. 애드고시에서 리젝당했습니다</a></li>
    <li><a href="#first-guess">2. 첫 번째 착각 — 크롤링이 안 돼서 그런가?</a></li>
    <li><a href="#real-culprit">3. 진짜 범인 — 여기저기 흩어진 제 흔적들</a></li>
    <li><a href="#removal-request">4. 서치 콘솔에 삭제 요청까지 넣었는데</a></li>
    <li><a href="#index-request">5. 색인 요청도 넣어봤습니다만</a></li>
    <li><a href="#retry">6. 그래서 재신청은 했냐면</a></li>
  </ul>
</div>

<h2 id="rejected">1. 애드고시에서 리젝당했습니다</h2>

블로그를 다시 만들고 나서 이런저런 걸 하나씩 붙이다가, 애드센스도 한번 신청해봤습니다. 어차피 밑져야 본전이고 리젝당해도 패널티는 없다고 하니 가볍게 들이받은 거였는데, 며칠 뒤에 메일이 하나 왔습니다.

> 정책 위반이 발견되었습니다.
>
> 가치가 별로 없는 콘텐츠
>
> 고객님의 사이트가 Google 게시자 네트워크의 사용 기준을 충족하지 않고 있습니다.

"가치가 별로 없는 콘텐츠"라니, 나름 진지하게 쓴 글들인데 좀 억울하더라고요. 근데 곱씹어보니 짚이는 데가 있었습니다. 저는 이 블로그를 시작하기 전에 **티스토리**, **브런치**, 그리고 **예전에 만들었던 구형 깃헙 블로그(`mingpd.github.io`)**를 전부 거쳐왔거든요. 옛날 글들을 이번 블로그로 마이그레이션까지 해왔으니, 어디선가 중복 콘텐츠로 걸렸을 가능성이 꽤 높아 보였습니다.

---

<h2 id="first-guess">2. 첫 번째 착각 — 크롤링이 안 돼서 그런가?</h2>

처음엔 "검색에 노출이 안 되니까 애드센스도 안 통과되는 거 아닐까?" 싶어서 크롤링 쪽부터 팠습니다. Claude Code를 붙잡고 `robots.txt`, `sitemap.xml`, GitHub Pages 빌드 상태를 하나씩 확인했는데 전부 정상이었습니다. 사이트맵도 구글 서치 콘솔 API로 직접 조회해보니 에러 0건이었고요.

문제는 홈페이지만 색인돼 있고 `/posts/`나 개별 글들은 전부 **"URL is unknown to Google"** 상태였다는 겁니다. 신생 도메인이라 구글이 아직 이 사이트를 진지하게 안 보고 있는 단계라는 결론까지 냈었죠.

![URL이 Google에 등록되어 있지 않음](/assets/img/posts/2026-08-12/url-unknown-to-google.png)
*서치 콘솔 URL 검사 결과 — "Google에는 아직 알려지지 않은 URL입니다."*

그런데 여기서 중요한 걸 하나 깨달았습니다. **애드센스는 구글 검색(Googlebot)과 별개인 자체 크롤러(Mediapartners-Google)로 사이트를 심사합니다.** 즉 검색 노출이 안 된다고 해서 애드센스 심사에 직접 영향을 주는 건 아니었던 거예요. "검색에 노출되면 재신청하자"는 제 나름의 전략은 사실 이 리젝 사유랑은 크게 상관이 없었던 셈입니다. 크롤링 문제는 별개로 계속 지켜봐야 할 숙제로 남겨두고, 진짜 범인을 찾으러 다시 나섰습니다.

---

<h2 id="real-culprit">3. 진짜 범인 — 여기저기 흩어진 제 흔적들</h2>

"가치가 별로 없는 콘텐츠"는 보통 콘텐츠 절대량이 부족하거나, 같은 글이 여러 곳에 중복으로 떠 있을 때 걸립니다. 저는 이미 51개 넘는 글을 써둔 상태라 분량 문제는 아니었고, 결국 옛날 플랫폼들에 남아있는 흔적을 하나씩 추적했습니다.

### 브런치 — 완전 비공개 처리

이관 대상이었던 글 21개를 전부 작가서랍으로 비공개(발행 취소) 처리했습니다. 지금은 브런치 계정에 공개된 글이 0개입니다.

### 티스토리 — 전체 비공개 전환

운영하던 티스토리 블로그도 글을 전부 비공개로 돌려서 검색 결과에 아예 안 잡히게 정리했습니다.

### 구형 깃헙 블로그(`mingpd.github.io`) — 진짜 범인은 캐노니컬이었다

여기서 진짜 원인을 하나 찾았습니다. 예전 Hexo 블로그의 테마 템플릿을 열어봤더니, `<link rel="canonical">` 태그가 **자기 자신의 주소를 가리키도록** 박혀있더라고요.

![mingpd.github.io의 자기참조 canonical 태그](/assets/img/posts/2026-08-12/mingpd-canonical-self-reference.png)
*개발자도구로 확인한 구 블로그의 canonical 태그 — 자기 자신을 가리키고 있었습니다.*

캐노니컬은 "여러 주소에 같은 내용이 있을 때 진짜 원본이 어디인지" 검색엔진에게 알려주는 태그입니다. 이게 옛 블로그 자신을 가리키고 있으니, 구글 입장에서는 "이 글의 원본은 옛 블로그다"라고 읽었을 거고, 새 블로그(`panddu.github.io`)에 옮겨온 같은 글은 반대로 무단 복제 콘텐츠처럼 보였을 가능성이 큽니다.

그래서 Hexo 테마의 `head.ejs` 템플릿을 직접 고쳐서, 각 글의 Front Matter에 지정한 `canonical` 값을 최우선으로 쓰도록 바꾸고, 홈 화면도 새 블로그 주소(`https://panddu.github.io/`)를 캐노니컬로 잡도록 예외 처리를 추가했습니다. 유입이 많은 [스팸체 생성기](/posts/2019/04/spammaker/) 글도 캐노니컬을 새 블로그 주소로 선언해서, 이 글로 들어오는 트래픽은 그대로 살리면서 "원본은 새 블로그"라는 신호만 명확히 정리했습니다.

빌드하다가 삽질도 좀 했습니다. 로컬 Node 16 환경에서 빌드하니 결과물이 조용히 전부 0바이트로 깨지는 문제가 있었는데, 알고 보니 오래된 Hexo 버전이 최신 Node랑 안 맞는 문제였습니다. 프로젝트에 미리 박혀있던 로컬 Node 10 경로로 다시 빌드하니 정상적으로 나왔습니다. 오래된 정적 빌더는 이럴 때 진짜 애를 먹이네요.

### 얇은 콘텐츠 페이지도 잠깐 숨겼습니다

디스코드 수다방(`board.html`)이랑 카카오 오픈채팅 링크(`chat.html`)는 본문 텍스트 없이 링크·위젯만 있는 페이지라, 애드센스 심사 기간만이라도 배포에서 빼두는 게 나을 것 같아서 `_config.yml`의 `exclude` 목록에 잠깐 올려놨습니다. 사이드바에서도 해당 링크를 주석 처리해서, 방문자가 실수로 깨진 링크를 밟는 일도 없게 막아뒀습니다.

---

<h2 id="removal-request">4. 서치 콘솔에 삭제 요청까지 넣었는데</h2>

브런치·티스토리에서 검색 결과가 완전히 빠지는 걸 앞당기려고, 서치 콘솔의 URL 삭제(제거) 도구로도 신청을 넣었습니다.

![서치 콘솔 URL 삭제 요청 목록](/assets/img/posts/2026-08-12/tistory-removal-request.png)
*서치 콘솔 삭제 도구 — 티스토리 URL 제거 요청이 "일시적으로 삭제됨" 상태로 처리된 모습.*

그런데 이걸 하면서 하나 배운 게, **이 삭제 요청은 구글 검색 결과 화면에서만 임시로(보통 6개월) 숨기는 기능**이라는 겁니다. 원본 페이지 자체가 삭제되는 게 아니라서, 브런치나 티스토리 쪽 글을 실제로 비공개 처리하는 작업은 어차피 따로 해줘야 했습니다. 검색 결과만 가린다고 안심할 문제가 아니었던 거죠.

---

<h2 id="index-request">5. 색인 요청도 넣어봤습니다만</h2>

최근에 쓴 오리지널 글 중에서 퀄리티 있다고 생각하는 9개를 골라서, 서치 콘솔에서 수동으로 색인 생성 요청을 넣었습니다. 그리고 구글 서치 콘솔 API로 실시간으로 색인 상태를 다시 조회해봤는데,

![색인 생성 요청됨](/assets/img/posts/2026-08-12/index-request-queued.png)
*"URL이 우선순위 크롤링 대기열에 추가되었습니다"라는 안내가 떴습니다.*

며칠이 지나도 9개 전부 여전히 "Google에는 아직 알려지지 않은 URL입니다" 그대로였습니다. 홈페이지조차 마지막 크롤 시각이 며칠째 그대로였고요. 신생 도메인이라 그런지, 색인 요청 자체가 크롤 우선순위를 크게 못 올려주는 것 같습니다. 이 부분은 여전히 진행 중인 숙제입니다.

---

<h2 id="retry">6. 그래서 재신청은 했냐면</h2>

원래는 "검색에 노출되고 트래픽이 실제로 들어오기 시작하면 재신청하자"는 게 제 계획이었습니다. 재시도해서 또 막히면 페널티가 있다는 얘기를 들어서 신중하게 가려고 한 거였는데, 앞서 말했듯이 애드센스 심사는 검색 색인 여부와는 별개 트랙이라는 걸 알게 됐습니다. 그래서 색인을 기다리기보다, 지금까지 정리한 것들(브런치 비공개, 티스토리 비공개, 캐노니컬 수정, 얇은 페이지 제외)을 근거로 먼저 재검토를 요청해보기로 했습니다.

![문제 수정 확인 후 검토 요청](/assets/img/posts/2026-08-12/review-request-button.png)
*"문제를 수정했음을 확인합니다"에 체크하고 검토 요청 버튼을 눌렀습니다.*

**결론은 아직 안 났습니다.** 심사 결과가 나오는 대로 이어서 정리해보겠습니다. 승인이 나면 지금 숨겨둔 게시판·오픈채팅 링크도 원래대로 복구할 거고, 또 막히면 이번엔 정말 콘텐츠 자체의 분량과 깊이를 하나씩 다시 뜯어봐야 할 것 같습니다.

---

### 지금까지 체크리스트

- [x] 브런치 이관 글 21개 전부 비공개
- [x] 티스토리 전체 비공개
- [x] 구 깃헙 블로그 캐노니컬을 새 블로그 주소로 수정
- [x] 서치 콘솔 URL 삭제(제거) 요청
- [x] 얇은 콘텐츠 페이지(게시판·오픈채팅) 임시 제외
- [x] 오리지널 글 9개 수동 색인 요청
- [ ] 애드센스 재검토 결과 — **대기 중**
- [ ] (승인 시) 게시판·오픈채팅 링크 복구

결과 나오는 대로 후속편으로 업데이트하겠습니다.
