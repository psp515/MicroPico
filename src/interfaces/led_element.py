from utime import sleep_us
from machine import PWM, Pin

from src.rpip_const import RPIP_MAX_READ

# by default scale 0-255
# but can set certain duty

class BaseLed():
    def __init__(self, pin, frequency=1000, default_duty=0, default_action_time_ms=200):

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

        value = max(min(value, 255), 0)
        duty = self._calc_duty(value)
        if duty == self._duty:
            return

        self._gently(duty, animate_time_ms)


    def off(self, time = None):
        if 0 == self._duty:
            return

        self._gently(self._off_duty(), time)

    def _gently(self, duty, time):
        # TODO : refactor step=257 caculate number of steps and perform store value not duty ??
        if time is None:
            time = self._default_action_time_ms

        span = self._step if duty > self._duty else -self._step
        # value cannot equal 0 because _prev_duty check
        timespan_us = self._calc_span_us(time, abs(self._duty - duty))

        for i in range(self._duty, duty, span):
            self._led.duty_u16(i)
            sleep_us(timespan_us)

    def _calc_duty(self, value):
        return (self._on_duty() * value) / 256

    def _calc_span_us(self, total_time_ms, intervals):
        return int((total_time_ms*1000) / intervals)

    def _off_duty(self):
        return 0

    def _on_duty(self):
        return RPIP_MAX_READ