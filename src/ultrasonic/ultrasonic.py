from machine import Pin
import utime
from src.enums.length_units_enum import LengthUnit
from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice
from src.tools.distance import Distance


class Ultrasonic(InputDevice):
    """
    Class for managing ultrasonic distance sensor.
    """
    precision: int
    unit: LengthUnit
    _pin: []
    _init_pin: []

    def __init__(self,
                 trigger_pin: int,
                 echo_pin: int,
                 unit: LengthUnit = LengthUnit.CENTIMETER,
                 precision: int = 1):
        """
        Configures pins and sets trigger pin off.

        :param echo_pin:  Pin connected to echo pin in sensor.
        :param trigger_pin: Pin connected to trigger pin in sensor.
        :param unit: Unit of distance value.
        :param precision:
        """

        self._pin = [trigger_pin, echo_pin]
        self._init_pin = [Pin(trigger_pin, Pin.OUT), Pin(echo_pin, Pin.IN)]

        self.trigger.low()
        self.unit = unit
        self.precision = precision
        self._state = DeviceState.ON

    @property
    def initialized_pin(self):
        """
        :return: Pin object representing device with list [trigger, echo].
        """
        return self._init_pin

    @property
    def pin(self):
        """
        :return: Returns pin number list [trigger, echo].
        """
        return self._pin

    @property
    def echo(self):
        """
        :return: Returns echo pin.
        """
        return self._init_pin[1]

    @property
    def trigger(self):
        """
        :return: Returns trigger pin.
        """
        return self._init_pin[0]

    @property
    def distance(self):
        """
        Returns measured distance in provided unit.

        :return: Distance object.
        """

        if self._state is DeviceState.BUSY:
            return Distance(-1, self.unit)

        self._state = DeviceState.BUSY

        duration = self._read()
        length = round(duration / self._duration_to_length(self.unit), self.precision)

        self._state = DeviceState.ON

        if duration == -1:
            return Distance(-1, self.unit)

        return Distance(length, self.unit)

    def measure(self):
        """
        Measures distance with sensor.

        :return: Measurement duration, -1 (Invalid received information) or -2 (should be too big distance).
        """
        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY

        duration = self._read()

        self._state = DeviceState.ON

        return duration

    def _read(self):
        self.trigger.high()
        utime.sleep_us(10)
        self.trigger.low()

        primary = utime.ticks_us() + 10000

        while self.echo.value() == 0 and utime.ticks_us() < primary:
            pass

        start = utime.ticks_us()

        if primary <= start:
            # read error
            return -1

        secondary = start + 40000

        while self.echo.value() == 1 and utime.ticks_us() < secondary:
            pass

        duration = utime.ticks_us() - start

        if (duration > 38000):
            # read error
            return -2

        return duration


    def _duration_to_length(self, unit: LengthUnit):
        """
        Converts unit to constant used in calculations for ultrasonic distance sensor.

        :param unit: Unit class object.
        :return: Constant for ultrasonic sensor.
        """
        if unit == LengthUnit.CENTIMETER:
            return 58
        if unit == LengthUnit.METER:
            return 5800
        if unit == LengthUnit.INCH:
            return 148
        return 5.8