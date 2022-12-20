#!/usr/bin/python3
"""Define's a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializes a square.
        Args:
            size : The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square of object"""
        return (self.__size * self.__size)
