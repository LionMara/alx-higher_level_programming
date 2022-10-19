#!/usr/bin/python3
"""

Class Square defines a square based on 4-square.py
The class has a property and a property setter
"""


class Square:
    """
    class Square has a proprty and a setter
    it also contains public instance method area and my_print
    """
    def __init__(self, size=0):
        self.size = size

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

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#"*self.__size)
