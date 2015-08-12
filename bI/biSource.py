from biObject import *
import pyparsing as pyp

class biSource(biObject):
    'bI source file'
    def __init__(self, name):
        self.FileName = name
        if type(name) == type(''):
            self.handler = open(name, 'r')
        else:
            raise TypeError(type(name))
    def __str__(self):
        return 'source(\'%s\')' % self.FileName
    def py(self):
        return self.__class__.__name__ + '(\'%s\')' % self.FileName
    def parse(self):
        self.dat=[]
        return self.dat

if __name__ == '__main__':
    O = biSource('nul') ; print O, O.py()
    O = biSource(123) ; print O, O.py()
