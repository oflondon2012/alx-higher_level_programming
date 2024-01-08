#!/usr/bin/python3
"""Defines an inherited list class Mylist"""


class Mylist(list):
    """This module inherit from list"""

    def print_sortlist(self):
        """print the sorted list"""
        print(sorted(self))
