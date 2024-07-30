#!/usr/bin/python3
"""
Solve island perimeter problem
Get the surrounding water tiles next to
land tiles"""


def island_perimeter(grid):
    rows = 0
    cols = 0
    for row in grid:
        count = 0
        for idx, i in enumerate(row):
            if idx == 0 or idx > 0 and row[idx] != row[idx - 1]:
                count += i
        rows += count * 2
    for i in range(len(grid[0])):
        col = []
        for item in grid:
            col.append(item[i])
        count = 0
        for idx, i in enumerate(col):
            if idx == 0 or idx > 0 and col[idx] != col[idx - 1]:
                count += i
        cols += count * 2
    return rows + cols
