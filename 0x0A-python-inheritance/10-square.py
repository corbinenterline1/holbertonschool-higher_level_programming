#!/usr/bin/python3
"""0x0A - 10 - Square #1"""


class Square(__import__('9-rectangle').Rectangle):
    """Square class. Inherits Rectangle class,
    which inherits BaseGeometry class. Classception. Can't wait
    to start game programming. Got unity recently."""

    def __init__(self, size):
        """Initialization method for Square class. Size is validated
        by integer_validator method inherited from Rectangle's inheritance."""
        super().__init__(size, size)
        self.__size = size
