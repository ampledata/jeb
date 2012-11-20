#!/usr/bin/env python
"""JEB: Just Enough Blog Python Setup File."""

__author__ = 'Greg Albrecht <gba@gregalbrecht.com>'
__copyright__ = 'Copyright 2012 Greg Albrecht'
__license__ = 'Apache License 2.0'


import setuptools


setuptools.setup(
    version='1.0.0',
    name='jeb',
    description='JEB: Just Enough Blog',
    author='Greg Albrecht',
    author_email='gba@gregalbrecht.com',
    license='Apache License 2.0',
    url='https://github.com/ampledata/jeb',
    entry_points={'console_scripts': ['jeb = jeb:main']},
    install_requires=['jinja2', 'markdown', 'PyRSS2Gen']
)
