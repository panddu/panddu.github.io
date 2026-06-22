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

---

## 층층이 정돈된 계층 구조 (Layered Pipeline Map)

콘텐츠 기획부터 세상에 나오기까지의 4단계 계층 구조입니다. 최하단에서 데이터가 쌓이고 위로 가면서 지능이 더해져 최상단의 채널로 흘러갑니다.

<div class="project-layered-map" style="margin: 32px 0; display: flex; flex-direction: column; gap: 16px; width: 100%;">

  <!-- 1. Presentation Layer (최상단) -->
  <div style="background: var(--card); border: 2px solid var(--line); border-radius: 20px; padding: 22px 24px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.02); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, #ea4897, #8a5cff);"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
      <span style="font-size: 13px; font-weight: 800; color: #8a5cff; letter-spacing: 0.03em; text-transform: uppercase;">1. Presentation Layer (최상단)</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 12px; font-weight: 700;">최종 노출 채널</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-top: 14px;">
      <div style="background: var(--bg); border: 1px solid var(--line); padding: 16px; border-radius: 14px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <span style="font-size: 20px;">✍️</span>
          <strong style="font-size: 16px; color: var(--ink);">panddu.github.io</strong>
        </div>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">개발 로그, 생각 정리, 문제 해결 과정을 담아내는 마크다운 기반 깃허브 블로그</p>
      </div>
      <div style="background: var(--bg); border: 1px solid var(--line); padding: 16px; border-radius: 14px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <span style="font-size: 20px;">🎥</span>
          <strong style="font-size: 16px; color: var(--ink);">판교 뚜벅쵸 (YouTube)</strong>
        </div>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">영상 자산 및 목소리 복제, 자동 편집 등을 거쳐 공개되는 메인 영상 채널</p>
      </div>
    </div>
  </div>

  <!-- Connection Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -4px 0; color: var(--line);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <line x1="12" y1="19" x2="12" y2="5"></line>
      <polyline points="5 12 12 5 19 12"></polyline>
    </svg>
  </div>

  <!-- 2. Agent & Studio Layer -->
  <div style="background: var(--card); border: 2px solid var(--line); border-radius: 20px; padding: 22px 24px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.02); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, #316dff, #ea4897);"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
      <span style="font-size: 13px; font-weight: 800; color: #316dff; letter-spacing: 0.03em; text-transform: uppercase;">2. Agent & Studio Layer</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 12px; font-weight: 700;">콘텐츠 기획 및 협업 자동화</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-top: 14px;">
      <div style="background: var(--bg); border: 1px solid var(--line); padding: 16px; border-radius: 14px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <span style="font-size: 18px;">🤖</span>
          <strong style="font-size: 16px; color: var(--ink);">mingus-agent</strong>
        </div>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">지능형 비서. 웹 리서치, 자료 조사, QnA 상담소 데이터 분류 및 핵심 인사이트 가공 담당</p>
      </div>
      <div style="background: var(--bg); border: 1px solid var(--line); padding: 16px; border-radius: 14px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <span style="font-size: 18px;">🎬</span>
          <strong style="font-size: 16px; color: var(--ink);">mingus-studio</strong>
        </div>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">제작 허브. 영상 각본(스크립트) 작성, FCPXML 자동 생성 및 음성/자막 편집 관리</p>
      </div>
    </div>
    <div style="margin-top: 14px; font-size: 12px; color: var(--muted); background: var(--bg); padding: 10px 14px; border-radius: 8px; text-align: center; border: 1px dashed var(--line);">
      💡 <strong>mingus-agent</strong>와 <strong>mingus-studio</strong>가 지속적으로 상호 작용하며 원본을 정제된 글과 영상 대본으로 빌딩합니다.
    </div>
  </div>

  <!-- Connection Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -4px 0; color: var(--line);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <line x1="12" y1="19" x2="12" y2="5"></line>
      <polyline points="5 12 12 5 19 12"></polyline>
    </svg>
  </div>

  <!-- 3. Skill & Engine Layer -->
  <div style="background: var(--card); border: 2px solid var(--line); border-radius: 20px; padding: 22px 24px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.02); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: #1fa34a;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 800; color: #1fa34a; letter-spacing: 0.03em; text-transform: uppercase;">3. Skill & Engine Layer</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 12px; font-weight: 700;">실행 허브 & 비즈니스 로직</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; margin-top: 14px;">
      <div style="flex: 1; min-width: 280px;">
        <strong style="font-size: 18px; color: var(--ink); display: block; margin-bottom: 6px;">🛠️ mingus-kit</strong>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">지능/프리젠테이션 레이어와 하단의 영속 데이터 레이어를 이어주는 허브. 실제로 작동 가능한 다양한 스킬(CLI 커맨드)들이 구현되어 있습니다.</p>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 8px; flex-shrink: 0; max-width: 100%;">
        <span style="font-size: 12px; background: var(--chip); color: var(--ink); border: 1px solid var(--line); padding: 6px 12px; border-radius: 8px; font-weight: 600;">👤 persona-build</span>
        <span style="font-size: 12px; background: var(--chip); color: var(--ink); border: 1px solid var(--line); padding: 6px 12px; border-radius: 8px; font-weight: 600;">📂 resume / wrap</span>
        <span style="font-size: 12px; background: var(--chip); color: var(--ink); border: 1px solid var(--line); padding: 6px 12px; border-radius: 8px; font-weight: 600;">📝 worklog</span>
        <span style="font-size: 12px; background: var(--chip); color: var(--ink); border: 1px solid var(--line); padding: 6px 12px; border-radius: 8px; font-weight: 600;">💡 panddu-idea</span>
      </div>
    </div>
  </div>

  <!-- Connection Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -4px 0; color: var(--line);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <line x1="12" y1="19" x2="12" y2="5"></line>
      <polyline points="5 12 12 5 19 12"></polyline>
    </svg>
  </div>

  <!-- 4. Persistence Layer (최하단) -->
  <div style="background: var(--card); border: 2px solid var(--line); border-radius: 20px; padding: 22px 24px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.02); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; height: 5px; background: #fb8c20;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 800; color: #fb8c20; letter-spacing: 0.03em; text-transform: uppercase;">4. Persistence Layer (최하단)</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 12px; font-weight: 700;">영속 데이터 저장소</span>
    </div>
    <div style="display: flex; align-items: center; gap: 16px; margin-top: 14px;">
      <img src="/assets/img/bear-app-icon.png" alt="Bear App Icon" style="width: 54px; height: 54px; border-radius: 12px; flex-shrink: 0; border: 1px solid var(--line);">
      <div>
        <strong style="font-size: 18px; color: var(--ink); display: block; margin-bottom: 4px;">🐻 Bear App (노트)</strong>
        <p style="margin: 0; font-size: 13px; color: var(--muted); line-height: 1.5;">모든 생각, 콘텐츠 소스, 일기, 업무 로그, 영상각 아이디어들이 가장 깊은 곳에 영속화되어 쌓여 있습니다. 이 전체 구조의 단일 진실 공급원(SSOT) 역할을 수행합니다.</p>
      </div>
    </div>
  </div>

