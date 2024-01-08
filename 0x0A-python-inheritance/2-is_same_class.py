#!/usr/bin/python3
"""Function that return true if object is exatly else false"""


def is_same_class(obj, a_class):
    """ check if is object or not of subclass"""
    if type(obj) == a_class:
        return True
    return False
