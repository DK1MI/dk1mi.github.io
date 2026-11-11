#!/usr/bin/env python3
"""
ssg.py - the static site generator for rz01.org

Usage:  python3 ssg.py

Reads   content/*.md      one Markdown file per page, output to /<slug>/index.html
        content/_index.md  intro text of the home page
        layout.html        the HTML shell shared by all pages
        static/            copied unchanged (img/, files/, style.css, favicons, ...)
Writes  output/            the complete website: the static files plus
                           <slug>/index.html, index.html (intro + list of posts)
                           and index.xml (RSS)

output/ is deleted and rebuilt from scratch on every run, so never edit it.

Front matter (between two '---' lines at the top of a Markdown file):
    title:     page title (required)
    date:      YYYY-MM-DD or "YYYY-MM-DD HH:MM" (UTC). Pages with a date are
               posts: they show "Posted on", appear on the home page and in
               the RSS feed. Pages without a date are standalone pages.
    summary:   optional RSS description; defaults to the first paragraph.
    show_date: false  hides the "Posted on" line (the post is still listed).
    lang:      language of the page, e.g. "de" (default: "en-us").

No dependencies besides the Python 3 standard library.
"""

import html
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------- config ---

SITE_URL = "https://rz01.org"
SITE_TITLE = "rz01.org"
FEED_ITEMS = 11  # number of newest posts in index.xml
DEFAULT_LANG = "en-us"

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
LAYOUT = ROOT / "layout.html"
STATIC = ROOT / "static"
OUTPUT = ROOT / "output"

# ------------------------------------------------------ markdown renderer ---
#
# A small Markdown renderer covering what this site uses:
#   # headings (optional "{#id}" suffix sets the id attribute)
#   paragraphs, hard line breaks (two trailing spaces or a trailing backslash)
#   **bold**, *italic*, _italic_, `code`, [links](url), ![images](src), <https://autolinks>
#   - bullet and 1. numbered lists (nested by indentation, loose or tight)
#   > blockquotes, --- horizontal rules, ``` fenced code blocks, | pipe | tables |
#   raw HTML: blocks starting with a block-level tag are passed through
#   unchanged, inline tags (<br>, <span ...>, ...) are kept as they are.

