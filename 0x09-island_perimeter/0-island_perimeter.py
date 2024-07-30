#!/usr/bin/python3
"""
Solve island perimeter problem
Get the surrounding water tiles next to
land tiles"""


def island_perimeter(grid):
    """
    Solve island perimeter problem
    Get the surrounding water tiles next to
    land tiles"""
    perimeter = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:
                continue
            to_check = []
            if j != len(row) - 1:
                to_check.append(row[j+1])
            if i != len(grid) - 1:
                to_check.append(grid[i+1][j])
            if j != 0:
                to_check.append(row[j-1])
            if i != 0:
                to_check.append(grid[i-1][j])
            perimeter += sum(to_check)
    return perimeter
