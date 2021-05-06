from typing import Optional

from pydantic import BaseModel


class BETInput(BaseModel):
    """Default BET Fitting response"""

    pressure: list
    loading: list
    pressureMode: str
    pressureUnit: str
    materialBasis: str
    materialUnit: str
    loadingBasis: str
    loadingUnit: str
    material: str
    adsorbate: str
    temperature: int


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
