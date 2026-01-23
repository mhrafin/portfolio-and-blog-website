import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Production settings
# Override development settings for production deployment

# Production site URL (HTTPS)
SITEURL = 'https://mhrafin.dev'
RELATIVE_URLS = False

# Enable feeds for production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Clean output directory on production builds
DELETE_OUTPUT_DIRECTORY = True

# Disable caching for production to ensure fresh builds
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
