#!/usr/bin/python3
"""
matrix_divided divides a given matrix with
a given divisor

"""


def matrix_divided(matrix, div):
    for i in range(0, len(matrix)-1):
        for j in range(len(matrix[i])):
            if type(j) not in [float, int] or len(matrix[i]) < 2:
                raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    matrix1 = [list(map(lambda j: round(j/div, 2),
                        matrix[i])) for i in range(len(matrix))]

    return matrix1
