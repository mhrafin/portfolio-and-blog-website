# Usage Guide

This project uses a `Makefile` to automate common tasks.

## Common Commands

### Build the Site
Generates the static site in the `output/` directory. This also automatically builds the TailwindCSS.
```bash
make html
```

### Serve Locally
Builds the site and serves it at `http://localhost:8000`.
```bash
make serve
```

### Development Server (Auto-reload)
Builds, serves, and watches for changes (both content and theme) to regenerate automatically.
```bash
make devserver
```

### Clean Output
Removes the `output/` directory.
```bash
make clean
```

### Build CSS
Compiles TailwindCSS. This is automatically called by `make html`.
```bash
make build-css
```

### Watch CSS
Watches for changes in Tailwind classes and recompiles CSS in real-time.
```bash
make watch-css
```

## Writing Content

Content is written in Markdown and placed in the `content/content/` directory.

### File Metadata
Pelican requires metadata at the top of each Markdown file:

```markdown
Title: My Article Title
Date: 2023-10-27 10:00
Category: Blog
Tags: python, pelican
Slug: my-article-slug
Authors: Mahedi Hassan Rafin
Summary: A brief summary of the article.

Article content goes here...
```

## Syncing Content

### Sync to AWS
Syncs the `output/` directory to the configured S3 bucket for the website, and `content/` to the Obsidian backup bucket.
```bash
make sync-to-aws
```

### Sync from AWS
Syncs content from the Obsidian S3 bucket back to the local `content/` directory.
```bash
make sync-content-from-aws
```
