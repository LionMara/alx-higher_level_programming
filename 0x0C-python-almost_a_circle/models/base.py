#!/usr/bin/python3

'''
Class Base it will do
a bunch of stuff

'''

class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = ++__nb_objects
