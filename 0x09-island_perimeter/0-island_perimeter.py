#!/usr/bin/python3
"""Lets try and get this area right"""


def island_perimeter(grid):
    """We get the perimeter of the grid"""
    perimeter = 0
    for index, value in enumerate(grid):
        if 1 in value:
            for j in range(len(value) - 1):
                if value[j] == 1:
                    if index == 0:
                        if j > 0:
                            if value[j - 1] == 0:
                                perimeter += 1
                            if value[j + 1] == 0:
                                perimeter += 1
                            if grid[index + 1][j] == 0:
                                perimeter += 1
                        else:
                            if value[j + 1] == 0:
                                perimeter += 1
                            if grid[index + 1][j] == 0:
                                perimeter += 1
                    else:
                        if j > 0:
                            if value[j - 1] == 0:
                                perimeter += 1
                            if value[j + 1] == 0:
                                perimeter += 1
                            if grid[index - 1][j] == 0:
                                perimeter += 1
                            if grid[index + 1][j] == 0:
                                perimeter += 1
                        else:
                            if value[j + 1] == 0:
                                perimeter += 1
                            if grid[index - 1][j] == 0:
                                perimeter += 1
                            if grid[index + 1][j] == 0:
                                perimeter += 1
    return perimeter
