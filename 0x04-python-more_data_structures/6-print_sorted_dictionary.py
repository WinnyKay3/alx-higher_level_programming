#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for t in keys:
        print("{}: {}".format(t, a_dictionary.get(t)))
