#!/usr/bin/python3
"""0x0A - 0 - Lookup"""


def lookup(obj):
    """
    Lookup function.
    Returns dir() of an object.
    dir() tries to return a list of valid attributes of the object.

    Args:
        obj: object to list attributes of.
        """
    return dir(obj)
