#!/usr/bin/python3

''' Importing Base '''
from models.base import Base


class Rectangle(Base):
    ''' Class rectangle that inherits from Class Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor for Rectangle '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Setter for width'''
        self.__width = width

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Setter for height'''
        self.__height = height

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Setter for x'''
        self.__x = x

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Setter for y'''
        self.__y = y
