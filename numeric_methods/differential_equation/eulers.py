from typing import Callable, List, Tuple

def eulers_method(f: Callable[..., float], x: float, y: float, start: float, end: float, n: int) -> List[Tuple[float, float]]:
    """
    Function to solve a first order differential equation using Euler's method.

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
        y += h * f(y)
        x += h
        result.append((x, y))
    return result
