#!/usr/bin/python3
def uniq_add(my_list=[]):
    t = 0
    for n in dict.fromkeys(my_list):
        t += n
    return t
