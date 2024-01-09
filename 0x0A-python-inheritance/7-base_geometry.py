#!/usr/bin/python3
"""Module BaseGeometry which have 2 methods"""


class BaseGeometry():
    """Implement the properties"""

    def area(self):
        """Area not implemented at all"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer value of 2 arguments
        Args:
            name (str): The name of value validated
            value (int): The value to be validated
        Raises:
            TypeError: if the value not an integer
            ValueError: If the value is less than or equal o
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
