# Theme and Customization

The project uses a custom Pelican theme located in the `theme/` directory.

## Theme Structure

```
theme/
├── static/
│   └── css/
│       ├── input.css       # TailwindCSS source file
│       └── output.css      # Generated CSS (do not edit directly)
└── templates/
    ├── base.html           # Base template extended by others
    ├── index.html          # Blog index page (list of articles)
    ├── article.html        # Single article page
    └── portfolio.html      # Landing page (custom template)
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

-   **`base.html`**: Contains the HTML skeleton, `<head>`, navigation, and footer. Defines blocks like `content` that other templates fill.
-   **`portfolio.html`**: The home page. It likely contains custom layout for the portfolio showcase.
-   **`index.html`**: Lists blog posts. Loops through `articles`.
-   **`article.html`**: Displays a single blog post.

## Custom Filters

Custom Jinja2 filters are located in the `tools/` directory and registered in `pelicanconf.py`.

-   **`wrap_images`**: Wraps `<img>` tags in a container for styling.
-   **`no_img`**: Likely extracts text content without images.

These are added to `JINJA_FILTERS` in `pelicanconf.py`.
