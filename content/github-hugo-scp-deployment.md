---
title: Hugo Deployment via SCP and Github Actions
date: 2025-06-19
---

## Introduction {#introduction}

This post describes how to automatically deploy your [Hugo](https://gohugo.io) project hosted on Github to any (shared) webhost as soon as you push changes to the underlying github repository. The prerequisite for this is that the target host is accessible via SSH. I followed this good tutorial and adapted the procedure to my needs: [Github actions: Deploy a Hugo website to a FTP server](https://revolugame.com/p/gitbub-actions-deploy-a-hugo-website-to-a-ftp-server/).

## Preconditions: SSH Key {#preconditions-ssh-key}

First create a new SSH key locally on your computer:

```
# ssh-keygen -t rsa -f ~/webhost
```

Then copy the content of the private key ( *~/webhost*) to the clipboard, go to Github.com, then to the website repository, click on **Settings** > **Secrets and Variables** > **Actions** and finally on **New Repository Secret**. Name the new secret “ **SSH_KEY**” and then enter the previously generated private key. Make sure **that an empty line remains at the end**.

Now we have securely stored the SSH key in Github and can use it from our script.

The public key must then be stored with the hoster. If you use cPanel, you can do this under **Tools** > **SSH Access** > **Manage SSH Keys**. Do not forget to authorize the newly added public key.

## Creating the Github Workflow {#creating-the-github-workflow}

Now we can write the actual workflow script. To do this, we create the file *main.yml* within the directory *.github/workflows* in our git repository:

```
# mkdir -p ./.github/workflows
# vim ./.github/workflows/main.yml

```

Paste the following into the file you just created:

```
name: 🚀 Deploy to prod

# Will trigger the workflow on each push to the main branch
on:
  push:
    branches:
      - main

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  # The first job will build the hugo site and upload the artifact
  build:
    name: 🔧 Build Hugo site
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.147.8
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb

      - name: Install Dart Sass Embedded
        run: sudo snap install dart-sass-embedded

      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0

      - name: Install Node.js dependencies
        run: '[[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true'

      - name: Build with Hugo
        env:
          # For maximum backward compatibility with Hugo modules
          HUGO_ENVIRONMENT: production
          HUGO_ENV: production
        run: |
          hugo \
            --gc \
            --minify

      # We save the result as an artificat so we can use it in the next job
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: release-artifact
          path: './public'

  # The second job will deploy the site to the FTP server using the artifact from the first job
  deploy:
    name: 🎉 Deploy
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # Download the artifact we just created
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: release-artifact
          path: './public' # This is the path where the artifact will be downloaded to

      - name: Set globals
        id: globals
        shell: bash
        run: |
          echo "SSH_USER=XXXXXXXXXXXXXXXXX" >> "${GITHUB_OUTPUT}"
          echo "SSH_HOST=XXXXXXXXXXXXXXXXX" >> "${GITHUB_OUTPUT}"

      - name: Configure SSH
        run: |
          mkdir -p ~/.ssh/
          echo "${{ secrets.SSH_KEY }}" > ~/.ssh/webhost.key
          chmod 600 ~/.ssh/webhost.key
          cat >>~/.ssh/config <<END
          Host webhost
            HostName ${{ steps.globals.outputs.SSH_HOST }}
            User ${{ steps.globals.outputs.SSH_USER }}
            IdentityFile ~/.ssh/webhost.key
            StrictHostKeyChecking no
          END

      - name: gzip public folder
        run: tar -cvzf deploy.tgz ./public/*

      - name: upload tarball
        run: scp ./deploy.tgz webhost:/home/${{ steps.globals.outputs.SSH_USER }}/tmp/deploy.tgz

      - name: unzip deploy file
        run: ssh webhost 'tar -xvzf /home/${{ steps.globals.outputs.SSH_USER }}/tmp/deploy.tgz -C /home/${{ steps.globals.outputs.SSH_USER }}/tmp/'

      - name: delete public_html
        run: ssh webhost 'rm -rf /home/${{ steps.globals.outputs.SSH_USER }}/public_html'

      - name: move public_html
        run: ssh webhost 'mv /home/${{ steps.globals.outputs.SSH_USER }}/tmp/public /home/${{ steps.globals.outputs.SSH_USER }}/public_html'

      - name: delete tarball
        run: ssh webhost 'rm /home/${{ steps.globals.outputs.SSH_USER }}/tmp/deploy.tgz'

```

Before you start, you need to adjust the following two variables within the script:

- SSH_USER: Set this to the SSH user name
- SSH_HOST: Set this to the host name of your destination system

You also might need to adapt some paths for your specific environment.

## What it does and why {#what-it-does-and-why}

In summary, this workflow does the following

- First the website will be **built**
  - Hugo is downloaded in the desired version
  - Dependencies are installed
  - Hugo is executed and the website is generated
  - The result is uploaded as an artifact
- Now the artifact will be **deployed** which means that the generated website will be uploaded to the web host
  - The artifact is downloaded again
  - Global variables are set (target host and SSH user name)
  - SSH is configured on the client side, i.e. the key is created and an SSH config is generated
  - A tarball of the public folder is created
  - The tarball is uploaded to the target host
  - The tarball is unpacked
  - The directory containing the old version of the website is deleted
  - The directory with the new version is moved to the location of the old directory
  - The tarball is deleted

Why so complicated? Why not simply upload the new files via SFTP and overwrite the old files?

The reason for this is that in my case this took far too long and old, deleted files remain. Uploading and unpacking the tarball is much faster. The old version of the website can then be replaced with the new one in a flash. If something goes wrong during deployment, the old version is retained for as long as possible.

## Conclusion {#conclusion}

Using this workflow, I can now write a new blob post on my local computer, for example, and push it to my Github repo. This automatically triggers the Github workflow described above, which then regenerates the website and uploads it to my web host of choice.
