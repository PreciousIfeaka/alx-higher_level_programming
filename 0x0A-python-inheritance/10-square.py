#!/usr/bin/python3

"""
This module defines class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square which is a subclass of the
        Rectangle class
    """

    def __init__(self, size):
        """initializes an instance of the Square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
