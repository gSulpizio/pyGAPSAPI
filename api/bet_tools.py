import pygaps


def build_isotherm(inputParams):
    isotherm = pygaps.PointIsotherm(
        pressure=inputParams["pressure"],  # pressure here
        loading=inputParams["loading"],  # loading here
        # Now the model details can be specified
        # Unit parameters can be specified
        pressure_mode=inputParams["pressureMode"],  # Working in absolute pressure
        pressure_unit=inputParams["pressureUnit"],  # with units of bar
        material_basis=inputParams["materialBasis"],  # Working on a mass material basis
        material_unit=inputParams["materialUnit"],  # with units of kg
        loading_basis=inputParams["loadingBasis"],  # Working on a loading mass basis
        loading_unit=inputParams["loadingUnit"],  # with units of g
        # Finally the isotherm parameters
        material=inputParams["material"],  # Required
        adsorbate=inputParams["adsorbate"],  # Required
        temperature=inputParams["temperature"],  # Required
    )
    return isotherm


def get_BET_area(inputparams):

    isotherm = build_isotherm(inputparams)
    params = pygaps.area_BET(isotherm)
    return params
