---
layout: default
title: 소개
permalink: /about/
---

<section class="about-hero">
  <img class="about-hero__avatar" src="{{ '/assets/img/avatar.png' | relative_url }}" alt="판뚜|panddu 채널 프사" width="160" height="160">
  <h1 class="about-hero__title">안녕하세요. 판뚜입니다</h1>
  <p class="about-hero__tagline muted">파워 영세 유튜버 / 개발자이기만 하고 개발얘기 잘 안하는 파워 직장인</p>
</section>

이 블로그는 그 채널의 곁가지 같은 공간이에요. 영상으로 다루기엔 결이 안 맞거나 길이가 안 나오는 얘기, 시청자분들이 보내주신 질문 묶음, 가끔 적어두고 싶은 메모 같은 걸 올립니다. 본격적인 글쓰기라기보단 영상 옆에 두는 부록 같은 결로 갈 거 같아요.

## 시리즈

{% for s in site.data.series %}
{%- assign key = s[0] %}{%- assign meta = s[1] -%}
- <a href="{{ '/series/' | append: key | append: '/' | relative_url }}" class="series-badge" style="color: {{ meta.color }}; background: {{ meta.bg }};">{{ meta.bracket }}</a> {{ meta.desc }}
{% endfor %}

## 연락

- [https://www.youtube.com/@panddu](https://www.youtube.com/@panddu)
- mg.studio.kr@gmail.com
