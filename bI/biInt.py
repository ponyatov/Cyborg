from biObject import *

class biInt(biObject):
    'bI int type'
    def __init__(self, val):
        if type(val) == type(0):
            self.value = val
        elif type(val) == type(''):
            self.value = int(val)
        else:
            raise TypeError(val.__class__.__name__)
    def __str__(self):
        return '%s' % self.value
    def py(self):
        return self.__class__.__name__ + '(%s)' % self.value

if __name__ == '__main__':
    O = biInt(+123) ; print O, O.py()
    O = biInt('-456') ; print O, O.py()
    O = biInt(7.89) ; print O, O.py()  # # no int(float) constructor
