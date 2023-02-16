#!/usr/bin/python3
"""
This function finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """finds the peak of an unsorted list
    """

    low = 0
    high = len(list_of_integers) - 1
    if list_of_integers:
        while low < high:
            mid = (low + high) // 2
            if list_of_integers[mid] < list_of_integers[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return list_of_integers[low]
    else:
        return None