# panddu.github.io

판뚜|panddu 블로그. Jekyll + GitHub Pages.

`main`에 push하면 GitHub Pages가 자동 빌드해서 https://panddu.github.io 에 올림.

## 로컬에서 미리보기

### 1회 셋업 (이미 설치돼 있으면 스킵)

```bash
# Ruby 3.3 (시스템 Ruby는 너무 옛날 거)
brew install ruby@3.3

# PATH에 Ruby 3.3 + 사용자 gem bin 추가 (zsh 기준; bash면 .bashrc)
echo 'export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# bundler
gem install --user-install bundler

# 이 레포에서 의존성 설치 (vendor/bundle에 로컬 설치됨)
cd /Users/mingus/Workspace/panddu.github.io
bundle install
```

### 일상 미리보기

```bash
bundle exec jekyll serve --livereload
```

→ http://127.0.0.1:4000/ 에서 확인. 파일 수정하면 자동 새로고침.

**draft까지 같이 보려면:**
```bash
bundle exec jekyll serve --livereload --drafts
```

> ⚠️ `_config.yml` 만 예외 — 변경하면 서버를 다시 띄워야 반영됨 (Ctrl-C → 다시 실행).

서버 끄기: 터미널에서 Ctrl-C. 다른 터미널에서 강제로 끄려면 `pkill -f "jekyll serve"`.

### IntelliJ에서 미리보기

레포에 `.idea/runConfigurations/` 가 같이 들어있어서 IntelliJ에서 프로젝트 열면 우상단 Run dropdown에 두 config가 자동 등록됨:

- **Jekyll Preview** — 일반 모드
- **Jekyll Preview (drafts)** — `--drafts` 포함

PATH 환경변수가 박혀 있어 IntelliJ 안에서 Ruby 3.3 + bundle 잘 찾음. 다른 머신·다른 Ruby 경로 쓰면 Run → Edit Configurations → Environment variables의 PATH 수정.

## 글 쓰는 법

### 1. 파일 만들기

`_posts/YYYY-MM-DD-slug.md` 형식. 예: `_posts/2026-06-01-keyboard-review.md`.

날짜는 파일명에 반영되고 정렬에도 쓰여서 정확해야 함.

### 2. frontmatter (파일 맨 위 `---` 블록)

```yaml
---
layout: post
title: "글 제목"
date: 2026-06-01 22:00:00 +0900
category: daily      # daily | tech | review | comms 중 하나
series_no: 3         # (선택) 카테고리 안에서 번호
youtube_id: "abc123" # (선택) 유튜브 영상 임베드 — 글 상단에 박힘
---
```

- **`layout: post`** — 필수
- **`category`** — 카테고리 분류. 아래 넷 중 하나:
  - `daily` → `[일상]` 배지 (업계/회사 이야기·육아·관심사 등 아무 글)
  - `tech` → `[테크]` 배지 (개발·기술·툴 이야기)
  - `review` → `[리뷰]` 배지 (직접 써보고 남기는 장비·서비스 리뷰)
  - `comms` → `[문답]` 배지 (구독자 Q&A·뚜쪽 상담소 답글 모음)

  > 카테고리 표시명·설명·색은 `_data/series.yml`이 원본. 위는 요약이라 거기서 바꾸면 README도 같이 맞춰주면 됨.
- **`series_no`** — `#3` 같은 번호 (배지 옆에 박힘). 안 박으려면 생략.
- **`youtube_id`** — `https://youtu.be/abc123` 의 `abc123` 부분만. 영상 옆에 곁들이는 글일 때 사용.

### 3. 본문

frontmatter 아래에 마크다운으로 쓰면 됨. 마크다운 안에 HTML도 박을 수 있고, Jekyll Liquid 태그도 됨.

### Draft (작성 중인 글)

발행 안 하고 굴리고 싶은 초안은 `_drafts/` 디렉토리에 박는다. 파일명에 **날짜가 들어가지 않는다** — 그냥 `_drafts/slug.md`.

```
_drafts/
└── keyboard-review-vanguard.md   # 날짜 없음
```

