#!/usr/bin/python3
"""Addition module: a + b"""


def add_integer(a, b=98):
    """
    Addition function.
    a and b must be integers or floats, otherwise raise a TypeError exception
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b

    Args:
        a: first integer or float
        b: 2nd int or float, defaults at 98
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
