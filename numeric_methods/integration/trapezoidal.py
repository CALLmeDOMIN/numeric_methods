from typing import Callable


def trapezoidal_formula(f: Callable[..., float], n: int, a: float | int, b: float):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    result *= h

    return result
