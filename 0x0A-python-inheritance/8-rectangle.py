#!/usr/bin/python3

"""
This module defines a function that a value in a class method
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines a rectangle
        Attributes:
            width(int): width of the rectangle
            height(int): height of the rectangle
    """

    def __init__(self, width, height):
        """initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
