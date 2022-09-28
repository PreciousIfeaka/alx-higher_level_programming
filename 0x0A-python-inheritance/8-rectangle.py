#!/usr/bin/python3

"""
This module defines a function that a value in a class method
"""


class BaseGeometry:
    """Defines a class BaseGeometry
    Args: None
    """

    def area(self):
        """defines an area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """This class defines a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
