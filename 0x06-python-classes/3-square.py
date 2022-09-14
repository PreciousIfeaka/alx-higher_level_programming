#!/usr/bin/python3
"""
This module creates a square class.
"""


class Square:
    """This creates a class and defines it with attributes.
    Attributes:
    size(int): An integer that defines the square dimensions.
    """

    def __init__(self, size=0):
        if size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) is not int:
            raise TypeError('size must be an integer')
        self.__size = size

    def area(self):
        return (self.__size ** 2)
