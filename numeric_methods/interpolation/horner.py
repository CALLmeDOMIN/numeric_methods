def horner_interpolation(a, x):
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result
