"""Testing basic working of the API"""

from fastapi.testclient import TestClient

from BETtools import getBETArea
from .app import app


# client = TestClient(app)

x = list(map(lambda x: x / 100, list(range(0, 101))))


def langmuirEquation(nm, KH):
    return lambda p: (nm * KH * p) / (1 + KH * p)


loading = langmuirEquation(2, 5)

y = list(map(loading, x))


params = getBETArea(
    x, y, "relative", "bar", "mass", "kg", "mass", "g", "carbon", "nitrogen", 77
)
print(y)
