#!/usr/bin/python3
"""Rotate 2-D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2-D matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
