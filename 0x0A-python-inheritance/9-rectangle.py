#!/usr/bin/python3
"""
9-rectangle.py
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
add width and height and calculate AREA
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create subclass Rectangle of BaseGeometry"""
    def __init__(self, width, height):
        """
        width and height must be privat
        and must be positive integer
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """print rectangle width/height"""
        return '[Rectangle] ' + str(self.__width) + "/" + str(self.__height)
