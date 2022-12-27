class TemperatureUnit:
    """
    Temperature units enum.
    """
    CELSIUS = 0
    FAHRENHEIT = 1
    KELVIN = 2


def get_temperatureunit_name(unit: TemperatureUnit):
    if unit == TemperatureUnit.KELVIN:
        return "Kelvin"

    if unit == TemperatureUnit.CELSIUS:
        return "Celsius"

    return "Fahrenheit"


def get_temperatureunit_shortname(unit: TemperatureUnit):
    if unit == TemperatureUnit.KELVIN:
        return "K"

    if unit == TemperatureUnit.CELSIUS:
        return "°C"

    return "°F"




