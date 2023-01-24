from src.const import MINIMAL_EYE_BLINK_REACTION_TIME_MS
from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice
from utime import sleep_ms


class Led(OutputDevice):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, n: int = 1, blink_ms: int = 40):
        """
        Blinks led. If led is on additional function finish time extends by 20ms.
        (Turing off LED before blinks, turning led on after blinks)

        :param n: Number of blinkS.
        :param blink_ms: Single blink time.
        """

        if self._state is DeviceState.BUSY:
            return

        blink_ms = max(MINIMAL_EYE_BLINK_REACTION_TIME_MS, blink_ms)

        internal_state = self._state
        self._state = DeviceState.BUSY

        if internal_state is DeviceState.ON:
            self._init_pin.value(0)
            sleep_ms(MINIMAL_EYE_BLINK_REACTION_TIME_MS)

        span = int(blink_ms / 2)

        for _ in range(n):
            self._init_pin.value(1)
            sleep_ms(span)
            self._init_pin.value(0)
            sleep_ms(span)

        if internal_state is DeviceState.ON:
            self._init_pin.value(1)

        self._state = internal_state
