from machine import Pin

from src.enums.state_enum import DeviceState
from src.interfaces.device import Device


class InputDevice(Device):
    """
    Base class for input devices.
    """

    def __init__(self, pin: int, pull=Pin.PULL_UP):
        super().__init__(pin)
        self._initialized_pin = Pin(pin, Pin.IN, pull)
        self._state = DeviceState.ON

    def _read(self):
        """
        Internal method for reading value.
        """
        return self._initialized_pin.value()

    def __str__(self):
        return super(InputDevice, self).__str__() + \
        f" Class: InputDevice\n"
