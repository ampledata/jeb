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
