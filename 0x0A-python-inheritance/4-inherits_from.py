#!/usr/bin/python3
"""Module to check object is of a class inherit or not """


def inherits_from(obj, a_class):
    """Check for the inheritance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
