def trapezoidal_formula(f, n, a, b):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    result *= h

    return result
