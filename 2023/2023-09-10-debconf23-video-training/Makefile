presentation.html: slides.md config.cfg
	darkslide --mod=wide16x9 config.cfg -i

.PHONY: watch
watch:
	darkslide --mod=wide16x9 config.cfg -w -d /tmp/presentation.html

.PHONY: clean
clean:
	rm presentation.html
