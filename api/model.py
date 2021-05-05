from pydantic import BaseModel
from typing import Optional


class BETInput(BaseModel):
    """Default BET Fitting response"""

    inputPressure: list
    inputLoading: list
    inputPressureMode: str
    inputPressureUnit: str
    inputMaterialBasis: str
    inputMaterialUnit: str
    inputLoadingBasis: str
    inputLoadingUnit: str
    inputMaterial: str
    inputAdsorbate: str
    inputTemperature: int


class BETResponse(BaseModel):
    """Default BET Fitting response"""

    area: float
    c_const: float
    n_monolayer: float
    p_monolayer: float
    bet_slope: float
    bet_intercept: float
    corr_coef: float
    limits: list
