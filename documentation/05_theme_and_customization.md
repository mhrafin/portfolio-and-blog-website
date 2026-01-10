# Theme and Customization

[← Back to Documentation Index](01_project_overview.md)

The project uses a custom Pelican theme located in the `theme/` directory.

## Theme Structure

```
theme/
├── static/
│   ├── css/
│   │   ├── input.css       # TailwindCSS source file
│   │   └── output.css      # Generated CSS (do not edit directly)
│   └── images/             # Theme images
└── templates/
    ├── base.html           # Base template with navigation and HTML skeleton
    ├── index.html          # Blog listing page (articles loop)
    ├── article.html        # Single article page with metadata display
    ├── page.html           # Static page template (e.g., Contact)
    ├── contact.html        # Custom contact page template
    ├── portfolio.html      # Landing/home page with hero section
    └── 404.html            # Custom 404 error page
```

## Styling (TailwindCSS)

Styling is handled by TailwindCSS v4.

-   **Source**: `theme/static/css/input.css`
-   **Output**: `theme/static/css/output.css`
-   **Configuration**: `package.json` defines the dependencies.

To modify styles:
1.  Edit `theme/static/css/input.css` or add Tailwind classes directly in HTML templates.
2.  Run `make build-css` to regenerate `output.css`.

## Templates

-   **`base.html`**: Contains the HTML skeleton, `<head>`, navigation bar, and footer. Defines blocks like `content`, `nav`, `head`, `head_scripts`, `style`, and `script` that other templates can override or extend.
-   **`portfolio.html`**: The home page (saved as `index.html`). Features a hero section with background image, social links, and recent posts section.
-   **`index.html`**: Lists blog posts (saved as `blogs.html`). Loops through `articles_page.object_list` to display article summaries.
-   **`article.html`**: Displays a single blog post with metadata (date, author, read time), cover image, and formatted content.
-   **`page.html`**: Template for static pages like Contact and Thank You.
-   **`contact.html`**: Custom contact page template.
-   **`404.html`**: Custom 404 error page for better user experience.

## Custom Filters

Custom Jinja2 filters are located in the `tools/` directory and registered in `pelicanconf.py`.

-   **`wrap_images`** (`tools/wrap_images.py`): Wraps `<img>` tags in styled containers for better presentation in article content.
-   **`no_img`** (`tools/no_img.py`): Extracts text content while removing images, useful for article summaries on the listing page.

These filters are registered in `pelicanconf.py`:
```python
JINJA_FILTERS = {
    "wrap_images": wrap_images,
    "no_img": no_img
}
```

### Usage in Templates

**In article.html:**
```jinja
{{ article.content | wrap_images | safe }}
```

**In index.html (for summaries):**
```jinja
{{ article.summary | no_img | safe }}
```
