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
category: etc        # qna | qa | etc 중 하나
series_no: 3         # (선택) 시리즈 안에서 번호
youtube_id: "abc123" # (선택) 유튜브 영상 임베드 — 글 상단에 박힘
---
```

- **`layout: post`** — 필수
- **`category`** — 시리즈 분류. 아래 셋 중 하나:
  - `etc` → `[끄적]` 배지 (그 외 모두; 시리즈 안 묶이는 자유 글·메모·여담)
  - `qna` → `[뚜쪽상담소]` 배지 (시청자 질문 묶음)
  - `qa` → `[Q&A]` 배지 (단발 응답형 글)
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
| 시리즈(카테고리) 이름·색·설명 | `_data/series.yml` |
| 새 시리즈 추가 | `_data/series.yml`에 키 추가 + `series/<키>.html` 만들기 |
| About 페이지 내용 | `about.md` |
| 홈 hero 카피·프사 | `_layouts/home.html` |
| 사이트 전체 색·여백·폰트 | `assets/css/main.scss` |
| 댓글(giscus) 설정 | `_config.yml` → `giscus:` |
| 채널 프사 교체 | `assets/img/avatar.png` 덮어쓰기 (정사각형, 400px 이상 권장) |
| 댓글 로딩 GIF 교체 | `assets/img/party-parrot.gif` 덮어쓰기, 또는 `_includes/giscus.html`의 `src` 변경 |
| 푸터 (저작권·링크) | `_includes/footer.html` |

## mingus-agent에서 QnA 모음 글 자동 생성

mingus-agent의 `panddu.qna`가 시청자 QnA 시트를 클러스터링해서 이 블로그의 `_posts/`에 바로 떨어뜨릴 수 있음.

```bash
cd /Users/mingus/Workspace/mingus-agent

# 가장 단순 — 기본 예시 시트 + 이 블로그에 포스트 생성
./gradlew runPandduQna --args="--jekyll-out=/Users/mingus/Workspace/panddu.github.io"

# 다른 시트 + 예상 답변 10개까지 포함
QNA_DRAFTS=10 ./gradlew runPandduQna --args="<시트URL> --jekyll-out=/Users/mingus/Workspace/panddu.github.io"
```

→ `_posts/YYYY-MM-DD-qna.md` 생성. `category: qna` 로 자동 박힘.

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
├── _config.yml              # 사이트 메타 + giscus 설정 (편집 후 서버 재시작 필요)
├── Gemfile                  # github-pages gem (GitHub Pages와 같은 Jekyll 3.10)
├── _data/
│   └── series.yml           # 시리즈(카테고리) 메타: 표시명·색·설명
├── _layouts/
│   ├── default.html         # 모든 페이지의 베이스
│   ├── home.html            # 홈
│   ├── post.html            # 개별 글
│   └── series.html          # 시리즈 페이지 (글 목록)
├── _includes/
│   ├── head.html            # <head> 메타
│   ├── header.html          # 사이트 헤더 + nav
│   ├── footer.html          # 푸터
│   ├── post_meta.html       # 시리즈 배지 + 날짜
│   └── giscus.html          # 댓글 위젯
├── _posts/                  # 발행된 글 (YYYY-MM-DD-slug.md)
├── _drafts/                 # 작성 중 (날짜 없음, --drafts 플래그로만 빌드)
├── series/                  # 시리즈 페이지들 (각자 series_key로 _data 참조)
│   ├── index.html           # /series/ — 전체 시리즈 카드
│   ├── qna.html             # /series/qna/
│   ├── qa.html              # /series/qa/
│   └── etc.html             # /series/etc/
├── assets/
│   ├── css/main.scss        # 사이트 전체 스타일
│   └── img/
│       ├── avatar.png       # 채널 프사 (홈·about hero)
│       └── party-parrot.gif # 댓글 로딩 표시
├── about.md                 # /about/
├── index.html               # /, layout: home
└── README.md                # 이 파일
```

## 그 외 메모

- **포스트 URL 패턴**: `/posts/:year/:month/:slug/` (예: `/posts/2026/05/blog-start/`). `_config.yml`의 `permalink:` 에서 바꿀 수 있음.
- **giscus 댓글**은 GitHub Discussions 기반. 댓글 달려면 GitHub 계정 필요. 시청자층(개발자 아닌 분들) 진입 장벽 있으니 메인은 유튜브 댓글, 블로그는 보조라 보면 됨.
- **다크모드 미지원** — 현재 라이트 모드만. giscus 위젯도 라이트로 고정.
- **GitHub Pages 빌드 환경**과 로컬 환경이 같은 Jekyll 3.10 (`github-pages` gem) — "로컬은 되는데 prod에선 안 됨" 류 회피.
