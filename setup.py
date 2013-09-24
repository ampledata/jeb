#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
JEB: Just Enough Blog Python Setup File.

Source:: https://github.com/ampledata/jeb
"""

__author__ = 'Greg Albrecht <gba@gregalbrecht.com>'
__copyright__ = 'Copyright 2012 Greg Albrecht'
__license__ = 'Creative Commons Attribution 3.0 Unported License'


import os
import sys

try:
    from setuptools import setup
except ImportError:
    # pylint: disable=F0401,E0611
    from distutils.core import setup

packages = ['jeb']
requires = ['jinja2', 'markdown', 'PyRSS2Gen']


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist upload')
        sys.exit()


publish()


setup(
    version='1.1.0',
    name='jeb',
    description='JEB: Just Enough Blog',
    author='Greg Albrecht',
    author_email='gba@gregalbrecht.com',
    url='https://github.com/ampledata/jeb',
    entry_points={'console_scripts': ['jeb = jeb.cli:main']},
    package_dir={'jeb': 'jeb'},
    packages=packages,
    long_description=open('README.rst').read(),
    package_data={'': ['LICENSE']},
    license=open('LICENSE').read(),
    install_requires=requires,
    zip_safe=False,
    include_package_data=True
)
