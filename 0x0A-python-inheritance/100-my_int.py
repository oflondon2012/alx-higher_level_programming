#!/usr/bin/python3
"""MyInt module that inherits from int."""


class MyInt(int):
    """Implementing the operation of MyInt"""

    def __eq__(self, value):
        """Doing the overiding of operator"""
        return self.real != value

    def __ne__(self, value):
        return self.real == value
