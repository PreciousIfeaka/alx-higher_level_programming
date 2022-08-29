#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for char in my_list:
        if char == 'c':
            my_list.remove('c')
        if char == 'C':
            my_list.remove('C')
    my_string = ''.join(my_list)
    return my_string
