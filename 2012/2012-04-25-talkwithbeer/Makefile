LANDSLIDE = ~/git/landslide/src/landslide/main.py

all: presentation.html

presentation.html: index.rst config.cfg
	$(LANDSLIDE) config.cfg

preview: presentation.html
	x-www-browser $^
