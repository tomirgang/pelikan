AUTHOR = 'Tom'
SITENAME = "Tom's Blog"
SITEURL = 'https://tomirgang.de'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enalbe theme
THEME = 'blue-penguin-dark'

FAVICON = 'images/logo.png'

# Search settings
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "article"

# Theme settings

# Site Logo
SITELOGO = 'images/logo.png'

# HTML metadata
SITEDESCRIPTION = 'Toms Blog'

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Kategorien', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archiv', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
