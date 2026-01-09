# Usage Guide

This project uses a `Makefile` to automate common tasks.

## Common Commands

### Build the Site
Generates the static site in the `output/` directory. This also automatically builds the TailwindCSS.
```bash
make html
```

### Clean Output
Removes the `output/` directory.
```bash
make clean
```

### Regenerate on File Changes
Watches for changes and regenerates files automatically.
```bash
make regenerate
```

### Serve Locally
Builds and serves the site at `http://localhost:8000` with live reload.
```bash
make serve
```

### Serve Globally
Serves the site accessible on your network.
```bash
make serve-global
```

### Development Server
Development mode with auto-reload for both content and theme changes. Uses `development_pelicanconf.py`.
```bash
make devserver
```

### Development Server (Global)
Development server accessible on your network.
```bash
make devserver-global
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

### Sync Output to AWS
Syncs the `output/` directory to the configured S3 bucket using s3cmd with MD5 checksums.
```bash
make sync-output
```

### Sync Content to AWS
Syncs content to the Obsidian backup bucket.
```bash
make sync-content
```

### Sync All to AWS
Syncs both the output and content to AWS S3.
```bash
make sync-to-aws
```

### Sync from AWS
Syncs content from the Obsidian S3 bucket back to the local `content/` directory.
```bash
make sync-content-from-aws
```
