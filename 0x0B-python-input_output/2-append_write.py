#!/usr/bin/python3


"""Defines a file  appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file
    and returns number of elements added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
