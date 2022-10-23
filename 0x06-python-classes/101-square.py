#!/usr/bin/python3
"""
class Square defines a square based on 6-square.py
private instance:  size
   * property getter: size
   * property setter: size
private instance attribute: position
  * property getter: position
  * property setter: position

public instance: area
public instance method: my_print

"""

class Square:
    """class Square does couple of things """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(size, value):
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
           not all([type(i) == int for i in value]):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def __repr__(self):
        return (self.get_str())
