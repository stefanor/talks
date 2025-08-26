#!/usr/bin/make -f

presentation.html: slides.md config.cfg
	darkslide --mod=wide16x9 config.cfg --embed

.PHONY: watch
watch:
	darkslide --mod=wide16x9 config.cfg -w -d /tmp/presentation.html
