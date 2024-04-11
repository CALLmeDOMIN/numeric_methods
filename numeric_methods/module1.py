import numpy as np


def print_matrix(matrix):
    np_matrix = np.array(matrix)
    print(np_matrix)
    print()


def natural(a, x):
    if len(a) == 0:
        return 0
    return a[0] + sum(a[i] * x ** i for i in range(1, len(a)))


def horner(a, x):
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result


def divided_diff(x, y):
    n = len(y)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton(x, y, x_val):
    n = len(x)
    a = divided_diff(x, y)
    result = a[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_val - x[i]) + a[i]
    return result


def mse(y_true, y_pred):
    return sum((y_p - y_t) ** 2 for y_p, y_t in zip(y_pred, y_true)) / len(y_true)


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
