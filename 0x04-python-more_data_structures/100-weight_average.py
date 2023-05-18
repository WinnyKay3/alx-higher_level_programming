#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    k, t = 0, 0
    for n in my_list:
        k += n[0] * n[1]
        t += n[1]
    return k / t
