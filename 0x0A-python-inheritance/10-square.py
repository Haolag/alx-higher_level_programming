#!/usr/bin/python3
"""
10-rectangle.py
a class Rectangle that inherits from Rectangle (9-rectangle.py)
add calculate area and size
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and validate with integer validator"""
    def __init__(self, size):
        """validar si es un integer y retornar area"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """super sirve para modificar en la clase padre"""
