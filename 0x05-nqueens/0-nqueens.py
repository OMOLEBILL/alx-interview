#!/usr/bin/python3
"""
Script that solves the N queens problem
"""
import sys


def is_valid_position(solution, position):
    """
    Verifies if the position is valid for placing a queen
    """
    for queen in solution:
        if queen[1] == position[1] or (queen[0] + queen[1]) == (position[0] + position[1]) or \
                (queen[0] - queen[1]) == (position[0] - position[1]):
            return False
    return True


def solve_queens(row, n, solution):
    """
    Finds the solution recursively, from the root down
    """
    if row == n:
        print(solution)
    else:
        for col in range(n):
            position = [row, col]
            if is_valid_position(solution, position):
                solution.append(position)
                solve_queens(row + 1, n, solution)
                solution.remove(position)


def main(n):
    """
    Main function to solve the N queens problem
    """
    solution = []
    solve_queens(0, n, solution)


if __name__ == '__main__':
    # Validate the arguments from the command line
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Calling the main function
    main(n)
