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
        if (size <= 0):
            raise ValueError("width must b > 0")

        self.width = size
        self.height = size
