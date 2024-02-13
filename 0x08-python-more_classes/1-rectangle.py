#!/usr/bin/python3
"""module that represent a Rectangle class"""


class Rectangle:
    """Class that represent rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """Method that instantiates private attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width of rectangle
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Arg:
            value (int): The new width value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.
            Returns:
                int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Arg:
            value (int): The new height value.
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value=-0:
        raise ValueError("height must be >= 0")
    self.__height = value
