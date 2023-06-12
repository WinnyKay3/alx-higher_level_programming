#!usr/bin/python3

"""Defines an object attribute look up function."""


def lookup(obj):
    """Return a list of an objects available attributes."""
    return (dir(obj))
