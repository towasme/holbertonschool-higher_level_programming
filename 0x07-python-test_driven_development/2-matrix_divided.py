#!/usr/bin/python3


"""
matrix_divided module:
function that divides a number with all the elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Description:
        Returns the matrix divided by the number with a float or int type.
        If the number provided is not a int or a float then raise an TypeError.
        Each row must be the same size otherwise raise a TypeError.
        The matrix to be divided must have integers or float numbers otherwise raise a TypeError.
        If the number that divides is 0 the raise a ZeroDivisionError.
    Parameters:
        matrix: list of list containing float or integers.
        div: number used to divide each numebr in the matrix.
    return:
        New list.
    """

    row_size = len(matrix[0])
    new_matrix = []

    #check if list exist and elements in list exist

    #check if matrix is a list of lists
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if matrix has integers or floats
    for row in matrix:
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #check if all rows in the list have the same size
    for row in matrix:
        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    #check if number div is not integer or float
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    #check if number is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    #divide
    mini_list = []
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            mini_list.append(round((matrix[a][b]/div), 2))
        new_matrix.append(mini_list)
    return new_matrix
