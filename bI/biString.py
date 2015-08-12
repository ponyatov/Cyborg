from biObject import *

class biString(biObject):
    'bI striing type'
    def __init__(self, val):
        self.value=str(val)
    def __str__(self):
        return '"%s"'%self.value
    def py(self):
        return '"%s"'%self.value

if __name__ == '__main__':
    O = biString('Azaza') ; print O, O.py()
    O = biString('+123') ; print O, O.py()
    O = biString(+123) ; print O, O.py()
