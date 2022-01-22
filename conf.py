import os
import sys


sys.path.insert(0, os.path.abspath("."))

project = "Schlockchain"
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
]
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None)
}
myst_url_schemes = ["http", "https", ]
