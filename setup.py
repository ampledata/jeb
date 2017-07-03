#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
JEB: Just Enough Blog Python Setup File.

Source:: https://github.com/ampledata/jeb
"""

import os
import setuptools
import sys

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Creative Commons Attribution 3.0 Unported License'


packages = ['jeb']
requires = ['jinja2', 'markdown', 'PyRSS2Gen']


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    version='2.0.0b1',
    name='jeb',
    description='JEB: Just Enough Blog',
    author='Greg Albrecht',
    author_email='oss@undef.net',
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
