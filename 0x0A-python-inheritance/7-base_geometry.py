#!/usr/bin/python3
"""Module BaseGeometry which have 2 methods"""


def area(self):
    """Area not implemented at all"""
    raise Exception("area() is not implemented")


def integer_validator(self, name, value):
    """validate integer value of 2 arguments"""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")