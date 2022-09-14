#!/usr/bin/python3
"""
This module defines a square with given attributes.
"""


class Square:
    """Creates a square class and define its attributes

    Attributes:
        size(int): describes the size of the square.
    """
    def __init__(self, size = 0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
                raise ValueError('size must be >= 0')
        else:
            self.__size = size
