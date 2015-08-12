from biObject import *
import re

class biID(biObject):
    'bI identifier type'
    def __init__(self, val):
        if type(val) == type(''):
            if re.match(r'[a-zA-Z_][a-zA-Z0-9_]*',val):
                self.value = val
            else:
                raise ValueError('%s not match ID format'%val)
        else:
            raise TypeError(val)
    def __str__(self):
        return 'id:%s'%self.value
    def py(self):
        return self.value

if __name__ == '__main__':
    O = biID('Azaza') ; print O, O.py()
    O = biID('+123') ; print O, O.py()
    O = biID(+123) ; print O, O.py()
