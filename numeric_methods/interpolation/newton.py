from typing import List


def divided_diff(x: List[float], y: List[float]) -> List[float]:
    n = len(y)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton_interpolation(x: List[float], y: List[float], x_val: float) -> float:
    n = len(x)
    a = divided_diff(x, y)
    result = a[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_val - x[i]) + a[i]
    return result
