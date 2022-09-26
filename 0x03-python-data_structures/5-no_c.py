#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    my_string = my_string.translate({ord(c): None for c in "cC"})
    return my_string
