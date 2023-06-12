#!/usr/bin/python3

"""Defines a func that add attr to objects"""


def add_attribute(obj, attr, value):
    """Add a new attr to an obj if possible
    Args:
        Obj: The object to add add attr to
        attr (str): name of attr to add obj to
        value: value attr
    Raises:
        TypeError: if attr cannot be added"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
