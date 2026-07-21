#!/usr/bin/python3
"""This module supplies one function, add_integer(a, b)."""


def add_integer(a, b=98):
    """Adds two integers or floats cast to integers.

    Args:
        a: The first number.
        b: The second number, defaults to 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float, or if they are NaN/inf.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return a + b

