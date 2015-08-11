
DOC = README.md
DOC += doc/index.html

PDF = doc/Cyborg.pdf
TEX = doc/doc.tex

SRC = bI/bI.py

bI += src/Project.bI
bI += src/Deploy.bI 

TMP = tmp/bI.log

all: $(DOC) $(PDF)

$(PDF): $(TEX)
	mkdir -p tmp/tex
	pdflatex -output-directory tmp/tex $<

$(DOC): $(TMP) Makefile
$(TMP): $(SRC) $(bI) Makefile
	python bI/bI.py $(bI)
