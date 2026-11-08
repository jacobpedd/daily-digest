#!/usr/bin/env python3
"""Generate Jacob's daily digest RSS 2.0 feed from a JSON items file.

Usage: python3 generate.py items-YYYY-MM-DD.json
Writes feed.xml next to the items file. The daily job curates items
(via web search), writes the JSON, runs this, and pushes the repo.
"""
import json
import sys
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape
from datetime import datetime, timezone, timedelta

FEED_TITLE = "Jacob's Daily Digest"
FEED_LINK = "https://jacobpedd.github.io/daily-digest/"
FEED_DESC = "A personal daily news digest: Chiefs, Nebraska football, AI and agent tooling, running, and San Francisco."
FEED_URL = FEED_LINK + "feed.xml"
PT = timezone(timedelta(hours=-8), "PST")  # fixed sample offset; job computes real PDT/PST


def item_xml(item):
    pub = item["published"]  # ISO 8601 with offset
    dt = datetime.fromisoformat(pub)
    return f"""    <item>
      <title>{escape(item['title'])}</title>
      <link>{escape(item['url'])}</link>
      <guid isPermaLink="true">{escape(item['url'])}</guid>
      <pubDate>{format_datetime(dt, usegmt=False)}</pubDate>
      <category>{escape(item['category'])}</category>
      <description>{escape(item['summary'])}</description>
    </item>"""


def main():
    src = Path(sys.argv[1])
    items = json.loads(src.read_text())
    items.sort(key=lambda i: i["published"], reverse=True)
    now = format_datetime(datetime.now(PT), usegmt=False)
    body = "\n".join(item_xml(i) for i in items)
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{FEED_TITLE}</title>
    <link>{FEED_LINK}</link>
    <atom:link href="{FEED_URL}" rel="self" type="application/rss+xml"/>
    <description>{FEED_DESC}</description>
    <language>en-us</language>
    <lastBuildDate>{now}</lastBuildDate>
    <ttl>360</ttl>
{body}
  </channel>
</rss>
"""
    out = src.parent / "feed.xml"
    out.write_text(feed)
    print(f"wrote {out} with {len(items)} items")


if __name__ == "__main__":
    main()