</div>

---

## 영상 캡처용 요약 구조도 (Minimal Map for Capture)

화면 캡처를 통해 영상 소스로 바로 사용하실 수 있는 깔끔한 요약 레이아웃입니다.

<div class="project-capture-map" style="margin: 40px auto; padding: 28px; background: var(--bg); border: 2px solid var(--line); border-radius: 28px; max-width: 580px; display: flex; flex-direction: column; gap: 14px; align-items: center; box-sizing: border-box;">

  <!-- 1. Presentation Layer (최상단) -->
  <div style="width: 100%; display: flex; gap: 12px; box-sizing: border-box;">
    <!-- YouTube Box -->
    <div style="flex: 1; background: var(--card); border: 2.5px solid #8a5cff; border-radius: 16px; padding: 16px 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(138, 92, 255, 0.08); box-sizing: border-box; text-align: center; min-height: 110px;">
      <span style="font-size: 11px; font-weight: 900; color: #8a5cff; letter-spacing: 0.05em; margin-bottom: 6px;">L1. PRESENTATION</span>
      <strong style="font-size: 16px; color: var(--ink); letter-spacing: -0.02em;">판교 뚜벅쵸 (YouTube)</strong>
      <!-- YouTube SVG Icon -->
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 22px; height: 22px; fill: #FF0000; margin-top: 8px; filter: drop-shadow(0 2px 4px rgba(255,0,0,0.12));">
        <path d="M23.498 6.163a3.003 3.003 0 0 0-2.11-2.108C19.52 3.5 12 3.5 12 3.5s-7.52 0-9.388.555A3.003 3.003 0 0 0 .502 6.163C0 8.07 0 12 0 12s0 3.93.502 5.837a3.003 3.003 0 0 0 2.11 2.108c1.868.555 9.388.555 9.388.555s7.52 0 9.388-.555a3.003 3.003 0 0 0 2.11-2.108C24 15.93 24 12 24 12s0-3.93-.502-5.837zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
      </svg>
    </div>
    <!-- Blog Box -->
    <div style="flex: 1; background: var(--card); border: 2.5px solid #8a5cff; border-radius: 16px; padding: 16px 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(138, 92, 255, 0.08); box-sizing: border-box; text-align: center; min-height: 110px;">
      <span style="font-size: 11px; font-weight: 900; color: #8a5cff; letter-spacing: 0.05em; margin-bottom: 6px;">L1. PRESENTATION</span>
      <strong style="font-size: 16px; color: var(--ink); letter-spacing: -0.02em;">panddu.github.io</strong>
      <!-- GitHub SVG Icon -->
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 22px; height: 22px; fill: var(--ink); margin-top: 8px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">
        <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
      </svg>
    </div>
  </div>

  <!-- Arrow -->
  <div style="color: var(--muted); display: flex; justify-content: center; height: 16px; margin: -4px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </div>

  <!-- 2. Agent & Studio Layer -->
  <div style="width: 100%; display: flex; align-items: center; gap: 8px; box-sizing: border-box;">
    <!-- Agent Box -->
    <div style="flex: 1; background: var(--card); border: 2.5px solid #316dff; border-radius: 16px; padding: 14px 12px 10px 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(49, 109, 255, 0.08); box-sizing: border-box; text-align: center; min-height: 110px;">
      <span style="font-size: 11px; font-weight: 900; color: #316dff; letter-spacing: 0.05em; margin-bottom: 4px;">L2. INTELLIGENCE</span>
      <strong style="font-size: 16px; color: var(--ink); letter-spacing: -0.02em;">mingus-agent</strong>
      
      <!-- JetBrains Koog Logo Badge (Inline SVG to avoid 404) -->
      <div style="display: flex; align-items: center; gap: 6px; margin-top: 8px; background: var(--bg); padding: 4px 8px; border-radius: 8px; border: 1px solid var(--line); filter: drop-shadow(0 1px 2px rgba(0,0,0,0.02));">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" style="width: 14px; height: 14px; flex-shrink: 0;">
          <rect width="100" height="100" rx="18" fill="#000000"/>
          <path d="M15,85 L85,85 L85,15 L15,15 Z" fill="none" stroke="url(#jb-grad)" stroke-width="8"/>
          <text x="50" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-weight="900" font-size="42" fill="#FFFFFF" text-anchor="middle">JB</text>
          <defs>
            <linearGradient id="jb-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#FC256B" />
              <stop offset="50%" stop-color="#7B3CFF" />
              <stop offset="100%" stop-color="#3CBEFF" />
            </linearGradient>
          </defs>
        </svg>
        <span style="font-size: 11px; font-weight: 800; color: var(--ink-soft); letter-spacing: -0.01em;">Koog</span>
      </div>
    </div>
    <!-- Interaction Loop (양방향 화살표) -->
    <div style="display: flex; align-items: center; justify-content: center; color: #316dff; font-size: 26px; font-weight: 900; padding: 0 4px; filter: drop-shadow(0 2px 4px rgba(49, 109, 255, 0.15)); user-select: none;">
      ⇄
    </div>
    <!-- Studio Box -->
    <div style="flex: 1; background: var(--card); border: 2.5px solid #316dff; border-radius: 16px; padding: 16px 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(49, 109, 255, 0.08); box-sizing: border-box; text-align: center; min-height: 110px;">
      <span style="font-size: 11px; font-weight: 900; color: #316dff; letter-spacing: 0.05em; margin-bottom: 6px;">L2. INTELLIGENCE</span>
      <strong style="font-size: 16px; color: var(--ink); letter-spacing: -0.02em;">mingus-studio</strong>
      <span style="font-size: 20px; margin-top: 6px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">🎬</span>
    </div>
  </div>

  <!-- Arrow -->
  <div style="color: var(--muted); display: flex; justify-content: center; height: 16px; margin: -4px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </div>

  <!-- 3. Skill & Engine Layer -->
  <div style="width: 100%; background: var(--card); border: 2.5px solid #1fa34a; border-radius: 16px; padding: 18px 22px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 15px rgba(31, 163, 74, 0.08); box-sizing: border-box; min-height: 64px;">
    <span style="font-size: 13px; font-weight: 900; color: #1fa34a; letter-spacing: 0.05em;">L3. CORE ENGINE</span>
    <strong style="font-size: 20px; color: var(--ink); letter-spacing: -0.02em;">mingus-kit</strong>
    <span style="font-size: 20px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">🛠️</span>
  </div>

  <!-- Arrow -->
  <div style="color: var(--muted); display: flex; justify-content: center; height: 16px; margin: -4px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </div>

  <!-- 4. Persistence Layer (최하단) -->
  <div style="width: 100%; background: var(--card); border: 2.5px solid #fb8c20; border-radius: 16px; padding: 14px 22px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 15px rgba(251, 140, 32, 0.08); box-sizing: border-box; min-height: 64px;">
    <span style="font-size: 13px; font-weight: 900; color: #fb8c20; letter-spacing: 0.05em;">L4. PERSISTENCE</span>
    <strong style="font-size: 20px; color: var(--ink); letter-spacing: -0.02em;">Bear App</strong>
    <img src="/assets/img/bear-app-icon.png" alt="Bear App Icon" style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid var(--line); filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));">
  </div>

</div>



