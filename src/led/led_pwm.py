from utime import sleep_ms

from src.const import MINIMAL_EYE_BLINK_REACTION_TIME_MS
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

        if duty is None:
            duty = self._on_duty()

        if self._state is DeviceState.BUSY:
            return

        internal_state = self._state
        old = self.duty
        self._state = DeviceState.BUSY

        blink_ms = max(MINIMAL_EYE_BLINK_REACTION_TIME_MS, blink_ms)

        if internal_state is DeviceState.ON:
            self.off(animate_time_ms=MINIMAL_EYE_BLINK_REACTION_TIME_MS)

        span = int(blink_ms / 2)

        for _ in range(n):
            self._gently(duty, span)
            self._gently(self._off_duty(), span)

        if internal_state is DeviceState.ON:
            self._gently(old, MINIMAL_EYE_BLINK_REACTION_TIME_MS)

        self._state = internal_state

    def animate(self):
        pass