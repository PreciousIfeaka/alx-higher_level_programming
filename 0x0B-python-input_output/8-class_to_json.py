#!/usr/bin/python3

"""
This module defines a function that encodes a class type
"""

def class_to_json(obj):
    """encodes a class"""

    return obj.__dict__