frontmatter는 일반 포스트와 같지만 `date:`는 생략 가능 (있어도 무시됨).

- **기본 빌드에선 안 잡힘** — GitHub Pages 배포해도 사이트에 안 뜸.
- **로컬에서만 미리보기**: `bundle exec jekyll serve --drafts --livereload`. draft 글의 날짜는 "현재 시각"으로 잡힘.
- 완성되면 `_posts/YYYY-MM-DD-slug.md` 로 이동하면서 파일명에 날짜 박는다. 끝.

> ⚠️ draft 파일도 git에 push되긴 한다(이 레포가 public이라 누가 봐도 보임). 진짜 비공개로 굴릴 게 있으면 `.gitignore`에 `_drafts/` 추가하거나 다른 곳에 둘 것.

## 자주 바꾸는 것들 — 어디에서

| 바꾸고 싶은 것 | 위치 |
|---|---|
| 사이트 제목 (`판뚜` 같은 거) | `_config.yml` → `title:` |
| 사이트 설명 / SEO 메타 | `_config.yml` → `description:` |
| 태그라인 (홈 hero 부제) | `_config.yml` → `tagline:` |
| 상단 nav 메뉴 | `_config.yml` → `nav:` |
| OG 이미지 (카톡·페북 공유 썸네일) | `_config.yml` → `image:` + `defaults` 블록 |
| GA4 측정 ID | `_config.yml` → `google_analytics:` (production 빌드에만 출력) |
| 카테고리 이름·색·설명 | `_data/series.yml` (파일명은 series.yml 그대로) |
| 새 카테고리 추가 | `_data/series.yml`에 키 추가 + `series/<키>.html` 만들기 |
| About 페이지 내용 | `about.md` |
| 뚜벅뚜벅(자유게시판) 안내문 | `board.html` |
| 개인정보처리방침 | `privacy.md` |
| 홈 hero 카피·프사 | `_layouts/home.html` |
| 사이트 전체 색·여백·폰트 | `assets/css/main.scss` |
| 댓글(giscus) 설정 | `_config.yml` → `giscus:` |
| 채널 프사 교체 | `assets/img/avatar.png` 덮어쓰기 (정사각형, 400px 이상 권장) → 파비콘 재생성 필요 (아래 참조) |
| 파비콘 | `assets/img/{favicon-16x16,favicon-32x32,apple-touch-icon,android-chrome-192x192}.png` — `avatar.png`에서 자동 생성 (아래 참조) |
| 댓글 로딩 GIF 교체 | `assets/img/party-parrot.gif` 덮어쓰기, 또는 `_includes/giscus.html`의 `src` 변경 |
| 푸터 (저작권·소셜 아이콘) | `_includes/footer.html` |
| 헤더 (좌측 프사·사이트 타이틀·햄버거) | `_includes/header.html` |
| 사이드바 (검색·카테고리·뚜벅뚜벅 CTA) | `_includes/sidebar.html` |

### 채널 프사 / 파비콘 재생성

채널 프사 바꿨으면 다음 4개 사이즈도 같이 재생성 (macOS 내장 `sips` 사용 — ImageMagick 불필요):

```bash
cd assets/img/
sips -z 16 16   avatar.png --out favicon-16x16.png
sips -z 32 32   avatar.png --out favicon-32x32.png
sips -z 180 180 avatar.png --out apple-touch-icon.png
sips -z 192 192 avatar.png --out android-chrome-192x192.png
```

파비콘 link 태그 자체는 `_includes/head.html`에 박혀 있어서 파일만 교체하면 끝. ICO 파일은 안 만듦 — 모던 브라우저 전부 PNG favicon 지원.

## mingus-agent에서 QnA 모음 글 자동 생성

mingus-agent의 `panddu.qna`가 시청자 QnA 시트를 클러스터링해서 이 블로그의 `_posts/`에 바로 떨어뜨릴 수 있음.

