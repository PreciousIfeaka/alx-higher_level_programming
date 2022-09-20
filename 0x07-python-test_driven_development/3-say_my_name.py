#!/usr/bin/python3

"""This module contains a function that prints fullname
"""


def say_my_name(first_name, last_name=""):
    """This function prints the fullname"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
