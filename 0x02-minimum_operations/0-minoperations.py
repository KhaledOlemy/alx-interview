#!/usr/bin/python3
"""
Min Operations
"""


def minOperations(n: int) -> int:
    """
    Min Operations - H copier
    """
    currentCount: int = 1
    copier: int = 1
    noOperations: int = 1
    while (n > currentCount):
        remainingCount = n - currentCount
        if remainingCount / (copier * 2) == remainingCount // (copier * 2):
            copier = copier * 2
            noOperations += 2
        else:
            noOperations += 1
        currentCount += copier
    return noOperations
