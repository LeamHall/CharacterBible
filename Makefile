# Makefile to copy just the application stuff to the docker subdirectory.

SHELL = /usr/bin/bash

copy:
	#if [ ! -d "docker/app" ]
	#then
	#	mkdir -p docker/app
	#fi

	- mkdir -p docker/app
	- mkdir -p docker/data
	cp -Rp Dockerfile docker
	cp -Rp requirements.txt docker
	cp -Rp main.py docker
	cp -Rp sample.cfg docker
	cp -Rp data/people.db docker/data
	cp -Rp character_bible.py docker/app
	cp -Rp person docker/app
	cp -Rp datamine docker/app
	cp -Rp view docker/app

build: copy
	docker build -t characterbible -f docker/Dockerfile .

run: build
	docker run -it --rm -p 8000:8000 -v $(PWD)/docker/data:/data --name characterbible characterbible

