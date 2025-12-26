
import sys
sys.path.append('./tools')

from wrap_images import wrap_images
from no_img import no_img





JINJA_FILTERS ={"wrap_images": wrap_images,
                "no_img": no_img} 

AUTHOR = 'Mahedi Hassan Rafin'
SITENAME = 'Raf'
SITEURL = "https://mhrafin.dev"

# Tell Pelican where to find content
PATH = 'content'

# Ignore template files and other non-content files
IGNORE_FILES = [
    '.#*',
    '__pycache__',
    '*.pyc',
    '.DS_Store',
    '.obsidian',
    'templates/*',  # Ignore template directory entirely
]

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

STATIC_PATHS = ['images', 'extra']

# This is the key part - it moves files from 'extra' to your site root
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/googleaeadac67107de018.html': {'path': 'googleaeadac67107de018.html'}
}


PAGE_EXCLUDES = ["templates", ".obsidian", "extra"]

ARTICLE_EXCLUDES = ["templates", ".obsidian", "extra"]


THEME = "theme"

THEME_STATIC_DIR = 'static'

THEME_STATIC_PATHS = ['static']

INDEX_SAVE_AS = 'blogs.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

TEMPLATE_PAGES = {
    'portfolio.html': 'index.html',  # your custom landing page
    '404.html': '404.html',  # custom 404 page
}

# Cache settings for improved build performance
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CONTENT_CACHING_LAYER = 'reader'

# Sitemap plugin configuration
PLUGINS = ['sitemap']

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
