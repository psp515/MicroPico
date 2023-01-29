from utime import sleep_us, ticks_us, ticks_diff, sleep_ms
from machine import Pin

from src.dht11.const import *
from src.enums.state_enum import DeviceState
from src.exceptions.invalid_pulse_count import InvalidPulseCount
from src.interfaces.input_device import InputDevice
from src.tools.byte_reciver import BytesReciver
from src.tools.bytes_validator import BytesValidator
from src.tools.temperature import Temperature
from src.enums.temperature_units_enum import TemperatureUnit


class DHT11(InputDevice):
    """
    Class for managing dht11 temperature and humidity sensor.
    """
    _temperature: Temperature
    _humidity: float

    def __init__(self, pin: int, unit: TemperatureUnit = TemperatureUnit.CELSIUS, precision: int = 0):
        """
        Initializes sensor.
        :param pin: Data pin index.
        :param unit: Default temperature unit.
        :param precision: Precision of returned values.
        """
        super().__init__(pin)
        self._temperature = Temperature(0, unit)
        self._humidity = -1

        self._last_measure_success = -1
        self._last_measure = -1
        self.unit = unit
        self.precision = precision
        sleep_us(MIN_INTERVAL_US)
        self._read()

    @property
    def initialized_pin(self):
        """
        Function returns None in this module because pin is initialized multiple times.
        (In and Out operations are made on single pin)
        :return: None.
        """
        return None

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
        If device is busy function returns last read data.
        :return: Humidity in RHA.
        """
        if self._state is DeviceState.BUSY:
            return self._humidity

        self._state = DeviceState.BUSY

        self._read()

        self._state = DeviceState.ON

        return self._humidity

    @property
    def temperature(self):
        """
        Temperature read from sensor.
        If device is busy function returns last read data.
        :return: Temperature object with unit.
        """

        if self._state is DeviceState.BUSY:
            return self._temperature

        self._state = DeviceState.BUSY

        self._read()

        self._state = DeviceState.ON

        return self._temperature

    def _read(self):
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
                    self._last_measure_success = ticks_us()
            except InvalidPulseCount as ipc:
                pass
            finally:
                self._last_measure = ticks_us()

    def _can_measure(self):
        """
        Indicates if reading data from device is possible.
        """
        return ticks_diff(ticks_us(), self._last_measure) > MIN_INTERVAL_US or self._last_measure == -1

    def _initial_signal(self):
        """
        Sends initializing signal for dht11 sensor.
        """
        pin = Pin(self._pin, Pin.OUT, Pin.PULL_DOWN)
        pin.value(1)
        sleep_ms(50)
        pin.value(0)
        sleep_ms(14)
