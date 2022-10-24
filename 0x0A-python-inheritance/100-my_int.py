#!/usr/bin/python3
"""Class MyInt that inherits from int"""


class MyInt(int):
    """My int class"""

    def __eq__(self, value):
        """Myint is equal to"""
        return self.real != value

    def __ne__(self, value):
        """Myint is diferent to"""
        return self.real == value
