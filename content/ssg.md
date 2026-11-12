---
title: Back to an SSG - but this time my own
date: 2026-11-12
---

[In May of this year, I decided to stop using an SSG (Static Site Generator)](/handcrafted-html/) and instead write the HTML code by hand. I actually had no problem with it and really enjoyed it, but somehow I still felt the urge to do something completely different: to have my own SSG, just for this site and with as few features as possible. The features of the new SSG, created specifically for this site, are as follows:


- It builds the whole site with one command, written in Python 3 and without any dependencies
- Converts each Markdown file into a page: content/<slug>.md becomes /<slug>/index.html, so the file name sets the URL.
- Uses a simple template file that is populated with the generated HTML code: layout.html fills in {{ content }}, {{ title }} and {{ lang }}.
- Reads a few settings from the top of each file (front matter):
  - title (required)
  - date (YYYY-MM-DD or YYYY-MM-DD HH:MM, in UTC)
  - summary (the text shown in the RSS feed)
  - show_date: false (hides the "Posted on" line)
  - lang (the page language, e.g. de; the default is en-us)
- Treats a page as a post if it has a date:
  - With a date, it's a post. It shows "Posted on", is listed on the home page and goes into the RSS feed.
  - Without a date, it's a standalone page, like About, Contact or Bookmarks. It only shows up where something links to it.
- Builds the home page: the intro comes from content/_index.md, followed by all posts, newest first, grouped under a heading for each year.
- Writes an RSS feed (index.xml):
  - It contains the newest posts, with title, link, guid, pubDate and description.
  - The description is the summary (see above), or the first paragraph if there is no summary.
- Has its own Markdown converter that supports:
  - headings, optionally with a custom {#id} anchor
  - paragraphs and hard line breaks
  - bold, italic, strikethrough and inline code
  - links, images and <https://…> autolinks
  - nested bullet and numbered lists
  - blockquotes, horizontal rules and fenced code blocks
  - tables with column alignment
  - backslash escapes
  - raw HTML passed through unchanged, both whole blocks (like <audio> or <figure>) and inline tags (I use this for the Doom WAD log)
- Copies everything in static/ unchanged: images, files/, style.css, favicons, site.webmanifest, robots.txt, CNAME and so on.
- Puts all generated/copied content into output/: the folder is deleted and rebuilt on every run.
- Publishes itself: the GitHub Actions workflow .github/workflows/deploy.yml runs ssg.py and deploys output/ to GitHub Pages on every push to main.

What it deliberately doesn't do: there are no tags, categories, pagination, drafts, plugins or themes, and no local preview server.

So far, it works great and makes things super easy. It feels good to be independant from the dev team of an SSG that might change features in the future or depricate ones I like.

The source of this website and the SSG can be found here: [https://github.com/DK1MI/dk1mi.github.io](https://github.com/DK1MI/dk1mi.github.io).
