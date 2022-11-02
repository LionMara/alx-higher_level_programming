#!/usr/bin/python3
"""
append_write: function that appends to the end of a file
filename: filename to be apended to
text: text to be appended
"""


def append_write(filename="", text=""):
    """ appends a text """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        num_char = my_file.write(text)

    return num_char
