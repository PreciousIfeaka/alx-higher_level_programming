#!/usr/bin/python3

"""
This module defines a function that checks
if an object is an instance of a class or a base class
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or baseclass
    Args:
        obj(any type): The object to check for
        a_class(any class): the class to check in
    Returns:
        True if the object is an instance or False
    """

    return isinstance(obj, a_class)
