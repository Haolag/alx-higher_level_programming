#!/usr/bin/python3
# Matias López. <3959@holbertonschool.com>
"""
2-is_same_class.py
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """ Check if is a same class: return TRUE"""
    if type(obj) == a_class:
        return True
    else:
        return False
