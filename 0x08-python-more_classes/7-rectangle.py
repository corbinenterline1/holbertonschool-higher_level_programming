#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle class with private attributes width and height
    Public attributes:
    number_of_instances = self explanatory
    print_symbol = default '#', used for informal string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization with optional parameters.
        Increments class variable number_of_instances
        Args:
            self: calling its' class
            width: width of rectangle
            height: height of rectangle
            """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns perimeter of the rectangle
        Checks:
        height & width must be > 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Returns the informal string representation of
        the rectangle, using #
        Checks:
        height & width must be > 0
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            a = ""
            for y in range(self.__height):
                for x in range(self.__width):
                    a += str(self.print_symbol)
                if y < self.__height - 1:
                    a += "\n"
            return a

    def __repr__(self):
        """Returns the official string representation of
        the rectangle. Contains all the information about the object.
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Returns a custom message when an instance is deleted.
        Decrements class variable number_of_instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
