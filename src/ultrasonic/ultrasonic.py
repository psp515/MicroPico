from machine import Pin
import utime

from src.enums.length_units_enum import LengthUnit, ultrasonic_cast

class Ultrasonic:
    """
    Class for managing ultasonic distance sensor.
    """

    def __init__(self, trigger_pin, echo_pin):
        """
        Configures pins and sets trigger pin off.

        :param echo_pin:  Pin connected to echo pin in sensor.
        :param trigger_pin: Pin connected to trigger pin in sensor.
        """
        self._trigger = Pin(trigger_pin, Pin.OUT)
        self._trigger.low()
        self._echo = Pin(echo_pin, Pin.IN)

    def measure(self):
        """
        Measures distance with sensor.

        :return: Measurement duration or -1.
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
            return -1

        return duration

    def get_distance(self, unit=LengthUnit.Centimeter, precision=1):
        """
        Returns measured distance in provided unit.

        :param unit: Unit of returned value.
        :param precision: Precision of returned measurement.
        :return: Returns measured distance or -1 if measurement was unsuccessful.
        """

        duration = self.measure()

        if duration == -1:
            return -1

        return round(duration / ultrasonic_cast(unit), precision)


