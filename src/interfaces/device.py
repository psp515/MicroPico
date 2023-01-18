from machine import Pin
from src.enums.state_enum import DeviceState

class Device:
    """
    Class represents led object with provided base functions.
    """

    _pin: int
    _state: DeviceState

    def __init__(self, pin: int):
        self._pin = pin
        self._state = DeviceState.OFF

    @property
    def state(self):
        """
        :return: Device state.
        """
        return self._state

    @property
    def pin(self):
        """
        :return: Returns pin number.
        """
        return self._pin
