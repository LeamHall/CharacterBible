# Makefile

SHELL = /usr/bin/bash

.PHONY:test
test:
	python -m unittest

clean:
	find . -type f -name "*.pyc" -exec rm {} \;
	find . -type f -name "*.swp" -exec rm {} \;

lint:
	-flake8 --ignore E251,E266,W391
	-python -m pylint --recursive y --disable=C0209,C0116,R1734 .

coverage:
	coverage run -m unittest
	coverage report -m 

all: clean lint test coverage

