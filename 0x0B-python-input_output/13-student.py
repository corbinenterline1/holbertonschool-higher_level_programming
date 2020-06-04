#!/usr/bin/python3
"""0x0B - 13 - Student to disk and reload"""


class Student:
    """Student class. Currently contains
    public instance attributes:
    first_name
    last_name
    age
    init present, to_json retrieves a dictionary representation
    of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """Initialization for Student class.

        Args:
            self
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json returns the dictionary description with simple
        data structure (list, dictionary, string, integer & boolean)
        for JSON serialization of an object.
        Args:
        obj: object whose dict we need (phrasing lol)
        """
        if type(attrs) is list and all(isinstance(s, str) for s in attrs):
            fild = {}
            for i in attrs:
                if self.__dict__.get(i):
                    fild[i] = self.__dict__[i]
            return fild
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json replaces all attributes of the Student instance.

        Args:
            self
            json: can be assumed to always be a dictionary

        Checks public attributes of Student against json dictionary.
        Updates as found.
        """
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
