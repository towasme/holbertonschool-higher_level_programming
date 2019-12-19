#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squares.append(j**2)
        print()
