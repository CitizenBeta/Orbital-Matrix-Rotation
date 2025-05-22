# File Name: orbital_matrix_rotation.py
# Author: Zhang Anjun
# Date: 2025-05-22
# Version: 2.0
# © 2025 Zhang Anjun. All rights reserved.

from sys import exit as sysExit

def copyrightNotice():
    print("")
    print("Author: Zhang Anjun")
    print("Version: 2.0")
    print("© 2025 Zhang Anjun. All rights reserved.")
    print("")

def orbitalRotation(matrix, n, step):
    direction = sign(step)                                  # Find rotation direction
    step = modStep(n, step)                                 # Avoid full-circle rotations
    i = 0
    while i != step:                                        # Move multiple steps
        matrix = rotateOnePlace(matrix, n, direction)       # Move one place each time
        i = i + 1
    return matrix

def sign(step):
    if step >= 0:
        return 1
    elif step < 0:
        return -1

def modStep(n, step):
    circumference = getCircumference(n)
    if step < 0:
        step = step * (-1)                                  # Keep the "step" positive
    step = step % circumference                             # Reduce by full rotations
    return step

def rotateOnePlace(matrix, n, direction):                   # Move one place clockwise/anti-clockwise
    row, col = n, n                                         # Start at the top-left corner
    latest = matrix[row][col]
    j = 0
    while j != getCircumference(n):
        if direction == 1:                                  # Find next clockwise position
            row, col = nextClockwise(n, row, col)
        elif direction == -1:                               # Find next counterclockwise position
            row, col = nextCounterclockwise(n, row, col)
        matrix[row][col], latest = latest, matrix[row][col] # Place "latest" into new position. Take its old value into "latest"
        j = j + 1
    return matrix

def getCircumference(n):
    side = 7 - (2 * n)
    circumference = (4 * side) - 4
    return circumference

def nextClockwise(n, row, col):                             # Find next clockwise position
    if row == n and col < 6 - n:
        col = col + 1
    elif row < 6 - n and col == 6 - n:
        row = row + 1
    elif row == 6 - n and col > n:
        col = col - 1
    elif row > n and col == n:
        row = row - 1
    return row, col

def nextCounterclockwise(n, row, col):                      # Find next counterclockwise position
    if row == n and col > n:
        col = col - 1
    elif row < 6 - n and col == n:
        row = row + 1
    elif row == 6 - n and col < 6 - n:
        col = col + 1
    elif row > n and col == 6 - n:
        row = row - 1
    return row, col

def prompt():                                               # Get user input
    print("Matrix before rotation: ")
    matrix = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 8, 1, 2, 1, 4],
        [1, 2, 7, 5, 4, 3, 9],
        [0, 9, 8, 7, 6, 5, 4],
        [2, 4, 6, 8, 5, 9, 8],
        [4, 8, 0, 9, 5, 7, 3],
        [7, 6, 8, 2, 1, 0, 6],
    ]
    printMatrix(matrix)
    print("")
    n = int(input("Please choose an orbit (0-2): "))
    step = int(input("Please enter a rotation number: "))
    return matrix, n, step

def printMatrix(matrix):
    row = 0
    while row < 7:
        col = 0
        while col < 7:
            print(str(matrix[row][col]) + " ", end="")
            col = col + 1
        print("")
        row = row + 1

matrix, n, step = prompt()
orbitalRotation(matrix, n, step)
print("")
print("Matrix after rotation: ")
printMatrix(matrix)

copyrightNotice()
input("Press Enter to exit. ")
sysExit(0)
