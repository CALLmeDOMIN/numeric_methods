from typing import List


def horner_interpolation(a: List[float], x: float) -> float:
    """
    Function to calculate the interpolation of a polynomial using Horner's method.

    Args:
        a (List[float]): List of coefficients of the polynomial.
        x (float): Value to interpolate.

    Returns:
        float: Result of the interpolation.
    """
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result
