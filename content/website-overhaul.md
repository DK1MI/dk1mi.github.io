---
title: Website Overhaul
date: 2026-01-22
---

I thought long and hard about whether I should switch from [Hugo](https://gohugo.io/) to another static site generator. Not that I was unhappy with Hugo, I just felt like trying something new. In the end, I realized that I don't actually need a generator to convert Markdown to HTML. Basically, it would be enough to write the pages directly in HTML. Of course, a blog also has a few dynamic components:

- Tags
- RSS feed
- List of blog posts

I can do without the tags, but not the RSS feed and, of course, not the list of blog posts. However, since I already have the generated HTML as a base thanks to Hugo, it's actually very easy to continue writing directly in HTML.

While I'm busy working on the site, I might as well add some features or adjust the ones that have been bothering me:

## Menu Bar

All pages, i.e., non-blog posts, are now accessible via a horizontal menu at the top. This makes it easier to find things like the [RSS feed](/index.xml) or my [contact page](/contact) when you are linked directly to a blog post.

## Server Side Includes

One of the problems is that I don't want to change every page when I want to change the header or the horizontal menu below it, for example. I have now moved this code to a separate file, which is then embedded via [SSI (Server Side Includes)](https://nginx.org/en/docs/http/ngx_http_ssi_module.html) during each request.

## Dark Mode

After that, I did a little cleaning up, especially in the stylesheet. I also added a dark mode. When you visit this page for the first time, it should automatically display in dark or light mode, depending on the settings of your operating system/browser. However, you can change this manually in the menu bar at the top right. Unfortunately, I had to use some JavaScript code for this. I don't really like JS, but the end justifies the means.

## A new Workflow

My new workflow for creating posts is now as follows:

- First, I copy the HTML file of an existing post, change the name, adjust the date, and write the text.
- Then I copy all the images for this post into the *img* folder.
- Finally, I adjust the *index.html* (home page) and *index.xml* (RSS feed) by copying and adjusting the lines of the last post.

## Was it worth it?

I'm not sure yet.  But it was fun, and I finally tidied up a bit. I also really like the dark mode. I hope the extra effort doesn't lead to me writing less out of laziness. We'll see...
