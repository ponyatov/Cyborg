
DOC = README.md
DOC += doc/index.html

PDF = doc/ru/Cyborg.pdf
TEX = doc/ru/doc.tex

SRC = bI/bI.py

bI += src/Project.bI
bI += src/Deploy.bI 

TMP = tmp/bI.log

all: $(DOC) $(PDF)

$(PDF): $(TEX)
	mkdir -p tmp/tex
	pdflatex -halt-on-error -output-directory tmp/tex $<

$(DOC): $(TMP) Makefile
$(TMP): $(SRC) $(bI) Makefile
	python bI/bI.py $(bI)
