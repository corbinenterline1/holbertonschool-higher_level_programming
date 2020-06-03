#!/usr/bin/python3
"""Module for checking sub class of function """


def inherits_from(obj, a_class):
    """ inherits_from function returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the specified
    class; otherwise False.

    Args:
        obj: Object to compare
        a_class: Class to compare object to
        """
    if (issubclass(obj.__class__, a_class) and type(obj) != a_class):
        return True
    else:
        return False
