#!/usr/bin/python3
"""Module to check class or inherit from """


def is_kind_of_class(obj, a_class):
    """Function to check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj: Object to compare
        a_class: Class toc ompare object to
        """
    if isinstance(obj, a_class):
        return True
    else:
        return False
