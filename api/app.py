from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from BETtools import getBETArea
import logging


from model import BETInput, BETResponse

# from . import __version__


app = FastAPI(
    title="pyGAPS BET fitting",
    description="Offers a fit for BET surface calculation",
    # version=__version__,
)
# version?

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def root():
    """Return some HTML on the landing page"""
    return """
    <html>
        <head>
            <title>pyGAPS BET fitting</title>
        </head>
        <h1> Offers a fit for BET surface calculation </h1>
        <body>
            <p>This webservice provides BET fitting (BET surface calculation).</p>
            <p>Find the docs at <a href="./docs">/here</a> and the openAPI specfication at <a href="./openapi.json">/openapi.json</a>.</p>
        </body>
    </html>
    """


# version not working
@app.get("/version")
def read_version():
    """Return version for health checks"""
    return {"version": __version__}


@app.post("/BETFit", response_model=BETResponse)
def predict_xrd(parameters: BETInput):
    """Use pyGAPS to fit BET curves for isotherms"""
    try:
        return getBETArea(
            BETInput.inputPressure,
            BETInput.inputLoading,
            BETInput.inputPressureMode,
            BETInput.inputPressureUnit,
            BETInput.inputMaterialBasis,
            BETInput.inputMaterialUnit,
            BETInput.inputLoadingBasis,
            BETInput.inputLoadingUnit,
            BETInput.inputMaterial,
            BETInput.inputAdsorbate,
            BETInput.inputTemperature,
        )
    except Exception as excep:
        logger = logging.getLogger("api")
        logger.error("BET Fitting failed {}".format(excep))
        raise HTTPException(status_code=400, detail="BET Fitting failed")
