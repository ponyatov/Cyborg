# bI language interpreter in Python2
 
import os, sys, time, re
 
print time.localtime()[:6], sys.argv

from biSource import *

if len(sys.argv)==1:
    sys.argv+=['../src/Project.bI','../src/Deploy.bI']
for i in sys.argv[1:]:
    S = biSource(i)
    print S, S.py(), S.parse()
