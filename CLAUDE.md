# CLAUDE.md

## GitHub CLI (`gh`) 계정

이 레포에서 `gh` 명령어를 실행하기 전에 항상 github.com의 panddu 계정으로 전환한다:

```bash
gh auth switch --hostname github.com --user panddu
```

## ✍️ 블로그 포스트 작성 및 이미지/OG 지침

- **포스트 내 전용 이미지가 있는 경우**:
  - 해당 포스트 전용 썸네일(일러스트)을 생성했다면, 파일은 `/assets/img/posts/YYYY-MM-DD/thumbnail.jpg` 경로에 저장합니다.
  - 포스트 Front Matter에 `image: /assets/img/posts/YYYY-MM-DD/thumbnail.jpg` 형식으로 지정하여, 해당 포스트가 공유될 때 이 전용 이미지가 Open Graph(og:image)로 덮어씌워지도록 합니다.
- **포스트 내 전용 이미지가 없는 경우**:
  - Front Matter에 `image:` 필드를 명시하지 않습니다. 이 경우 `_config.yml`에 정의된 전역 공통 기본 이미지인 `/assets/img/og_default.jpg`가 자동으로 적용됩니다.

- **포스트 카테고리 분류 기준**:
  - `tech`: AI·개발·기술·업계에서 배운 구체적인 기술/지식 공유 및 튜토리얼
  - `comms`: 시청자 Q&A 및 상담소 문답 모음집
  - `review`: 장비, 서비스, 도구 등의 리뷰
  - `workroom`: 직접 개발한 미니 프로젝트나 도구 소개
  - `daily`: 단순 일상 기록, 기행문(약수터 등), 제품 구매기(테슬라 등) 등 사실 나열형 일상 글
  - `essay`: 개발자 라이프스타일, 협업에 대한 단상, 삶의 태도, 생각, 가벼운 수필 등 필자의 주관적인 통찰이나 감성이 중심이 되는 글

- **발행(`_drafts/` → `_posts/`) 시 타임스탬프**:
  - Front Matter의 `date:`는 초안을 처음 작성한 시각이 아니라 실제로 `_drafts/`에서 `_posts/`로 옮겨 발행하는 시각으로 설정합니다.
  - 이 값이 "24시간 이내 새 글" N 배지(`_includes/new_badge.html`) 판정 기준이라, 초안 작성 시각을 그대로 쓰면 배지가 조기에 사라지거나 애초에 뜨지 않습니다.
  - 이미 발행된 글의 `date`가 의심스러우면 `git log --all --name-status`로 `_drafts/<slug>.md` → `_posts/<date>-<slug>.md` rename 커밋 시각을 찾아 그 시각으로 정정합니다.

