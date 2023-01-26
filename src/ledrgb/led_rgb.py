from src.const import MAX_PWM_DUTY
from src.enums.reg_led_type import LedRGBType
from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice
from micropico import LedPWM


class LedRGB(OutputDevice):
    _pin: []
    _init_pin: []

    # noinspection PyMissingConstructor
    def __init__(self, red_pin, green_pin, blue_pin, led_type: LedRGBType, frequency: int = 1000):
        self._pin = [red_pin, green_pin, blue_pin]
        self._init_pin = [LedPWM(red_pin), LedPWM(green_pin), LedPWM(blue_pin)]
        self._init_pin[0].freq(frequency)
        self._init_pin[1].freq(frequency)
        self._init_pin[2].freq(frequency)
        self._led_type = led_type
        self._state = DeviceState.OFF

    @property
    def led_type(self):
        """
        :return: Led type common cathode / common anode
        """
        return self._led_type

    def on(self, animate_ms=600):
        """
        Turn's led on with maximal brightness.

        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY:
            return

        if animate_ms < 150:
            animate_ms = 150

        self._state = DeviceState.BUSY

        animate_avg = animate_ms / 3

        for led in self._init_pin:
            self._gently(led, self._on_duty(), animate_avg)

        self._state = DeviceState.ON

    def off(self, animate_ms=200):
        """
        Turn's led off.

        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY:
            self._state = DeviceState.OFF
            return

        if animate_ms < 150:
            animate_ms = 150

        self._state = DeviceState.BUSY

        animate_avg = animate_ms / 3

        for led in self._init_pin:
            self._gently(led, self._on_duty(), animate_avg)

        self._state = DeviceState.ON

    def color(self, r: int, g: int, b: int, animate_ms=600):
        """
        Turn on device with specified rgb values or turn's led on maximal duty.
        Could be used to animate value change.

        :param g: Value to set to green led in range 0-65535.
        :param b: Value to set to blue led in range 0-65535.
        :param r: Value to set to red led in range 0-65535.
        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY:
            self._state = DeviceState.ON
            return

        if animate_ms < 150:
            animate_ms = 150

        self._state = DeviceState.BUSY

        animate_avg = animate_ms / 3
        #todo

        self._state = DeviceState.ON

    def _off_duty(self):
        """
        :return: Returns duty value for led off state.
        """
        return 0 if self.led_type is LedRGBType.Cathode else MAX_PWM_DUTY

    def _on_duty(self):
        """
        :return: Returns duty value for led off state.
        """
        return MAX_PWM_DUTY if self.led_type is LedRGBType.Cathode else 0

    def _gently(self, led: LedPWM, duty: int, animate_ms: int):
        """
        Method animates duty change for led.

        :param duty: Duty to be set after change.
        :param led: Pwm led for animation.
        :param animate_ms: Approx. total animation time.
        """

        steps = self._f(animate_ms)

        if duty > self._init_pin.duty_u16():
            for i in range(self._g(self._init_pin.duty_u16(), steps),
                           self._g(duty, steps) + 1):
                led.duty = int(MAX_PWM_DUTY * i / steps)
        else:
            for i in range(self._g(self._init_pin.duty_u16(), steps),
                           self._g(duty, steps) - 1, -1):
                led.duty = int(MAX_PWM_DUTY * i / steps)

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

