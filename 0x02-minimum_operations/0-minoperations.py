#!/usr/bin/python3
"""
Min Operations problem solving - interview preparations
"""


def minOperations(n):
    """
    Min Operations - H copier
    Compute the minimum number of operations (copy all - paste) required
    to achieve the number of Hs needed
    """
    currentCount = 1
    copier = 1
    noOperations = 1
    while (n > currentCount):
        remainingCount = n - currentCount
        if remainingCount / (copier * 2) == remainingCount // (copier * 2):
            copier = copier * 2
            noOperations += 2
        else:
            noOperations += 1
        currentCount += copier
    return noOperations
