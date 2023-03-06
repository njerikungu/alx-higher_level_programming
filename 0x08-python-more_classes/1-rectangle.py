#!/usr/bin/python3
"""
Module 1-rectangle.py
Class Rectangle
with private attribute height and weight
"""


class Rectangle:
    """
    Represents class Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
