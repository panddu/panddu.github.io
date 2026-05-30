---
layout: default
title: 소개
permalink: /about/
---

<section class="about-hero">
  <img class="about-hero__avatar" src="{{ '/assets/img/avatar.png' | relative_url }}" alt="판교뚜벅쵸 채널 프사" width="160" height="160">
  <h1 class="about-hero__title">안녕하세요, 판뚜입니다</h1>
  <p class="about-hero__tagline muted">파워 영세 유튜버 / 판교 어딘가의 직장인</p>
</section>

판교 어딘가에서 직장 다니면서 가끔 유튜브 채널 **판교뚜벅쵸**를 굴리고 있습니다.

자칭 파워 영세 유튜버고, 본업은 직장인이라 영상은 퇴근하고 나서나 주말에 짬을 내서 만들어요. AI니 개발이니 뭐 그런 거 얘기하는 척하지만 사실 그쪽 전문가는 아니고, 그냥 한 명의 사용자로서 느낀 거 적당히 풀어놓는 채널 정도로 봐주시면 좋을 거 같습니다.

이 블로그는 그 채널의 곁가지 같은 공간이에요. 영상으로 다루기엔 결이 안 맞거나 길이가 안 나오는 얘기, 시청자분들이 보내주신 질문 묶음, 가끔 적어두고 싶은 메모 같은 걸 올립니다. 본격적인 글쓰기라기보단 영상 옆에 두는 부록 같은 결로 갈 거 같아요.

## 시리즈

{% for s in site.data.series %}
{%- assign key = s[0] %}{%- assign meta = s[1] -%}
- <a href="{{ '/series/' | append: key | append: '/' | relative_url }}" class="series-badge" style="color: {{ meta.color }}; background: {{ meta.bg }};">{{ meta.bracket }}</a> {{ meta.desc }}
{% endfor %}

## 자주 등장하는 사람들

- **뚜기** — 아들. 발달·찡찡·이유식·돌·사고 등의 이슈로 영상에 자주 끌려나옴.
- **뚜부인** — 아내. 영상 편집과 채널 운영의 절반 이상을 사실상 책임지는 분.

## 동네

판교, 용인, 수내, 정자, 동천동 어딘가. 동네 분들 종종 댓글로 만납니다.

## 연락

- 유튜브 채널: [@panddu](https://www.youtube.com/@panddu)
- **뚜쪽 상담소** (시청자 질문 폼) — 영상 설명란에서 받습니다.
- 이 블로그의 모든 글 하단에 GitHub 댓글이 있어요. 로그인 필요해서 진입 장벽 좀 있긴 한데, 그래도 남겨주시면 감사히 읽습니다.
