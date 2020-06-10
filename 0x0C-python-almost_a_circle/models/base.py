#!/usr/bin/python3
"""0x0C - Almost a circle.
Constructor for class Base."""
import json


class Base:
    """Base class for almost a circle project. Currently contains
    a constructor & a private class attribute __nb_objects. The goal
    is to manage id attribute in all future classes & avoid duplicating
    same code (by extension, same bugs).
    Attributes:
        __nb_objects = number of objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor.

        Args:
            self: lfes
            id: If id is not None, assign the public istance attribute id with
            this value. id is assumed to be an integer(no test needed).
            Otherwise, increment __nb_objects & assign the new value
            to the public instance attribute id."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries:
        the name is apt.
        if it's none or empty, return string: "[]"
        Otherwise, return the json string rep of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
        to a file.
        list_objs is a list of instances who inherits of Base. Aka,
        list of Rectangles or list of Square instances.
        If list_objs is None, save an empty list
        Filename format: <Class name>.json"""
        fn = str(cls.__name__) + '.json'    # FileName
        lsd = []    # LiSt of Dictionaries(representing objects)
        if list_objs is None:
            with open(fn, 'w') as jf:
                jf.write("[]")    # empty list saved to file
        for obj in list_objs:   # making list of dictionaries
            lsd.append(obj.to_dictionary())
        jslsd = Base.to_json_string(lsd)    # serializing list (to_json)
        with open(fn, 'w') as jf:
            jf.write(jslsd)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        json_string is a string representing a list of dictionaries
        if json_string is None, or empty, return an empty list."""
        ls = []
        if json_string is None or not json_string:
            return ls
        else:
            ls = json.loads(json_string)
            return ls

    @classmethod
    def create(cls, **dictionary):  # ** for unpacking list of dicts
        """returns an instance with all attributes already set.
        Creates dummy instance before, then calls update instance method
        to apply real values to "dummy" instance."""
        if not dictionary:
            return None
        if cls.__name__ == 'Rectangle':
            dum = cls(1, 1)  # width, height req. for rectangle
            dum.update(**dictionary)    # update dummy usin update classmeth
            return dum
        if cls.__name__ == 'Square':
            dum = cls(1)    # size
            dum.update(**dictionary)
            return dum

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from file. Returns
        empty list if feile doesn't exist."""
        fn = str(cls.__name__) + '.json'
        lsi = []    # LiSt of instances

        with open(fn) as f:  # hopefully catches no file, if not try block
            for line in f:
                lsd = Base.from_json_string(line)   # lsd is list of dicts
            for objs in lsd:
                lsi.append(cls.create(**objs))  # see why Base.create was funk
        return lsi
