.DEFAULT_GOAL := all

all: init develop

init:
	@echo Bypassing install_requires...
	# install_requires

develop:
	python setup.py develop

install_requirements:
	pip install -r requirements.txt --use-mirrors

uninstall:
	pip uninstall jeb

clean:
	rm -rf *.egg* build dist *.py[oc] */*.py[co] cover doctest_pypi.cfg \
	 	nosetests.xml pylint.log *.egg output.xml flake8.log tests.log \
		test-result.xml htmlcov fab.log
