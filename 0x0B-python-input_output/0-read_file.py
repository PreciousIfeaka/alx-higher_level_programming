#!/usr/bin/python3

"""
This module contains a function that reads a text file and
prints it to stdout
"""


def read_file(filename=""):
    """reads a file and prints it to stdout"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
