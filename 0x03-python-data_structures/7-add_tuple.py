#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    list_c = [x + y for x, y in zip(tuple_a, tuple_b)]
    return tuple(list_c[0:2])
