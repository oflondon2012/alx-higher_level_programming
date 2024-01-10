#!/usr/bin/python3
"""
Function that add two integer or float
"""


def add_integer(a, b=98):
    """
    Function to add two integers or floats
    Args:
        a (number): Float or Number
        b (:obj:number:optional): Float or Integer

    Raises:
        TypeError: check if the number is integer or float

    Returns:
        float:int: Integer or float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
