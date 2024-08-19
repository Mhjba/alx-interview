#!/usr/bin/python3
""" Making Change """

def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0

    count = [total+1]*(total+1)
    count[0] = 0

    for coin in coins:
        for tmp in range(coin, total+1):
            count[tmp] = min(count[tmp], count[tmp-coin] + 1)

    return count[total] if count[total] != total+1 else -1
