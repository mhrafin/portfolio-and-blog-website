# Project Overview

This project is a static website generated using **Pelican**, a Python-based static site generator. It serves as a portfolio and blog website.

## Documentation Index

-   [Setup and Installation](02_setup_and_installation.md)
-   [Usage Guide](03_usage_guide.md)
-   [Deployment](04_deployment.md)
-   [Theme and Customization](05_theme_and_customization.md)
-   [Configuration](06_configuration.md)

## Tech Stack

-   **Static Site Generator**: [Pelican](https://getpelican.com/) (Python)
-   **Styling**: [TailwindCSS v4](https://tailwindcss.com/) & [Flowbite](https://flowbite.com/)
-   **Dependency Management**:
    -   Python: [Pipenv](https://pipenv.pypa.io/en/latest/)
    -   Node.js: `npm` (for TailwindCSS)
-   **Build System**: GNU Make
-   **Deployment**: AWS S3

## Directory Structure

```
.
├── content/                # Source content (Markdown files)
│   ├── content/            # Actual content directory (configured in pelicanconf.py)
│   ├── extra/              # Static files (robots.txt, google verification, etc.)
│   ├── images/             # Content images
│   ├── pages/              # Static pages (Contact, Thank You, etc.)
│   └── templates/          # Content templates (ignored by Pelican)
├── theme/                  # Custom Pelican theme
│   ├── static/             # Static assets (CSS, Images)
│   │   └── css/
│   │       ├── input.css   # TailwindCSS source
│   │       └── output.css  # Generated CSS
│   └── templates/          # Jinja2 templates
│       ├── base.html       # Base template with navigation
│       ├── index.html      # Blog listing page
│       ├── article.html    # Single blog post
│       ├── page.html       # Static page template
│       ├── portfolio.html  # Home/landing page
│       └── 404.html        # Custom 404 page
├── tools/                  # Custom Python scripts/filters
│   ├── wrap_images.py      # Filter to wrap images in containers
│   └── no_img.py           # Filter to extract text without images
├── output/                 # Generated static site (ignored in git)
├── cache/                  # Pelican build cache (ignored in git)
├── documentation/          # Project documentation (this folder)
├── Makefile                # Build automation commands
├── pelicanconf.py          # Main Pelican configuration
├── development_pelicanconf.py  # Development configuration
├── publishconf.py          # Production configuration
├── tasks.py                # Invoke tasks (alternative to Makefile)
├── Pipfile & Pipfile.lock  # Python dependencies
└── package.json            # Node.js dependencies (TailwindCSS)
```

## Key Features

-   **Custom Theme**: Built from scratch using TailwindCSS v4 and Flowbite components.
-   **Custom Portfolio Landing Page**: Dedicated home page with hero section and recent posts.
-   **Blog System**: Separate blog listing and individual article pages with custom styling.
-   **Custom Jinja2 Filters**: Image wrapping and text extraction filters for flexible content display.
-   **Markdown Extensions**: Support for code highlighting, pymdownx.mark, and other extensions.
-   **Obsidian Integration**: Content structure designed to work with Obsidian, syncing via AWS S3.
-   **Automated Build**: Makefile handles CSS compilation and site generation.
-   **SEO Optimization**: Automatic sitemap generation and meta tags for improved search engine indexing.
-   **Read Time Estimation**: Automatic reading time calculation for articles.
-   **Build Caching**: Content caching for improved build performance.
-   **Custom 404 Page**: Custom error page for better user experience.
