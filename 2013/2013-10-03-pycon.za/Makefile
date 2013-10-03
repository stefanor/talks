include /usr/include/LaTeX.mk

talk.pdf: body.tex

body.tex: outline.otl
	./otl_beamer.py $^ > $@

.PHONY: run
run: talk.pdf
	impressive -c persistent -g 1024x768 -q -T 200 $^

.PHONY: preview
preview: talk.pdf
	xdg-open $<
