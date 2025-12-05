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
│   └── content/            # Actual content directory (configured in pelicanconf.py)
├── theme/                  # Custom Pelican theme
│   ├── static/             # Static assets (CSS, JS, Images)
│   └── templates/          # Jinja2 templates
├── tools/                  # Custom Python scripts/filters
├── output/                 # Generated static site (ignored in git)
├── documentation/          # Project documentation
├── Makefile                # Build automation commands
├── pelicanconf.py          # Main Pelican configuration
├── tasks.py                # Invoke tasks (alternative to Makefile)
├── Pipfile & Pipfile.lock  # Python dependencies
└── package.json            # Node.js dependencies
```

## Key Features

-   **Custom Theme**: Built from scratch using TailwindCSS.
-   **Obsidian Integration**: Content structure is designed to work with Obsidian, syncing via AWS S3.
-   **Automated Build**: Makefile handles CSS compilation and site generation.
