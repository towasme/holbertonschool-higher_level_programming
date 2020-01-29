#!/usr/bin/python3
"""
creation on a class base with a constructor
"""


import json


class Base:
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initial constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a new list in form of string"""
        new_str = "[]"
        if list_dictionaries is None:
            return new_str
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """method that returns a json string list"""
        new_str = []
        if json_string is None or json_string == []:
            return new_str
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representations o a list"""
        str_new = []
        if list_objs is None:
            with open(cls.__name__ + ".json", 'w', encoding='utf-8') as file:
                return file.write(cls.to_json_string(str_new))
        else:
            for obj in list_objs:
                new_dic = obj.to_dictionary()
                str_new.append(new_dic)
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as file:
            return file.write(cls.to_json_string(str_new))

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        new_list = []
        with open(cls.__name__ + ".json", 'w', encoding='utf-8') as file:
            if file is None:
                return new_list
            else:
                variable = cls.from_json_string(file.read())
                return