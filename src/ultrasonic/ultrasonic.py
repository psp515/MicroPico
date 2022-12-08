from machine import Pin
import utime



class Ultrasonic:
    """
    Class for managing ultasonic distance sensor.
    """

    def __init__(self, echo_pin, trigger_pin):
        """
        Configures pins and sets trigger pin off.

        :param echo_pin: Pin connected to echo pin in sensor.
        :param trigger_pin: Pin connected to trigger pin in sensor.
        """
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.trigger.low()
        self.echo = Pin(echo_pin, Pin.IN)
        self.duration = -1

    def _measure(self):
        """
        Measures distance with sensor. In case of unsuccesful measurement duration is set to -1.
        """
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

        end = utime.ticks_us()

        self.duration = end - start

        if (self.duration > 38000):
            # read error
            self.duration = -1

    def _calculate(self, factor, precision):
        self._measure()

        if self.duration == -1:
            return -1

        return round(self.duration / factor, precision)

    def get_inch(self, precision=1):
        """
        Returns distance to obstacle in inches.

        :param precision: Precision of returned measurement.
        """
        return self._calculate(148, precision)

    def get_cm(self, precision=0):
        """
        Returns distance to obstacle in centimeters.

        :param precision: Precision of returned measurement.
        """
        return self._calculate(58, precision)

    def get_m(self, precision=2):
        """
        Returns distance to obstacle in centimeters.

        :param precision: Precision of returned measurement.
        """
        return self._calculate(5800, precision)


