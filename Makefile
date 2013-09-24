# Makefile for JEB: Just Enough Blog.
#
# Author:: Greg Albrecht <gba@gregalbrecht.com>
# Copyright:: Copyright 2012 Greg Albrecht
# License:: Creative Commons Attribution 3.0 Unported License
# Source:: https://github.com/ampledata/jeb
#


.DEFAULT_GOAL := all

all: install_requirements develop

develop:
	python setup.py develop

install:
	python setup.py install

install_requirements:
	pip install -r requirements.txt --use-mirrors

clean:
	rm -rf *.egg* build dist *.py[oc] */*.py[co] cover doctest_pypi.cfg \
	 	nosetests.xml pylint.log *.egg output.xml flake8.log tests.log \
		test-result.xml htmlcov fab.log

lint:
	pylint -f colorized -i y -r n jeb/*.py tests/*.py *.py

pep8:
	flake8

flake8:
	flake8 --exit-zero  --max-complexity 12 jeb/*.py tests/*.py *.py | \
		awk -F\: '{printf "%s:%s: [E]%s\n", $$1, $$2, $$3}' | tee flake8.log

publish:
	python setup.py register sdist upload

nosetests:
	python setup.py nosetests

uninstall:
	pip uninstall -y jeb

test: install_requirements lint clonedigger flake8 nosetests
