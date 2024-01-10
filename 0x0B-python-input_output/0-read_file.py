#!/usr/bin/python3
"""
Module that read a text file
"""


def read_file(filename=""):
    """
    function that read a text file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
