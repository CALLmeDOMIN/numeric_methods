from typing import List


def mse(y_true: List[float], y_pred: List[float]) -> float:
    """
    Function to calculate the mean squared error.

    Args:
        y_true (List[float]): Real values.
        y_pred (List[float]): Predicted values.

    Returns:
        float: Mean squared error.
    """
    return sum((y_p - y_t) ** 2 for y_p, y_t in zip(y_pred, y_true)) / len(y_true)


def rmse(y_true: List[float], y_pred: List[float]) -> float:
    """
    Function to calculate the root mean squared error.

    Args:
        y_true (List[float]): Real values.
        y_pred (List[float]): Predicted values.

    Returns:
        float: Root mean squared error.
    """
    return mse(y_true, y_pred) ** 0.5


def mae(y_true: List[float], y_pred: List[float]) -> float:
    """
    Function to calculate the mean absolute error.

    Args:
        y_true (List[float]): Real values.
        y_pred (List[float]): Predicted values.

    Returns:
        float: Mean absolute error.
    """
    return sum(abs(y_p - y_t) for y_p, y_t in zip(y_pred, y_true)) / len(y_true)
