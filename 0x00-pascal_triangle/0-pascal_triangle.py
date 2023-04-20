#!/usr/bin/python3

"""This scripts prints the pascal triangle"""


def pascal_triangle(n):
    """We retrun the pascal array"""
    if n == 0:
        return ([])
    tringle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tringle[i - 1][j - 1] + tringle[i - 1][j]
        tringle.append(row)
    return tringle
