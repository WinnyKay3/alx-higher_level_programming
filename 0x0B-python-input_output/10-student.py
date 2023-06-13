#!/usr/bin/python3


"""Describes a class student"""


class Student:
    '''Represents a student'''

    def __init__(self, first_name, last_name, age):
        '''Initialize new student.'''

        self.fist_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''Gets a dict representation of tha student
        Args:
        att (list): attributes to represent (optional)'''
        if (type(attr) == list and
                all(type(ele) == str for ele in attr)):
            return {t: getattr(self, t) for t in attr if hasattr(self, t)}
        return self.__dict__
