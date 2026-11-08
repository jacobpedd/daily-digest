# daily-digest

Jacob's personal daily news digest, published as an RSS 2.0 feed via GitHub Pages.

- Feed: https://jacobpedd.github.io/daily-digest/feed.xml
- Landing page: https://jacobpedd.github.io/daily-digest/

Topics: Chiefs, Nebraska football, AI & agent tooling, running, San Francisco.

## How it works

An Instinct agent curates the day's items each morning, writes an items JSON file,
runs `generate.py`, and pushes the result:

```sh
python3 generate.py items-YYYY-MM-DD.json   # writes feed.xml and index.html
git add feed.xml index.html items-*.json && git commit -m "digest YYYY-MM-DD" && git push
```

The issue JSON is Techmeme-style (schema v2, see the docstring in `generate.py`):
a `summary` of the day at the top, then story blocks with `subheader`,
`sources` (name + URL) and verbatim `quotes` with attribution. `feed.xml` is the
only file readers poll; `index.html` renders the same issue as a web page.
