#!/usr/bin/python3
""" This module tries to find the minimum operations used
    to achieve a copy of H
"""


def minOperations(n: int) -> int:
    """we return the minimum number of operations"""
    if n < 0:
        return 0
    moves = 0
    fact = 2
    while n > 1:
        if (n % fact) == 0:
            n //= fact
            moves += fact
        else:
            fact += 1
    return moves
