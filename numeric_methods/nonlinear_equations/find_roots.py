from typing import Callable, Tuple, List


def find_roots(f: Callable[..., float], df: Callable[..., float], interval: Tuple[float, float], num_guesses: int, method: str = 'newtons', tol: float = 1e-6, max_iter: int = 1000, eps: float = 1e-6) -> List[float]:
    """
    Function to find the roots of a function using the Newton's or Secant method.

    Args:
        f (Callable[..., float]): Function to find the root of.
        df (Callable[..., float]): Derivative of the function.
        interval (Tuple[float, float]): Interval to search for the roots.
        num_guesses (int): Number of initial guesses to use.
        method (str, optional): Method to use ('newtons' or 'secant'). Defaults to 'newtons'.
        tol (float, optional): Tolerance to end the search. Defaults to 1e-6.
        max_iter (int, optional): Maximum of iterations to perform. Defaults to 1000.
        eps (float): Epsilon to avoid division by zero. Defaults to 1e-6.

    Raises:
        ValueError: If an invalid method is chosen.

    Returns:
        List[float]: The roots of the function.
    """
    from numpy import linspace as np_linspace

    roots = []
    initial_guesses = np_linspace(interval[0], interval[1], num_guesses)
    for x0 in initial_guesses:
        if method == 'newtons':
            from .newtons import newtons_method
            x, _ = newtons_method(f, df, x0, tol, max_iter, eps)
        elif method == 'secant':
            from .secant import secant_method
            x, _ = secant_method(f, x0, x0 + 1, tol, max_iter, eps)
        else:
            raise ValueError(
                'Invalid method. Please choose between "newtons" and "secant".')
        roots.append(x)
    return roots
