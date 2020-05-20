#!/usr/bin/python3
"""Class Square"""


class Square:
    """class Square with a private attribute size"""

    def __init__(self, __size=0):
        """Initialization method with optional size parameter, with check
        for integer

        Args:
            self: calling it's class
            size: size of square, default is 0
            """
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        """Returns the area of the current square

        Args:
            self: calling it's class
            """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns the size of the current square

        Args:
            self: calling it's class
            """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size attribute

        Args:
            self: calling it's class
            value: new size of square
            """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
