from utime import sleep_ms

from src.enums.state_enum import DeviceState
from src.exceptions.invalid_value import InvalidValueProvidedException
from src.interfaces.output_device import OutputDevice


class DigitalLed(OutputDevice):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, n=1, time_ms=100):
        """
        Functions blinks diode n-times. If led is on function turns off led then performs blinking and
        restores first state (Additional 50ms for actions).

        :param n: Number of blinks (min 1).
        :param time_ms: Time of single blink (min 1ms).
        """

        if self._state is DeviceState.IN_ACTION:
            return

        if time_ms < 1:
            raise InvalidValueProvidedException("Led blink span is at least 1 ms.")

        if n < 1:
            raise InvalidValueProvidedException("Minimal number of blinks is 1.")

        internal_state = self._state
        self._state = DeviceState.IN_ACTION

        if internal_state:
            self._init_pin.value(0)
            sleep_ms(50)

        span = int(time_ms / 2)

        for _ in range(n):
            self._init_pin.value(1)
            sleep_ms(span)
            self._init_pin.value(0)
            sleep_ms(span)

        if internal_state is DeviceState.ON:
            # no need to delay because it is off
            self._init_pin.value(1)

        self._state = internal_state
