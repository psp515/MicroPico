from src.interfaces.base_led import BaseLed
from utime import sleep_us


class Led(BaseLed):
    def blink(self, n=1, value=None, blink_time_ms=None):
        if blink_time_ms is None:
            blink_time_ms = self._default_action_time_ms

        timespan = self._calc_span_us(blink_time_ms, 2)
        duty = self._on_duty() if value is None else self._calc_duty(value)

        if self._duty != 0:
            self._led.duty_u16(0)
            sleep_us(100)

        for _ in range(n):
            self._blink(timespan, duty)

        self._led.duty_u16(self._duty)

    def _blink(self, timespan, duty):
        self._led.duty_u16(duty)
        sleep_us(timespan)
        self._led.duty_u16(0)
        sleep_us(timespan)