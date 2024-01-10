#!/usr/bin/python3
"""
Module that wrote a string to file
"""


def write_file(filename="", text=""):
    """
    function that write a string to file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    return num
