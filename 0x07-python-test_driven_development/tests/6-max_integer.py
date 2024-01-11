#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function implememtation
    """
    if len(list) == 0:
        return None
    results = list[0]
    a = 1
    while a < len(list):
        if list[a] > results:
            results = list[a]
        a += 1
    return results
