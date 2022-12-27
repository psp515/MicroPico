from src.enums.temperature_units_enum import TemperatureUnit, get_temperatureunit_shortname
from src.tools.temperature_converter import TemperatureConverter


class Temperature:
    """
    Represents tempearture with unit
    """
    _temperature: float
    _unit: TemperatureUnit

    def __init__(self, temperature: float, unit: TemperatureUnit):
        """
        Initializes temperature object
        :param temperature: Starting temperature.
        :param unit: Temperature unit.
        """
        self._temperature = temperature
        self._unit = unit

    @property
    def unit(self):
        """
        :return: Object unit.
        """
        return self._unit

    @property
    def temperature(self):
        """
        :return: Temperature value.
        """
        return self._temperature

    def __str__(self):
        return f"{self._temperature} {get_temperatureunit_shortname(self._unit)}"

    def change_unit(self, unit: TemperatureUnit, precision: int = 1):
        """
        Functions changes temperature unit and converts temperature to this unit.
        :param unit: TemperatureUnit enum item.
        :param precision: Precision of calculations.
        """
        tc = TemperatureConverter()

        if self._unit == TemperatureUnit.CELSIUS:
            self._temperature = tc.convert_from_celsius(unit, self._temperature, precision)
        elif self._unit == TemperatureUnit.KELVIN:
            self._temperature = tc.convert_from_kelvin(unit, self._temperature, precision)
        else:
            self._temperature = tc.convert_from_fahrenheit(unit, self._temperature, precision)

        self._unit = unit


