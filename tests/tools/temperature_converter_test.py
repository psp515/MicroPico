import unittest

from src.tools.temperature_converter import TemperatureConverter
from src.enums.temperature_units_enum import TemperatureUnit


class TemperatureConverterTest(unittest.TestCase):
    def test_convert_from_celcius(self):
        input = [[100, 120, 300],
                 [100, -120, 300.01],
                 [100, -120, 300]]
        ans = [[100, 120, 300],
               [373.1, 153.1, 573.2],
               [212, -184, 572]]
        self._global_test(input, ans, TemperatureConverter().convert_from_celsius, 1)

    def test_convert_from_kelvin(self):
        input = [[100, 345, 300],
                 [100, -120, 300.01],
                 [100, -120, 300]]
        ans = [[-173, 72, 27],
               [100, -120, 300],
               [-280, -676, 80]]
        self._global_test(input, ans, TemperatureConverter().convert_from_kelvin, 0)

    def test_convert_from_fahrenheit(self):
        input = [[100, 345, 300],
                 [100, -120, 300.01],
                 [100, -120, 300]]
        ans = [[37.78, 173.89, 148.89],
               [310.93, 188.71, 422.04],
               [100, -120, 300]]
        self._global_test(input, ans, TemperatureConverter().convert_from_fahrenheit, 2)

    def _global_test(self, inputs, answers, func, precision):
        i = 0
        for unit in [TemperatureUnit.Celsius, TemperatureUnit.Kelvin, TemperatureUnit.Fahrenheit]:
            for j in range(len(answers[i])):
                self.assertEqual(func(unit, inputs[i][j], precision), answers[i][j], f"Should be {answers[i][j]}.")
            i += 1

