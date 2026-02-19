#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    
    Args:
        matrix: A list of lists of integers/floats.
        div: A number (integer or float) to divide by.
        
    Returns:
        A new matrix with the results rounded to 2 decimal places.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    # Bölən (div) üçün yoxlamalar
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Matris formatı üçün yoxlamalar
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_type)

    # Matrisin sətir uzunluqlarının bərabərliyinin yoxlanması
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_size)

    # Yeni matrisin yaradılması və elementlərin bölünməsi
    return [[round(item / div, 2) for item in row] for row in matrix]
