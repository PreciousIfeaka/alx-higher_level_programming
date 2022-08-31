#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for x in list(my_set):
        sum = sum + x
    return sum
