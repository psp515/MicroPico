from src.enums.state_enum import DeviceState
from src.interfaces.output_device import OutputDevice
from utime import sleep_ms


class Led(OutputDevice):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, n=1, blink_ms=40):
        """
        Blinks led. If led is on additional function finish time extends by 20ms.
        (Turing off LED before blinks, turning led on after blinks)

        :param n: Number of blinkS.
        :param blink_ms: Single blink time.
        """

        if self._state is DeviceState.BUSY:
            return

        if blink_ms < 20:
            blink_ms = 20

        internal_state = self._state
        self._state = DeviceState.BUSY

        if internal_state is DeviceState.ON:
            self._init_pin.value(0)
            sleep_ms(20)

        span = int(blink_ms / 2)

        for _ in range(n):
            self._init_pin.value(1)
            sleep_ms(span)
            self._init_pin.value(0)
            sleep_ms(span)

        if internal_state is DeviceState.ON:
            self._init_pin.value(1)

        self._state = internal_state
