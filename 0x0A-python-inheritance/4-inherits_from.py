#!/usr/bin/python3

"""
This module defines a function that checks if an object
is an instance of the specified class directly or indirectly
"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class
        directly or indirectly.
    Args:
        obj(any type): the object to check for
        a_class(any class): the class to check in
    Return: True if the object is an instance of the class or False
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
