from biObject import *

class biInt(biObject):
    'bI int type'
    def __init__(self, int):
        self.val = int
    def py(self):
        return self.__class__.__name__ + '(%s)' % self.val

if __name__ == '__main__':
    print biObject().py()
    print biInt(123).py()
