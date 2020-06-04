#!/usr/bin/python3
"""0x0B - 10 - Class to JSON"""


def class_to_json(obj):
    """class_to_json returns the dictionary description with simple
    data structure (list, dictionary, string, integer & boolean)
    for JSON serialization of an object.

    Args:
        obj: object whose dict we need (phrasing lol)
        """
    return obj.__dict__
