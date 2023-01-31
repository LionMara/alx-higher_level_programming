#!/usr/bin/python3

"""
Function returns true if object is an
instance of a class that inherited
from specified class
obj: object
a_class: class

"""


def inherits_from(obj, a_class):
    """Checks for inheritance"""

    if type(obj) is a_class:
        return True

    else:
        return  False
