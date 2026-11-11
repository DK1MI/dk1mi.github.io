# rz01.org

Source of [rz01.org](https://rz01.org). The pages are generated from Markdown by `ssg.py`
(Python 3, standard library only).

## Writing a post

Create `content/<slug>.md` — the file name becomes the URL (`/<slug>/`):

```markdown
---
title: My new project
date: 2026-11-20
---

Intro text with **bold**, *italic*, `code` and a [link](https://example.org).

## A section {#optional-anchor-id}

![](/img/my-new-project-01.jpg)
```

Then run:

```
python3 ssg.py
```

This rebuilds the complete website in `output/`: it deletes `output/`, copies everything
from `static/` into it and writes `<slug>/index.html` for every Markdown file, the home page
`index.html` (intro from `content/_index.md` + list of all posts by year) and the RSS feed
`index.xml`. `output/` is what gets deployed; never edit files in it by hand.

### Front matter

| key         | meaning                                                                   |
|-------------|---------------------------------------------------------------------------|
| `title`     | page title (required)                                                     |
| `date`      | `YYYY-MM-DD` or `YYYY-MM-DD HH:MM` (UTC). With a date the page is a post: it shows "Posted on", is listed on the home page and goes into the RSS feed. Without a date it is a standalone page (e.g. About). The time is only used for the feed and to order posts of the same day. |
| `summary`   | RSS description (optional, defaults to the first paragraph + "...")       |
| `show_date` | `false` hides the "Posted on" line but keeps the page in the list        |

### Markdown

Headings (`{#id}` sets an anchor id), paragraphs, `**bold**`, `*italic*`, `` `code` ``,
links, images, `<https://autolinks>`, bullet and numbered lists (nested by indentation),
`>` blockquotes, `---` rules, fenced ```` ``` ```` code blocks, pipe tables. Raw HTML works
too: blocks starting with an HTML block tag (`<table>`, `<figure>`, `<div>`, ...) are copied
unchanged, inline tags like `<br>` or `<span>` are kept as they are.

## Layout

- `content/` – Markdown sources
- `layout.html` – the HTML shell (head, logo, navigation) of every page; `{{ content }}` marks
  where the page content goes
- `static/` – files copied unchanged into the site: `img/`, `files/`, `style.css`, favicons,
  `robots.txt`, `CNAME`, ...
- `output/` – the generated website

## Publishing

`.github/workflows/deploy.yml` builds the site with `ssg.py` and publishes `output/` to GitHub
Pages on every push to `main`. `output/` itself is not committed (see `.gitignore`).
One-time setup: repository *Settings → Pages → Build and deployment → Source: GitHub Actions*.
