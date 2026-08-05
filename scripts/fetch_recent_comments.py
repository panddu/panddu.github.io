#!/usr/bin/env python3
"""giscus(=GitHub Discussions) 최근 댓글 상위 N개를 _data/recent_comments.json으로 저장.

- 스레드 최상위 댓글만 대상(GraphQL Discussion.comments가 대댓글은 별도 replies 필드라
  구조적으로 이미 제외됨).
- 블로그 주인(EXCLUDE_LOGINS) 계정으로 단 댓글은 제외.
- discussion.title == 해당 글의 pathname (giscus mapping: "pathname" 설정 덕분).
"""
import json
import os
import sys
import urllib.request

REPO_OWNER = "panddu"
REPO_NAME = "panddu.github.io"
CATEGORY_ID = "DIC_kwDOSsPSNs4C-J2r"  # _config.yml giscus.category_id (Announcements)
EXCLUDE_LOGINS = {"panddu"}
LIMIT = 5
BODY_MAX_LEN = 60

QUERY = """
query($owner: String!, $name: String!, $categoryId: ID) {
  repository(owner: $owner, name: $name) {
    discussions(first: 20, orderBy: {field: UPDATED_AT, direction: DESC}, categoryId: $categoryId) {
      nodes {
        title
        comments(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
          nodes {
            bodyText
            createdAt
            author { login }
          }
        }
      }
    }
  }
}
"""


def main():
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({
            "query": QUERY,
            "variables": {"owner": REPO_OWNER, "name": REPO_NAME, "categoryId": CATEGORY_ID},
        }).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "panddu-recent-comments-bot",
        },
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.load(resp)

    if payload.get("errors"):
        print(json.dumps(payload["errors"], ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

    discussions = payload["data"]["repository"]["discussions"]["nodes"]

    comments = []
    for d in discussions:
        pathname = d["title"]
        for c in d["comments"]["nodes"]:
            author = c.get("author")
            login = author["login"] if author else None
            if not login or login in EXCLUDE_LOGINS:
                continue
            body = " ".join(c["bodyText"].split())
            if len(body) > BODY_MAX_LEN:
                body = body[:BODY_MAX_LEN].rstrip() + "…"
            comments.append({
                "body": body,
                "author": login,
                "created_at": c["createdAt"],
                "url": pathname,
            })

    comments.sort(key=lambda c: c["created_at"], reverse=True)
    top = comments[:LIMIT]
    for c in top:
        c["date"] = c.pop("created_at")[:10].replace("-", ".")

    os.makedirs("_data", exist_ok=True)
    with open("_data/recent_comments.json", "w", encoding="utf-8") as f:
        json.dump(top, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
