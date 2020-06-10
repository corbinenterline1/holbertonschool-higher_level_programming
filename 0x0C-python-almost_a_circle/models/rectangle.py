#!/usr/bin/python3
"""0x0C - Almost a circle.
Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class. Currently contains private attributes,
    and constructor method."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor.  Calls the super class Base with id.
        Uses setters for private instance attributes."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width GET"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle instance.
        Checks:
        width must be an integer
        width must be > 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height GET"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle instance.
        Checks:
        height must be an integer
        height must be > 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x GONNA GIVE IT TO YA"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of rectangle instance.
        Checks:
        x must be an integer
        x must be >= 0"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y GIT"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of rectangle instance.
        Checks:
        y must be an integer
        y must be >= 0"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns width * height of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with '#'.
        Offsets by y and x, if appicable"""
        if self.__y > 0:
            print("\n" * self.__y, end='')
        for line in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            print('#' * self.__width, end='')
            if line < self.__height - 1:
                print()
        print()

    def __str__(self):
        """Returns a formal string representation of the
        Rectangle."""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates attributes in order of arguments:
        1st: id
        2nd: width
        3rd: height
        4th: x
        5th: y
        Uses no-keyword arg if there, otherwise key-worded args"""
        larg = ['', '', '', '', '']
        if args and len(args) > 0:
            for argy in range(len(args)):
                larg[argy] = args[argy]
            if larg[0]:
                self.id = larg[0]
            if larg[1]:
                self.width = larg[1]
            if larg[2]:
                self.height = larg[2]
            if larg[3]:
                self.x = larg[3]
            if larg[4]:
                self.y = larg[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle instance.
        Creating own because this one shows Rectangle_width and height, wich
        show with superclass name in normal __dict__."""
        cdic = {}
        cdic['id'] = self.id
        cdic['width'] = self.width
        cdic['height'] = self.height
        cdic['x'] = self.x
        cdic['y'] = self.y
        return cdic
