from typing import Callable, Tuple


def false_position_method(func: Callable[..., float], a: float, b: float, tol: float = 1e-6, max_iter: int = 100) -> Tuple[float, list, list]:
    """
    Function to find the root of a function using the false position method.

    Args:
        func (Callable[..., float]): Function to find the root of.
        a (float): Start of the interval.
        b (float): End of the interval.
        tol (float, optional): Tolerance to stop the method. Defaults to 1e-6.
        max_iter (int, optional): Maximum of iterations to perform. Defaults to 100.

    Returns:
        Tuple[float, list, list]: The root of the function, the iterations and the errors.
    """
    if func(a) * func(b) >= 0:
        print("Błąd: f(a) i f(b) muszą mieć różne znaki")
        return None

    iterations = []
    errors = []

    c = a
    for _ in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        iterations.append(c)
        errors.append(abs(func(c)))

        if abs(func(c)) < tol:
            return c, iterations, errors

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return c, iterations, errors
