#!/usr/bin/python3
"""
Write a class BaseGeometry and add def area,
def integer_validator where validates value with TypeError
and ValueError
"""


class BaseGeometry:
    """
    add integer validator to anterior task
    """
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
