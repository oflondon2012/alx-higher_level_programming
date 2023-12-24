#!usr/bin/python3
"""This is Square class module """


class Square:
    """Square class module"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiaization of a new square:
        Args:
            size (int): Represent the size of new square.
            position (int, int): New square position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise TypeError("Size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for postion of the sqaure"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """ calculate area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square along with # xter"""
        if self.__size == 0:
            print("")
            return

        [print("") for j in range(0, self.__position[1])]
        for j in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")
