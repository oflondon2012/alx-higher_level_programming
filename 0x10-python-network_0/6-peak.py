#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    lb = 0
    hb = len(list_of_integers) - 1
    
    while lb <= hb:
        bm = (hb + lb) // 2
        if (bm == 0 or list_of_integers[bm] >= list_of_integers[bm - 1]) and \
           (bm == len(list_of_integers) - 1 or list_of_integers[bm] >= list_of_integers[bm + 1]):
               return list_of_integers[bm]
        elif bm > 0 and list_of_integers[bm] < list_of_integers[bm + 1]:
            lb = bm + 1
        else:
            hb = bm - 1

    return None
