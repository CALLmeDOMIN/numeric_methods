from typing import List


def horner_interpolation(a: List[float], x: float) -> float:
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result
