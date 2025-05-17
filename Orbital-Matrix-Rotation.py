# File Name: orbital_matrix_rotation.py
# Author: Zhang Anjun
# Date: 2025-05-07
# Version: 0.1
# © 2025 Zhang Anjun. All rights reserved.

def prompt():
    matrix = [
        [ 1,  2,  3,  4,  5,  6,  7],
        [ 8,  9, 10,  1,  2,  3,  4],
        [10, 11, 12, 13, 14, 15, 16],
        [ 0,  9,  8,  7,  6,  5,  4],
        [ 2,  4,  6,  8, 10,  9,  8],
        [ 4,  8,  0,  9,  5,  7,  3],
        [ 7,  6,  8,  2,  1,  0,  6],
    ]

    n = int(input("Please choose an orbit: "))
    step = int(input("Please enter a rotation number: "))
    return matrix, n, step

def direction(step):                        # Determine whether clockwise or anti-clockwise
    if step >= 0:
        return 1
    elif step < 0:
        return -1

def orbit(n, i, j, step):
    if direction(step) == 1:                # Move 1 place clockwise
        if i == n and j < 6 - n:
            j = j + 1
        elif i < 6 - n and j == 6 - n:
            i = i + 1
        elif i == 6 - n and j > n:
            j = j - 1
        elif i > n and j == n:
            i = i - 1
    else:                                   # Move 1 place anti-clockwise
        if i == n and j > n:
            j = j - 1
        elif i < 6 - n and j == n:
            i = i + 1
        elif i == 6 - n and j < 6 - n:
            j = j + 1
        elif i > n and j == 6 - n:
            i = i - 1
    return i, j


def swap(matrix, i, j, latest):
    matrix[i][j] = latest
    i, j = orbit(n, i, j, step)
    latest = matrix[i][j]

def rotation(matrix, n, step):
    i, j = n, n
    k = 20
    while k != 0:
        print(matrix[i][j])
        i, j = orbit(n, i, j, step)
        k = k - 1
    
matrix, n, step = prompt()
rotation(matrix, n, step)