#!/usr/bin/python3
"""
Module 3-rectangle.py
class Rectangle
private attribute height and width
"""


class Rectangle:
    """
    Represents a Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        new Rectangle.
        Args:
            width (int): The width
            height (int): The height
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """Return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the Rectangle #'s
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
            string represenation of the object
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        prints a message for every instance deletion
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
