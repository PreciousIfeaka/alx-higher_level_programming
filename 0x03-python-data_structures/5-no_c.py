#!/usr/bin/python3
def no_c(my_string):
    line = list(my_string)
    for x in line:
        if x == 'c':
            line.remove('c')
        if x == 'C':
            line.remove('C')
    my_string = "".join(line)
    return my_string
