#!/usr/bin/python3
"""
a class Square that defines a square by: 4-square.py
"""


class Square:
    """
    Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    """

    def __init__(self, size=0):

        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):

        self.__size = size

        if type(self.__size) is not int:
            raise TypeError('size must be an integer')

        if self.__size < 0:
            raise ValueError('size must be >= 0')

        def area(self):
            """
            Returns square area
            """
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
