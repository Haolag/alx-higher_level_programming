#!/usr/bin/python3
"""
9-student.py
Write a class Student that defines a student by
"""


class Student:
    """
    class student and def, nomb, apellido, age
    """
    def __init__(self, first_name, last_name, age):
        """inicialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary"""
        return self.__dict__
