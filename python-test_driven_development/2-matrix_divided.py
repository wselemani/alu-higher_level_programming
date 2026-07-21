#!/usr/bin/python3
"""This module supplies one function, matrix_divided(matrix, div)."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor number (integer or float).

    Returns:
        A new matrix containing the rounded results.

    Raises:
        TypeError: If matrix is invalid or rows have mismatched sizes,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
