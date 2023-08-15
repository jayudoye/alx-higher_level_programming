#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_1, len_2 = len(tuple_a), len(tuple_b)
    if len_1 == 0:
        w, x = 0, 0
    elif len_1 == 1:
        w, x = tuple_a[0], 0
    else:
        w, x = tuple_a[0], tuple_a[1]
    if len_2 == 0:
        y, z = 0, 0
    elif len_2 == 1:
        y, z = tuple_b[0], 0
    else:
        y, z = tuple_b[0], tuple_b[1]
    return (w + y, x + z)
