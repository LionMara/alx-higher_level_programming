#!/usr/bin/python3
"""
Class MYList that inherits from lists
it

"""


class MyList(list):
    """Prints the list """
    def print_sorted(self):
        print(sorted(self))
