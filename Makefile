# Makefile to copy just the application stuff to the project subdirectory.

SHELL = /usr/bin/bash

build: 
	docker build -t characterbible -f project/Dockerfile .

run: build
	docker run -d --rm -p 8000:8000 -v $(PWD)/project/data:/data --name characterbible characterbible

test:
	pytest

