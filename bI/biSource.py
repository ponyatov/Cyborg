from biObject import *
from biComment import *
from biID import *
from biString import *
import pyparsing as pp
import re

class biSource(biObject):
    'bI source file'
    def __init__(self, name):
        self.FileName = name
        if type(name) == type(''):
#             self.handler = open(name, 'r')
            self.log = open(name + '.log', 'w')
        else:
            raise TypeError(type(name))
        print >> self.log, self, '\n\n', self.parse()
    def __str__(self):
        return 'source(\'%s\')' % self.FileName
    def py(self):
        return self.__class__.__name__ + '(\'%s\')' % self.FileName
    comment = pp.Regex('//[^\n]*').\
        setParseAction(lambda a,b,c:biComment(c[0]))
    id = pp.Regex(r'[a-zA-Z_][a-zA-Z0-9_]*').\
        setParseAction(lambda a,b,c:biID(c[0]))
    op = pp.Word('+-*/^=&|^!:~')
    lb = pp.Word('([{')
    rb = pp.Word(')]}')
    str = (\
        pp.QuotedString('"',multiline=True)^\
        pp.QuotedString("'",multiline=True)).\
            setParseAction(lambda a,b,c:biString(c[0]))
    parser = pp.OneOrMore(comment ^ id ^ op ^ lb ^ rb ^ str) 
    def parse(self):
        T=''
        for i in self.parser.parseFile(self.FileName):#,parseAll=True)
            T+='%s\n'%i 
        return T
#         return self.parser.parseString(self.handler.read())

if __name__ == '__main__':
    O = biSource('nul') ; print O, O.py()
    O = biSource(123) ; print O, O.py()
