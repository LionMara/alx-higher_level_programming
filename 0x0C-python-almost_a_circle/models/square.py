#!/usr/bin/python3
'''importing Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Class Square that inherits from class Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor class'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Str implementation'''

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, size):
        '''getter size'''

        if (type(size) != int):
            raise TypeError("width must be an integer")
        '''if (size <= 0):
            raise ValueError("width must b > 0")'''

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        ''' updates th square class '''

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
