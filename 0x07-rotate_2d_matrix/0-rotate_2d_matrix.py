#!/usr/bin/python3
"""We rotate a matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """We rotate the the matrix in place"""
    n = len(matrix)

    # transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
