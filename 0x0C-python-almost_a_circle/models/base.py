#!/usr/bin/python3

"""
A module that defines a class
"""
from json import dumps, loads
"""from os.path import isfile
import csv
import turtle
from random import randint, sheffle, randrange"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method that returns JSON which represent a list dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return dumps([])
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save JSON string rep to a file"""
        if list_objs is None:
            dict_list = []
        else:
            dict_list = [i.to_dictionary() for i in list_objs]
        fname = "{}.json".format(cls.__name__)
        with open(fname, "w") as f:
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Getter method function
        """
        if json_string is None or json_string == "":
            return []
        else:
            return loads(json_string)
