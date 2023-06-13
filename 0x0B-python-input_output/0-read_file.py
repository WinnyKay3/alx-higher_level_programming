#!/usr/bin/python3


"""Defines a text reading func."""


def read_file(filename=""):
    """Reads text from a file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
