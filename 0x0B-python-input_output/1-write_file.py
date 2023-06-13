#!/usr/bin/python3

"""Defines a file writing func"""


def write_file(filename="", text=""):
    """Writes a string to text file UTF8 and returns
        the number of elements written"""


    with open(filename, 'w') as file:
        return file.write(text)
