#!/usr/bin/python3
"""Prints my name"""


def say_my_name(first_name, last_name=""):
    """
    Function to print full name.
    first_name and last_name must be strings, otherwise TypeError
    No return

    Args:
        first_name: first name
        last_name: last name, default is blank
        """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is '' or first_name is "":
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
