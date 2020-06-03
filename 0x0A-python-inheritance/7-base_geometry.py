#!/usr/bin/python3
"""0x0A 7 - Integer validator"""


class BaseGeometry:
    """BaseGeometry Class. Contains public instance
    methods area(returns area) and integer_validator that validates value."""

    def area(self):
        """area function, currently poop.

        Args:
            self: self
            """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.
        If value is not an integer, raises TypeError.
        If value is less than or equal to 0, raises ValueError.

        Args:
            self: self
            name: assumed to always be a string
            value: value to be validated.
            """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
