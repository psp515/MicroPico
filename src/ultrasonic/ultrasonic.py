from machine import Pin
import utime
from src.enums.length_units_enum import LengthUnit
from src.tools.distance import Distance


class Ultrasonic:
    """
    Class for managing ultasonic distance sensor.
    """
    precision: int
    unit: LengthUnit

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
        self._trigger = Pin(trigger_pin, Pin.OUT)
        self._trigger.low()
        self._echo = Pin(echo_pin, Pin.IN)
        self.unit = unit
        self.precision = precision

    @property
    def distance(self):
        """
        Returns measured distance in provided unit.

        :return: Distance object.
        """

        duration = self.measure()

        if duration == -1:
            return Distance(-1, self.unit)

        length = round(duration / self._duration_cast(self.unit), self.precision)
        return Distance(length, self.unit)

    def measure(self):
        """
        Measures distance with sensor.

        :return: Measurement duration, -1 (Invalid received information) or -2 (should be too big distance).
        """
        self._trigger.high()
        utime.sleep_us(10)
        self._trigger.low()

        primary = utime.ticks_us() + 10000

        while self._echo.value() == 0 and utime.ticks_us() < primary:
            pass

        start = utime.ticks_us()

        if primary <= start:
            # read error
            return -1

        secondary = start + 40000

        while self._echo.value() == 1 and utime.ticks_us() < secondary:
            pass

        duration = utime.ticks_us() - start

        if (duration > 38000):
            # read error
            return -2

        return duration

    def _duration_cast(self, unit: LengthUnit):
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