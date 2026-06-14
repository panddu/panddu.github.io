---
layout: post
title: "내가 굴리는 4개 프로젝트"
date: 2026-06-14 10:10:00 +0900
category: tech
description: "mingus-kit, mingus-agent, mingus-studio, panddu.github.io가 어떻게 연결되는지 정리한 구조도 드래프트"
---

<style>
.mk-board{
  --mk-bg:#faf8f4;
  --mk-paper:#ffffff;
  --mk-ink:#182033;
  --mk-muted:#5f6b7e;
  --mk-line:#dfe5ef;
  --mk-green:#1fa34a;
  --mk-green-soft:#effbf2;
  --mk-blue:#316dff;
  --mk-blue-soft:#f0f5ff;
  --mk-pink:#ea4897;
  --mk-pink-soft:#fff1f7;
  --mk-purple:#8a5cff;
  --mk-purple-soft:#f5efff;
  --mk-orange:#fb8c20;
  --mk-orange-soft:#fff3e6;
  position:relative;
  margin:8px 0 20px;
  padding:22px 24px;
  background:
    radial-gradient(circle at 12% 14%, rgba(251,140,32,.10), transparent 0 18%),
    radial-gradient(circle at 84% 18%, rgba(49,109,255,.10), transparent 0 16%),
    radial-gradient(circle at 68% 86%, rgba(138,92,255,.10), transparent 0 20%),
    linear-gradient(180deg, #fffdf9, var(--mk-bg));
  border:1px solid #eee8dd;
  border-radius:28px;
  overflow:hidden;
}
.mk-board *{box-sizing:border-box;}
.mk-board__canvas{
  position:relative;
  min-height:520px;
}
.mk-card{
  position:absolute;
  width:250px;
  padding:18px 18px 16px;
  background:rgba(255,255,255,.88);
  border:2px solid var(--mk-line);
  border-radius:24px;
  box-shadow:0 18px 38px rgba(17,24,39,.08);
  backdrop-filter:blur(8px);
}
.mk-card--kit{
  left:10px;
  top:18px;
  border-color:rgba(31,163,74,.55);
  background:linear-gradient(180deg, rgba(239,251,242,.92), rgba(255,255,255,.94));
}
.mk-card--agent{
  right:10px;
  top:18px;
  width:250px;
  border-color:rgba(49,109,255,.45);
  background:linear-gradient(180deg, rgba(240,245,255,.94), rgba(255,255,255,.96));
}
.mk-card--studio{
  right:10px;
  top:276px;
  border-color:rgba(234,72,151,.45);
  background:linear-gradient(180deg, rgba(255,241,247,.94), rgba(255,255,255,.96));
}
.mk-card--blog{
  left:10px;
  top:276px;
  width:250px;
  border-color:rgba(138,92,255,.42);
  background:linear-gradient(180deg, rgba(245,239,255,.94), rgba(255,255,255,.96));
}
.mk-chip{
  display:inline-flex;
  align-items:center;
  gap:6px;
  padding:6px 12px;
  border-radius:999px;
  font-size:13px;
  font-weight:800;
  letter-spacing:.01em;
  border:1px solid currentColor;
  background:#fff;
}
.mk-card--kit .mk-chip{color:var(--mk-green);}
.mk-card--agent .mk-chip{color:var(--mk-blue);}
.mk-card--studio .mk-chip{color:var(--mk-pink);}
.mk-card--blog .mk-chip{color:var(--mk-purple);}
.mk-card__name{
  margin:14px 0 8px;
  font-size:30px;
  line-height:1.05;
  letter-spacing:-.03em;
  font-weight:900;
  color:var(--mk-ink);
}
.mk-card__meta{
  margin:0;
  color:#334155;
  font-size:15px;
  line-height:1.55;
  font-weight:700;
  letter-spacing:-.01em;
}
.mk-card__accent{
  display:inline-flex;
  align-items:center;
  padding:7px 12px 6px;
  margin:0 0 10px;
  border-radius:999px;
  font-size:13px;
  font-weight:900;
  letter-spacing:.02em;
}
.mk-card__accent--koog{
  background:var(--mk-blue);
  color:#fff;
  box-shadow:0 10px 24px rgba(49,109,255,.22);
}
.mk-bear{
  position:absolute;
  left:50%;
  top:206px;
  transform:translateX(-50%);
  display:flex;
  align-items:center;
  gap:14px;
  padding:12px 14px 12px 10px;
  border-radius:20px;
  background:rgba(255,255,255,.74);
  border:1px dashed rgba(251,140,32,.45);
  box-shadow:0 12px 28px rgba(17,24,39,.06);
}
.mk-bear__logo{
  width:58px;
  height:58px;
  border-radius:16px;
  object-fit:cover;
  flex:none;
  box-shadow:0 8px 18px rgba(17,24,39,.10);
}
.mk-bear__title{
  margin:0;
  font-size:22px;
  line-height:1;
  font-weight:900;
  color:var(--mk-orange);
  letter-spacing:-.03em;
}
.mk-mobile-list{display:none;}
@media (max-width: 820px){
  .mk-board{padding:24px 16px 22px;}
  .mk-board__canvas{display:none;}
  .mk-mobile-list{
    display:grid;
    gap:14px;
  }
  .mk-mobile-card{
    padding:16px;
    border-radius:18px;
    background:#fff;
    border:1px solid var(--mk-line);
  }
  .mk-mobile-card h3{
    margin:10px 0 8px;
    font-size:22px;
    line-height:1.1;
    letter-spacing:-.03em;
  }
  .mk-mobile-card p{
    margin:0;
    color:#374151;
    font-size:15px;
    line-height:1.58;
  }
  .mk-mobile-flow{
    margin-top:10px;
    font-size:13px;
    color:#6b7280;
  }
}
</style>

<section class="mk-board">
  <div class="mk-board__canvas">
    <article class="mk-card mk-card--kit">
      <span class="mk-chip">운영</span>
      <h3 class="mk-card__name">mingus-kit</h3>
      <p class="mk-card__meta">유튜브 분석 · 블로그 분석<br>캘린더 연동 · 세션영속화</p>
    </article>

    <article class="mk-card mk-card--agent">
      <span class="mk-chip">분석</span>
      <h3 class="mk-card__name">mingus-agent</h3>
      <div class="mk-card__accent mk-card__accent--koog">KOOG + 로컬 AI</div>
      <p class="mk-card__meta">QnA / 상담소 데이터 분류 및 가공<br>자동 자막 생성 보정</p>
    </article>

    <article class="mk-card mk-card--studio">
      <span class="mk-chip">제작</span>
      <h3 class="mk-card__name">mingus-studio</h3>
      <p class="mk-card__meta">목소리 복제 · 자동 자막 달기<br>파컷 프로젝트 생성</p>
    </article>

    <article class="mk-card mk-card--blog">
      <span class="mk-chip">공개</span>
      <h3 class="mk-card__name">panddu.github.io</h3>
      <p class="mk-card__meta">posts</p>
    </article>

    <div class="mk-bear">
      <img class="mk-bear__logo" src="/assets/img/bear-app-icon.png" alt="Bear logo">
      <div>
        <p class="mk-bear__title">Bear</p>
      </div>
    </div>

  </div>

  <div class="mk-mobile-list">
    <article class="mk-mobile-card">
      <span class="mk-chip" style="color:var(--mk-green)">운영</span>
      <h3>mingus-kit</h3>
      <p>스킬과 세션영속화를 묶는 운영 허브.</p>
      <div class="mk-mobile-flow">세션영속화 / `wrap-all` / Bear</div>
    </article>
    <article class="mk-mobile-card">
      <span class="mk-chip" style="color:var(--mk-blue)">분석</span>
      <h3>mingus-agent</h3>
      <p>Koog와 로컬 AI로 QnA, 상담소 데이터를 분류하고 가공한다.</p>
      <div class="mk-mobile-flow">자동 자막 생성 보정 / `qna_recording.txt`</div>
    </article>
    <article class="mk-mobile-card">
      <span class="mk-chip" style="color:var(--mk-pink)">제작</span>
      <h3>mingus-studio</h3>
      <p>대본과 음성을 실제 편집 자산으로 만든다.</p>
      <div class="mk-mobile-flow">`voice.wav` / `subtitles.srt` / `FCPXML`</div>
    </article>
    <article class="mk-mobile-card">
      <span class="mk-chip" style="color:var(--mk-purple)">공개</span>
      <h3>panddu.github.io</h3>
      <p>포스트를 공개하는 채널.</p>
      <div class="mk-mobile-flow">posts</div>
    </article>
    <article class="mk-mobile-card">
      <span class="mk-chip" style="color:var(--mk-orange)">원본</span>
      <h3>Bear</h3>
      <p>persona, worklog 같은 사용자 원본 데이터 저장소.</p>
    </article>
  </div>
</section>
