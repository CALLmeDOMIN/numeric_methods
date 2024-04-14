def natural_interpolation(a, x):
    if len(a) == 0:
        return 0
    return a[0] + sum(a[i] * x ** i for i in range(1, len(a)))
