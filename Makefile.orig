# Makefile to copy just the application stuff to the project subdirectory.

SHELL = /usr/bin/bash

build: 
	docker build -t cb_app   -f project/Dockerfile .
	docker build -t cb_nginx -f project/Dockerfile.nginx .

run: build
	docker run -d --rm -v $(PWD)/project/data:/data --name cb_app --net=backend --ip=172.19.0.2  cb_app
	docker run -d --rm --name cb_nginx --net=frontend --ip=172.18.0.2  cb_nginx
 
test:
	pytest

stop:
	docker stop cb_nginx
	docker stop cb_app
