#!/usr/bin/python3
''' Defines peak-finding algorithm'''


def find_peak(list_of_int):
    '''Return peak in a list of unsorted int'''
    if list_of_int == []:
        return None

    size = len(list_of_int)
    if size == 1:
        return list_of_int[0]
    elif size == 2:
        return max(list_of_int)

    mid = int(size / 2)
    peak = list_of_int[mid]
    if peak > list_of_int[mid - 1] and peak > list_of_int[mid + 1]:
        return peak
    elif peak < list_of_int[mid - 1]:
        return find_peak(list_of_int[:mid])
    else:
        return find_peak(list_of_int[mid + 1:])
