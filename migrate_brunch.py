#!/usr/bin/env python3
import os
import re
import json
import urllib.request
import urllib.parse
from datetime import datetime
import html

# 마이그레이션 대상 브런치 글 번호
ARTICLE_NOS = [13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 32, 33, 36, 37, 38, 39, 41, 42]

# 카테고리 매핑 (daily / tech / review)
CATEGORY_MAP = {
    # 테크 카테고리
    20: "tech",
    22: "tech",
    25: "tech",
    27: "tech",
    39: "tech",
    41: "tech",
    
    # 리뷰 카테고리
    32: "review",
    # 그 외 일상 카테고리 (daily)
}

# 영문 슬러그 매핑 테이블
SLUG_MAP = {
    13: "what-do-you-do",
    14: "dating-developers",
    15: "explain-developer-job-to-friend",
    16: "developer-couple-anniversary",
    17: "taxi-driver-meets-developer",
    18: "designer-developer-conflict",
    19: "developer-favorite-planner",
    20: "server-developer-fear-event",
    22: "why-messenger-app-needs-server",
    23: "homebody-developer-pojo",
    24: "how-to-report-error-to-server-developer",
    25: "server-developer-fear-migration",
    27: "advice-to-junior-use-existing-libraries",
    32: "super-mario-maker-coding-education",
    33: "planner-workshop-vs-developer-workshop",
    36: "planner-favorite-developer",
    37: "developer-dinner-vs-non-developer",
    38: "why-i-hate-work-today",
    39: "app-developer-learned-by-dba",
    41: "dev-knowledge-for-junior-planner",
    42: "road-to-10k-youtube-subscribers"
}

# 로컬 저장소 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "_posts")
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "img", "brunch")

# 필요한 디렉토리 생성
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def download_html(article_no):
    """브런치 글 HTML을 다운로드합니다. urllib의 리다이렉션 시 헤더 누락으로 인한 루프를 수동 핸들링으로 방지합니다."""
    url = f"https://brunch.co.kr/@panddu/{article_no}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for _ in range(5):
        try:
            class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
                def http_error_301(self, req, fp, code, msg, hdrs): return None
                def http_error_302(self, req, fp, code, msg, hdrs): return None
                def http_error_303(self, req, fp, code, msg, hdrs): return None
                def http_error_307(self, req, fp, code, msg, hdrs): return None
            
            opener = urllib.request.build_opener(NoRedirectHandler)
            req = urllib.request.Request(url, headers=headers)
            with opener.open(req) as response:
                html_data = response.read()
                # charset 감지 (없으면 utf-8)
                content_type = response.headers.get("Content-Type", "")
                encoding = "utf-8"
                if "charset=" in content_type:
                    encoding = content_type.split("charset=")[-1].strip()
                return html_data.decode(encoding, errors="replace")
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                new_url = e.headers.get("Location")
                if not new_url:
                    print(f"[-] Redirect code {e.code} but no Location header.")
                    break
                url = urllib.parse.urljoin(url, new_url)
                continue
            else:
                print(f"[-] HTTP Error {e.code} for article {article_no}: {e.reason}")
                return None
        except Exception as e:
            print(f"[-] Connection error for article {article_no}: {e}")
            return None
    return None

def extract_props_json(html_content):
    """HTML 소스에서 props 속성에 인코딩된 JSON 데이터를 추출합니다."""
    match = re.search(r'props="([^"]+)"', html_content)
    if not match:
        return None
    escaped_props = match.group(1)
    props_str = html.unescape(escaped_props)
    try:
        return json.loads(props_str)
    except Exception as e:
        print(f"[-] JSON parsing error: {e}")
        return None

