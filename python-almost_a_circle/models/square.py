#!/usr/bin/python3
"""This module provides the Square class template.

The template inherits from the Rectangle class and manages size dimensions
by reusing width and height properties without creating new attributes.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A model mapping structural layouts for a square instance."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a geometric Square profile using the Rectangle core."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square via its width property."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size by synchronously updating width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides the str method to return square-specific info."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assigns positional args or key/value kwargs to attributes."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

