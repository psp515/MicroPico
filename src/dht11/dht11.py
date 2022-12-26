import utime
from machine import Pin
from micropython import const

from src.exceptions.invalid_pulse_count import InvalidPulseCount
from src.tools.byte_reciver import BytesReciver
from src.tools.bytes_validator import BytesValidator
from src.tools.temperature import Temperature
from src.enums.temperature_units_enum import TemperatureUnit

MAX_UNCHANGED = const(100)
MIN_INTERVAL_US = const(500000)
BIT_LEVEL_US = const(50)
EXPECTED_PULSES = const(84)
SKIP_PULSES = const(4)


class DHT11:
    _temperature: Temperature
    _humidity: float

    def __init__(self,
                 pin: int,
                 unit: TemperatureUnit = TemperatureUnit.Celsius,
                 precision: int = 0,
                 log_errors=False):

        self._pin = pin
        self._temperature = Temperature(0, unit)
        self._humidity = -1

        self._last_measure_success = -1
        self._last_measure = utime.ticks_us()

        self.unit = unit
        self.precision = precision
        self.log_errors = log_errors

        self._measure()

    @property
    def last_measure_success(self):
        """
        Represents time when was last successfull data read.
        :return: Time in ticks (us).
        """
        return self._last_measure_success

    @property
    def humidity(self):
        self._measure()
        return self._humidity

    @property
    def temperature(self):
        self._measure()
        return self._temperature

    def _measure(self):
        if utime.ticks_diff(utime.ticks_us(), self._last_measure) < MIN_INTERVAL_US and (
                self._last_measure_success != -1):
            return

        pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
        self._initial_signal(pin)

        try:
            receiver = BytesReciver(pin, EXPECTED_PULSES, SKIP_PULSES, MAX_UNCHANGED, BIT_LEVEL_US)
            received_bytes = receiver.capture_bytes()
            if BytesValidator().validate_checksum(received_bytes[0:4],
                                                  [received_bytes[4]]):
                self._humidity = round(received_bytes[0] + received_bytes[1] / 10, 0)
                tmp = Temperature(received_bytes[2] + received_bytes[3] / 10, TemperatureUnit.Celsius)
                tmp.change_unit(self.unit)
                self._temperature = tmp
                self._last_measure_success = utime.ticks_us()
        except InvalidPulseCount as ipc:
            if self.log_errors:
                print(ipc)
        finally:
            self._last_measure = utime.ticks_us()

    def _initial_signal(self, pin):
        pin.value(1)
        utime.sleep_ms(50)
        pin.value(0)
        utime.sleep_ms(14)

