#!/usr/bin/python3
"""Module to determine an instance of a class"""


def is_kind_of_class(obj, a_class):
    """check if object is an instance of a clas or not"""
    if isinstance(obj, a_class):
        return True
    return False
