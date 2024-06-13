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
    if n <= 1:
        return 0
    currentCount = 2
    copier = 1
    noOperations = 2
    while n > currentCount:
        remainingCount = n - currentCount
        if remainingCount % currentCount == 0:
            currentCount += copier
            copier = currentCount
            noOperations += 2
        else:
            currentCount += copier
            noOperations += 1
    if currentCount > n:
        return 0
    return noOperations
