#!/usr/bin/python3
""" json module - JavaScript oBJECT nOTATION """

import json

"""
save_to_json_file: function tha writes an object
to file using JSON rep'n

"""


def save_to_json_file(my_obj, filename):
    """ adds json objects to json file """

    json_obj = json.dumps(my_obj)

    with open(filename, mode="a", encoding="utf-8") as my_file:
        my_file.write(json_obj)
