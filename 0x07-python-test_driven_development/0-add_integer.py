#!/usr/bin/python3

"""
* add_integer adds two values and returns the sum
* both the values must be integers or floats
* if they're floats, they have to be casted

"""


def add_integer(a, b=98):

    """adds two ints """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    

    return int(a) + int(b)
