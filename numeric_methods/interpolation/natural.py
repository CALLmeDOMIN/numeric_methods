from typing import List


def natural_interpolation(a: List[float], x: float) -> float:
    if len(a) == 0:
        return 0
    return a[0] + sum(a[i] * x ** i for i in range(1, len(a)))
