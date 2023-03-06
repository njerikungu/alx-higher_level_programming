#!/usr/bin/python3
"""
Module 5-square
"""


class Square:
    """
    Square definition
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none
        """
        self.size = size

    @property
    def size(self):
        """"
        Getter

        Return's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        Prints square with #'s
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
