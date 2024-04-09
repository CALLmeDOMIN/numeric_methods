import numpy as np


def print_matrix(matrix):
    np_matrix = np.array(matrix)
    print(np_matrix)
    print()


def matrix_pivoting(matrix, intercept, k):
    max_value = matrix[k][k]
    max_index = k
    for j in range(k + 1, len(matrix)):
        if abs(matrix[j][k]) > abs(max_value):
            max_value = matrix[j][k]
            max_index = j
    matrix[k], matrix[max_index] = matrix[max_index], matrix[k]
    intercept[k], intercept[max_index] = intercept[max_index], intercept[k]


def gaussian_elimination(matrix, intercept):
    for k in range(len(matrix)):
        matrix_pivoting(matrix, intercept, k)
        if matrix[k][k] == 0:
            continue
        for i in range(k + 1, len(matrix)):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, len(matrix)):
                matrix[i][j] -= factor * matrix[k][j]
            intercept[i] -= factor * intercept[k]


def lu_decomposition(length, matrix, intercept):
    L = np.zeros((length, length))
    U = np.zeros((length, length))

    for i in range(length):
        L[i][i] = 1
        for j in range(i, length):
            sm = 0
            for k in range(i):
                sm += L[i][k] * U[k][j]
            U[i][j] = matrix[i][j] - sm
        for j in range(i + 1, length):
            sm = 0
            for k in range(i):
                sm += L[j][k] * U[k][i]
            L[j][i] = (matrix[j][i] - sm) / U[i][i]

    z = np.zeros(length)
    for i in range(length):
        sm = 0
        for j in range(i):
            sm += L[i][j] * z[j]
        z[i] = intercept[i] - sm

    x = np.zeros(length)
    for i in range(length - 1, -1, -1):
        sm = 0
        for j in range(i + 1, length):
            sm += U[i][j] * x[j]
        x[i] = (z[i] - sm) / U[i][i]

    return x
