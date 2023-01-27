from src.const import MAX_PWM_DUTY, BLINK_SPAN_MS
from src.enums.reg_led_type import LedRGBType
from src.enums.state_enum import DeviceState
from micropico import LedPWM
from src.interfaces.output_device import OutputDevice


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


        #TODO: pwm warnings

    @property
    def led_type(self):
        """
        :return: Led type common cathode / common anode
        """
        return self._led_type

    def blink(self, r: int, g: int, b: int, n: int = 1, blink_ms:int = 600):
        """
        Blinks led. If led is on additional function finish time extends by BLINK_SPAN_MS.
        (Turing off LED before blinks, turning led on after blinks)

        :param g: Value to set on green led in range 0-65535.
        :param b: Value to set on blue led in range 0-65535.
        :param r: Value to set on red led in range 0-65535.
        :param n: Number of blinks.
        :param blink_ms: Single blink time.
        """
        if self._state is DeviceState.BUSY:
            return

        internal_state = self._state
        self._state = DeviceState.BUSY

        old_r = self._init_pin[0].duty
        old_g = self._init_pin[1].duty
        old_b = self._init_pin[2].duty

        animate_avg = int(max(BLINK_SPAN_MS, blink_ms) / 3)

        if internal_state is DeviceState.ON:
            for led in self._init_pin:
                led.value(self._off_duty(), BLINK_SPAN_MS)

        for _ in range(n):
            for led in self._init_pin:
                led.value(self._off_duty(), BLINK_SPAN_MS)
            for led, value in zip(self._init_pin, [old_r, old_g, old_b]):
                led.value(value, animate_avg)

        if internal_state is DeviceState.ON:
            for led, value in zip(self._init_pin, [old_r, old_g, old_b]):
                led.value(value, animate_avg)

        self._state = internal_state

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

        animate_avg = int(animate_ms / 3)

        for led in self._init_pin:
            led.value(self._on_duty(), animate_avg)

        self._state = DeviceState.ON

    def off(self, animate_ms=200):
        """
        Turn's led off.

        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY or self._state == DeviceState.OFF:
            return

        self._state = DeviceState.BUSY

        if animate_ms < 150:
            animate_ms = 150

        animate_avg = int(animate_ms / 3)

        for led in self._init_pin:
            led.value(self._off_duty(), animate_avg)

        self._state = DeviceState.ON

    def color(self, r: int, g: int, b: int, animate_ms=600):
        """
        Turn on device with specified rgb values or turn's led on maximal duty.
        Could be used to animate value change.

        :param g: Value to set on green led in range 0-65535.
        :param b: Value to set on blue led in range 0-65535.
        :param r: Value to set on red led in range 0-65535.
        :param animate_ms: Approx. total animation time.
        """
        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        if animate_ms < 150:
            animate_ms = 150

        if self._led_type is LedRGBType.Cathode:
            r = MAX_PWM_DUTY - r
            g = MAX_PWM_DUTY - g
            b = MAX_PWM_DUTY - b

        animate_avg = int(animate_ms / 3)

        for led, value in zip(self._init_pin, [r, g, b]):
            led.value(value, animate_avg)

        self._state = DeviceState.ON

    @property
    def pin(self):
        """
        :return: List of pin numbers in order [r, g, b].
        """
        return self._pin

    @property
    def initialized_pin(self):
        """
        :return: List of LedPWM in order [init_r, init_g, init_b].
        """
        return self._init_pin

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



