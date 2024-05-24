from typing import Callable, List, Tuple


def runge_kutta_method(f: Callable[..., float], x: float, y: float, start: float, end: float, n: int) -> List[Tuple[float, float]]:
    """
    Function to solve a first order differential equation using Runge-Kutta's method.

    Args:
        f (Callable[..., float]): Function representing the differential equation.
        x (float): Argument of the function.
        y (float): Value of the function.
        start (float): Start of the interval.
        end (float): End of the interval.
        n (int): Number of steps to take.

    Returns:
        List[Tuple[float, float]]: List of tuples with the x and y values of the function.
    """
    h = (end - start) / n
    result = []
    for _ in range(n):
        k1 = h * f(y)
        k2 = h * f(y + k1 / 2)
        k3 = h * f(y + k2 / 2)
        k4 = h * f(y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        result.append((x, y))
    return result