def download_image(img_url, article_no, img_idx):
    """이미지를 다운로드하고 로컬 저장 경로를 반환합니다."""
    try:
        # 쿼리스트링(?fname=...)이 있는 경우 실제 이미지 파일명을 파싱하여 확장자 추출
        parsed_url = urllib.parse.urlparse(img_url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        filename = ""
        if "fname" in query_params:
            real_url = query_params["fname"][0]
            filename = os.path.basename(urllib.parse.urlparse(real_url).path)
        else:
            filename = os.path.basename(parsed_url.path)
            
        ext = os.path.splitext(filename)[1]
        if not ext:
            ext = ".png" # 기본값
            
        # 정규화된 파일명 결정
        local_filename = f"{article_no}_{img_idx}{ext}"
        local_path = os.path.join(IMAGES_DIR, local_filename)
        
        # 다운로드 실행
        req = urllib.request.Request(img_url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req) as response:
            with open(local_path, "wb") as f:
                f.write(response.read())
                
        print(f"    [+] Saved image: {local_filename}")
        return f"/assets/img/brunch/{local_filename}"
    except Exception as e:
        print(f"    [-] Image download failed: {img_url} -> {e}")
        return img_url # 실패 시 원본 CDN URL 유지

def render_text_node(node):
    """텍스트 노드를 재귀적으로 평가하여 마크다운을 빌드합니다."""
    node_type = node.get("type")
    if node_type == "br":
        return "\n"
    elif node_type == "text":
        text = node.get("text", "")
        style = node.get("style", {})
        
        # bold 스타일 처리
        is_bold = style.get("isBold", False) or node.get("styleType") == "bold"
        if is_bold and text.strip():
            text = f"**{text}**"
            
        # inline code 처리 (브런치에 code style이 있을 경우)
        if style.get("isCode", False):
            text = f"`{text}`"
            
        return text
    elif node_type == "anchor":
        url = node.get("url", "")
        inner_data = node.get("data", [])
        inner_text = "".join(render_text_node(child) for child in inner_data)
        if not inner_text:
            inner_text = url
        return f"[{inner_text}]({url})"
    else:
        # 하위 노드가 있으면 계속 탐색
        if "data" in node:
            return "".join(render_text_node(child) for child in node["data"])
        return node.get("text", "")

def convert_body_to_markdown(body_list, article_no):
    """브런치 본문 JSON 트리를 Jekyll Markdown 형식으로 변환합니다."""
    markdown_lines = []
    img_idx = 1
    
    for element in body_list:
        el_type = element.get("type")
        
        if el_type == "text":
            size = element.get("size", "")
            data = element.get("data", [])
            text_content = "".join(render_text_node(child) for child in data)
            
            # 헤더 태그 변환
            if size == "h1":
                markdown_lines.append(f"\n## {text_content}\n")
            elif size == "h2":
                markdown_lines.append(f"\n### {text_content}\n")
            elif size == "h3":
                markdown_lines.append(f"\n#### {text_content}\n")
            else:
                # 일반 텍스트 문단
                if text_content == "\n" or not text_content.strip():
                    markdown_lines.append("\n")
                else:
                    markdown_lines.append(f"{text_content}\n")
                    
        elif el_type == "quotation":
            kind = element.get("kind", "quote")
            data = element.get("data", [])
            text_content = "".join(render_text_node(child) for child in data)
            
            # 인용구 변환
            quoted_text = "\n".join(f"> {line}" for line in text_content.split("\n"))
            markdown_lines.append(f"\n{quoted_text}\n")
            
        elif el_type == "img":
            img_url = element.get("url")
            caption = element.get("caption", "").strip()
            
            if img_url:
                local_url = download_image(img_url, article_no, img_idx)
                img_idx += 1
                markdown_lines.append(f"\n![{caption}]({local_url})")
                if caption:
                    markdown_lines.append(f"\n<p class=\"caption\" style=\"font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;\"><i>{caption}</i></p>\n")
                else:
                    markdown_lines.append("\n")
                    
        elif el_type == "video":
            video_host = element.get("host")
            video_id = element.get("id")
            caption = element.get("caption", "").strip()
            
            if video_host == "youtube" and video_id:
                markdown_lines.append(
                    f'\n<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 20px 0;">\n'
                    f'  <iframe src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>\n'
                    f'</div>\n'
                )
                if caption:
                    markdown_lines.append(f"<p class=\"caption\" style=\"font-size: 0.85em; color: gray; text-align: center; margin-top: -12px;\"><i>{caption}</i></p>\n")
                    
        elif el_type == "hr":
            markdown_lines.append("\n---\n")
            
        elif el_type == "bullet":
            data = element.get("data", [])
            text_content = "".join(render_text_node(child) for child in data)
            markdown_lines.append(f"- {text_content}\n")
            
        elif el_type == "numbered":
            data = element.get("data", [])
            text_content = "".join(render_text_node(child) for child in data)
            markdown_lines.append(f"1. {text_content}\n")
            
        elif el_type == "opengraph":
            # 본문에 이미 녹아 있는 링크 카드(OpenGraph)는 마크다운에서는 기본 하이퍼링크 형태로 유지하거나 생략
            pass
            
    return "".join(markdown_lines)

def clean_title(title):
    """YAML 프론트매터 파싱 오류를 방지하기 위해 제목의 큰따옴표를 치환하고 정제합니다."""
    title = title.replace('"', '\\"') # 큰따옴표 이스케이프
    return title

def migrate_article(article_no):
    """개별 브런치 글 마이그레이션을 처리합니다."""
    print(f"[*] Processing article {article_no}...")
    
    # 1. HTML 다운로드
    html_content = download_html(article_no)
    if not html_content:
        return False
        
    # 2. props JSON 파싱
    props = extract_props_json(html_content)
    if not props or "article" not in props:
        print(f"[-] Could not find article props for {article_no}")
        return False
        
    article_data = props["article"][1]
    
    # 3. 메타데이터 파싱
    title = clean_title(article_data.get("title", [0, ""])[1])
    publish_timestamp = article_data.get("publishTimestamp", [0, 0])[1]
    
    # Unix timestamp -> YYYY-MM-DD HH:MM:SS +0900
    pub_date = datetime.fromtimestamp(publish_timestamp / 1000.0)
    formatted_date = pub_date.strftime("%Y-%m-%d %H:%M:%S +0900")
    date_slug = pub_date.strftime("%Y-%m-%d")
    
    # 4. 카테고리 매핑
    category = CATEGORY_MAP.get(article_no, "daily")
    
    # 5. 본문 파싱 및 마크다운 변환
    content_str = article_data.get("content", [0, "{}"])[1]
    try:
        content_json = json.loads(content_str)
        body_list = content_json.get("body", [])
    except Exception as e:
        print(f"[-] Failed to parse content JSON for article {article_no}: {e}")
        return False
        
    markdown_content = convert_body_to_markdown(body_list, article_no)
    
    # 6. Jekyll Post 파일 작성
    slug = SLUG_MAP.get(article_no, f"brunch-{article_no}")
    post_filename = f"{date_slug}-{slug}.md"
    post_path = os.path.join(POSTS_DIR, post_filename)
    
    jekyll_post = f"""---
layout: post
title: "{title}"
date: {formatted_date}
category: {category}
---

> 💡 이 글은 <a href="https://brunch.co.kr/@panddu/{article_no}" target="_blank">판뚜의 브런치(@panddu/{article_no})</a>로부터 마이그레이션된 글입니다.

{markdown_content}"""

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(jekyll_post)
        
    print(f"[+] Successfully migrated article {article_no} -> {post_filename}")
    return True

def main():
    success_count = 0
    failed_articles = []
    
    print("=== Brunch to GitHub Blog Migration Started ===")
    print(f"Total target articles: {len(ARTICLE_NOS)}")
    
    # 이전 파일 정리
    import glob
    old_files = glob.glob(os.path.join(POSTS_DIR, "*-brunch-*.md"))
    for f in old_files:
        try:
            os.remove(f)
            print(f"[*] Cleaned up old post file: {os.path.basename(f)}")
        except Exception as e:
            print(f"[-] Failed to clean up {f}: {e}")
    
    for no in ARTICLE_NOS:
        if migrate_article(no):
            success_count += 1
        else:
            failed_articles.append(no)
            
    print("\n=== Migration Completed ===")
    print(f"Success: {success_count}/{len(ARTICLE_NOS)}")
    if failed_articles:
        print(f"Failed articles: {failed_articles}")
    else:
        print("All articles successfully migrated!")

if __name__ == "__main__":
    main()
