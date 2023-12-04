#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    r_list = []
    for n in my_list:
        if n % 2 == 0:
            r_list.append(True)
        else:
            r_list.append(False)
    return r_list
