.PHONY: all
all: $(patsubst %.ps,%-full.png,$(wildcard *.ps)) $(patsubst %.ps,%-crop.png,$(wildcard *.ps))

%.pdf: %.ps
	ps2pdf $^

%-full.png: %.pdf
	inkscape --pdf-poppler -b white -o $@ -w 1280 $^

%-crop.png: %.pdf
	inkscape --pdf-poppler -b white -o $@ -d 144 --export-area=45:0:898:480 $^

.PHONY: clean
clean:
	rm -f *.pdf *.png
