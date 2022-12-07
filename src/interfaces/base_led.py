from utime import sleep_us
from machine import PWM, Pin

from src.rpip_const import RPIP_MAX_PWM_DUTY


class BaseLed():
    step_constant = 257

    def __init__(self, pin, frequency=1000, default_duty=0, default_action_time_ms=500):

        # TODO : chcek if invalid pin

        self._led = PWM(Pin(pin))
        self._led.freq(frequency)
        self._duty = default_duty
        self._led.duty_u16(default_duty)
        self._default_action_time_ms = default_action_time_ms

    @property
    def duty(self):
        return self._duty

    @duty.setter
    def duty(self, duty):
        duty = max(min(self._on_duty(), duty), self._off_duty())
        self._duty = duty
        self._led.duty_u16(duty)

    def on(self, value=None, animate_time_ms=None):
        if value is None:
            self._gently(self._on_duty(), animate_time_ms)
            return

        duty = self._calc_duty(value)

        if self._duty == duty:
            return

        self._gently(duty, animate_time_ms)

    def off(self, animate_time_ms=None):
        if 0 == self._duty:
            return

        self._gently(self._off_duty(), animate_time_ms)

    def _gently(self, duty, animate_time_ms):
        if animate_time_ms is None:
            animate_time_ms = self._default_action_time_ms

        # 255*257 = 256^2 - 1 so 257 is step
        step = self.step_constant if duty > self._duty else -self.step_constant
        intervals = abs(self._duty - duty) / self.step_constant

        # value cannot equal 0 because _duty check
        timespan_us = self._calc_span_us(animate_time_ms, intervals)

        for i in range(intervals):
            self._duty = self._duty + step
            self._led.duty_u16(self._duty)
            sleep_us(timespan_us)

    def _calc_duty(self, value):
        return value * 257

    def _calc_span_us(self, total_time_ms, intervals):
        return int((total_time_ms * 1000) / intervals)

    def _off_duty(self):
        return 0

    def _on_duty(self):
        return RPIP_MAX_PWM_DUTY