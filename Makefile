# Makefile to copy just the application stuff to the docker subdirectory.

SHELL = /usr/bin/bash

copy:
	#if [ ! -d "docker/app" ]
	#then
	#	mkdir -p docker/app
	#fi
	cp -Rp Dockerfile docker
	cp -Rp requirements.txt docker
	cp -Rp main.py docker
	cp -Rp data docker/app
	cp -Rp character_bible.py docker/app
	cp -Rp person docker/app
	cp -Rp datamine docker/app
	cp -Rp view docker/app

build: copy
	docker build -t characterbible -f docker/Dockerfile .

run: build
	docker run -it --rm -p 8000:8000 -v $(pwd)/docker/data:/data --name characterbible characterbible

