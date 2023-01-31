#!/usr/bin/python3

'''
Class Base it will do
a bunch of stuff

'''


class Base():
    ''' This is the base of the project
        all the functions will stay here
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor for the base class '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
