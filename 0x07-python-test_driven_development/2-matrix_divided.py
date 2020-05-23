#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divides items of matrix by div.
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception
    each row of the matrix must be of the same size,
    otherwise raise a TypeError exception
    div must be a number(integer or float),
    otherwise raise a TypeError exception
    div can't be equal to 0, otherwise raise a ZeroDivisionError
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns: new matrix

    Args:
        matrix: input matrix
        div: number to divide items by
        """
    divtrix = []
    l = 0
    d = 0

    if type(matrix) is not list or matrix is None:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if matrix == []:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        divlist = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix '
                            '(list of lists) of integers/floats')
        if l == 0:
            l = len(row)
        if l != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [float, int]:
                raise TypeError('matrix must be a matrix '
                                '(list of lists) of integers/floats')
            divlist.append(round(element / div, 2))
        divtrix.append(divlist)
    return (divtrix)
