import numpy as np

x = list(np.linspace(0, 1, 100))


def langmuirEquation(nm, KH):
    return lambda p: (nm * KH * p) / (1 + KH * p)


loading = langmuirEquation(2, 5)

y = list(map(loading, x))
