from time import ticks_us

from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice


class PIR(InputDevice):
    """
    Class represents PIR motion sensor.
    """
    def __init__(self, pin):
        super().__init__(pin)
        self._last_movement = -1
        self._state = DeviceState.ON

    @property
    def movement(self):
        """
        Property represents if some movement occured.
        :return: True if sensor found movement else false.
        """
        if self._state is DeviceState.IN_ACTION:
            return

        self._state = DeviceState.IN_ACTION

        value = self._init_pin.value()

        if value == 0:
            self._last_movement = ticks_us()

        self._state = DeviceState.ON
        return self._state_to_boolean(value)


