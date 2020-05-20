#!/usr/bin/python3
"""Class Square"""


class Square:
    """class Square with a private attribute size"""
    __size = None

    def __init__(self, __size=None):
        """Initialization method with optional size parameter

        Args:
            self: calling it's class
            size: size of square, default is 0
            """
        self.__size = __size
