from utime import ticks_us

from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice


class IR(InputDevice):
    """
        Class represents IR motion sensor.
        (For line break sensors)
        """

    def __init__(self, pin):
        super().__init__(pin)
        self._last_movement = -1

    @property
    def movement(self):
        """
        Property represents if some movement occurred.
        :return: True if sensor found movement else false.
        """
        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY

        moved = bool((self._read() + 1) % 2)

        if moved == 0:
            self._last_movement = ticks_us()

        self._state = DeviceState.ON

        return moved
