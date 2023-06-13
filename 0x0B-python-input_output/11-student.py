#!/usr/bin/python3


'''Descibes a class student'''


class Student:
    '''Reprsents a student'''
    def __init__(self, first_name, last_name, age):
        '''Initialize a new student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''Gets a dict representation of student'''
        if (type(attr) == list and
                all(type(ele) == str for ele in attr)):
            return {t: getattr(self, t) for t in attr if hasattr(self, t)}
        return self.__dict__
    
    def reload_from_json(self, json):
        '''Replaces all attributes of the student'''
        for t, n in json.items():
            setattr(self, t, n)
