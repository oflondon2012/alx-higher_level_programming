#!/usr/bin/python3
""" Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle  class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class initialization with declaration of args"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter function for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y is not an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Function that get x cordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x cordinate of rectangle & raise error as nece"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Function that get y cordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y cordinate of rectangle & raise error as necessary"""
        if not isinstance(value, int):
            raise TypeError("y must be ab integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using '#' and taking into account the x"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args, **kwargs):
        """function that assign arguments in the order
        args:
            Value to update the attribute in specific order
        kwargs:
            keyward argument which represent att and names
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """function that return dict of rectangle"""
        rec_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }

    def __str__(self):
        """Custom string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"
