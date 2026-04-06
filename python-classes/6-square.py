#!/usr/bin/python3
"""Module that defines a Square class with position"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property to retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the private size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property to retrieve the private position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set the private position attribute"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout"""
        if self.__size == 0:
            print("")
            return

        # Handle vertical offset (position[1])
        [print("") for i in range(self.__position[1])]

        # Handle horizontal offset (position[0]) and print square
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
