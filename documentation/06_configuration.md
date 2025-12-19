# Configuration

The main configuration file is `pelicanconf.py`.

## Key Settings

-   **`AUTHOR`**: Site author name.
-   **`SITENAME`**: Website title.
-   **`PATH`**: Source content directory (set to `content/content`).
-   **`THEME`**: Path to the theme directory (`theme`).
-   **`TIMEZONE`**: Site timezone (e.g., `'Europe/Rome'`).
-   **`DEFAULT_LANG`**: Default language code (`en`).

## URL Settings

-   **`INDEX_SAVE_AS`**: `'blogs.html'` - The blog index is saved as `blogs.html`.
-   **`ARTICLE_SAVE_AS`**: `'blog/{slug}.html'` - Articles are saved under `blog/` with their slug.
-   **`TEMPLATE_PAGES`**: Maps custom templates to output files.
    -   `'portfolio.html': 'index.html'` - Renders the `portfolio.html` template as the site's root `index.html`.

## Plugins and Filters

-   **`JINJA_FILTERS`**: Registers custom filters from `tools/`.
    ```python
    JINJA_FILTERS = {
        "wrap_images": wrap_images,
        "no_img": no_img
    }
    ```

-   **`PLUGINS`**: List of enabled Pelican plugins.
    -   `sitemap` - Generates an XML sitemap for SEO

### Sitemap Configuration

-   **`SITEMAP`**: Configuration for the sitemap plugin.
    ```python
    SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.7,
            'indexes': 0.5,
            'pages': 0.6
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'weekly',
            'pages': 'monthly'
        }
    }
    ```

## Exclusions

-   **`PAGE_EXCLUDES`** & **`ARTICLE_EXCLUDES`**: Directories to ignore (e.g., `templates`, `.obsidian`).
