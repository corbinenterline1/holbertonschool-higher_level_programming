#!/usr/bin/python3
"""Square printing module"""


def print_square(size):
    """
    Prints a square using #.
    size must be an integer, otherwise TypeError
    size must be 0 or greater, otherwise ValueError
    if size is a float and less than 0, TypeError

    Args:
        size: size length of the square
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print()
        return
    for y in range(size):
        for x in range(size):
            print("#", end='')
        print()
