#!/usr/bin/python3
# Matias López - <3959@holbertonschool.com>
"""
3-is_kind_of_class.py
a function that returns True if the object is an
instance of, or if the object is an instance of a
class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check instance of object and return true"""

    return (isinstance(obj, a_class))
