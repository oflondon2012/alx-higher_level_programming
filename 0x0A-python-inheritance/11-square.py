#!/usr/bin/python3
"""
Module of rectangle and sqaure
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Implementing the square module
"""


class Square(Rectangle):
    """ square method"""
    def __init__(self, size):
        """ size initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
