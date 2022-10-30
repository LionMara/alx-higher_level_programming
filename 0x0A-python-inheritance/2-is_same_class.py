#!/usr/bin/python3

"""
Returns True if object is an instance of
specified class
otherwise false

obj: object to be checked
a_class: cross-reference against

"""

def is_same_class(obj, a_class):
    """function to check instance of class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
