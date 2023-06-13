#!/usr/bin/python3


"""Describes a JSON file reading function"""
import json


def load_from_json_file(filename):
    """function that creates an object from JSON file"""
    with open(filename) as f:
        return json.load(f)
