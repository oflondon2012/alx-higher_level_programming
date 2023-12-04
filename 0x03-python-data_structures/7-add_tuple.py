#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    f_tuple = tuple_a[:2] + (0, 0)
    s_tuple = tuple_b[:2] + (0, 0)
    sum_tuple = (f_tuple[0] + s_tuple[0], f_tuple[1] + s_tuple[1])
    return sum_tuple