BLOCK_TAGS = {
    "address", "article", "aside", "audio", "blockquote", "center", "details",
    "dialog", "div", "dl", "fieldset", "figcaption", "figure", "footer", "form",
    "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "iframe", "li", "main",
    "nav", "ol", "p", "pre", "section", "summary", "table", "tbody", "td",
    "tfoot", "th", "thead", "tr", "ul", "video", "canvas", "picture", "script",
    "style",
}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "source", "track", "wbr"}

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*([^`]*)$")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+\{#([^}\s]+)\})?[ \t]*$")
HR_RE = re.compile(r"^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$")
LIST_RE = re.compile(r"^( *)([-*+]|\d{1,9}[.)])(?:[ \t]+|$)")
QUOTE_RE = re.compile(r"^ {0,3}> ?")
TABLE_SEP_RE = re.compile(r"^ *\|? *:?-+:? *(\| *:?-+:? *)*\|? *$")
HTML_OPEN_RE = re.compile(r"^ {0,3}<(/?)([A-Za-z][A-Za-z0-9-]*)(?=[\s/>]|$)")
ONLY_TAGS_RE = re.compile(r"^\s*(<!--.*?-->|</?[A-Za-z][A-Za-z0-9-]*(?:\s[^<>]*)?/?>\s*)+$", re.S)
ENTITY_RE = re.compile(r"&(#[0-9]+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);")


def _is_html_block_start(line):
    m = HTML_OPEN_RE.match(line)
    if m and m.group(2).lower() in BLOCK_TAGS:
        return True
    s = line.strip()
    return s.startswith("<!--") or (s.startswith("<") and bool(ONLY_TAGS_RE.match(s)))


def _starts_block(line):
    """Lines that end a paragraph."""
    return bool(
        FENCE_RE.match(line) or HEADING_RE.match(line) or HR_RE.match(line)
        or QUOTE_RE.match(line) or LIST_RE.match(line) or _is_html_block_start(line)
    )


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def render_markdown(text):
    lines = text.replace("\r\n", "\n").replace("\t", "    ").split("\n")
    return "\n\n".join(_blocks(lines, tight=False))


def _blocks(lines, tight):
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        # fenced code block
        m = FENCE_RE.match(line)
        if m:
            fence = m.group(1)
            ind = _indent(line)
            code = []
            i += 1
            while i < n:
                s = lines[i]
                if s.strip().startswith(fence[0] * len(fence)) and not s.strip().strip(fence[0]):
                    i += 1
                    break
                code.append(s[min(ind, _indent(s)):])
                i += 1
            out.append("<pre><code>" + html.escape("\n".join(code), quote=False) + "</code></pre>")
            continue

        # heading
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            body = re.sub(r"[ \t]+#+[ \t]*$", "", m.group(2) or "")
            attr = f' id="{html.escape(m.group(3))}"' if m.group(3) else ""
            out.append(f"<h{level}{attr}>{render_inline(body)}</h{level}>")
            i += 1
            continue

        # horizontal rule
        if HR_RE.match(line):
            out.append("<hr>")
            i += 1
            continue

        # raw HTML block
        if _is_html_block_start(line):
            i, block = _html_block(lines, i)
            out.append(block)
            continue

        # blockquote
        if QUOTE_RE.match(line):
            inner = []
            while i < n and lines[i].strip() and QUOTE_RE.match(lines[i]):
                inner.append(QUOTE_RE.sub("", lines[i], count=1))
                i += 1
            out.append("<blockquote>\n" + "\n".join(_blocks(inner, False)) + "\n</blockquote>")
            continue

        # list
        if LIST_RE.match(line):
            i, block = _list(lines, i)
            out.append(block)
            continue

        # table
        if "|" in line and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]) and "-" in lines[i + 1]:
            i, block = _table(lines, i)
            out.append(block)
            continue

        # paragraph
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not _starts_block(lines[i]):
            para.append(lines[i])
            i += 1
        content = render_inline("\n".join(l.lstrip() for l in para).rstrip())
        out.append(content if tight else f"<p>{content}</p>")
    return out


def _html_block(lines, i):
    """Pass raw HTML through. A block opened by a non-void tag runs until that
    tag is closed again (blank lines inside are allowed), anything else until
    the next blank line."""
    n = len(lines)
    m = HTML_OPEN_RE.match(lines[i])
    name = m.group(2).lower() if m and not m.group(1) else None
    if name and name not in VOID_TAGS:
        depth = 0
        open_re = re.compile(rf"<{name}(?=[\s/>])", re.I)
        close_re = re.compile(rf"</{name}\s*>", re.I)
        start = i
        while i < n:
            depth += len(open_re.findall(lines[i])) - len(close_re.findall(lines[i]))
            i += 1
            if depth <= 0:
                break
        # also take whatever follows the closing tag on following non-blank lines
        while i < n and lines[i].strip():
            i += 1
        return i, "\n".join(lines[start:i])
    start = i
    while i < n and lines[i].strip():
        i += 1
    return i, "\n".join(lines[start:i])


def _list(lines, i):
    n = len(lines)
    first = LIST_RE.match(lines[i])
    base = len(first.group(1))
    ordered = first.group(2)[0].isdigit()
    start = int(first.group(2)[:-1]) if ordered else 1
    items = []  # list of line lists
    loose = False
    while i < n:
        line = lines[i]
        m = LIST_RE.match(line)
        if m and len(m.group(1)) == base and m.group(2)[0].isdigit() == ordered:
            content_indent = len(m.group(0)) if line[len(m.group(0)):].strip() else len(m.group(1)) + len(m.group(2)) + 1
            items.append({"indent": content_indent, "lines": [line[len(m.group(0)):]]})
            i += 1
            continue
        if not line.strip():
            # blank line: continue only if the list goes on afterwards
            j = i
            while j < n and not lines[j].strip():
                j += 1
            if j >= n:
                break
            nxt = lines[j]
            m2 = LIST_RE.match(nxt)
            if _indent(nxt) >= items[-1]["indent"] or (m2 and len(m2.group(1)) == base and m2.group(2)[0].isdigit() == ordered):
                loose = True
                items[-1]["lines"].extend([""] * (j - i))
                i = j
                continue
            break
        if _indent(line) >= items[-1]["indent"]:
            items[-1]["lines"].append(line[items[-1]["indent"]:])
            i += 1
            continue
        if _indent(line) > base and LIST_RE.match(line):
            # nested list indented less than the content: still belongs to the item
            items[-1]["lines"].append(line[min(_indent(line), items[-1]["indent"]):])
            i += 1
            continue
        if not _starts_block(line) and items[-1]["lines"][-1].strip():
            items[-1]["lines"].append(line.strip())  # lazy continuation
            i += 1
            continue
        break

    tag = "ol" if ordered else "ul"
    attr = f' start="{start}"' if ordered and start != 1 else ""
    out = [f"<{tag}{attr}>"]
    for item in items:
        body = item["lines"]
        while body and not body[-1].strip():
            body.pop()
        if any(not l.strip() for l in body):
            loose = True
        out.append((item, body))
    rendered = [out[0]]
    for item, body in out[1:]:
        parts = _blocks(body, tight=not loose)
        if not parts:
            rendered.append("<li></li>")
        elif len(parts) == 1 and not loose:
            rendered.append(f"<li>{parts[0]}</li>")
        else:
            rendered.append("<li>" + "\n".join(parts) + "\n</li>")
    rendered.append(f"</{tag}>")
    return i, "\n".join(rendered)


def _split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, k = [], "", 0
    while k < len(s):
        if s[k] == "\\" and k + 1 < len(s) and s[k + 1] == "|":
            cur += "|"
            k += 2
            continue
        if s[k] == "|":
            cells.append(cur.strip())
            cur = ""
        else:
            cur += s[k]
        k += 1
    cells.append(cur.strip())
    return cells


def _table(lines, i):
    n = len(lines)
    head = _split_row(lines[i])
    aligns = []
    for c in _split_row(lines[i + 1]):
        if c.startswith(":") and c.endswith(":"):
            aligns.append("center")
        elif c.endswith(":"):
            aligns.append("right")
        elif c.startswith(":"):
            aligns.append("left")
        else:
            aligns.append(None)
    i += 2
    rows = []
    while i < n and lines[i].strip() and "|" in lines[i]:
        rows.append(_split_row(lines[i]))
        i += 1

    def cell(tag, text, k):
        a = aligns[k] if k < len(aligns) else None
        style = f' style="text-align: {a}"' if a else ""
        return f"<{tag}{style}>{render_inline(text)}</{tag}>"

    out = ["<table>", "<thead>", "<tr>"]
    out += [cell("th", c, k) for k, c in enumerate(head)]
    out += ["</tr>", "</thead>", "<tbody>"]
    for r in rows:
        r = (r + [""] * len(head))[:len(head)]
        out.append("<tr>" + "".join(cell("td", c, k) for k, c in enumerate(r)) + "</tr>")
    out += ["</tbody>", "</table>"]
    return i, "\n".join(out)


# ---- inline ----

INLINE_TAG_RE = re.compile(r"<!--.*?-->|</?[A-Za-z][A-Za-z0-9-]*(?:\s+[^<>]*?)?\s*/?>", re.S)
AUTOLINK_RE = re.compile(r"(?<!\]\()<((?:https?|ftp|mailto|gopher):[^<>\s]+)>")
CODE_RE = re.compile(r"(?<![\\`])(`+)(.+?)(?<!`)\1(?!`)", re.S)
ESCAPE_RE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(\s*<?([^\s)>]*)>?(?:\s+\"([^\"]*)\")?\s*\)")
LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*(<[^>]*>|[^\s()]*(?:\([^\s()]*\)[^\s()]*)*)(?:\s+\"([^\"]*)\")?\s*\)", re.S)
STRONG_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*|(?<![A-Za-z0-9])__(?=\S)(.+?)(?<=\S)__(?![A-Za-z0-9])", re.S)
EM_RE = re.compile(r"\*(?=[^\s*])(.+?)(?<=[^\s*])\*|(?<![A-Za-z0-9_])_(?=[^\s_])(.+?)(?<=[^\s_])_(?![A-Za-z0-9_])", re.S)
DEL_RE = re.compile(r"~~(?=\S)(.+?)(?<=\S)~~", re.S)


def _attr(s):
    return html.escape(s, quote=True)


def _escape_text(s):
    """HTML-escape text but keep valid entities like &rsquo; intact."""
    s = re.sub(r"&(?!(#[0-9]+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;")


def render_inline(text):
    store = []

    def keep(s):
        store.append(s)
        return f"\x00{len(store) - 1}\x00"

    # hard line breaks
    text = re.sub(r"(?: {2,}|\\)\n", lambda m: keep("<br>") + "\n", text)
    text = CODE_RE.sub(lambda m: keep("<code>" + html.escape(_strip_code(m.group(2)), quote=False) + "</code>"), text)
    text = ESCAPE_RE.sub(lambda m: keep(html.escape(m.group(1), quote=False)), text)
    text = AUTOLINK_RE.sub(lambda m: keep(f'<a href="{_attr(m.group(1))}">{html.escape(m.group(1).removeprefix("mailto:"))}</a>'), text)
    text = INLINE_TAG_RE.sub(lambda m: keep(m.group(0)), text)

    def image(m):
        title = f' title="{_attr(m.group(3))}"' if m.group(3) else ""
        return keep(f'<img src="{_attr(m.group(2))}" alt="{_attr(_plain(m.group(1)))}"{title}>')

    text = IMAGE_RE.sub(image, text)

    def link(m):
        url = m.group(2)
        if url.startswith("<") and url.endswith(">"):
            url = url[1:-1]
        title = f' title="{_attr(m.group(3))}"' if m.group(3) else ""
        return keep(f'<a href="{_attr(url)}"{title}>') + m.group(1) + keep("</a>")

    prev = None
    while prev != text:  # links may be nested in emphasis and vice versa
        prev = text
        text = LINK_RE.sub(link, text)

    text = _escape_text(text)
    for _ in range(3):
        text = STRONG_RE.sub(lambda m: f"<strong>{m.group(1) or m.group(2)}</strong>", text)
        text = EM_RE.sub(lambda m: f"<em>{m.group(1) or m.group(2)}</em>", text)
        text = DEL_RE.sub(lambda m: f"<del>{m.group(1)}</del>", text)

    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], text)
    return text


def _strip_code(s):
    if len(s) > 2 and s[0] == " " and s[-1] == " " and s.strip():
        return s[1:-1]
    return s


def _plain(s):
    """Text content of a Markdown snippet (for alt attributes and summaries)."""
    return html.unescape(re.sub(r"<[^>]+>", "", render_inline(s)))


# ------------------------------------------------------------------ site ---

class Page:
    def __init__(self, path):
        self.path = path
        self.slug = path.stem
        raw = path.read_text(encoding="utf-8")
        self.meta, self.body_md = parse_front_matter(raw, path)
        if "title" not in self.meta:
            sys.exit(f"{path}: front matter has no 'title'")
        self.title = self.meta["title"]
        self.date = None
        if self.meta.get("date"):
            try:
                d = self.meta["date"]
                fmt = "%Y-%m-%d %H:%M" if " " in d else "%Y-%m-%d"
                self.date = datetime.strptime(d, fmt).replace(tzinfo=timezone.utc)
            except ValueError:
                sys.exit(f"{path}: invalid date '{self.meta['date']}' (use YYYY-MM-DD or YYYY-MM-DD HH:MM)")
        self.lang = self.meta.get("lang") or DEFAULT_LANG
        self.show_date = self.date is not None and self.meta.get("show_date", "true").lower() not in ("false", "no", "0")
        self.body_html = render_markdown(self.body_md)

    @property
    def url(self):
        return f"/{self.slug}/"

    @property
    def summary(self):
        if self.meta.get("summary"):
            return self.meta["summary"]
        m = re.search(r"<p>(.*?)</p>", self.body_html, re.S)
        text = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))) if m else ""
        return " ".join(text.split()) + "..." if text else ""


def parse_front_matter(raw, path):
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        sys.exit(f"{path}: front matter is not closed with '---'")
    meta = {}
    for line in raw[3:end].strip().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            sys.exit(f"{path}: invalid front matter line: {line!r}")
        meta[key.strip().lower()] = value.strip()
    body = raw[end + 4:]
    return meta, body.lstrip("\n")


def render_page(layout, content, title=SITE_TITLE, lang=DEFAULT_LANG):
    return (layout.replace("{{ title }}", html.escape(title, quote=False))
                  .replace("{{ lang }}", html.escape(lang))
                  .replace("{{ content }}", content))


def enhance(body):
    """Lazy-load images and let wide tables scroll sideways on small screens."""
    body = re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy"', body)
    return re.sub(r"<table\b.*?</table>", lambda m: f'<div class="table-wrap">{m.group(0)}</div>', body, flags=re.S | re.I)


def build_post_page(layout, page):
    parts = ["<article>", f"<h1>{html.escape(page.title, quote=False)}</h1>"]
    if page.show_date:
        parts.append(f'<i>Posted on <time datetime="{page.date:%Y-%m-%d}">{page.date:%Y-%m-%d}</time></i>')
    parts += ["", enhance(page.body_html), "</article>"]
    return render_page(layout, "\n".join(parts), f"{page.title} – {SITE_TITLE}", page.lang)


def build_index(layout, intro_html, posts):
    out = [intro_html, ""]
    year = None
    for p in posts:
        if p.date.year != year:
            if year is not None:
                out.append("      </ul>")
            year = p.date.year
            out.append(f"      <h2>{year}</h2>")
            out.append('      <ul class="no-hyphen">')
        out.append("        <li>")
        out.append(f"            <span>{p.date:%Y-%m-%d}</span>")
        out.append(f'            <a href="{p.url}">{html.escape(p.title, quote=False)}</a>')
        out.append("        </li>")
    if year is not None:
        out.append("      </ul>")
    return render_page(layout, "\n".join(out))


def build_feed(posts):
    def esc(s):
        return html.escape(s, quote=False)

    out = [
        '<?xml version="1.0" encoding="utf-8" standalone="yes"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        f"    <title>{esc(SITE_TITLE)}</title>",
        f"    <link>{SITE_URL}/</link>",
        f"    <description>Recent content on {esc(SITE_TITLE)}</description>",
        "    <language>en-us</language>",
        f'    <atom:link href="{SITE_URL}/index.xml" rel="self" type="application/rss+xml" />',
    ]
    if posts:
        out.append(f"    <lastBuildDate>{posts[0].date.strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>")
    for p in posts[:FEED_ITEMS]:
        out += [
            "    <item>",
            f"      <title>{esc(p.title)}</title>",
            f"      <link>{SITE_URL}{p.url}</link>",
            f'      <guid isPermaLink="true">{SITE_URL}{p.url}</guid>',
            f"      <pubDate>{p.date.strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>",
            f"      <description>{esc(p.summary)}</description>",
            "    </item>",
        ]
    out += ["  </channel>", "</rss>", ""]
    return "\n".join(out)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    layout = LAYOUT.read_text(encoding="utf-8")
    pages = [Page(p) for p in sorted(CONTENT.glob("*.md")) if not p.name.startswith("_")]
    static_names = {p.name for p in STATIC.iterdir()} if STATIC.exists() else set()
    for p in pages:
        if p.slug in static_names or p.slug in ("index.html", "index.xml"):
            sys.exit(f"{p.path}: '{p.slug}' clashes with a file in static/")

    # start from a clean output directory
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    if STATIC.exists():
        shutil.copytree(STATIC, OUTPUT)
    OUTPUT.mkdir(exist_ok=True)

    posts = sorted((p for p in pages if p.date), key=lambda p: p.date, reverse=True)
    for p in pages:
        write(OUTPUT / p.slug / "index.html", build_post_page(layout, p))

    intro_file = CONTENT / "_index.md"
    intro = ""
    if intro_file.exists():
        intro = render_markdown(parse_front_matter(intro_file.read_text(encoding="utf-8"), intro_file)[1])
    write(OUTPUT / "index.html", build_index(layout, intro, posts))
    write(OUTPUT / "index.xml", build_feed(posts))

    print(f"{len(pages)} pages ({len(posts)} posts) written to {OUTPUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
