import utime
from machine import Pin

from src.tools.temperature_converter import TemperatureConverter
from src.enums.temperature_units_enum import TemperatureUnit


class DHT11:
    """
    Instance of DHT11 sensor.
    """
    _temperature: float
    _humidity: float

    def __init__(self, pin):
        """
        Initializes object

        :param pin:
        """
        self._pin = Pin(pin, Pin.OUT, Pin.PULL_DOWN)
        self._last_measure = utime.ticks_us()
        self._temperature = -1
        self._humidity = -1

    def get_temperature(self, temperature_unit=TemperatureUnit.Celsius, precision=0):
        """
        Refreshes data from sensor and returns its.

        :param temperature_unit: Unit of returned temperature.
        :param precision: Precision of returned temperature.
        :return: Temperature.
        """
        self._measure()
        return TemperatureConverter().convert_from_celsius(temperature_unit, self._temperature, precision)

    def get_humidity(self):
        """
        Refreshes data from sensor and returns its.

        :return: Humidity.
        """
        self._measure()
        return self._humidity

    def get(self, temperature_unit=TemperatureUnit.Celsius, precision=0):
        """
        Refreshes data from sensor and returns its.

        :param temperature_unit: Unit of returned temperature.
        :param precision: Precision of returned temperature.
        :return: Tuple (temperature, humidity)
        """
        self._measure()
        return (TemperatureConverter().convert_from_celsius(temperature_unit, self._temperature, precision), self._humidity)

    def _measure(self):
        """
        Reads temperature and humidity from sensor.
        """


        #TODO read time span ()
        pass