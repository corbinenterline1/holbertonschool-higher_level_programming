#!/usr/bin/python3
"""0x0C - Almost a circle
Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class. Parent is Rectangle, whose
    parent is Base. A square is a special rectangle :)"""

    def __init__(self, size, x=0, y=0, id=None):
        """class Square constructor. Calls super class with
        args.

        Args:
            self
            size: width & height are same for a square
            x
            y
            id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides inherited __str__ to return one
        applicable for Square."""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Size getter. Gets width (could be height, tis square)."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter. Assigns width, then height, with same value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes in order of arguments:
        1st: id
        2nd: size
        3rd: x
        4th: y
        Uses no-keyword arg if there, otherwise key-worded args"""
        larg = ['', '', '', '']
        if args and len(args) > 0:
            for argy in range(len(args)):
                larg[argy] = args[argy]
            if larg[0]:
                self.id = larg[0]
            if larg[1]:
                self.size = larg[1]
            if larg[2]:
                self.x = larg[2]
            if larg[3]:
                self.y = larg[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns dictionary representation of Square instance."""
        cdic = {}
        cdic['id'] = self.id
        cdic['size'] = self.size
        cdic['x'] = self.x
        cdic['y'] = self.y
        return cdic
