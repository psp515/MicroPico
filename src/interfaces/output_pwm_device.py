from machine import PWM, Pin
from utime import sleep_us

from src.const import MAX_ADC
from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice


class OutputDevicePWM(OutputDevice):
    """
    Base class for pwm output devices.
    """

    _step_constant: int = 257
    """ Step is solution of equations 255 * x = 256^2 - 1, it is used to calculate in duty 
    because on function takes value in range 0-255."""

    _init_pin: PWM

    def __init__(self, pin: int, frequency: int = 1000):
        self._pin = pin
        self._init_pin = PWM(Pin(pin))
        self._init_pin.freq(frequency)
        self._init_pin.duty_u16(0)
        self._state = DeviceState.OFF

    @property
    def duty(self):
        """
        Returns device duty.

        :return: Device duty.
        """
        return self._init_pin.duty_u16()

    @duty.setter
    def duty(self, duty):
        """
        Sets device duty directly.

        :param duty: Duty to be set on element.
        """
        duty = self._validate_duty(duty)
        self._init_pin.duty_u16(duty)

    @property
    def freq(self):
        """
        :return: Device current frequency.
        """
        return self._init_pin.freq()

    @freq.setter
    def freq(self, freq):
        """
        Sets device frequency.

        :param freq: New device frequency.
        """
        if freq < 1:
            return

        self._init_pin.freq(freq)

    def on(self, value: int = 255, animate: bool = True, animate_time_ms: int = 100):
        """
        Turn on device with specified value from range 0-255 or turn's led on maximal duty.
        Could be used to animate value change.

        :param animate: Terminates is brightness is changed instantly.
        :param value: Value to set to device in range 0-255.
        :param animate_time_ms: Total animation time.
        """

        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        duty = self._calc_duty(value)

        if self._init_pin.duty_u16() == duty:
            return

        if not animate:
            # Quick change
            self._init_pin.duty_u16(duty)
        else:
            # Slow Change
            self._gently(duty, animate_time_ms)

        self._state = DeviceState.ON

    def off(self, animate: bool = True, animate_time_ms: int = 100):
        """
        Turns device off.

        :param animate: Terminates is brightness is changed instantly.
        :param animate_time_ms: Total animation time.
        """
        if self._state is DeviceState.BUSY or self._state is DeviceState.OFF:
            return

        self._state = DeviceState.BUSY

        duty = self._off_duty()

        if not animate:
            # Quick change
            self._init_pin.duty_u16(duty)
        else:
            # Slow Change
            self._gently(duty, animate_time_ms)

        self._state = DeviceState.ON

    def toggle(self, animate: bool = True, value: int = 255, animate_time_ms: int = 100):
        """
        Toggles device state.

        :param animate: Terminates is brightness is changed instantly.
        :param value: Value to set to device in range 0-255.
        :param animate_time_ms: Total animation time.
        """
        if self._state is DeviceState.BUSY:
            return

        if self._state is DeviceState.OFF:
            self.on(value, animate, animate_time_ms)
        else:
            self.off(animate, animate_time_ms)

    def _gently(self, duty: int, animate_time_ms: int):
        """
        Method animates duty change for led.

        :param duty: Duty to be set after change.
        :param animate_time_ms: Total animation time.
        """
        # value cannot equal 0 because _duty check
        intervals = int(abs(self._init_pin.duty_u16() - duty) / self._step_constant)

        timespan_us = max(int((animate_time_ms * 1000) / intervals), 100)

        # 255*257 = 256^2 - 1 so 257 is step
        step = self._get_step(duty)

        for i in range(intervals):
            tmp_duty = self._init_pin.duty_u16() + step
            self._init_pin.duty_u16(tmp_duty)
            sleep_us(timespan_us)

    def _calc_duty(self, value):
        """
        Calculates duty from value.

        :param value: Value from range (0-255)
        :return: PWM duty.
        """
        return self._validate_duty(value * self._step_constant)

    def _validate_duty(self, duty):
        """
        Returns validated duty value.

        :param duty: New duty.
        :return: Validated duty.
        """
        return max(min(self._on_duty(), duty), self._off_duty())

    def _off_duty(self):
        """
        :return: Returns duty value for led off state.
        """
        return 0

    def _on_duty(self):
        """
        :return: Returns duty value for led off state.
        """
        return MAX_ADC

    def _get_step(self, duty):
        """
        Function returns step -_step_constant if duty is decreasing or _step_constant if duty is increasing.

        :param duty: Duty to be set.
        :return: Valid step.
        """
        return self._step_constant if duty > self._init_pin.duty_u16() else - self._step_constant

    def __str__(self):
        super(OutputDevicePWM, self).__str__() + \
        f"Class: {self.__class__.__name__}\n"
