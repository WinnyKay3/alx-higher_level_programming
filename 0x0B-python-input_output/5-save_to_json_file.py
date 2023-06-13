#!/usr/bin/python3


"""Write and convert to JSON string"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
