#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            real += 1
        except (IndexError, TypeError):
            break
    print("")
    return real
