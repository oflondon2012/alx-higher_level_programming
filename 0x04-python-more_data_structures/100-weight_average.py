#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

        tw_sum = 0
        t = 0

        for tup in my_list:
            tw_sum += tup[0] * tup[1]
            t += tup[1]

        return (tw_sum / t)
