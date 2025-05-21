# File Name: orbital_matrix_rotation.py
# Author: Zhang Anjun
# Date: 2025-05-21
# Version: 1.2
# © 2025 Zhang Anjun. All rights reserved.

from sys import exit as sysExit

def orbitalRotation(matrix, n, step):
    step = modStep(n, step)
    absStep = step * direction(step)
    if step == 0:
        return matrix
    i = 0
    while i != absStep:
        row, col = n, n
        latest = matrix[row][col]
        j = 0
        while j != calCircumference(n):
            nextRow, nextCol = orbit(n, step, row, col)
            matrix[nextRow][nextCol], latest = latest, matrix[nextRow][nextCol]
            row, col = nextRow, nextCol
            j = j + 1
        i = i + 1
    return matrix

def calCircumference(n):
    side = 7 - (2 * n)
    circumference = (4 * side) - 4
    return circumference

def modStep(n, step):
    sign = direction(step)
    absStep = sign * step
    circumference = calCircumference(n)
    step = (absStep % circumference) * sign
    return step

def nextSwapPosition(n, step, row, col):
    while step != 0:
        row, col = orbit(n, step, row, col)
        step = step - direction(step)
    return row, col

def orbit(n, step, row, col):                                       # Move 1 place clockwise/anti-clockwise. Use a loop to control moving
    if direction(step) == 1:
        row, col = clockwiseRotation(n, row, col)
    elif direction(step) == -1:
        row, col = anticlockwiseRotation(n, row, col)
    return row, col

def direction(step):                                                # Determine whether clockwise or anti-clockwise
    if step >= 0:
        return 1
    elif step < 0:
        return -1

def clockwiseRotation(n, row, col):                                 # Move 1 place clockwise
    if row == n and col < 6 - n:
        col = col + 1
    elif row < 6 - n and col == 6 - n:
        row = row + 1
    elif row == 6 - n and col > n:
        col = col - 1
    elif row > n and col == n:
        row = row - 1
    return row, col

def anticlockwiseRotation(n, row, col):                             # Move 1 place anti-clockwise
    if row == n and col > n:
        col = col - 1
    elif row < 6 - n and col == n:
        row = row + 1
    elif row == 6 - n and col < 6 - n:
        col = col + 1
    elif row > n and col == 6 - n:
        row = row - 1
    return row, col

def prompt():
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
    while row != 7:
        print(matrix[row])
        row = row + 1

def copyrightNotice():
    print("")
    print("Author: Zhang Anjun")
    print("Version: 1.2")
    print("© 2025 Zhang Anjun. All rights reserved.")
    print("")

matrix, n, step = prompt()
orbitalRotation(matrix, n, step)
print("")
print("Matrix after rotation: ")
printMatrix(matrix)

copyrightNotice()
input("Press Enter to exit. ")
sysExit(0)
