#!/usr/bin/python3
"""
function that returns the list of available attributes and methods
"""


def lookup(obj):
    """
    return the list of available attributes and method
    of an object

    Args:
        obj

    Returns:
        list
    """
    return dir(obj)
