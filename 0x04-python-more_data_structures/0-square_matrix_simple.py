#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = matrix.copy()
    for i in range(len(matrix)):
        squares[i] = (list(map(lambda j: j * j, squares[i])))
    return (squares)
