#!/usr/bin/python3
"""
Module that append a string at the end of test file
"""


def append_write(filename="", text=""):
    """
    function that append
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
