#!/usr/bin/python3
"""2D matrix rotation module."""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix."""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            temp = matrix[i][j]
            # Move elements from left to top
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move elements from bottom to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move elements from right to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Assign temp to right
            matrix[j][n - 1 - i] = temp
