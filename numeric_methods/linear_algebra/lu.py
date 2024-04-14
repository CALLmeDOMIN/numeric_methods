from numpy import zeros as np_zeros


def lu_decomposition(length, matrix, intercept):
    L = np_zeros((length, length))
    U = np_zeros((length, length))

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

    z = np_zeros(length)
    for i in range(length):
        sm = 0
        for j in range(i):
            sm += L[i][j] * z[j]
        z[i] = intercept[i] - sm

    x = np_zeros(length)
    for i in range(length - 1, -1, -1):
        sm = 0
        for j in range(i + 1, length):
            sm += U[i][j] * x[j]
        x[i] = (z[i] - sm) / U[i][i]

    return x
