#!/usr/bin/python3
"""
read_file: function that reads text file in UTF-8 encoding
and prints out to stdout
filename: filename to be read

"""


def read_file(filename=""):
    """ a function that prints to stdout"""

    with open(filename, encoding="utf-8") as filename:
        print(filename.read())
