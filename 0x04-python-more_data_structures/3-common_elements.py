#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for x in set_1:
        for y in set_2:
            if y is x:
                my_list.append(x)
    return set(my_list)
