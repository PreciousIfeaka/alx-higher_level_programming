#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    elif len(my_list) == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
