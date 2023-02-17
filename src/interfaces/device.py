from machine import Pin
from src.enums.state_enum import DeviceState


class Device:
    """
    Class represents led object with provided base functions.
    """

    _pin: int
    _state: DeviceState
    _initialized_pin: Pin

    def __init__(self, pin: int):
        self._pin = pin
        self._state = DeviceState.OFF
        self._initialized_pin = None

    @property
    def initialized_pin(self):
        """
        Represents used initialized pins for device.
        :return: Pin object representing device.
        """
        return self._initialized_pin

    @property
    def pin(self):
        """
        Represents used pins numbers for device.
        :return: Device pin number.
        """
        return self._pin

    @property
    def state(self):
        """
        :return: Device state.
        """
        return self._state

    def __str__(self):
        return f"Pin: {self._pin},\n" + \
               f"State: {self._state},\n" + \
               f"Pin type: {self._initialized_pin}\n" + \
               f"Class: Device\n"