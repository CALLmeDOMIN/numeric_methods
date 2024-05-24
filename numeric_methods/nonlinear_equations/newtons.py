from typing import Callable, Tuple


def newtons_method(f: Callable[..., float], df: Callable[..., float], x0: float, tol: float = 1e-6, max_iter: int = 1000, eps: float = 1e-6) -> Tuple[float, int]:
    """
    Function to find the root of a function using Newton's method.

    Args:
        f (Callable[..., float]): Function to find the root of.
        df (Callable[..., float]): Derivative of the function.
        x0 (float): Initial guess
        tol (float, optional): Tolerance to stop the method. Defaults to 1e-6.
        max_iter (int, optional): Maximum of iterations to perform. Defaults to 1000.
        eps (float, optional): Epsilon to avoid division by zero. Defaults to 1e-6.

    Returns:
        Tuple[float, int]: The root of the function and the number of iterations.
    """
    x = x0
    for i in range(max_iter):
        try:
            x_new = x - f(x)/(df(x) + eps)
        except ZeroDivisionError:
            return None, i+1
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x_new, i+1
