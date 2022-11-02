#!/usr/bin/python3

""" json module - JavaScript Object Notation """

import json

"""
returns an object rep'd by a JSON string
my_str: JSON string to be convrted

"""


def from_json_string(my_str):
    """ returns a python data structure """

    return json.loads(my_str)
