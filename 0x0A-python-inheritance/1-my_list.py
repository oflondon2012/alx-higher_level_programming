#!/usr/bin/python3
"""Defines an inherited list class Mylist"""


class MyList(list):
    """This module inherit from list"""

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
