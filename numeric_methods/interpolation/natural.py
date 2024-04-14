from typing import List


def natural_interpolation(a: List[float], x: float) -> float:
    """
    Function to calculate the interpolation of a polynomial using natural interpolation method.

    Args:
        a (List[float]): List of coefficients of the polynomial.
        x (float): Value to interpolate.

    Returns:
        float: Result of the interpolation.
    """
    if len(a) == 0:
        return 0
    return a[0] + sum(a[i] * x ** i for i in range(1, len(a)))
