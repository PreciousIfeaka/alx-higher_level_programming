#!/usr/bin/python3
"""
This module contains a function that returns a list of
available attributes and methods of an object
"""


def lookup(obj):
    """gives the list of attributes and methods of an object
    """
    return dir(obj)
