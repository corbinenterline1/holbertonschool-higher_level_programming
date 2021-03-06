#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle class with private attributes width and height"""

    def __init__(self, width=0, height=0):
        """Initialization with optional parameters.

        Args:
            self: calling its' class
            width: width of rectangle
            height: height of rectangle
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle instance.
        Checks:
        width must be an integer
        width must be >= 0

        Args:
            self: calling its' class
            value: value to set width to
            """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle instance.
        Checks:
        height must be an integer
        height must be >= 0

        Args:
            self: calling its' class
            value: value to set width to
            """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
