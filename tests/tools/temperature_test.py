import unittest

from src.enums.temperature_units_enum import TemperatureUnit
from src.tools.temperature import Temperature

class TemperatureTest(unittest.TestCase):
    def test_change_to_kelvin(self):
        self.global_test(Temperature(20, TemperatureUnit.Celsius), TemperatureUnit.Kelvin, 293.1)
        self.global_test(Temperature(20, TemperatureUnit.Kelvin), TemperatureUnit.Kelvin, 20)
        self.global_test(Temperature(50, TemperatureUnit.Fahrenheit), TemperatureUnit.Kelvin, 283.1)

    def test_change_to_celcius(self):
        self.global_test(Temperature(20, TemperatureUnit.Celsius), TemperatureUnit.Celsius, 20)
        self.global_test(Temperature(293.15, TemperatureUnit.Kelvin), TemperatureUnit.Celsius, 20)
        self.global_test(Temperature(20, TemperatureUnit.Fahrenheit), TemperatureUnit.Celsius, -6.7)

    def test_change_to_fahrenheit(self):
        self.global_test(Temperature(20, TemperatureUnit.Celsius), TemperatureUnit.Fahrenheit, 68)
        self.global_test(Temperature(300, TemperatureUnit.Kelvin), TemperatureUnit.Fahrenheit, 80.3)
        self.global_test(Temperature(20, TemperatureUnit.Fahrenheit), TemperatureUnit.Fahrenheit, 20)

    def global_test(self, tmp: Temperature, new_unit: TemperatureUnit, ans: float):
        tmp.change_unit(new_unit, precision=1)
        self.assertEqual(tmp.temperature, ans, f"Should be {ans}.")
