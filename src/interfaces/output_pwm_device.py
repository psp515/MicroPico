from machine import PWM, Pin
from src.const import MAX_PWM_DUTY, MIN_FREQ, MAX_FREQ, DEFAULT_SPAN
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
        if freq < MIN_FREQ or freq > MAX_FREQ:
            return

        self._init_pin.freq=freq

    def value(self, value: int = None, animate_ms: int = DEFAULT_SPAN):
        """
        Turn on device with specified value from range 0-65535 or turn's led on maximal duty.
        Could be used to animate value change.

        :param value: Value to set to device in range 0-65535.
        :param animate_ms: Approx. total animation time.
        """

        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        duty = self._calc_duty(value)

        self._gently(self._init_pin.duty_u16, self._init_pin.duty_u16(), duty, animate_ms)

        self._state = DeviceState.ON

    def on(self, animate_ms: int = DEFAULT_SPAN):
        """
        Turn on device with maximal duty.
        Could be used to animate value change.

        :param animate_ms: Approx. total animation time.
        """

        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        duty = self._on_duty()

        self._gently(self._init_pin.duty_u16, self._init_pin.duty_u16(), duty, animate_ms)

        self._state = DeviceState.ON

    def off(self, animate_ms: int = DEFAULT_SPAN):
        """
        Turns device off.

        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY or self._state is DeviceState.OFF:
            return

        self._state = DeviceState.BUSY

        duty = self._off_duty()

        self._gently(self._init_pin.duty_u16, self._init_pin.duty_u16(), duty, animate_ms)

        self._state = DeviceState.OFF

    def toggle(self, animate_ms: int = DEFAULT_SPAN):
        """
        Toggles device state.

        :param value: Value to set to device in range 0-65535.
        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY:
            return

        if self._state is DeviceState.OFF:
            self.value(animate_ms=animate_ms)
        else:
            self.off(animate_ms)

    def _gently(self, led_duty_func, led_duty: int, duty: int, animate_ms: int):
        """
        Method animates duty change for pwm device.

        :param led_duty_func: Function, setting object duty.
        :param led_duty: Device duty.
        :param duty: Duty to be set after change.
        :param animate_ms: Approx. total animation time.
        """

        if led_duty == duty:
            return

        steps = self._f(animate_ms)
        step_direction = 1 if duty > led_duty else -1
        start = self._g(led_duty, steps)
        end = self._g(duty, steps) + (1 if duty > led_duty else -1)

        for i in range(start, end, step_direction):
            led_duty_func(int(MAX_PWM_DUTY * i / steps))

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
        Calculates duty from value. Created for implementing other value ranges.

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
        return super(OutputDevicePWM, self).__str__() + \
        f"Class: {self.__class__.__name__}\n"
