
DOC = README.md
DOC += doc/index.html

SRC = bI/bI.py

bI += src/Project.bI
bI += src/Deploy.bI 

TMP = tmp/bI.log

all: $(DOC)

$(DOC): $(TMP) Makefile
$(TMP): $(SRC) $(bI) Makefile
	python bI/bI.py $(bI)
