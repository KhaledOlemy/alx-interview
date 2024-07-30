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
            if i == 0:
                if j == 0:
                    to_check = [row[j+1], grid[i+1][j]]
                elif j == len(row) - 1:
                    to_check = [row[j-1], grid[i+1][j]]
                else:
                    to_check = [row[j-1], row[j+1], grid[i+1][j]]
            elif i == len(grid) - 1:
                if j == 0:
                    to_check = [row[j+1], grid[i-1][j]]
                elif j == len(row) - 1:
                    to_check = [row[j-1], grid[i-1][j]]
                else:
                    to_check = [row[j-1], row[j+1], grid[i-1][j]]
            else:
                if j == 0:
                    to_check = [row[j+1], grid[i-1][j], grid[i+1][j]]
                elif j == len(row) - 1:
                    to_check = [row[j-1], grid[i-1][j], grid[i+1][j]]
                else:
                    to_check = [row[j-1], row[j+1], grid[i+1][j], grid[i-1][j]]
            perimeter += sum(to_check)
    return perimeter
