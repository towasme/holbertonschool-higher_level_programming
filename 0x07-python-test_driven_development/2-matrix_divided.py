#!/usr/bin/python3


"""
matrix_divided module:
function that divides a number with all the elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns the matrix divided by the number with a float or int type.

    if the number provided is not a int or a float then raise an TypeError.

    Each row must be the same size otherwise raise a TypeError.

    The matrix to be divided must have integers or float numbers otherwise raise a TypeError.

    If the number that divides is 0 the raise a ZeroDivisionError.
    """

    row_size = len(matrix[0])
    new_matrix = []

    #check if list exist and elements in list exist

    #check if matrix is a list of lists
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if matrix has integers or floats
    for row in matrix:
        for elem in row:
            if ((type(elem) is not int) or (type(elem) is not float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if matrix has the same size

    for x in range(len(matrix)):
        print("{}\n", row_size)
        print("{}\n", len(matrix))
        if row_size != len(matrix[x]):
            raise TypeError("Each row of the matrix must have the same size")

    #check if number is integeror float
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")

    #check if number is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            new_matrix[a][b] = matrix[a][b] / div
    return new_matrix
