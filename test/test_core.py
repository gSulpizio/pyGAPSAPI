from api.BETtools import getBETArea

from .utils import x,y 

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
    response = getBETArea(inputParams)
    print(response)
