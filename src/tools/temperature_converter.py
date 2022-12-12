from src.exceptions.invalid_value import InvalidValueProvidedException
from src.enums.temperature_units_enum import TemperatureUnit


class TemperatureConverter:
    """
    Class provides functions for temperature conversion.
    """

    def convert_from_celsius(self, temperature_unit: TemperatureUnit, value: float, precision=0):
        """
        Converts Celsius to provided unit.

        :param temperature_unit: Unit to convert.
        :param value: Value to convert.
        :param precision: Returned value decimal places.
        :return: Converted value to valid unit or value otherwise.
        """

        if temperature_unit == TemperatureUnit.Celsius:
            return round(value, precision)

        return self._converter(temperature_unit, value, precision, [
            lambda x: x,
            lambda x: (x * 1.8) + 32,
            lambda x: x + 273.15
        ])


    def convert_from_kelvin(self, temperature_unit: TemperatureUnit, value: float, precision=0):
        """
        Converts Kelvin to provided unit.

        :param temperature_unit: Unit to convert.
        :param value: Value to convert.
        :param precision: Returned value decimal places.
        :return: Converted value to valid unit or value otherwise.
        """

        if temperature_unit == TemperatureUnit.Kelvin:
            return round(value, precision)

        return self._converter(temperature_unit, value, precision, [
            lambda x: x - 273.15,
            lambda x: (x - 273.15) * 1.8 + 32,
            lambda x: x
        ])

    def convert_from_fahrenheit(self, temperature_unit: TemperatureUnit, value: float, precision=0):
        """
        Converts Fahrenheit to provided unit.

        :param temperature_unit: Unit to convert.
        :param value: Value to convert.
        :param precision: Returned value decimal places.
        :return: Converted value to valid unit or value otherwise.
        """
        if temperature_unit == TemperatureUnit.Fahrenheit:
            return round(value, precision)

        return self._converter(temperature_unit, value, precision, [
            lambda x: (x - 32) / 1.8,
            lambda x: x,
            lambda x: ((x - 32) / 1.8) + 273.15
        ])

    def _converter(self, temperature_unit, value, precision, conversion_funcs):
        """
        Converts value to provided unit.

        :param temperature_unit: Unit to convert.
        :param value: Value to convert.
        :param precision: Returned value decimal places.
        :param conversion_funcs: Conversion functions
        :return: Converted value to unit or value otherwise.
        """
        return round(conversion_funcs[temperature_unit](value), precision)
