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
        Matrix to be div must have int or float otherwise raise a TypeError.
        If the number that divides is 0 the raise a ZeroDivisionError.
    Parameters:
        matrix: list of list containing float or integers.
        div: number used to divide each numebr in the matrix.
    return:
        New list.
    """

    row_size = len(matrix[0])
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
#    #check if matrix is a list of lists
    if type(matrix) is not list:
        raise TypeError(msg)
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(msg)

#    #check if list exist and elements in list exist
    if len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg)

#    #check if matrix has integers or floats
    for row in matrix:
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError(msg)

#    #check if all rows in the list have the same size
    for row in matrix:
        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

#    #check if number div is not integer or float
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

#    #check if number is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

#    #divide
    for a in range(len(matrix)):
        mini_list = []
        for b in range(len(matrix[a])):
            number = round(matrix[a][b]/div, 2)
            mini_list.append(number)
        new_matrix.append(mini_list)
    return new_matrix
