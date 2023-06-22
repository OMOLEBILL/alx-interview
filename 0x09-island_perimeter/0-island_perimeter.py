#!/usr/bin/python3
"""Lets try and get this area right"""


def island_perimeter(grid):
    """We get the perimeter of the grid"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with assuming all sides are land

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:  # Top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 2
    return perimeter
