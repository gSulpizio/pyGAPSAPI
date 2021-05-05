from func_timeout import func_set_timeout
import pygaps


def buildIsotherm(
    inputPressure,
    inputLoading,
    inputPressureMode,
    inputPressureUnit,
    inputMaterialBasis,
    inputMaterialUnit,
    inputLoadingBasis,
    inputLoadingUnit,
    inputMaterial,
    inputAdsorbate,
    inputTemperature,
):
    isotherm = pygaps.PointIsotherm(
        pressure=inputPressure,  # pressure here
        loading=inputLoading,  # loading here
        # Now the model details can be specified
        # Unit parameters can be specified
        pressure_mode=inputPressureMode,  # Working in absolute pressure
        pressure_unit=inputPressureUnit,  # with units of bar
        material_basis=inputMaterialBasis,  # Working on a mass material basis
        material_unit=inputMaterialUnit,  # with units of kg
        loading_basis=inputLoadingBasis,  # Working on a loading mass basis
        loading_unit=inputLoadingUnit,  # with units of g
        # Finally the isotherm parameters
        material=inputMaterial,  # Required
        adsorbate=inputAdsorbate,  # Required
        temperature=inputTemperature,  # Required
    )
    return isotherm


@func_set_timeout(60)
def getBETArea(
    inputPressure,
    inputLoading,
    inputPressureMode,
    inputPressureUnit,
    inputMaterialBasis,
    inputMaterialUnit,
    inputLoadingBasis,
    inputLoadingUnit,
    inputMaterial,
    inputAdsorbate,
    inputTemperature,
):
    isotherm = buildIsotherm(
        inputPressure,
        inputLoading,
        inputPressureMode,
        inputPressureUnit,
        inputMaterialBasis,
        inputMaterialUnit,
        inputLoadingBasis,
        inputLoadingUnit,
        inputMaterial,
        inputAdsorbate,
        inputTemperature,
    )
    params = pygaps.area_BET(isotherm)
    return params
