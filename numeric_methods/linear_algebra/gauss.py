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
