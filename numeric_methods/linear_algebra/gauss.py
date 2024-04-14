from typing import List, Tuple


def matrix_pivoting(matrix: List[List[float]], intercept: List[float], k: int) -> None:
    """
    Function to pivot the matrix.

    Args:
        matrix (List[List[float]]): Matrix to pivot.
        intercept (List[float]): Intercept of the matrix.
        k (int): Index of the current iteration.
    """

    max_value = matrix[k][k]
    max_index = k
    for j in range(k + 1, len(matrix)):
        if abs(matrix[j][k]) > abs(max_value):
            max_value = matrix[j][k]
            max_index = j

    matrix[k], matrix[max_index] = matrix[max_index], matrix[k]
    intercept[k], intercept[max_index] = intercept[max_index], intercept[k]


def gaussian_elimination(matrix: List[List[float]], intercept: List[float]) -> Tuple[List[List[float]], List[float]]:
    """
    Function to solve a system of linear equations using the Gaussian elimination method.

    Args:
        matrix (List[List[float]]): Matrix of the system.
        intercept (List[float]): Intercept of the system.

    Returns:
        Tuple[List[List[float]], List[float]]: Tuple with the matrix and the intercept of the system.
    """
    for k in range(len(matrix)):
        matrix_pivoting(matrix, intercept, k)
        if matrix[k][k] == 0:
            continue
        for i in range(k + 1, len(matrix)):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, len(matrix)):
                matrix[i][j] -= factor * matrix[k][j]
            intercept[i] -= factor * intercept[k]

    return (matrix, intercept)
