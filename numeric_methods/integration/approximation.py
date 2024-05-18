from typing import Callable, List


def approximate_integral(f: Callable[[float], float], base: List[any], start: float, end: float) -> List[float]:
    """
    Function to approximate the integral of a function using a polynomial base and the Gauss-Legendre formula.

    Args:
        f (Callable[[float], float]): Function to integrate.
        base (List[any]): Base of the polynomial.
        start (float): Start of the interval.
        end (float): End of the interval.

    Returns:
        List[float]: Coefficients of the polynomial.
    """
    from numeric_methods import gauss_legendre_formula, lu_decomposition

    matrix = []
    intercept = []

    for i in range(len(base)):
        row = []
        for j in range(len(base)):
            row.append(gauss_legendre_formula(
                lambda x: x**(i + j), 4, start, end))
        matrix.append(row)
        intercept.append(gauss_legendre_formula(
            lambda x: ((x ** i) * f(x)), 4, start, end))

    return lu_decomposition(len(base), matrix, intercept)
