#!/usr/bin/python3

"""
A function that returns true if an object is an
instance  of, or an object is an instance of a
class
obj: object
a_class: class

"""


def is_kind_of_class(obj, a_class):
    """ checks for instance and class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
