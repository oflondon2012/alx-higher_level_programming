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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
