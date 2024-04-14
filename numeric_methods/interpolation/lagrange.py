from typing import List


def lagrange_interpolation(x_points: List[float], y_points: List[float], x: float) -> float:
    n = len(x_points)
    result = 0
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        p = 1
        for j in range(n):
            xj = x_points[j]
            if i != j:
                p *= (x - xj) / (xi - xj)
        result += p * yi
    return result
