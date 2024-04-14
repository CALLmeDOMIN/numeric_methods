from typing import Callable


def trapezoidal_formula(f: Callable[..., float], n: int, a: float, b: float) -> float:
    """
    Function to calculate the integral of a function using the trapezoidal formula.

    Args:
        f (Callable[..., float]): Function to integrate. Should return a number.
        n (int): Number of subintervals.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.

    Returns:
        float: Result of the integral.
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    result *= h

    return result
