---
layout: post
title: "\"코딩 몰라도 된다 vs 기본기 필수\" 댓글 91개 까봤습니다 (2:1의 비밀)"
date: 2026-11-05 21:00:00 +0900
category: essay
excerpt: "지난번 '개발 지식은 높은데 코딩 못하는 사람 뽑을 것인가' 영상 이후 댓글이 91개나 달렸습니다. 궁금해서 찬반 통계를 전수 조사해 봤더니 소름 돋게 '2 : 1' 황금 비율이 나오더군요. 현업 개발자들의 뼈 때리는 댓글들을 정리해 봅니다."
---

<p style="margin: 0 0 24px;">
  <a href="https://youtu.be/SDbYbAoKoC4" target="_blank" rel="noopener noreferrer" style="font-weight: 600; display: inline-flex; align-items: center; gap: 8px; color: #e62117; text-decoration: none;">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" style="flex-shrink: 0;"><path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.11C19.517 3.545 12 3.545 12 3.545s-7.517 0-9.388.508a3.003 3.003 0 0 0-2.11 2.11C0 8.033 0 12 0 12s0 3.967.502 5.837a3.003 3.003 0 0 0 2.11 2.11c1.871.508 9.388.508 9.388.508s7.517 0 9.388-.508a3.003 3.003 0 0 0 2.11-2.11C24 15.967 24 12 24 12s0-3.967-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    <span style="border-bottom: 1px solid rgba(230, 33, 23, 0.35);">▶ 원본 영상 보기: “뽑는다? 안 뽑는다?”.. 판뚜네 개발팀 콜로세움 열렸습니다</span>
  </a>
</p>

