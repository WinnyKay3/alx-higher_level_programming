#!/usr/bin/python3

"""Defines an inherited list class Mylist."""



class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print the list in a sorted way, ascending order"""

        list_t = self[:]
        list_t.sort()
        print(list_t)
