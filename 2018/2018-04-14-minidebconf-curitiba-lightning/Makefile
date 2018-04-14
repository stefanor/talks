include /usr/include/LaTeX.mk

talk.pdf: body.tex

body.tex: outline.otl otl_beamer.py
	./otl_beamer.py $< > $@

.PHONY: ourclean
ourclean: clean
	rm -f talk.pdf.cache body.tex

.PHONY: run
run: talk.pdf
	impressive -c persistent -g 1280x720 -q -T 200 $^

.PHONY: preview
preview: talk.pdf
	xdg-open $<

.PHONY: projector
projector:
	xrandr --output eDP1 --output HDMI1 --auto --same-as eDP1
	xrandr --output eDP1 --scale-from 1280x720 --fb 1280x720

.PHONY: no-projector
no-projector:
	xrandr --output eDP1 --auto --scale-from 1920x1080 --output HDMI1 --off
