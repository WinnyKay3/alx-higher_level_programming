#!/usr/bin/python3


"""Describes a python class to JSON function"""


def class_to_json(obj):
    """Return the dictionary representation of simple data structure"""
    return obj.__dict__
