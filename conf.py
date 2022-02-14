import os
import sys
import sphinx_bootstrap_theme


sys.path.insert(0, os.path.abspath("."))

# project = "Schlockchain"
project = "My Awesome Site"
copyright = "2022, Michael B <gloc.mike@hey.com>"
author = "Michael B <gloc.mike@hey.com>"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv"]
html_static_path = ["_static"]
templates_path = ["_templates"]
myst_enable_extensions = [
    "colon_fence",
    "substitution",
]
myst_substitutions = {
    "snippet": "I'm a **substitution**"
}

intersphinx_mapping = {"sphinx": ("https://www.sphinx-doc.org/en/master/", None)}
myst_url_schemes = [
    "http",
    "https",
]

html_theme = "alabaster"
# Alabaster sidebars
html_sidebars = {
  '**': [
    "about.html",
    "navigation.html",
    "relations.html",
    "luv_sphinx.html",
    "searchbox.html",
    "donate.html",
  ]
}

html_title = "LOL, It's a Nice Site"

# To add a logo above the sidebar
html_logo = "_static/python-logo-generic.svg"

# If adding your own CSS styling
html_css_files = ["my_custom.css"]

# Sphinx Book sidebars
# html_sidebars = {"**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]}
# html_theme = "sphinx_book_theme"

# Bootstrap Theme
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Bootstrap Theme
# html_theme = 'furo'
