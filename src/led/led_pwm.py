from utime import sleep_ms

from src.const import BLINK_SPAN_MS
from src.enums.state_enum import DeviceState
from src.interfaces.output_pwm_device import OutputDevicePWM


class LedPWM(OutputDevicePWM):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, duty: int = None, n: int = 1, blink_ms: int = 400):
        """
        Blinks led. If led is on additional function finish time extends by 50ms.
        (Turing off LED before blinks, turning led on after blinks)

        :param duty: Blink brightness.
        :param n: Number of blinks.
        :param blink_ms: Single blink time.
        """

        if self._state is DeviceState.BUSY:
            return

        if duty is None:
            duty = self._on_duty()

        internal_state = self._state
        old = self.duty
        self._state = DeviceState.BUSY

        blink_ms = max(BLINK_SPAN_MS, blink_ms)

        if internal_state is DeviceState.ON:
            self._gently(self._initialized_pin.duty_u16, self._initialized_pin.duty_u16(), self._off_duty(), BLINK_SPAN_MS)

        span = int(blink_ms / 2)

        for _ in range(n):
            self._gently(self._initialized_pin.duty_u16, self._initialized_pin.duty_u16(), duty, span)
            self._gently(self._initialized_pin.duty_u16, self._initialized_pin.duty_u16(), self._off_duty(), span)

        if internal_state is DeviceState.ON:
            self._gently(self._initialized_pin.duty_u16, self._initialized_pin.duty_u16(), old, BLINK_SPAN_MS)

        self._state = internal_state
