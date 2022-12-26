class TemperatureUnit:
    """
    Temperature units enum.
    """
    Celsius = 0
    Fahrenheit = 1
    Kelvin = 2


def get_temperatureunit_name(unit:TemperatureUnit):
    if unit == TemperatureUnit.Kelvin:
        return "Kelvin"

    if unit == TemperatureUnit.Celsius:
        return "Celsius"

    return "Fahrenheit"


def get_temperatureunit_shortname(unit: TemperatureUnit):
    if unit == TemperatureUnit.Kelvin:
        return "K"

    if unit == TemperatureUnit.Celsius:
        return "°C"

    return "°F"




