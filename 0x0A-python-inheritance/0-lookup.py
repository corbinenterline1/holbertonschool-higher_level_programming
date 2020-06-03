#!/usr/bin/python3
"""Returns list of available attributes & methods of an object
using dir()."""


def lookup(obj):
    """
    Lookup function.
    Returns dir() of an object.
    dir() tries to return a list of valid attributes of the object.

    Args:
        obj: object to list attributes of.
        """
    return dir(obj)
