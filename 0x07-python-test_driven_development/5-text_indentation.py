#!/usr/bin/python3
"""This module indents texts"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ".", "?",or ":"
    
    Args:
        text (str): the string to be printed."""



    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = ".\n\n".join(text.replace(". ",".").split('.'))
    text = "?\n\n".join(text.replace("? ","?").split('?'))
    text = ":\n\n".join(text.replace(": ",":").split(':'))
    print(text)
