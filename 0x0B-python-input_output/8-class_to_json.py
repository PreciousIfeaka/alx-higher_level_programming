#!/usr/bin/python3

"""
This module defines a function that encodes a class type
"""
import json

def class_to_json(obj):
    """encodes a class"""

    return json.dumps(obj.__dict__)
