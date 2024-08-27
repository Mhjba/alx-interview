#!/usr/bin/python3
"""Island Perimeter """


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    """

    perimete = 0
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if (grid[i][k] == 1):
                if (i <= 0 or grid[i - 1][k] == 0):
                    perimete += 1
                if (i >= len(grid) - 1 or grid[i + 1][k] == 0):
                    perimete += 1
                if (k <= 0 or grid[i][k - 1] == 0):
                    perimete += 1
                if (k >= len(grid[i]) - 1 or grid[i][k + 1] == 0):
                    perimete += 1
    return perimete
