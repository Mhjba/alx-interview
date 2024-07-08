#!/usr/bin/python3
"""Minimum Operations python3 challenge"""


def minOperations(n):
    """Calculates the fewest number of operations"""

    operations = 0
    counter = 2

    while n > 1:
        while n % counter == 0:
            operations += counter
            n /= counter
        counter += 1

    return operations
