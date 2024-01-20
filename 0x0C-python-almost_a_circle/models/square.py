#!/usr/bin/python3
"""A square class use to calculate square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Rectangle class that inherits from the Base class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a new instance and set the arguments """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of the square and the arguments"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments in the order of id, width, height, x and y"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A dictionary representation of square"""
        sqr_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }
        return sqr_dict

    def __str__(self):
        """Print the square representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
