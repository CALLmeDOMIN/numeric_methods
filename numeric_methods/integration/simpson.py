def simpson_formula(f, n, a, b):
    n *= 2
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    integral = f(x[0]) + f(x[-1])

    for i in range(1, n, 2):
        integral += 4 * f(x[i])

    for i in range(2, n-1, 2):
        integral += 2 * f(x[i])

    integral *= h / 3

    return integral
