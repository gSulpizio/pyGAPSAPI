from api.bet_tools import getBETArea
from api.model import BETInput
from .utils import x, y
import numpy as np

inputParams = BETInput(
    pressure=x,
    loading=y,
    pressureMode="relative",
    pressureUnit="bar",
    materialBasis="mass",
    materialUnit="kg",
    loadingBasis="mass",
    loadingUnit="g",
    material="carbon",
    adsorbate="nitrogen",
    temperature=77,
)


def testFit():
    """Test fitting function"""
    response = getBETArea(dict(inputParams))
    assert np.abs(response["area"] - 3668.673520004670) < 0.1
