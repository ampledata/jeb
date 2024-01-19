#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate syntax highlighted articles from Markdown.

Derived from stefanB's blog post: http://bit.ly/H0qZ3O
"""

import datetime
import os
import shlex
import subprocess

import jinja2
import markdown
import PyRSS2Gen

__version__ = "3.0.0-beta1"
__author__ = "Greg Albrecht <oss@undef.net>"
__copyright__ = "Copyright Greg Albrecht https://ampledata.org"
__license__ = "Apache License, Version 2.0"


JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(["templates"]))

# TODO(gba@20121120) Move these constants out of jeb.py and into a conf or env
BLOG_TITLE = "Greg Albrecht's ampledata.org"
BLOG_URL = "https://ampledata.org/"
BLOG_DESCRIPTION = "If it has an IP, I've touched it."


def get_article_ts(article_file):
    """Get the git timestamp for the article file."""
    git_cmd = "git log --reverse --pretty=format:%aD"
    spc = subprocess.Popen(
        shlex.split(" ".join([git_cmd, article_file])), stdout=subprocess.PIPE
    )
    return spc.stdout.read().decode().split("\n")[0]


def generate_rss(articles):
    """Generate RSS feed of Blog Articles."""
    rss_items = []

    for article in articles:
        article_link = BLOG_URL + article["html_file"]

        rss_items.append(
            PyRSS2Gen.RSSItem(
                title=article["friendly_name"],
                link=article_link,
                guid=PyRSS2Gen.Guid(article_link),
                pubDate=get_article_ts(article["html_file"]),
            )
        )

    rss = PyRSS2Gen.RSS2(
        title=BLOG_TITLE,
        description=BLOG_DESCRIPTION,
        link=BLOG_URL,
        lastBuildDate=datetime.datetime.utcnow(),
        items=rss_items,
    )
    rss.write_xml(open("index.xml", "w", encoding="UTF-8"))


def generate_article_names(article_file):
    article = {}
    article["name"] = os.path.basename(os.path.splitext(article_file)[0])
    article["file"] = article_file
    article["html_file"] = ".".join([article["name"], "html"])
    article["friendly_name"] = article["name"].replace("_", " ")
    return article


def generate_index(articles):
    index_template = JINJA2_ENV.get_template("index.html")

    rendered_index = index_template.render(title=BLOG_TITLE, articles=articles)

    with open("index.html", "w", encoding="UTF-8") as index_fd:
        index_fd.write(rendered_index)


def generate_articles(articles):
    article_template = JINJA2_ENV.get_template("article.html")

    for article in articles:
        article_content = ""

        print(("in:", article["file"]))
        print(("out:", article["html_file"]))

        with open(article["file"], "r", encoding="UTF-8") as article_fd:
            article_content = article_fd.read()

        article_content = markdown.markdown(article_content, extensions=["codehilite"])

        rendered_article = article_template.render(
            title=article["friendly_name"], article_content=article_content
        )

        with open(article["html_file"], "w", encoding="UTF-8") as article_fd:
            article_fd.write(rendered_article)
