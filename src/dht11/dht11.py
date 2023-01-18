import utime
from machine import Pin

from src.dht11.const import *
from src.exceptions.invalid_pulse_count import InvalidPulseCount
from src.tools.byte_reciver import BytesReciver
from src.tools.bytes_validator import BytesValidator
from src.tools.temperature import Temperature
from src.enums.temperature_units_enum import TemperatureUnit


#TODO : Implement Device Class
#TODO : Fix

class DHT11:
    """
    Class for managing dht11 tempearture and humidity sensor.
    """
    _temperature: Temperature
    _humidity: float

    def __init__(self,
                 pin: int,
                 unit: TemperatureUnit = TemperatureUnit.CELSIUS,
                 precision: int = 0):
        """
        Initializes sensor.
        :param pin: Data pin index.
        :param unit: Default temperature unit.
        :param precision: Precision of returned values.
        """
        self._pin = pin
        self._temperature = Temperature(0, unit)
        self._humidity = -1

        self._last_measure_success = -1
        self._last_measure = -1

        self.unit = unit
        self.precision = precision

        self._measure()

    @property
    def last_measure_success(self):
        """
        Represents time when was last successful data read.
        :return: Time in ticks (us).
        """
        return self._last_measure_success

    @property
    def humidity(self):
        """
        Humidity read from sensor.
        :return: Humidity in RHA.
        """
        self._measure()
        return self._humidity

    @property
    def temperature(self):
        """
        Temperature read from sensor.
        :return: Temperature object with unit.
        """
        self._measure()
        return self._temperature

    def _measure(self):
        """
        Read data from sensor and updates stored data.
        """
        if self._can_measure():
            self._initial_signal()
            try:
                receiver = BytesReciver(self._pin, EXPECTED_PULSES, SKIP_PULSES, MAX_UNCHANGED, BIT_LEVEL_US)
                received_bytes = receiver.capture_bytes()
                if BytesValidator().validate_checksum(received_bytes[0:4], [received_bytes[4]]):
                    self._humidity = round(received_bytes[0] + received_bytes[1] / 10, 0)
                    tmp = Temperature(received_bytes[2] + received_bytes[3] / 10, TemperatureUnit.CELSIUS)
                    tmp.change_unit(self.unit)
                    self._temperature = tmp
                    self._last_measure_success = utime.ticks_us()
            except InvalidPulseCount as ipc:
                pass
            finally:
                self._last_measure = utime.ticks_us()

    def _can_measure(self):
        return abs(utime.ticks_us() - self._last_measure) > MIN_INTERVAL_US or self._last_measure == -1

    def _initial_signal(self):
        """
        Sends initializing signal for dht11 sensor.
        """
        pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
        pin.value(1)
        utime.sleep_ms(50)
        pin.value(0)
        utime.sleep_ms(14)
