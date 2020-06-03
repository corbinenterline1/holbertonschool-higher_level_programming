#!/usr/bin/python3
"""0x0A - 2 - Exact same object"""


def is_same_class(obj, a_class):
    """Function to check class of object against a class.
    Returns True if the object is exactly an instance of the
    specified class; otherwise False. Pythonic-ized!

    Args:
        obj: Object to compare
        a_class: Class to compare object to.
        """
    return (type(obj) == a_class)
