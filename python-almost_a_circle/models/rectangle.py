#!/usr/bin/python3
"""This module provides the Rectangle class template.

The template inherits structural management properties from the Base module
and applies robust parameter type testing alongside standard area geometry.
"""
from models.base import Base


class Rectangle(Base):
    """A model mapping spatial layout profiles for rectangle instances."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a brand new geometric Rectangle profile.

        Args:
            width (int): Total linear breadth of the asset.
            height (int): Total vertical rise of the asset.
            x (int, optional): Horizontal coordinate offset. Defaults to 0.
            y (int, optional): Vertical coordinate offset. Defaults to 0.
            id (int, optional): Unique identification handle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the active private width dimension."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the horizontal width metric after running validation rules."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the active private height dimension."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the vertical height metric after running validation rules."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the private horizontal offset value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the horizontal padding value after running validation rules."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the private vertical offset value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the vertical padding value after running validation rules."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes and returns the surface area of the rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the visual layout map with character hashes taking care of x and y."""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Overrides str method to return standard structured info."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Assigns positional args or key/value kwargs to attributes."""
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }


