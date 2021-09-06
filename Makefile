# run:
# 	python3 -m venv venv
#  	./venv/bin/pip install -r requirements.txt
# .ONESHELL:

.PHONY: getwallpapers_env
getwallpapers_env:
	if ! [ -d "venv" ]; then python3 -m venv venv; fi
	source venv/bin/activate;
	pip3 install -r requirements.txt;
	bash

.PHONY: getwallpapers_test
getwallpapers_test:
	python3 -m unittest tests/*
