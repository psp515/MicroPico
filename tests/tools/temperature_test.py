import unittest

from src.enums.temperature_units_enum import TemperatureUnit
from src.tools.temperature import Temperature

class TemperatureTest(unittest.TestCase):
    def test_change_to_kelvin(self):
        self.global_test(Temperature(20, TemperatureUnit.CELSIUS), TemperatureUnit.KELVIN, 293.1)
        self.global_test(Temperature(20, TemperatureUnit.KELVIN), TemperatureUnit.KELVIN, 20)
        self.global_test(Temperature(50, TemperatureUnit.FAHRENHEIT), TemperatureUnit.KELVIN, 283.1)

    def test_change_to_celcius(self):
        self.global_test(Temperature(20, TemperatureUnit.CELSIUS), TemperatureUnit.CELSIUS, 20)
        self.global_test(Temperature(293.15, TemperatureUnit.KELVIN), TemperatureUnit.CELSIUS, 20)
        self.global_test(Temperature(20, TemperatureUnit.FAHRENHEIT), TemperatureUnit.CELSIUS, -6.7)

    def test_change_to_fahrenheit(self):
        self.global_test(Temperature(20, TemperatureUnit.CELSIUS), TemperatureUnit.FAHRENHEIT, 68)
        self.global_test(Temperature(300, TemperatureUnit.KELVIN), TemperatureUnit.FAHRENHEIT, 80.3)
        self.global_test(Temperature(20, TemperatureUnit.FAHRENHEIT), TemperatureUnit.FAHRENHEIT, 20)

    def global_test(self, tmp: Temperature, new_unit: TemperatureUnit, ans: float):
        tmp.change_unit(new_unit, precision=1)
        self.assertEqual(tmp.temperature, ans, f"Should be {ans}.")
