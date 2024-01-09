#!/usr/bin/python3
"""Function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Implementing the attributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
