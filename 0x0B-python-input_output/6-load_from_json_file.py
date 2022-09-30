#!/usr/bin/python3

"""
This module defines a function that deserializes
an object from a json file
"""
import json


def load_from_json_file(filename):
    """deserializes an object from a json file"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
