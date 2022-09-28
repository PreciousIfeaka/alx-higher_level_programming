#!/usr/bin/python3

"""
This module defines a function that checks if
an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class
    Args:
        obj(any type): The given object to check
        a_class(any class): The class to check in
    """

    if type(obj) is a_class:
        return True
    else:
        return False