```bash
cd /Users/mingus/Workspace/mingus-agent

# 가장 단순 — 기본 예시 시트 + 이 블로그에 포스트 생성 (drafts 모드: AI 예상 답변)
./gradlew runPandduQna --args="--jekyll-out=/Users/mingus/Workspace/panddu.github.io"

# 다른 시트 + 예상 답변 10개까지 포함
QNA_DRAFTS=10 ./gradlew runPandduQna --args="<시트URL> --jekyll-out=/Users/mingus/Workspace/panddu.github.io"

# answers 모드 — 시트 N열에 사용자가 직접 적은 답변을 영상 편수별로 _drafts/에 떨굼.
# 회사·실명·이메일 등 민감정보는 regex+LLM 하이브리드로 마스킹.
# 검토하고 다듬은 뒤 _posts/로 옮겨 발행.
./gradlew runPandduQna --args="--mode=answers --jekyll-out=/Users/mingus/Workspace/panddu.github.io"
```

→ drafts 모드는 `_posts/YYYY-MM-DD-qna.md` 1개, answers 모드는 `_drafts/YYYY-MM-DD-counsel-ep0N.md` 영상편수별 다수. 둘 다 `category: comms` 자동 ([문답] 배지). 다른 카테고리로 떨구려면 `QNA_POST_CATEGORY=<키>`.

**제목·날짜·파일 슬러그 오버라이드 환경변수:**

| 변수 | 기본값 | 예 |
|---|---|---|
| `QNA_POST_TITLE` | `뚜쪽 상담소 모음 (YYYY.MM.DD)` | `"2026년 5월 시청자 질문 모음"` |
| `QNA_POST_DATE` | 오늘(KST) | `2026-05-30` |
| `QNA_POST_SLUG` | `qna` | `qna-2026-05` → 파일명 `YYYY-MM-DD-qna-2026-05.md` |

같은 날짜·슬러그로 다시 돌리면 **덮어씀** (경고 출력).

> QnA 도구 자체의 다른 옵션(`QNA_LIMIT`, `QNA_DRAFTS`, `QNA_STYLE_SHEET` 등)은 mingus-agent의 `src/main/kotlin/panddu/qna/README.md` 참조.

## 배포

GitHub Pages가 `main` 브랜치에서 자동 빌드.

```bash
git add ...
git commit -m "..."
git push                # 끝. 1~2분 후 https://panddu.github.io 반영
```

빌드 실패하면: https://github.com/panddu/panddu.github.io/actions 에서 로그 확인.

## 디렉토리 구조

```
panddu.github.io/
├── _config.yml              # 사이트 메타 + giscus + GA4 + OG image (편집 후 서버 재시작 필요)
├── Gemfile                  # github-pages gem (GitHub Pages와 같은 Jekyll 3.10)
├── _data/
│   └── series.yml           # 카테고리 메타: 표시명·색·설명 (파일명 series.yml 유지)
├── _layouts/
│   ├── default.html         # 모든 페이지의 베이스 + 사이드바 토글 / 검색 / 카운터 JS
│   ├── home.html            # 홈
│   ├── post.html            # 개별 글
│   └── series.html          # 카테고리 페이지 (글 목록)
├── _includes/
│   ├── head.html            # <head> 메타 + GA4 + GoatCounter 트래커 + 네이버 인증
│   ├── header.html          # 사이트 헤더 + nav + 햄버거
│   ├── sidebar.html         # 좌측 사이드바 (검색·카테고리·뚜벅뚜벅 CTA)
│   ├── footer.html          # 푸터 (저작권·소셜·개인정보·방문 카운터)
│   ├── post_meta.html       # 카테고리 배지 + 날짜
│   └── giscus.html          # 글 댓글 위젯 (board.html은 자체 임베드)
├── _posts/                  # 발행된 글 (YYYY-MM-DD-slug.md)
├── _drafts/                 # 작성 중 (날짜 없음, --drafts 플래그로만 빌드)
├── series/                  # 카테고리 페이지 (URL은 /series/* 유지)
│   ├── index.html           # /series/ — 전체 카테고리 카드 (제목은 "카테고리")
│   ├── daily.html           # /series/daily/ → 일상
│   ├── tech.html            # /series/tech/ → 테크
│   ├── review.html          # /series/review/ → 리뷰
│   └── comms.html           # /series/comms/ → 문답
├── assets/
│   ├── css/main.scss        # 사이트 전체 스타일 (사이드바·드로어·카테고리·게시판 등 다 포함)
│   ├── js/qna.js            # QnA 페이지 인터랙션 (카테고리 필터 토글 · PC 전용 맨 위로 가기 버튼)
│   └── img/
│       ├── avatar.png       # 채널 프사 (홈·about hero·OG 이미지 fallback)
│       ├── favicon-*.png    # 16/32/180/192 파비콘
│       └── party-parrot.gif # 댓글 로딩 표시
├── board.html               # /board/ — 뚜벅뚜벅 자유게시판 (Giscus 임베드)
├── privacy.md               # /privacy/ — 개인정보처리방침
├── about.md                 # /about/
├── index.html               # /, layout: home
├── search.json              # 사이드바 글 검색 인덱스 (Jekyll이 site.posts 기반 자동 생성)
├── robots.txt               # 크롤러 안내 + sitemap 위치
└── README.md                # 이 파일
```

