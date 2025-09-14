AUTHOR = 'Mahedi Hassan Rafin'
SITENAME = 'Raf'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


THEME = "theme"

THEME_STATIC_DIR = 'static'

THEME_STATIC_PATHS = ['static']

INDEX_SAVE_AS = 'blogs.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

TEMPLATE_PAGES = {
    'portfolio.html': 'index.html',  # your custom landing page
}
