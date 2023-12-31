#!/usr/bin/python3
"""Module of Rectangle practicing subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialization of a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
