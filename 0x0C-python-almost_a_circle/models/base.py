#!/usr/bin/python3
'''moduls that are imported'''
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns JSON represenation of list_dictionaries '''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' savs json rep of Python to file'''

        for obj in list_objs:
            if obj.__class__.__name__ == 'Rectangle':
                filename = 'Rectangle.json'
            elif obj.__class__.__name__ == 'Square':
                filename = 'Square.json'

        if list_objs is None:
            with open(filename, "w") as fp:
                fp.write([])

        obj_list = []
        with open(filename, "w") as fp:
            for obj in list_objs:
                obj_string = obj.to_dictionary()
                obj_list.append(obj_string)
            list_dict = Base.to_json_string(obj_list)

            fp.write(list_dict)
