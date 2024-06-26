from typing import List
from numpy import array as np_array


def print_matrix(matrix: List[List[float]]) -> None:
    """
    Function to print a matrix.

    Args:
        matrix (List[List[float]]): Matrix to print.
    """
    np_matrix = np_array(matrix)
    print(np_matrix)
    print()
