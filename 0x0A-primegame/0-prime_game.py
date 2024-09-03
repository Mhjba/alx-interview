#!/usr/bin/python3
"""Define isWineer function, a solution to the Prime Game problem"""


def rm_multiples(ls, x):
    """removes multiple of primes"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

def isWinner(x, nums):
    """ Determines the winner of the prime game """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_picks = 0
    maria_picks = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben_picks += 1
        else:
            maria_picks += 1
    if ben_picks > maria_picks:
        return "Ben"
    if maria_picks > ben_picks:
        return "Maria"
    return None
