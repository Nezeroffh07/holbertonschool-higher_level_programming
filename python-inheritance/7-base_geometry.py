#!/usr/bin/python3
"""
This module defines a class BaseGeometry based on 6-base_geometry.py.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
