#!/usr/bin/python3

"""Defines a class myint that inherits from int."""

class MyInt(int):
    """inverts int operators"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
