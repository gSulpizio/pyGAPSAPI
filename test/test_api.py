"""Testing basic working of the API"""

from fastapi.testclient import TestClient
import json


from api.app import app
from api.model import BETInput
from .utils import x, y

client = TestClient(app)


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


def testFitAPI():
    """Test fitting endpoint"""
    response = client.post("/BETFit", json=dict(inputParams))
    print(response.status_code)

    body = json.loads(response.text)
    print(body)


def testReadMain():
    response = client.get("/")
    assert response.status_code == 200

