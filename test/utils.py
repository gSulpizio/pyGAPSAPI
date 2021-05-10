import numpy as np

x = list(np.linspace(0, 1, 100))


def langmuir_equation(nm, KH):
    return lambda p: (nm * KH * p) / (1 + KH * p)


loading = langmuir_equation(2, 5)

y = list(map(loading, x))
