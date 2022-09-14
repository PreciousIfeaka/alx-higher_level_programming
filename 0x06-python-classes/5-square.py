#!/usr/bin/python3

"""
This module creates and implements class methods.
"""


class Square:
    """This class is created to implement methods and it is not empty
    Attributes:
        size(int): the size or dimensions of the square
        area(int): computes the area
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        self.__size = size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return (Self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for m in range(self.__size):
                    print("#", end="")
                print()
