#!/usr/bin/python3
"""
11-student.py
Public method def reload_from_json(self, json):
that replaces all attributes of the Student instance
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

    def to_json(self, attrs=None):
        """dictionary representation
        attrs: list of attributes
        return: dict representation of instance
        """
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for x in json:
            self.__dict__.update({x: json[x]})
