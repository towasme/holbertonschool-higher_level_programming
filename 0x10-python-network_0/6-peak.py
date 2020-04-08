#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ function to find the peak
    """
    if list_of_integers:
        size = len(list_of_integers)
        half_size = size / 2
        pos_sup = size - 1
        pos_inf = 0
        sup = list_of_integers[pos_sup - 1]
        inf = list_of_integers[pos_inf]
        peak = list_of_integers[pos_sup]

        for i in range(int(half_size)):
            if inf > sup:
                if inf > peak:
                    peak = inf
            else:
                if sup > peak:
                    peak = sup
            pos_inf += 1
            pos_sup -= 1
        return peak
    else:
        return None
