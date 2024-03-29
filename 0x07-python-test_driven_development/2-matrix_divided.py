#!/usr/bin/python3
'''decimal module'''
import decimal

"""
matrix_divided divides a given matrix with
a given divisor

"""


def matrix_divided(matrix, div):
    """divides matrix by an integer"""

    erro_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(erro_msg)

    len_rows = []
    row_count = 0

    for row in matrix:
        if type(row) is not list:
            raise TypeError(erro_msg)

        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(erro_msg)
        row_count += 1

    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
