#!/usr/bin/python3
"""
Min Operations
"""


def minOperations(n: int) -> int:
    """
    Min Operations - H copier
    """
    currentCount: int = 1  # initial H count
    copier: int = 1  # initial copier of the H (current count) in the file
    noOperations: int = 1  # Initial copy (first operation)
    while (n > currentCount):
        remainingCount = n - currentCount
        if remainingCount / (copier * 2) == remainingCount // (copier * 2):
            copier = copier * 2
            noOperations += 2  # Paste then copy
        else:
            noOperations += 1  # Paste
        currentCount += copier
    return noOperations
