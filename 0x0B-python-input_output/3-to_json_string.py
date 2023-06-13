#!/usr/bin/python3

"""Defines a string to JSON function"""

import json


def to_json_string(my_obj):
    """function that returns JSON representation of string obj"""
    return json.dumps(my_obj)