<div class="toc-box">
  <p class="toc-title">목차</p>
  <ul>
    <li><a href="#prologue">1. 발단: 판뚜네 댓글창이 왜 이렇게 뜨겁죠?</a></li>
    <li><a href="#stats">2. 통계: 91개 댓글 전수 조사 결과 (정확히 2:1?)</a></li>
    <li><a href="#pro-coding">3. 친코딩파 (66.7%): "악보 못 보는 피아니스트와 장애의 공포"</a></li>
    <li><a href="#anti-coding">4. 탈코딩파 (33.3%): "어셈블리어의 기시감과 기획자의 인프라 침공"</a></li>
    <li><a href="#killing-point">5. 킬링 포인트: "고민하는 사이 육각형만 뽑혀갔다"</a></li>
    <li><a href="#epilogue">6. 마치며: 결국 '코드'가 아니라 '책임'의 문제</a></li>
    <li><a href="#youtube-section">🎬 원본 토론 영상 보기</a></li>
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
    color: var(--ink, #1f2937);
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
    color: var(--accent, #0284c7);
  }
  .quote-box {
    background: var(--quote-bg, #f8fafc);
    border: 1px solid var(--line, #e2e8f0);
    border-left: 4px solid var(--accent, #5b6cff);
    padding: 16px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    font-size: 15.5px;
    line-height: 1.7;
    color: var(--ink, #1f2937);
  }
  .quote-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    flex-wrap: wrap;
    gap: 8px;
  }
  .quote-author {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--accent, #5b6cff);
  }
  .comment-jump-link {
    font-size: 12px;
    color: var(--muted, #64748b);
    text-decoration: none;
    padding: 2px 8px;
    border-radius: 4px;
    background: var(--chip, rgba(0,0,0,0.05));
    border: 1px solid var(--line, rgba(0,0,0,0.1));
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 3px;
  }
  .comment-jump-link:hover {
    color: var(--accent, #5b6cff);
    border-color: var(--accent, #5b6cff);
  }
</style>

<h2 id="prologue">1. 발단: 판뚜네 댓글창이 왜 이렇게 뜨겁죠?</h2>

며칠 전, 저희 팀 회의실에서 점심 먹다 터진 난상토론을 유튜브에 올렸습니다.

> **"시스템 설계와 CS 지식은 시니어급인데, 자바든 파이썬이든 코드는 한 줄도 못 읽는 지원자가 오면 뽑을 것인가?"**

저는 그냥 평소처럼 판교 직장인의 가벼운 잡담 영상으로 올렸는데, 댓글창 알림이 쉴 새 없이 울리더라고요. 

영세 채널 치고는 이례적일 정도로 현직 시니어 개발자, 빅테크 재직자, 대기업 IT PM, 비개발자 기획자, 심지어 해외에서 채용하시는 분들까지 등판하셔서 진지한 장문의 현장 경험담을 쏟아내셨습니다. 

대댓글을 하나하나 달다 보니 문득 궁금해졌습니다.  
**"과연 현업 사람들은 '친코딩파'와 '탈코딩파' 중 어디에 더 많이 손을 들어줬을까?"**

그래서 달린 댓글 **91개**를 하나도 빠짐없이 엑셀에 모아서 전수 조사를 돌려봤습니다.

---

<h2 id="stats">2. 통계: 91개 댓글 전수 조사 결과 (정확히 2:1?)</h2>

우선 91개 전체 댓글의 분포는 이렇습니다:

- **친코딩파 (안 뽑는다 / 코드 필수)**: 42개 (46.2%)
- **탈코딩·반코딩파 (뽑는다 / AI·설계 우선)**: 21개 (23.1%)
- **중립·기타 (판단 유보 / 닭과 달걀 / 뚜기 귀엽다 등)**: 28개 (30.8%)

여기서 단순 감상이나 중립 의견을 제외하고, **명확하게 찬반 입장을 밝힌 63명**만 추려봤는데요. 

결과가 소름 돋게 떨어집니다.

```text
친코딩파 (안 뽑는다 / 코드 기본기 필수)   : 42명 (66.7%)
탈코딩파 (뽑는다 / 설계와 AI 활용이 우선) : 21명 (33.3%)
```

**정확히 2 : 1 황금 비율**이 나왔습니다.  
아무리 바이브코딩과 AI 에이전트가 판을 쳐도, 현업에서는 **"그래도 코드를 읽고 검증하는 기본기는 절대 타협 못 한다"**는 입장이 2배 더 우세했던 것이죠.

하지만 33.3%를 차지한 '탈코딩파'의 반론도 결코 만만치 않았습니다. 양쪽의 뼈 때리는 베스트 코멘트들을 모아봤습니다.

---

<h2 id="pro-coding">3. 친코딩파 (66.7%): "악보 못 보는 피아니스트와 장애의 공포"</h2>

친코딩파 분들의 의견을 관통하는 키워드는 **'유지보수'**, **'운영 장애(핫픽스)'**, 그리고 **'비용'**이었습니다.

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 해외 비영리단체 채용 담당자</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgzVlaoLz38xko2vm914AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "거장이 악보 안 보고 감으로 피아노 치는 것과, 일반인이 감으로 콩쿠르 상 한번 탔다고 거장이 되는 건 완전히 다른 이야기입니다. 코딩 기초 없이 AI로 딸깍해서 가져온 결과물을 보면 도대체 무슨 프로젝트를 하겠다는 건지 의도조차 파악이 안 됩니다. 저희는 최소한 코드 까막눈은 아닌 사람으로 데려갑니다."
</div>

가장 많은 무릎을 치게 만들었던 '피아노 악보' 비유입니다. 이미 기본기가 극에 달해 악보를 안 봐도 되는 경지와, 악보를 볼 줄 몰라서 감으로만 치는 것은 겉보기엔 비슷해 보여도 본질이 다르다는 지적이었죠.

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 시니어 백엔드 개발자</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=Ugz_Pbl-KOE3v-iipb54AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "어제 코딩할 줄 모르는 팀원이 바이브코딩으로 만든 코드를 봤습니다. 이걸 어디서부터 고쳐야 할지 답답했습니다... 기본 개념 없이 오직 '구현'만 목표로 만들어 놔서 유지보수와 추가 개발이 지옥문이겠더라고요."
</div>

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 대기업 전산 시스템 관리자</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgxBI3bcsKiDMzKGR0d4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "평소엔 저도 AI에게 다 시키지만, 전사 긴급 장애가 터졌을 때는 제가 직접 코드를 한 줄 한 줄 뜯어봅니다. 시스템이 뻗었을 때 결국 책임은 사람이 지는 거니까요. 6개월 뒤든 5년 뒤든 코드를 직접 읽을 줄 아는 자가 우위를 점할 수밖에 없습니다."
</div>

또 하나 현실적인 지적은 **'토큰 가성비'**였습니다:

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 현직 개발자 (토큰 경제학)</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgyYpJ2dpFjckp_o0TR4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "코드를 볼 줄 모르면 문제점이나 수정 지점을 찾는 것조차 AI한테 계속 물어보며 토큰을 태워야 합니다. 코드를 읽는 사람과 토큰 사용량 격차가 벌어지면 결국 가성비가 안 나옵니다."
</div>

결국 **"장애 났을 때 감당할 수 있냐"**와 **"남이 싼 똥을 치울 수 있냐"**라는 실무자의 짙은 피로감이 친코딩파의 66.7%를 만들었습니다.

---

<h2 id="anti-coding">4. 탈코딩파 (33.3%): "어셈블리어의 기시감과 기획자의 인프라 침공"</h2>

반면 33.3%의 탈코딩파는 **'엔지니어링의 역사'**와 **'현업의 급격한 체감 변화'**를 근거로 들었습니다.

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 시니어 엔지니어</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgzWHGMG08wquCvC-Ot4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "예전에 C언어나 고수준 언어가 처음 나왔을 때도 '기계어나 어셈블리어를 꼭 알아야 진정한 프로그래머인가?'라고 묻지 않았습니까? 프로그래밍 언어 자체가 점차 인간의 언어 쪽으로 추상화되는 과정일 뿐입니다."
</div>

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 대기업 IT PM</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgzQ7CQdXGmQ3VpRoqt4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "개발 코드에 직접 손대는 사람은 이제 저평가합니다. 시스템 전체 흐름을 제어하고 큰 그림을 그릴 줄 아는 사람을 고평가합니다."
</div>

실제로 대기업 8년 차 개발자분(<a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgwnwAGG2jt1XCJb6Sh4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 ↗</a>)께서는 *"영상 속 주니어분 말씀처럼, 솔직히 저도 요즘 코드를 거의 안 봅니다"*라며 고백하셨고, 한 IT 기획자분은 상징적인 한마디를 던지셨습니다:

<div class="quote-box">
  <div class="quote-header">
    <span class="quote-author">💬 IT 기획자</span>
    <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgwWfYqH6fJFBzSEZj94AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
  </div>
  "음… IT 기획자가 AI로 테라폼(IaaC) 인프라 코드까지 다 짜고 있습니다만…?!?!!"
</div>

원래 인프라 엔지니어의 고유 영역이었던 클라우드 코드마저 기획자가 AI로 뚝딱 짜내는 시대인데, 개발자가 특정 언어 문법에 매달리는 게 과연 본질이냐는 질문이었습니다. 

---

<h2 id="killing-point">5. 킬링 포인트: "고민하는 사이 육각형만 뽑혀갔다"</h2>

진지한 토론 와중에 댓글창을 빵 터지게 만든 명언들도 있었습니다.

* **현실적인 취업 시장의 비극**:  
  > *"누굴 뽑을지 고민하는 사이, 코드만 못 짜는 사람과 설계만 못하는 사람 둘 다 떨어지고 **'꽉 찬 육각형 인재'**만 뽑혀갔습니다 ㅋㅋㅋ"*  
  <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgzGsOspDv_9o193W654AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
* **최종 면접 합격 기준**:  
  > *"코딩을 모르더라도 AI가 생성한 코드에 대해 **책임지고 대신 감옥에 갈 수 있는 신뢰**가 있다면 채용 OK입니다."*  
  <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=Ugyp-Lu2sqmTpSFlbhB4AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>
* **가장 짧고 강렬한 자조**:  
  > *"이젠 친코딩파 마저도 코딩 못함"*  
  <a href="https://www.youtube.com/watch?v=SDbYbAoKoC4&lc=UgxyBQm37GyntTZTDS94AaABAg" target="_blank" rel="noopener noreferrer" class="comment-jump-link">댓글 원문 보기 ↗</a>

---

<h2 id="epilogue">6. 마치며: 결국 '코드'가 아니라 '책임'의 문제</h2>

댓글 91개를 하나하나 읽으면서 제가 내린 결론은 하나였습니다.

우리가 회의실에서 치고받았던 논쟁은 사실 **"코드를 직접 타이핑할 줄 아느냐"**의 문제가 아니었습니다.  
**"AI가 만든 시스템에 문제가 생겼을 때, 그 동작을 끝까지 추적하고 온전히 책임질 수 있는가"**의 문제였던 거죠.

악보를 못 봐도 피아노를 연주할 순 있습니다.  
하지만 연주 도중 건반 하나가 빗나갔을 때, 어디서부터 화음이 깨졌는지 짚어낼 수 없는 연주자에게 오케스트라의 한 파트를 온전히 맡기기는 아직 불안한 법입니다.

영상 말미에도 말씀드렸지만, 사실 6개월 뒤에 제가 무슨 생각을 하고 있을지도 저 스스로 잘 모르겠습니다. 

지금은 '친코딩파'의 2:1 판정승이지만, 과연 6개월 뒤 프론티어 AI 모델들이 또 한 번 퀀텀 점프를 했을 때는 이 비율이 어떻게 바뀌어 있을까요? 😄

---

<h2 id="youtube-section">🎬 원본 토론 영상 보기</h2>

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
