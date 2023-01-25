from machine import PWM, Pin
from src.const import MAX_PWM_DUTY
from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice


class OutputDevicePWM(OutputDevice):
    """
    Base class for pwm output devices.
    """
    _init_pin: PWM

    def __init__(self, pin: int, frequency: int = 1000):
        self._pin = pin
        self._init_pin = PWM(Pin(pin))
        self._init_pin.freq(frequency)
        self._init_pin.duty_u16(0)
        self._state = DeviceState.OFF
        self._prev = -1

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

    def on(self, value: int = None, animate_time_ms: int = 200):
        """
        Turn on device with specified value from range 0-255 or turn's led on maximal duty.
        Could be used to animate value change.

        :param value: Value to set to device in range 0-255.
        :param animate_time_ms: Total animation time.
        """

        if value is None:
            value = self._on_duty()

        if self._state is DeviceState.BUSY:
            self._state = DeviceState.ON
            return

        self._state = DeviceState.BUSY

        duty = self._calc_duty(value)

        if self._prev == duty:
            return

        self._prev = duty

        self._gently(duty, animate_time_ms)

        self._state = DeviceState.ON

    def off(self, animate_time_ms: int = 200):
        """
        Turns device off.

        :param animate_time_ms: Total animation time.
        """
        if self._state is DeviceState.BUSY or self._state is DeviceState.OFF:
            return

        self._state = DeviceState.BUSY

        duty = self._off_duty()

        self._prev = duty

        self._gently(duty, animate_time_ms)

        self._state = DeviceState.OFF

    def toggle(self, value: int = 255, animate_time_ms: int = 200):
        """
        Toggles device state.

        :param value: Value to set to device in range 0-255.
        :param animate_time_ms: Total animation time.
        """
        if self._state is DeviceState.BUSY:
            return

        if self._state is DeviceState.OFF:
            self.on(value, animate_time_ms)
        else:
            self.off(animate_time_ms)

    def _gently(self, duty: int, animate_time_ms: int):
        """
        Method animates duty change for led.

        :param duty: Duty to be set after change.
        :param animate_time_ms: Total animation time.
        """

        steps = self._f(animate_time_ms)

        if duty > self._init_pin.duty_u16():
            for i in range(self._g(self._init_pin.duty_u16(), steps),
                           self._g(duty, steps) + 1):
                self._init_pin.duty_u16(int(MAX_PWM_DUTY * i / steps))
        else:
            for i in range(self._g(self._init_pin.duty_u16(), steps),
                           self._g(duty, steps) - 1, -1):
                self._init_pin.duty_u16(int(MAX_PWM_DUTY * (i / steps)))

    def _g(self, duty, steps):
        """
        Function calculates actual step.
        :param duty: Actual duty.
        :param steps: Total steps.
        :return: Actual step.
        """
        return int(duty * steps / MAX_PWM_DUTY)

    def _f(self, time):
        """
        Method created for converting animation time to number of
        :param time: Operation time length.
        :return: Number of steps.
        """
        return int(time * 11.9971 + 10.0264)

    def _calc_duty(self, value):
        """
        Calculates duty from value. Created for implementing step.

        :param value: Duty value.
        :return: PWM duty.
        """
        return value

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
        return MAX_PWM_DUTY

    def __str__(self):
        super(OutputDevicePWM, self).__str__() + \
        f"Class: {self.__class__.__name__}\n"
