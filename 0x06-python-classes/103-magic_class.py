#!/usr/bin/python3
"""
dis: dissassembly of python code
math: math module

"""
import dis
import math


"""
class MagicClass computes area and circumfrerence
of a given radius.
public class: area
public class: circumference
"""


class MagicClass:
    """computes area and circumference"""

    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
