---
title: bear2hugo.py - Migrating from Bear Blog to Hugo
date: 2024-08-16 13:00
---

I’ve written the following small Python script to migrate a [Bear Blog](https://bearblog.dev/) to [Hugo](https://gohugo.io/):

```
import csv
import os

with open('post_exports.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    os.makedirs("./pages", exist_ok = True)
    os.makedirs("./posts", exist_ok = True)
    for row in csv_reader:
        dir = ""
        if row[11] == "True":
            dir = "pages/"
        else:
            dir = "posts/"
        with open(dir + row[4]+'.md', 'w') as post:
            publish = row[9]
            if publish == 'False':
                draft = "true"
            else:
                draft = "false"
            post.write("+++\n")
            post.write("slug = '" + row[4] + "'\n")
            post.write("title = '" + row[3] + "'\n")
            post.write("date = " + row[6] + "\n")
            post.write("draft = " + draft + "\n")
            post.write("tags = " + row[8] + "\n")
            post.write("+++\n")
            post.write(row[12])

```

It’s not really sophisticated but it does the job. Here’s all you need to know:

- Create a new directory, e.g. *~/bear2hugo/*
- Create a new file *bear2hugo.py* in this directory and copy the above content into this file
- Download the export file from Bear Blog via the menu item “Export all blog data”
- Place the resulting file *post_exports.csv* together with *bear2hugo.py* in *~/bear2hugo/*
- Execute the script: *# python3 bear2hugo.py*
- It will create two new directories *pages* and *posts*
- It will parse through CSV file and create a Mardown file for each post and page inside the corresponding directories
- You can now copy the files into your *content/* and *content/blog/* directory and use them with Hugo
