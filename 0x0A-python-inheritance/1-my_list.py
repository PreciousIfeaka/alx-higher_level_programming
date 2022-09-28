#!/usr/bin/python3

"""
Module contains a subclass that inherits from list class
"""


class MyList(list):
    """A class that inherits from the list class
    """

    def print_sorted(self):
        """Prints a list in ascending sort"""
        print(sorted(self))
