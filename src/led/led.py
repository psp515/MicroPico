from src.interfaces.base_led import BaseLed
from utime import sleep_us


class Led(BaseLed):
    """
    Simple Led class for managing single led element.
    """
    def __init__(self, pin, frequency=1000, default_duty=0, default_blink_time_ms=500, interval_break_us=1500):
        super().__init__(pin, frequency, default_duty, interval_break_us)
        self.default_blink_time_ms = default_blink_time_ms

    def blink(self, n=1, value=None, blink_time_ms=None):
        """
        Blinks led. If led is on, method first disables led then blinks and after blinks automatically turns led on
        with previous value (Total time needed is extended by half of blink_time_ms or default_blink_time_ms).

        :param n: Number of blinks.
        :param value: Blink glow.
        :param blink_time_ms: Time for one blink.
        """

        if blink_time_ms is not None:
            timespan = self._calc_span_us(blink_time_ms, 2)
        else:
            timespan = self._calc_span_us(self.default_blink_time_ms, 2)

        duty = self._on_duty() if value is None else self._calc_duty(value)

        if self._duty != 0:
            self._led.duty_u16(0)
            sleep_us(self.interval_span_us)

        for _ in range(n):
            self._blink(timespan, duty)

        self._led.duty_u16(self._duty)

    def _blink(self, timespan, duty):
        """
        Blinks led.

        :param timespan: Half of total blink time.
        :param duty: Led glow.
        """
        self._led.duty_u16(duty)
        sleep_us(timespan)
        self._led.duty_u16(0)
        sleep_us(timespan)
