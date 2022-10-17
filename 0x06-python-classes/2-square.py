#!/usr/bin/python3

"""
Class Square
the class makes a square with private instance size

"""


class Square:
    """ A class that defines square by size """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")

        self.__size = size
