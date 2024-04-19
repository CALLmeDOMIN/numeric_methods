from numpy import sqrt as np_sqrt
from typing import Callable

"""
    Weights and points for Gauss-Legendre quadrature.
"""

p_2 = [-1 / np_sqrt(3), 1 / np_sqrt(3)]
w_2 = [1, 1]

p_3 = [-np_sqrt(3 / 5), 0, np_sqrt(3 / 5)]
w_3 = [5 / 9, 8 / 9, 5 / 9]

p_4 = [-np_sqrt((3 + 2 * np_sqrt(6 / 5)) / 7), -np_sqrt((3 - 2 * np_sqrt(6 / 5)) / 7),
       np_sqrt((3 - 2 * np_sqrt(6 / 5)) / 7), np_sqrt((3 + 2 * np_sqrt(6 / 5)) / 7)]
w_4 = [(18 - np_sqrt(30)) / 36, (18 + np_sqrt(30)) / 36,
       (18 + np_sqrt(30)) / 36, (18 - np_sqrt(30)) / 36]

p_5 = [-1 / 3 * np_sqrt(5 + 2 * np_sqrt(10 / 7)), -1 / 3 * np_sqrt(5 - 2 * np_sqrt(10 / 7)),
       0, 1 / 3 * np_sqrt(5 - 2 * np_sqrt(10 / 7)), 1 / 3 * np_sqrt(5 + 2 * np_sqrt(10 / 7))]
w_5 = [(322 - 13 * np_sqrt(70)) / 900, (322 + 13 * np_sqrt(70)) / 900, 128 /
       225, (322 + 13 * np_sqrt(70)) / 900, (322 - 13 * np_sqrt(70)) / 900]


def gauss_legendre_formula(f: Callable[..., float], n: int, start: float, end: float) -> float:
    """
    Function to calculate the integral of a function using Gauss-Legendre formula.

    Args:
        f (Callable[..., float]): Function to integrate. Should return a number.
        n (int): Number of points to use in the formula.
        start (float): Start of the interval.
        end (float): End of the interval.

    Returns:
        float: Result of the integral.
    """
    p, w = [], []

    if n == 2:
        p, w = p_2, w_2
    elif n == 3:
        p, w = p_3, w_3
    elif n == 4:
        p, w = p_4, w_4
    elif n == 5:
        p, w = p_5, w_5

    integral = 0
    for i in range(n):
        integral += w[i] * f((end - start) / 2 * p[i] + (start + end) / 2)

    return (end - start) / 2 * integral


def generate_subintervals(amount, start, end):
    intervals = []
    step = (end - start) / amount
    for i in range(amount):
        intervals.append((start + i * step, start + (i + 1) * step))
    return intervals


def gauss_legendre_formula_intervals(f: Callable[..., float], n: int, start: float, end: float, amount: int) -> float:
    """
    Function to calculate the integral of a function using Gauss-Legendre formula with subintervals.

    Args:
        f (Callable[..., float]): Function to integrate. Should return a number.
        n (int): Number of points to use in the formula.
        start (float): Start of the interval.
        end (float): End of the interval.
        amount (int): Amount of subintervals to use.

    Returns:
        float: Result of the integral.
    """
    intervals = generate_subintervals(amount, start, end)
    result = 0
    for r in intervals:
        result += gauss_legendre_formula(f, n, r[0], r[1])
    return result
