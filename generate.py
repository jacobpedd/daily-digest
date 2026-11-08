#!/usr/bin/env python3
"""Generate Jacob's daily digest (RSS 2.0 feed + landing page) from a JSON issue file.

Usage: python3 generate.py items-YYYY-MM-DD.json
Writes feed.xml and index.html next to the items file. The daily job curates
items (via web search), writes the JSON, runs this, and pushes the repo.

Schema v2 (Techmeme-style):
{
  "date": "YYYY-MM-DD",
  "summary": "2-5 sentence summary of the day (plain text, may use - not --)",
  "items": [
    {
      "category": "Chiefs|Nebraska|AI & Agents|Running|San Francisco",
      "title": "headline",
      "url": "primary source URL (must be real)",
      "published": "ISO 8601 with offset",
      "subheader": "one line under the headline",
      "sources": [{"name": "ESPN", "url": "..."}],
      "quotes": [{"text": "verbatim quote", "by": "Name, role", "url": "optional source of the quote"}]
    }
  ]
}
Only "category", "title", "url", "published" are required. Keep items in
editorial order; the generator does not re-sort them.
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


def cdata(text):
    return "<![CDATA[" + text.replace("]]>", "]] >") + "]]>"


def sources_html(sources):
    if not sources:
        return ""
    links = " &middot; ".join(
        f'<a href="{escape(s["url"])}">{escape(s["name"])}</a>' for s in sources
    )
    return f"<p>Sources: {links}</p>"


def quotes_html(quotes):
    out = []
    for q in quotes or []:
        by = escape(q["by"])
        if q.get("url"):
            by = f'<a href="{escape(q["url"])}">{by}</a>'
        out.append(f"<blockquote>&ldquo;{escape(q['text'])}&rdquo; - {by}</blockquote>")
    return "\n".join(out)


def story_html(item):
    parts = []
    if item.get("subheader"):
        parts.append(f"<p><b>{escape(item['subheader'])}</b></p>")
    q = quotes_html(item.get("quotes"))
    if q:
        parts.append(q)
    s = sources_html(item.get("sources"))
    if s:
        parts.append(s)
    return "\n".join(parts) or escape(item.get("subheader", ""))


def item_xml(item):
    dt = datetime.fromisoformat(item["published"])
    return f"""    <item>
      <title>{escape(item['title'])}</title>
      <link>{escape(item['url'])}</link>
      <guid isPermaLink="true">{escape(item['url'])}</guid>
      <pubDate>{format_datetime(dt, usegmt=False)}</pubDate>
      <category>{escape(item['category'])}</category>
      <description>{cdata(story_html(item))}</description>
    </item>"""


def summary_item_xml(issue, pretty_date):
    guid = f"{FEED_LINK}#today-{issue['date']}"
    now = format_datetime(datetime.now(PT), usegmt=False)
    desc = f"<p>{escape(issue['summary'])}</p>"
    return f"""    <item>
      <title>Today in one minute - {escape(pretty_date)}</title>
      <link>{FEED_LINK}</link>
      <guid isPermaLink="true">{guid}</guid>
      <pubDate>{now}</pubDate>
      <description>{cdata(desc)}</description>
    </item>"""


def story_block_html(item):
    quotes = ""
    for q in item.get("quotes") or []:
        by = escape(q["by"])
        if q.get("url"):
            by = f'<a href="{escape(q["url"])}">{by}</a>'
        quotes += f'    <blockquote>&ldquo;{escape(q["text"])}&rdquo; <cite>- {by}</cite></blockquote>\n'
    sources = ""
    if item.get("sources"):
        links = " &middot; ".join(
            f'<a href="{escape(s["url"])}">{escape(s["name"])}</a>' for s in item["sources"]
        )
        sources = f'    <p class="sources">{links}</p>\n'
    sub = f'    <p class="subhead">{escape(item["subheader"])}</p>\n' if item.get("subheader") else ""
    return f"""  <article class="story">
    <span class="cat">{escape(item["category"])}</span>
    <h3><a href="{escape(item["url"])}">{escape(item["title"])}</a></h3>
{sub}{quotes}{sources}  </article>"""


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jacob's Daily Digest - {pretty_date}</title>
<link rel="alternate" type="application/rss+xml" title="Jacob's Daily Digest" href="feed.xml">
<style>
  body {{ font-family: -apple-system, system-ui, sans-serif; max-width: 680px; margin: 2.5rem auto; padding: 0 1.25rem; color: #1a1a1a; line-height: 1.5; }}
  header h1 {{ font-size: 1.7rem; margin: 0; }}
  header .dateline {{ color: #444; font-weight: 600; margin-top: 0.2rem; }}
  header .topics {{ color: #777; font-size: 0.9rem; margin-top: 0.2rem; }}
  header .topics a {{ color: #0969da; }}
  .today {{ background: #f6f8fa; border: 1px solid #e3e6e8; border-radius: 8px; padding: 0.9rem 1.1rem; margin: 1.4rem 0 2rem; }}
  .today h2 {{ font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.06em; color: #666; margin: 0 0 0.4rem; }}
  .today p {{ margin: 0; }}
  article.story {{ margin: 0 0 1.8rem; }}
  .cat {{ display: inline-block; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: #8b0000; }}
  h3 {{ font-size: 1.12rem; margin: 0.15rem 0 0.25rem; }}
  h3 a {{ color: #1a1a1a; }}
  .subhead {{ margin: 0.15rem 0 0.4rem; font-weight: 600; color: #333; }}
  blockquote {{ margin: 0.5rem 0; padding-left: 0.9rem; border-left: 3px solid #d0d7de; color: #444; font-style: italic; }}
  blockquote cite {{ display: block; font-style: normal; font-size: 0.85rem; color: #666; margin-top: 0.15rem; }}
  blockquote cite a {{ color: #666; }}
  .sources {{ font-size: 0.85rem; color: #666; margin: 0.3rem 0 0; }}
  .sources a {{ color: #0969da; }}
  footer {{ margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid #e3e6e8; font-size: 0.85rem; color: #777; }}
  footer code {{ background: #f2f2f2; padding: 0.15em 0.4em; border-radius: 4px; word-break: break-all; }}
</style>
</head>
<body>
<header>
  <h1>Jacob's Daily Digest</h1>
  <div class="dateline">{pretty_date}</div>
  <div class="topics">Chiefs &middot; Nebraska &middot; AI &amp; agent tooling &middot; running &middot; San Francisco &middot; <a href="feed.xml">RSS feed</a></div>
</header>
<section class="today" id="today-{date}">
  <h2>Today in one minute</h2>
  <p>{summary}</p>
</section>
<main>
{stories}</main>
<footer>
  Rebuilt every morning. Subscribe in any RSS reader: <code>{feed_url}</code>
</footer>
</body>
</html>
"""


def main():
    src = Path(sys.argv[1])
    issue = json.loads(src.read_text())
    items = issue["items"]
    date = datetime.strptime(issue["date"], "%Y-%m-%d")
    pretty_date = date.strftime("%A, %B ") + str(date.day) + date.strftime(", %Y")
    now = format_datetime(datetime.now(PT), usegmt=False)

    body = "\n".join([summary_item_xml(issue, pretty_date)] + [item_xml(i) for i in items])
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
    feed_out = src.parent / "feed.xml"
    feed_out.write_text(feed)

    index = INDEX_TEMPLATE.format(
        pretty_date=pretty_date,
        date=issue["date"],
        summary=escape(issue["summary"]),
        stories="\n".join(story_block_html(i) for i in items) + "\n",
        feed_url=FEED_URL,
    )
    index_out = src.parent / "index.html"
    index_out.write_text(index)
    print(f"wrote {feed_out} ({len(items)} stories + summary) and {index_out}")


if __name__ == "__main__":
    main()
