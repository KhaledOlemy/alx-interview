#!/usr/bin/python3
"""
Pascal Triangle module.
"""


def pascal_triangle(n):
    """
    Makes Pascal Pyramid, where a value is determined by the addition of
    the same index in the previous layer, and the previous index of the
    previous layer as well. The triangle is built top first.
    args:
        n: layers of triangle.
    return: array of arrays, each array takes a whole horizontal layer.
    """
    if n <= 0:
        return []
    output = []
    for i in range(1, n+1):
        line = [1]*i
        if i <= 2:
            output.append(line)
            continue
        prev = output[-1]
        for j in range(i):
            if j == 0 or list(range(i)).index(j) == list(range(i))[-1]:
                continue
            else:
                line[j] = prev[j] + prev[j - 1]
        output.append(line)
    return output
