# File Name: orbital_matrix_rotation.py
# Author: Zhang Anjun
# Date: 2025-05-18
# Version: 1.1
# © 2025 Zhang Anjun. All rights reserved.

def orbitalRotation(matrix, n, step):
    r, c = n, n                             # n, n is the starting upper left index
    latest = matrix[r][c]
    step = modStep(step)                    # Reduce rotation time when step is bigger than circumference
    r, c = nextPosition(n, step, r, c)      # "latest" is the previous number of the updated matrix[r][c]
    matrix, latest = swapElement(matrix, r, c, latest)
    while r != n or c != n:                 # Break the loop when go back to the starting point
        r, c = nextPosition(n, step, r, c)
        matrix, latest = swapElement(matrix, r, c, latest)
    return matrix

def modStep(step):
    side = 7 - (2 * n)
    circumference = (4 * side) - 4
    step = ((direction(step) * step) % circumference) * direction(step)
    return step

def nextPosition(n, step, r, c):            # Find the next position to swap
    while step != 0:
        r, c = orbit(n, step, r, c)
        step = step - direction(step)
    return r, c

def swapElement(matrix, r, c, latest):
    matrix[r][c], latest = latest, matrix[r][c]
    return matrix, latest

def orbit(n, step, r, c):                   # Move 1 place clockwise/anti-clockwise. Use a loop to control moving
    if direction(step) == 1:
        r, c = clockwiseRotation(n, r, c)
    elif direction(step) == -1:
        r, c = anticlockwiseRotation(n, r, c)
    return r, c

def direction(step):                        # Determine whether clockwise or anti-clockwise
    if step >= 0:
        return 1
    elif step < 0:
        return -1

def clockwiseRotation(n, r, c):             # Move 1 place clockwise
    if r == n and c < 6 - n:
        c = c + 1
    elif r < 6 - n and c == 6 - n:
        r = r + 1
    elif r == 6 - n and c > n:
        c = c - 1
    elif r > n and c == n:
        r = r - 1
    return r, c

def anticlockwiseRotation(n, r, c):         # Move 1 place anti-clockwise
    if r == n and c > n:
        c = c - 1
    elif r < 6 - n and c == n:
        r = r + 1
    elif r == 6 - n and c < 6 - n:
        c = c + 1
    elif r > n and c == 6 - n:
        r = r - 1
    return r, c

def prompt():
    # matrix = readMatrix()
    matrix = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 8, 1, 2, 1, 4],
        [1, 2, 7, 5, 4, 3, 9],
        [0, 9, 8, 7, 6, 5, 4],
        [2, 4, 6, 8, 5, 9, 8],
        [4, 8, 0, 9, 5, 7, 3],
        [7, 6, 8, 2, 1, 0, 6],
    ]
    n = int(input("Please choose an orbit (0-2): "))
    step = int(input("Please enter a rotation number: "))
    return matrix, n, step

def printMatrix(matrix):
    r = 0
    while r != 7:
        print(matrix[r])
        r = r + 1

def readMatrix():                           # Optional feature: let the user to enter a matrix
    matrix = []
    i = 0
    while i != 7:
        j = 0
        r = []
        while j != 7:
            value = int(input("Please enter a number: "))
            r.append(value)
            j = j + 1
        matrix.append(r)
        i = i + 1
    return matrix

matrix, n, step = prompt()
print("Matrix before rotation: ")
printMatrix(matrix)
orbitalRotation(matrix, n, step)
print("")
print("Matrix after rotation: ")
printMatrix(matrix)
