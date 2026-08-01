---
layout: post
title: "스팸체 생성기"
date: 2019-04-18 14:00:30 +0900
category: workroom
excerpt: "글귀를 스팸체, 한국인전용체로 바꿔주는 미니 웹앱입니다."
---

> 💡 이 글은 예전 블로그(mingpd.github.io)에서 마이그레이션된 글입니다.

## 소개

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin: 20px 0;">
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px;">
    <div style="font-size: 13px; font-weight: 700; color: var(--accent); margin-bottom: 8px;">스팸체</div>
    <p style="margin: 0 0 10px; color: var(--ink-soft);">스팸체를 만들 수 있습니다.</p>
    <div style="font-family: &quot;SF Mono&quot;, Menlo, Consolas, monospace; font-size: 0.92em; background: var(--code-bg); border-radius: 8px; padding: 10px 12px; white-space: nowrap; overflow-x: auto; line-height: 1.6;">亼✣팸ღㅊㅔ✽를✚만✬들✏㐃✺있✪습L1딻.✮</div>
  </div>
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px;">
    <div style="font-size: 13px; font-weight: 700; color: var(--accent); margin-bottom: 8px;">한국인전용체</div>
    <p style="margin: 0 0 10px; color: var(--ink-soft);">한국인만 읽을 수 있는 글을 만들 수 있습니다.</p>
    <div style="font-family: &quot;SF Mono&quot;, Menlo, Consolas, monospace; font-size: 0.92em; background: var(--code-bg); border-radius: 8px; padding: 10px 12px; white-space: nowrap; overflow-x: auto; line-height: 1.6;">한국읹많 읽읊 수 있늕 글읊 많들 쑮 있습니땂.</div>
  </div>
</div>

<div style="border: 1px solid var(--line, #e8eaf0); border-radius: 10px; overflow: hidden; margin: 20px 0 24px;">
  <iframe src="/assets/workroom/spammaker/widget.html" width="100%" height="630" frameborder="0" style="display:block;"></iframe>
</div>

## 변환 규칙

| 규칙 | 예시 |
| --- | --- |
| 가능한 경우 한글을 가로로 쪼개자. | 스위치 → 스우ㅣㅊㅣ |
| 쪼개진 자모를 특문으로 바꾸자. | ㄱㅏㄴㅏ → 7r ㄴr |
| 초성, 종성을 복잡하게 바꾸자. | 치킨먹자 → 칧킪먻짞 |
| 공백을 특수문자로 채우자. | 연결 고리 → 연결✦고리 |
| 공백이 아니어도 특정 확률로 특문을 넣자. | 동해물과백두 → 동해물✿과❅백♛➳두 |
| 영문자를 전각으로 바꾸자. | abc → ａｂｃ |
| 숫자를 전각으로 바꾸거나 특문으로 바꾸자. | 123 → 丨己彐 |
| 위를 다 하고도 바꿀 수 있다면 바꾸자. | 스고 → 亼卫 |

위 규칙 중 한글을 다루는 부분의 원리가 궁금하다면 [한글 유니코드를 초성, 중성, 종성으로 쪼개자](/posts/2019/04/unicode-hangle/)를 참고해주세요.
