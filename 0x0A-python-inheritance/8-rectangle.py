#!/usr/bin/python3
"""0x0A 8 - Rectangle"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle Class, parent BaseGeometry.
    Currently, initialization values are validated
    using inherited method integer_validator."""

    def __init__(self, width, height):
        """Initialization method for Rectangle.
        Width & height are validated using inherited
        method integer_validator from BaseGeometry.

        Args:
            self: self
            width: width
            height: height lol
            """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
