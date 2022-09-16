#!/usr/bin/python3

"""
This module implements methods on class square
"""


class Square:
    """empty class with size private attributes
    Attributes:
        size(int): dimension of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(num, int) for num in value):
                if all(num >= 0 for num in value):
                    self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
