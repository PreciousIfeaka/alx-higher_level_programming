#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for int in my_list:
        print('{:d}'.format(my_list[n - 1]))
        n = n - 1
