#!/usr/bin/python3

"""Defines a clss rectangle that inherits from basegeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """return arae of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Print string representation of obj"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
