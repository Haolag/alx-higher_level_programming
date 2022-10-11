#!/usr/bin/python3
"""
class Square defines a square by: 1-square.py
"""


class Square:
    """
    Private instance attribute: size
    Size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
