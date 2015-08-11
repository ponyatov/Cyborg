
DOC = README.md
DOC += doc/index.html

PDF = doc/ru/Cyborg.pdf
TEX = doc/ru/doc.tex doc/header.tex doc/ru/header.tex
TEX += doc/ru/about.tex
TEX += bI/doc/bI.tex

SRC = bI/bI.py

bI += src/Project.bI
bI += src/Deploy.bI 

TMP = tmp/bI.log

all: $(DOC) $(PDF)

.PHONY: pdf
pdf: $(PDF)
$(PDF): $(TEX)
	mkdir -p tmp/tex
	pdflatex -halt-on-error -output-directory tmp/tex $<

$(DOC): $(TMP) Makefile
$(TMP): $(SRC) $(bI) Makefile
	python bI/bI.py $(bI)

.PHONY: bI
bI:
	python bI/bI.py $(bI)
