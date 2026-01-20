#!/usr/bin/python3
"""
Module that contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): divisor

    Returns:
        list of lists: new matrix with values divided and rounded to 2 decimals
    """
    # Validate div
    if type(div) is bool or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure and contents
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = None
    for row in matrix:
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if type(item) is bool or not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Build and return new matrix (do not modify original)
    return [[round(item / div, 2) for item in row] for row in matrix]

