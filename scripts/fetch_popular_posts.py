#!/usr/bin/env python3
"""GA4 인기글 Top N을 _data/popular_posts.json으로 저장.

이 GA4 property는 서비스 계정을 viewer로 추가하는 게 거부되어(로컬 blog-analytics
스킬과 동일한 이유), 서비스 계정이 아니라 블로그 소유 계정의 OAuth refresh token을
재사용한다. google-auth 라이브러리 의존 없이 stdlib만으로 토큰 갱신 + Data API 호출.

필요 환경변수: GA4_CLIENT_ID, GA4_CLIENT_SECRET, GA4_REFRESH_TOKEN
"""
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

PROPERTY_ID = "539653871"
LIMIT = 5
START_DATE = "28daysAgo"

TOKEN_URL = "https://oauth2.googleapis.com/token"
REPORT_URL = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"


def refresh_access_token():
    data = urllib.parse.urlencode({
        "client_id": os.environ["GA4_CLIENT_ID"],
        "client_secret": os.environ["GA4_CLIENT_SECRET"],
        "refresh_token": os.environ["GA4_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, headers={
        "Content-Type": "application/x-www-form-urlencoded",
    })
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["access_token"]


def fetch_report(access_token):
    body = json.dumps({
        "dateRanges": [{"startDate": START_DATE, "endDate": "today"}],
        "dimensions": [{"name": "pagePath"}, {"name": "pageTitle"}],
        "metrics": [{"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 20,
    }).encode("utf-8")
    req = urllib.request.Request(REPORT_URL, data=body, headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main():
    access_token = refresh_access_token()
    report = fetch_report(access_token)

    posts = []
    seen_paths = set()
    for row in report.get("rows", []):
        path = row["dimensionValues"][0]["value"]
        title = row["dimensionValues"][1]["value"]
        views = int(row["metricValues"][0]["value"])

        # 글 상세 페이지만 (목록/시리즈/기타 페이지 제외): /posts/<year>/<month>/<slug>/
        parts = [p for p in path.strip("/").split("/") if p]
        if len(parts) < 3 or parts[0] != "posts":
            continue
        if path in seen_paths:
            continue
        seen_paths.add(path)

        posts.append({"title": title, "url": path, "views": views})
        if len(posts) >= LIMIT:
            break

    output = {
        # Liquid의 date 필터는 명시 오프셋을 그대로 찍고(사이트 timezone 설정과 무관하게
        # 로컬 변환을 안 해줌), 그래서 UTC가 아니라 KST 오프셋을 붙여서 저장한다.
        "generated_at": datetime.now(KST).isoformat(timespec="seconds"),
        "posts": posts,
    }

    os.makedirs("_data", exist_ok=True)
    with open("_data/popular_posts.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
