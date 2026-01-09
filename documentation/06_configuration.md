# Configuration

The main configuration file is `pelicanconf.py`.

## Key Settings

-   **`AUTHOR`**: Site author name (`'Mahedi Hassan Rafin'`).
-   **`SITENAME`**: Website title (`'Raf'`).
-   **`SITEURL`**: Production site URL (`'https://mhrafin.dev'`).
-   **`PATH`**: Source content directory (`'content'`).
-   **`THEME`**: Path to the theme directory (`'theme'`).
-   **`TIMEZONE`**: Site timezone (`'Europe/Rome'`).
-   **`DEFAULT_LANG`**: Default language code (`'en'`).

## Content Settings

-   **`STATIC_PATHS`**: Directories to copy as-is (`['images', 'extra']`).
-   **`EXTRA_PATH_METADATA`**: Maps files from extra/ to site root:
    ```python
    EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/googleaeadac67107de018.html': {'path': 'googleaeadac67107de018.html'}
    }
    ```
-   **`IGNORE_FILES`**: Patterns to ignore (`['.#*', '__pycache__', '*.pyc', '.DS_Store', '.obsidian', 'templates/*']`).
-   **`PAGE_EXCLUDES`**: Directories to exclude from pages (`["templates", ".obsidian", "extra"]`).
-   **`ARTICLE_EXCLUDES`**: Directories to exclude from articles (`["templates", ".obsidian", "extra"]`).

## URL Settings

-   **`INDEX_SAVE_AS`**: `'blogs.html'` - The blog index is saved as `blogs.html`.
-   **`ARTICLE_URL`**: `'blog/{slug}.html'` - URL pattern for articles.
-   **`ARTICLE_SAVE_AS`**: `'blog/{slug}.html'` - Articles are saved under `blog/` with their slug.
-   **`TEMPLATE_PAGES`**: Maps custom templates to output files:
    ```python
    TEMPLATE_PAGES = {
        'portfolio.html': 'index.html',  # Custom landing page
        '404.html': '404.html',          # Custom 404 page
    }
    ```

## Plugins and Filters

-   **`JINJA_FILTERS`**: Registers custom filters from `tools/`:
    ```python
    JINJA_FILTERS = {
        "wrap_images": wrap_images,  # Wraps images in styled containers
        "no_img": no_img             # Extracts text without images
    }
    ```

-   **`PLUGINS`**: List of enabled Pelican plugins:
    ```python
    PLUGINS = ['sitemap', 'readtime']
    ```
    - `sitemap` - Generates an XML sitemap for SEO
    - `readtime` - Calculates reading time for articles

## Markdown Configuration

-   **`MARKDOWN`**: Markdown processing settings:
    ```python
    MARKDOWN = {
        'extensions': [
            'markdown.extensions.codehilite',  # Code syntax highlighting
            'markdown.extensions.extra',       # Extra features (tables, etc.)
            'markdown.extensions.meta',        # Metadata support
            'pymdownx.mark',                   # Highlighting/marking text
        ],
        'extension_configs': {
            'markdown.extensions.codehilite': {'css_class': 'highlight'},
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
            'pymdownx.mark': {},
        },
        'output_format': 'html5',
    }
    ```

### Sitemap Configuration

-   **`SITEMAP`**: Configuration for the sitemap plugin:
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

## Build Performance

-   **`CACHE_CONTENT`**: `True` - Enables content caching for faster builds.
-   **`LOAD_CONTENT_CACHE`**: `True` - Loads cached content from previous builds.
-   **`CHECK_MODIFIED_METHOD`**: `'mtime'` - Uses file modification time to detect changes.
-   **`CONTENT_CACHING_LAYER`**: `'reader'` - Caches at the reader level.

## Feed Settings

-   **`FEED_ALL_ATOM`**: `None` - Disables Atom feed generation (typically for development).
-   **`CATEGORY_FEED_ATOM`**: `None`
-   **`TRANSLATION_FEED_ATOM`**: `None`
-   **`AUTHOR_FEED_ATOM`**: `None`
-   **`AUTHOR_FEED_RSS`**: `None`

## Pagination

-   **`DEFAULT_PAGINATION`**: `10` - Number of articles per page.
    ```

## Exclusions

-   **`PAGE_EXCLUDES`** & **`ARTICLE_EXCLUDES`**: Directories to ignore (e.g., `templates`, `.obsidian`).
