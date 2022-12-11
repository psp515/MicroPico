import unittest

from src.exceptions.invalid_value import InvalidValueProvidedException
from src.tools.temperature_converter import TemperatureConverter
from src.enums.temperature_units_enum import TemperatureUnit


# TODO : test

class TemperatureConverterTest(unittest.TestCase):

    def convert_from_celcius(self):
        input = []
        ans = []
        self._global_test(input, ans, TemperatureConverter().convert_from_celsius)

    def convert_from_kelvin(self):
        input = []
        ans = []
        self._global_test(input, ans, TemperatureConverter().convert_from_kelvin)

    def convert_from_fahrenheit(self):
        input = []
        ans = []
        self._global_test(input, ans, TemperatureConverter().convert_from_fahrenheit)
        self._error_test(-1000,)
        self._error_test(-1000,)


    def _error_test(self, value, unit, func):
        error = False
        try:
            func(unit, value)
        except InvalidValueProvidedException:
            error = True

        self.assertEqual(error, True, "Should be error.")


    def _global_test(self, inputs, answers, func):
        i = 0
        for unit in []:
            for i in range(2):
                self.assertEqual(func(unit, inputs[i]), answers[i], f"Should be {answers[i]}.")
                i += 1
