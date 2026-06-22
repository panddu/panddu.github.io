---
layout: post
title: "내 개인 프로젝트 계층 구조 및 역할 분담"
category: project
---

최근 구상하고 운영 중인 개인 프로젝트들의 계층 구조를 직관적인 박스 레이아웃으로 정리해 보았습니다. 이 구조는 최하단의 지식 저장소부터 최상단의 외부 채널까지 물 흐르듯 이어지는 콘텐츠 생성 파이프라인을 보여줍니다.

<div class="project-arch-container" style="margin: 40px 0; font-family: inherit; display: flex; flex-direction: column; gap: 24px; max-width: 100%;">

  <!-- 1. Presentation Layer (최상단) -->
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); transition: transform 0.2s, box-shadow 0.2s; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent);"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 700; text-transform: uppercase; color: var(--accent); letter-spacing: 0.05em;">1. Presentation Layer (최상단)</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 20px; font-weight: 600;">외부 노출 채널</span>
    </div>
    <h3 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 700; color: var(--ink);">블로그 & 유튜브</h3>
    <p style="margin: 0 0 16px 0; font-size: 14px; color: var(--muted); line-height: 1.6;">최종 제작된 결과물과 영상이 독자 및 시청자들에게 제공되는 채널입니다.</p>
    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 200px; background: var(--bg); border: 1px solid var(--line); padding: 12px 16px; border-radius: 10px;">
        <strong style="display: block; font-size: 15px; color: var(--ink); margin-bottom: 4px;">✍️ panddu.github.io</strong>
        <span style="font-size: 13px; color: var(--muted);">기술 및 일상 블로그 포스팅 발행</span>
      </div>
      <div style="flex: 1; min-width: 200px; background: var(--bg); border: 1px solid var(--line); padding: 12px 16px; border-radius: 10px;">
        <strong style="display: block; font-size: 15px; color: var(--ink); margin-bottom: 4px;">🎥 판교 뚜벅쵸 채널</strong>
        <span style="font-size: 13px; color: var(--muted);">유튜브 영상 업로드 및 시청자 소통</span>
      </div>
    </div>
  </div>

  <!-- Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -8px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="color: var(--muted); transform: rotate(180deg);">
      <path d="M12 4V20M12 20L18 14M12 20L6 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>

  <!-- 2. Agent & Studio Layer -->
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent); opacity: 0.8;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 700; text-transform: uppercase; color: var(--accent); letter-spacing: 0.05em;">2. Agent & Studio Layer</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 20px; font-weight: 600;">콘텐츠 생성 및 지능 레이어</span>
    </div>
    <h3 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 700; color: var(--ink);">mingus-agent × mingus-studio</h3>
    <p style="margin: 0 0 16px 0; font-size: 14px; color: var(--muted); line-height: 1.6;">두 시스템이 긴밀하게 협동하고 상호 작용하며, 블로그 포스트 초안 및 영상 대본을 자동으로 기획하고 작성합니다.</p>
    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 200px; background: var(--bg); border: 1px solid var(--line); padding: 12px 16px; border-radius: 10px;">
        <strong style="display: block; font-size: 15px; color: var(--ink); margin-bottom: 4px;">🤖 mingus-agent</strong>
        <span style="font-size: 13px; color: var(--muted);">자율적인 테스크 기획 및 정보 서치</span>
      </div>
      <div style="flex: 1; min-width: 200px; background: var(--bg); border: 1px solid var(--line); padding: 12px 16px; border-radius: 10px;">
        <strong style="display: block; font-size: 15px; color: var(--ink); margin-bottom: 4px;">🎬 mingus-studio</strong>
        <span style="font-size: 13px; color: var(--muted);">콘텐츠 빌딩, 영상 기획 및 스크립트 작성</span>
      </div>
    </div>
  </div>

  <!-- Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -8px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="color: var(--muted); transform: rotate(180deg);">
      <path d="M12 4V20M12 20L18 14M12 20L6 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>

  <!-- 3. Skill & Engine Layer -->
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent); opacity: 0.6;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 700; text-transform: uppercase; color: var(--accent); letter-spacing: 0.05em;">3. Skill & Engine Layer</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 20px; font-weight: 600;">실행 엔진 및 커맨드</span>
    </div>
    <h3 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 700; color: var(--ink);">mingus-kit</h3>
    <p style="margin: 0 0 16px 0; font-size: 14px; color: var(--muted); line-height: 1.6;">지능 레이어와 영속성 레이어를 이어주는 허브입니다. 실질적인 작업 커맨드와 비즈니스 로직(스킬)을 내장하고 있습니다.</p>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
      <span style="font-size: 12px; background: var(--chip); color: var(--accent); padding: 6px 12px; border-radius: 8px; font-weight: 500;">👤 persona-build</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--accent); padding: 6px 12px; border-radius: 8px; font-weight: 500;">📂 resume / wrap</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--accent); padding: 6px 12px; border-radius: 8px; font-weight: 500;">📝 worklog</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--accent); padding: 6px 12px; border-radius: 8px; font-weight: 500;">💡 panddu-idea</span>
    </div>
  </div>

  <!-- Arrow -->
  <div style="display: flex; justify-content: center; align-items: center; margin: -8px 0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="color: var(--muted); transform: rotate(180deg);">
      <path d="M12 4V20M12 20L18 14M12 20L6 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>

  <!-- 4. Persistence Layer (최하단) -->
  <div style="background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent); opacity: 0.4;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <span style="font-size: 13px; font-weight: 700; text-transform: uppercase; color: var(--accent); letter-spacing: 0.05em;">4. Persistence Layer (최하단)</span>
      <span style="font-size: 12px; background: var(--chip); color: var(--ink-soft); padding: 4px 10px; border-radius: 20px; font-weight: 600;">데이터 영속화 및 기지</span>
    </div>
    <h3 style="margin: 0 0 10px 0; font-size: 20px; font-weight: 700; color: var(--ink);">Bear App (노트)</h3>
    <p style="margin: 0 0 12px 0; font-size: 14px; color: var(--muted); line-height: 1.6;">모든 생각, 콘텐츠 소스, 기록, 페르소나가 저장되는 기초 데이터베이스 역할을 담당합니다.</p>
    <span style="font-size: 13px; display: inline-flex; align-items: center; gap: 6px; color: var(--muted);">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: #22c55e;"></span>
      모든 시스템의 영속성 레벨 지탱 (Single Source of Truth)
    </span>
  </div>

</div>

## 파이프라인 흐름
1. **Bear**에서 기록된 콘텐츠 원천 아이디어나 페르소나 데이터가 시작점이 됩니다.
2. **`mingus-kit`**이 이 데이터를 호출하여 다룰 수 있는 스킬 엔진 역할을 수행합니다.
3. **`mingus-agent`와 `mingus-studio`**가 이 스킬셋을 활성화하여 기획/조사/대본 작성을 자동화합니다.
4. 완성된 콘텐츠는 최상단의 **유튜브**나 **블로그**로 퍼블리싱됩니다.
