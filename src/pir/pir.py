from time import ticks_us
from src.interfaces.input_device import InputDevice


class PIR(InputDevice):
    """
    Class represents PIR motion sensor.
    """
    def __init__(self, pin):
        super().__init__(pin)
        self._last_movement = -1

    @property
    def movement(self):
        """
        Property represents if some movement occured.
        :return: True if sensor found movement else false.
        """
        value = self._pin.value()

        if value == 0:
            self._last_movement = ticks_us()

        return not self._state_to_boolean(value)


