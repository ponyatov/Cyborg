# bI language interpreter in Python 2.8

import os, sys, time, re

print time.localtime()[:6], sys.argv

log = sys.stdout # open('tmp/bI.log', 'w')

class bIsource:
    '''
    source file in bI language
    '''
    def __init__(self, FileName):
        print >> log, self.__class__, FileName
        self.FileName = FileName
        self.src = open(FileName, 'r')
        self.out = self.touchopen('tmp/' + FileName + '.out')
        print self.out
    def touchopen(self, FileName):
        '''
        create file with autocreate dir tree
        if filename has /-slashed dir tree component
        '''
        T = FileName.split('/')
        if len(T) > 1:
            D = ''
            for i in T[:-1]:
                D += '%s/' % i
                try:
                    os.mkdir(D[:-1])
                except:
                    pass
        return open(FileName,'w')

for SrcFileName in sys.argv[1:]:
    bIsource(SrcFileName)
