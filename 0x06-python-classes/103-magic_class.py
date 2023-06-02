#!/usr/bin/python3
"""Define a MagicClass matching a bytecode provided."""

import math

class MagicClass:
    """ represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass
        Args:
            radius (float or int): radius of the new MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return(self.__radius ** 2 * math.pi)

    def circumfrence(self):
        return (2 * math.pi * self.__radius)
