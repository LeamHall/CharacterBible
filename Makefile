# Makefile

SHELL = /usr/bin/bash

.PHONY:test
test:
	python -m unittest discover

clean:
	find . -type f -name "*.pyc" -exec rm {} \;
	find . -type f -name "*.swp" -exec rm {} \;

lint:
	-python -m black -l 79 .
	-flake8 --ignore E251,E266,W391
	-python -m pylint --recursive y --disable=C0209,C0116,R1734 .

coverage:
	coverage run -m unittest discover
	coverage report -m 

all: clean lint test coverage

