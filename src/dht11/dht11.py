import utime
from machine import Pin
from micropython import const

from src.tools.temperature import Temperature
from src.tools.temperature_converter import TemperatureConverter
from src.enums.temperature_units_enum import TemperatureUnit



MAX_UNCHANGED = const(100)
MIN_INTERVAL_US = const(200000)
HIGH_LEVEL = const(50)
EXPECTED_PULSES = const(84)

class DHT11:
    """
    Instance of DHT11 sensor.
    """
    _temperature: float
    _humidity: float

    precision: int
    unit: TemperatureUnit
    throws_measure_exceptions: bool

    def __init__(self, pin: int,
                 unit: TemperatureUnit = TemperatureUnit.Celsius,
                 precision: int = 0,
                 throws_measure_exceptions: bool = False):

        self._pin = Pin(pin, Pin.OUT, Pin.PULL_DOWN)
        self._temperature = -1
        self._humidity = -1
        self._last_measure_success = utime.ticks_us()

        self.unit = unit
        self.precision = precision
        self.throws_measure_exceptions = throws_measure_exceptions

    @property
    def last_measure_success(self):
        """
        Represents last successful data read from sensor.
        :return: Time in ticks (us).
        """
        return self._last_measure_success

    @property
    def temperature(self):
        if self._can_measure():
            self._measure()

        temperature = TemperatureConverter().convert_from_celsius(self.unit, self._temperature, self.precision)
        return Temperature(temperature, self.unit)

    @property
    def humidity(self):
        if self._can_measure():
            self._measure()

        return self._humidity

    def _can_measure(self):
        return self._last_measure_success + MIN_INTERVAL_US <= utime.ticks_us()

    def _measure(self):
        """
        Reads temperature and humidity from sensor.
        """

        #TODO read time span ()


        self._last_measure_success = utime.ticks_us()

    def _initial_signal(self):
        pass

    def _capture_pulses(self):
