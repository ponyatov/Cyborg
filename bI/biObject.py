class biObject:
    'bI generic object'
    def py(self):
        return self.__class__.__name__ + '()'
    def __str__(self):
        return self.py()

if __name__ == '__main__':
    print biObject()
