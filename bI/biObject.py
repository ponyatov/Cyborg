class biObject:
    'bI generic object'
    def __str__(self):
        'dump in human-readable form'
        return 'object'
    def py(self):
        'dump in Python syntax: object can be recreated by eval()'
        return self.__class__.__name__ + '()'
    def cpp(self):
        'dump in C++'
        return self.__class__.__name__ + '()'

if __name__ == '__main__':
    O = biObject()
    print 'str & bI:', O ##
    print 'py:', O.py()
    print 'c++:', O.cpp()
