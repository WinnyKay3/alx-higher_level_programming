#!/usr/bin/python3
"""Describe a class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the rect class

    Attr:
        size (int): size of square
        x(int): x coordinate of de square's position
        y(int): y coordinate of de square's position"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new instance of the square class"""

        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the Square instance based on *args and **kwargs.

        Args:
            *args: List of arguments.
            **kwargs: Dictionary of keyword arguments.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value
