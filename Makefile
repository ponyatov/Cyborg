
DOC = README.md
DOC += doc/index.html

PDF = doc/Cyborg_ru.pdf
TEX = doc/ru/doc.tex doc/header.tex doc/ru/header.tex
TEX += doc/ru/about.tex

SRC = bI/bI.py
SRC += bI/biObject.py bI/biInt.py bI/biSource.py bI/biComment.py

bI += src/Project.bI
bI += src/Deploy.bI
TEX += bI/doc/bI.tex
TEX += bI/doc/comments.tex
TEX += bI/doc/int.tex bI/doc/float.tex bI/doc/string.tex

TMP = tmp/bI.log

all: $(DOC) $(PDF)

.PHONY: pdf
pdf: $(PDF)
TEXTMP = tmp/tex
$(PDF): $(TEX)
	mkdir -p $(TEXTMP)
	pdflatex -halt-on-error -output-directory $(TEXTMP) $<
	pdflatex -halt-on-error -output-directory $(TEXTMP) $<
	cp $(TEXTMP)/doc.pdf $(PDF)

$(DOC): $(TMP) Makefile
$(TMP): $(SRC) $(bI) Makefile
	python bI/bI.py $(bI)

.PHONY: bI
bI:
	python bI/bI.py $(bI)
