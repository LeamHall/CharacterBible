# Makefile

SHELL = /usr/bin/bash

.PHONY:test
test:
	python -m unittest

clean:
	find . -type f -name "*.pyc" -exec rm {} \;
	find . -type f -name "*.swp" -exec rm {} \;

all: clean test
	coverage run -m unittest
	coverage report -m 
	python -m black -l79 .
	-flake8 --ignore E251,E266,W391


