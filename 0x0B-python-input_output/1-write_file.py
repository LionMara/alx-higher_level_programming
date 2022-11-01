#!/usr/bin/python3

"""
write_file: writes a string to a file
returns number of files written
filename: file to written to
test: text to be written
"""


def write_file(filename="", text=""):
    """ returns number of chars """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        num_bytes = my_file.write(text)

    return num_bytes
