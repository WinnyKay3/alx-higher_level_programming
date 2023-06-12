#!/usr/bin/python3

"""Defines whether an object is an exact instance of class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj (any): object to check
        a_class (type): class to match type of obj to
    Returns:
            if obj is exactly an instance of a_class - True
            otherwise - False."""
    if type(obj) == a_class:
        return True
    return False
