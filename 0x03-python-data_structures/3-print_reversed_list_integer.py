#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        c = len(my_list) - 1
        while c >= 0:
            print("{:d}".format(my_list[c]))
            c -= 1
