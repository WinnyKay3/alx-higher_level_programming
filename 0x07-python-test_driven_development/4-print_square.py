#!/usr/bin/python3


"""Defines a square-printing function."""



def print_square(size):
    """Print a square with the # character

    Args:
        size(int) : length of square."""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float or size < 0:
        raise TypeError("size must be an integer")

    for n in range(size):
        for k in range(size):
            print("#", end="")
        print()

