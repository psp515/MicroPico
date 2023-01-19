from machine import PWM, Pin
from utime import sleep_us

from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice

#TODO : Finish Class
# TODO Think of using inus for nicer animation
class OutputPWMDevice(OutputDevice):
    """
    Base class for pwm output devices.
    """

    step_constant = 257
    """ Step is solution of equations 255 * x = 256^2 - 1, it is used to calculate in duty 
    because on function takes value in range 0-255."""

    _init_pin: PWM

    def __init__(self, pin: int, frequency=1000):
        self._pin = pin
        self._state = DeviceState.OFF
        self._init_pin = PWM(Pin(pin))
        self._init_pin.freq(frequency)
        self._init_pin.duty_u16(0)




    @property
    def duty(self):
        """
        Stores lest PWM duty used in element.

        Returns
        -------
        :return: Latest PWM duty.

        """
        return self._duty

    @duty.setter
    def duty(self, duty):
        """
        Can be used to set element duty directly.

        :param duty: Duty to be set on element.
        """
        duty = max(min(self._on_duty(), duty), self._off_duty())
        self._duty = duty
        self._init_pin.duty_u16(duty)

    def on(self, value=None, animate_time_ms=None):
        """
        Turn on led with specified value from range 0-255 or turn's led on maximal duty.
        Could be used to animate value change.

        :param value:
        :param animate_time_ms: Total animation time
        """
        if value is None:
            self._gently(self._on_duty(), animate_time_ms)
            return

        duty = self._calc_duty(value)

        if self._duty == duty:
            return

        self._gently(duty, animate_time_ms)

    def off(self, animate_time_ms=None):
        """
        Turns led off.

        :param animate_time_ms: Total animation time.
        """
        if 0 == self._duty:
            return

        self._gently(self._off_duty(), animate_time_ms)

    def _gently(self, duty, animate_time_ms):
        """
        Method animates duty change for led.

        :param duty: Duty to be set after change.
        :param animate_time_ms: Total animation time.
        """
        # value cannot equal 0 because _duty check
        intervals = abs(self._duty - duty) / self.step_constant

        timespan_us = self.interval_span_us
        if animate_time_ms is not None:
            timespan_us = self._calc_span_us(animate_time_ms, intervals)

        # 255*257 = 256^2 - 1 so 257 is step
        step = self.step_constant if duty > self._duty else -self.step_constant

        for i in range(intervals):
            self._duty = self._duty + step
            self._init_pin.duty_u16(self._duty)
            sleep_us(timespan_us)

    def _calc_duty(self, value):
        """
        Calculates duty from value.

        :param value: Value from range (0-255)
        :return: PWM duty.
        """
        return value * self.step_constant

    def _calc_span_us(self, total_time_ms, intervals):
        """
        Calculates led duty change interval.

        :param total_time_ms: Total swap time span in milliseconds.
        :param intervals: Number of incrementations of duty
        :return: Interval change break in microseconds.
        """
        return int((total_time_ms * 1000) / intervals)

    def _off_duty(self):
        """
        Method created in case of rgb led (anode / katode)
        :return: Returns duty value for led off state.
        """
        return 0