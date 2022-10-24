#!/usr/bin/python3
"""
A function that returns True if the object is an instance
"""


def inherits_from(obj, a_class):
    """
    inherits_from: Check if is inherited for specificed class
    Args:
    obj: object
    a_class: class
    """
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False
