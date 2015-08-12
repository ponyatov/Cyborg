from biObject import *
 
class biComment(biObject):
    'bI comment type'
    def __init__(self, val): self.value = val
    def __str__(self):
        return '//%s\n' % self.value
    def py(self):
        return '##%s\n' % self.value
 
if __name__ == '__main__':
     O = biComment('-456') ; print O, O.py()
     O = biComment(+123) ; print O, O.py()
