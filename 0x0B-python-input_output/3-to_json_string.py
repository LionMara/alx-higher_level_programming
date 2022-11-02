#!/usr/bin/python3

""" json module enables usage of JavaScript Object Notation """

import json


"""
to_json_string: returns the JSON rep of a string
my_obj: obj to be transformed

"""


def to_json_string(my_obj):
    """ returns JSON rep'n of an object """

    return json.dumps(my_obj)
