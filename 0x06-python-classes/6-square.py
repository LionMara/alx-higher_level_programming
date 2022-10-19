#!/usr/bin/python3
"""
class Square defined based on 5-square.
private instance attribute size with:
   * it has property size,
   * it has property setter self
private instance attribute positon
   * property getter position
   * property setter position
init instantiation
public instance method : area
public instance method : my_print

"""


class Square:
    """
    class Square does a couble of good stuff
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" "*self.__position[0] + "#"*self.__size)
