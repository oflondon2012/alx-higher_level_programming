#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = []
    for i, j in my_dict.items():
        if j == value:
            tmp.append(i)
    for i in tmp:
        del my_dict[i]
    return my_dict
