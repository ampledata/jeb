#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CLI methods for JEB."""

import glob

import jeb

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Creative Commons Attribution 3.0 Unported License'


def main():
    """Reads in all article content and renders to HTML."""
    article_files = glob.glob('articles/*.md')
    articles = []
    for article_file in article_files:
        articles.append(jeb.generate_article_names(article_file))

    jeb.generate_articles(articles)
    jeb.generate_index(articles)
    jeb.generate_rss(articles)


if __name__ == '__main__':
    sys.exit(main())