## 그 외 메모

- **포스트 URL 패턴**: `/posts/:year/:month/:slug/` (예: `/posts/2026/05/blog-start/`). `_config.yml`의 `permalink:` 에서 바꿀 수 있음.
- **giscus 댓글**은 GitHub Discussions 기반. 댓글 달려면 GitHub 계정 필요. 시청자층(개발자 아닌 분들) 진입 장벽 있으니 메인은 유튜브 댓글, 블로그는 보조라 보면 됨.
- **giscus 위젯 UI는 미니멀** — 작성·답글·반응만 가능. **수정·삭제·이미지 첨부는** [GitHub Discussions](https://github.com/panddu/panddu.github.io/discussions)에서 직접. 이거 뚜벅뚜벅 페이지 안내문에 박혀있음.
- **사이드바** — 데스크탑(≥1340px)은 좌측 외부 fixed, 그 미만은 햄버거 off-canvas 드로어.
- **검색** — `/search.json` 인덱스에서 substring 매칭 후 드롭다운. simple-jekyll-search 없이 자체 구현 (default.html 인라인 JS).
- **방문 카운터** — GoatCounter (`panddu.goatcounter.com`). 푸터에서 JSON 받아와 "방문 N" 텍스트 렌더. 위젯 노출은 GoatCounter Settings → Visitor counter에서 활성화 필요.
- **SEO** — 페이지별 description은 frontmatter `description:`. og:image는 `_config.yml`의 `defaults` 블록에서 전역 (jekyll-seo-tag가 site.image 안 잡는 이슈 우회).
- **Search Console** — Google은 GA4로 자동 인증 (별도 메타 X). Naver는 `head.html`에 `naver-site-verification` 메타 박혀있음.
- **다크모드** — 시스템 설정(`prefers-color-scheme`)을 기본으로 따르고, 헤더 우상단 🌙/☀️ 토글로 명시 전환(선택은 `localStorage`에 저장). 색은 전부 `assets/css/main.scss` 상단의 CSS 변수(`:root` 라이트 / `@mixin theme-dark` 다크)로 관리 — 새 색 추가 시 양쪽 토큰만 맞추면 됨. FOUC 방지용 인라인 스크립트는 `_includes/head.html` 최상단, 토글·giscus 테마 동기화 JS는 `_layouts/default.html`. giscus 위젯도 토글에 맞춰 `postMessage`로 라이트/다크 전환됨.
- **QnA 포스트 인터랙션** (`assets/js/qna.js`) — `.qna-report` 있는 페이지에서만 동작. 카드 상단 카테고리 chip(개발/취업/일상)을 누르면 그 카테고리 질문만 표시, 다시 누르면 전체 복귀. PC(≥768px)에서만 우하단에 "맨 위로 가기" 플로팅 버튼(스크롤 200px 이상 시 페이드인). 닉네임 chip은 앵커(`#qna-<slug>`)라 클릭 시 해당 질문으로 점프.
- **GitHub Pages 빌드 환경**과 로컬 환경이 같은 Jekyll 3.10 (`github-pages` gem) — "로컬은 되는데 prod에선 안 됨" 류 회피.
