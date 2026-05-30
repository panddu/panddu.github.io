source "https://rubygems.org"

# GitHub Pages가 native로 빌드하는 버전과 동일하게 묶는다.
# 로컬과 prod 빌드 결과 일치 → "로컬은 되는데 push하면 안 됨" 류 회피.
gem "github-pages", group: :jekyll_plugins

# github-pages가 끌고 오는 플러그인 외에 추가로 쓰는 것만 여기에.
group :jekyll_plugins do
  # (현재 없음 — 필요해지면 GitHub Pages 화이트리스트 안에서 추가)
end

# Windows/JRuby에서 필요한 timezone/listen — macOS에선 무관하지만 관용적으로 둔다.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
