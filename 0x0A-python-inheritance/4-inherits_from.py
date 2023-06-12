#!/usr/bin/python3

"""Defines an inherited class checking func"""


def inherits_from(obj, a_class):
    """check if object is an inherited instance
    Args:
        obj: object to check
        a_class: class to match the type of obj
    Return:
        if obj is an inherited instance of a_class - True
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
