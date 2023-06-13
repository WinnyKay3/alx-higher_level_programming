#!/usr/bin/python3


"""Describes a class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dict representation of a student"""
        return self.__dict__
