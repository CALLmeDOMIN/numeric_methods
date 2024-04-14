from typing import List


def mse(y_true: List[float], y_pred: List[float]) -> float:
    return sum((y_p - y_t) ** 2 for y_p, y_t in zip(y_pred, y_true)) / len(y_true)


def rmse(y_true: List[float], y_pred: List[float]) -> float:
    return mse(y_true, y_pred) ** 0.5


def mae(y_true: List[float], y_pred: List[float]) -> float:
    return sum(abs(y_p - y_t) for y_p, y_t in zip(y_pred, y_true)) / len(y_true)
