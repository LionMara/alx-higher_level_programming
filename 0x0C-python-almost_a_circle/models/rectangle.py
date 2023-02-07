#!/usr/bin/python3

''' Importing Base '''
from models.base import Base


class Rectangle(Base):
    ''' Class rectangle that inherits from Class Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor for Rectangle '''

        '''
        if (type(height) != int):
            raise TypeError("height must be an integer")
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Get the area of the rectangle'''
        return self.width * self.height

    def display(self):
        ''' outputs '#' of the rectangle '''

        w = self.width
        h = self.height
        x = self.x
        y = self.y

        for i in range(y):
            print('')

        for i in range(h):
            print(' '*x, end='')
            print('#'*w)

    def update(self, *args):
        '''updates values of using only args'''

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
