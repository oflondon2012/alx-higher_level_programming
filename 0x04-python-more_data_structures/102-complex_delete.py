#!/usr/bin/python3
def complex_delete(my_dict, value):
    tdic = my_dict.copy()
    for i, j in tdic.items():
        if value == j:
            my_dict.pop(i)
        return my_dict
