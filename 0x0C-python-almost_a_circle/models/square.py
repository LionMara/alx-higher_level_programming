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
            self.id, self.x, self.y, self.height)
