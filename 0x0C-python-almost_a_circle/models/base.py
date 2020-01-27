#!/usr/bin/python3
"""
creation on a class base with a constructor
"""


import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """initial constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns a new list in form of string"""
        new_str = "[]"
        if list_dictionaries is None:
            return new_str
        else:
            return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """writes the json string representations o a list"""
        str_new = []
        if list_objs is None:
            return str_new
        else:

        with open(filename, 'w', encoding='utf-8') as file:
            return file.write(json.dumps())
