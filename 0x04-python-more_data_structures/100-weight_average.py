#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

        tw_sum = 0
        t_den = 0

        for s, w in my_list:
            tw_sum += s * w
            t_den += w
        if t_den == 0:
            return 0

        return (tw_sum / t_den)
