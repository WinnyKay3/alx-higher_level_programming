#!/usr/bin/python3

"""Defines a class rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Set the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """To retrieve attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Get area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Get perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Sets the print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += "#" * self.__width + "\n"

        return rectangle[:-1]
