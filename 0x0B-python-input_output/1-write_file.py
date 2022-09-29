#!/usr/bin/python3

"""
This module defines a function that writes a text to a file
"""


def write_file(filename="", text=""):
    """writes a text to a file"""

    with open(filename, 'a', encoding="utf-8") as f:
        write_file = f.write(text)
        return (write_file)
