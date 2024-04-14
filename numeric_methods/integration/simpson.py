from typing import Callable


def simpson_formula(f: Callable[..., float], n: int, a: float, b: float) -> float:
    """
    Function to calculate the integral of a function using Simpson's formula.

    Args:
        f (Callable[..., float]): Function to integrate. Should return a number.
        n (int): Number of subintervals.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.

    Returns:
        float: Result of the integral.
    """
    n *= 2
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    integral = f(x[0]) + f(x[-1])

    for i in range(1, n, 2):
        integral += 4 * f(x[i])

    for i in range(2, n-1, 2):
        integral += 2 * f(x[i])

    integral *= h / 3

    return integral
