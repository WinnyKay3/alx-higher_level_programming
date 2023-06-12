#!/usr/bin/python3


"""Defines a class and inherited class checking func"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited

    Args:
        obj: object to check
        a_class: class to match the type of object to
    Returns:
        if obj is an instance or inherited instance of a_class - True
        otherwise - False."""
    if isinstance(obj, a_class):
        return True
    return False
