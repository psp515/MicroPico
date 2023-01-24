from utime import sleep_ms

from src.const import MINIMAL_EYE_BLINK_REACTION_TIME_MS
from src.enums.state_enum import DeviceState
from src.interfaces.output_pwm_device import OutputDevicePWM


class LedPWM(OutputDevicePWM):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, value: int = 255, n=1, blink_ms=100):
        """
        Blinks led. If led is on additional function finish time extends by 20ms.
        (Turing off LED before blinks, turning led on after blinks)

        :param value: Blink brightness.
        :param n: Number of blinks.
        :param blink_ms: Single blink time.
        """
        if self._state is DeviceState.BUSY:
            return

        internal_state = self._state
        self._state = DeviceState.BUSY

        blink_ms = max(MINIMAL_EYE_BLINK_REACTION_TIME_MS, blink_ms)

        if internal_state is DeviceState.ON:
            self.off(animate_time_ms=MINIMAL_EYE_BLINK_REACTION_TIME_MS)

        span = int(blink_ms / 2)

        for _ in range(n):
            self.on(value=value, animate_time_ms=span)
            self.off(animate_time_ms=span)

        if internal_state is DeviceState.ON:
            self.on(value=value, animate_time_ms=MINIMAL_EYE_BLINK_REACTION_TIME_MS)

        self._state = internal_state

    def animate(self):
        pass