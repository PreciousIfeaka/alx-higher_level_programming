#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            div = 0
            print(f"out of range")
        except ZeroDivisionError:
            div = 0
            print(f"division by 0")
        except (ValueError, TypeError):
            div = 0
            print(f"wrong type")
        finally:
            c.append(div)
    return c
