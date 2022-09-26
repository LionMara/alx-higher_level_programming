#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len1 = len(my_list) - 1
    while len1 >= 0:
        print("{:d}".format(my_list[len1]))
        len1 -= 1
