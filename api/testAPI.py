"""Testing basic working of the API"""

from fastapi.testclient import TestClient
import json


from BETtools import getBETArea
from app import app
from model import BETInput


client = TestClient(app)

x = list(map(lambda x: x / 100, list(range(0, 101))))


def langmuirEquation(nm, KH):
    return lambda p: (nm * KH * p) / (1 + KH * p)


loading = langmuirEquation(2, 5)

y = list(map(loading, x))


inputParams2 = {
    "inputPressure": x,
    "inputLoading": y,
    "inputPressureMode": "relative",
    "inputPressureUnit": "bar",
    "inputMaterialBasis": "mass",
    "inputMaterialUnit": "kg",
    "inputLoadingBasis": "mass",
    "inputLoadingUnit": "g",
    "inputMaterial": "carbon",
    "inputAdsorbate": "nitrogen",
    "inputTemperature": 77,
}

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


def testFitAPI(inputParams):
    """Test fitting endpoint"""
    response = client.post("/BETFit", json=json.dumps(inputParams.__dict__))
    print(response.status_code)

    body = json.loads(response.text)
    print(body)


def testFit(inputParams):
    """Test fitting function"""
    response = getBETArea(inputParams)
    print(response)


def testReadMain():
    response = client.get("/")
    assert response.status_code == 200


if __name__ == "__main__":
    testFit(inputParams)
    testFitAPI(inputParams)
    testReadMain()
