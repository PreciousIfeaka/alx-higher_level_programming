#!/usr/bin/python3

"""
This module defines a function that writes an object to a text file
using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object in json to a txt file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
