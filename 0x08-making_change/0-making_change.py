#!/usr/bin/env python3
"""makeChange code file
"""


def makeChange(coins, total):
    """
    makeChange code file
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    coin_count = 0
    for coin in coins:
        while coin <= total:
            total -= coin
            coin_count += 1
    if total != 0:
        coin_count = -1
    return coin_count
