#!/usr/bin/python3

"""
This module contains a function that deserializes a json string
"""

import json


def from_json_string(my_str):
    """Deserializes a json string"""

    return json.loads(my_str)
