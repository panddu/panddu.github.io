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

