#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CLI methods for JEB."""

import glob
import sys

import jeb

__author__ = "Greg Albrecht <oss@undef.net>"
__copyright__ = "Copyright Greg Albrecht https://ampledata.org"
__license__ = "Apache License, Version 2.0"


def main():
    """Reads in all article content and renders to HTML."""
    article_files = glob.glob("articles/*.md")
    articles = []
    for article_file in article_files:
        articles.append(jeb.generate_article_names(article_file))

    jeb.generate_articles(articles)
    jeb.generate_index(articles)
    jeb.generate_rss(articles)


if __name__ == "__main__":
    sys.exit(main())
