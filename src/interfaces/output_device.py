from src.enums.state_enum import DeviceState
from src.interfaces.device import Device
from machine import Pin


class OutputDevice(Device):
    """
    Class represents output device with provided base functions.
    """

    def __init__(self, pin: int):
        super().__init__(pin)
        self._init_pin = Pin(pin, Pin.OUT)

    def on(self):
        """
        Turns device on.
        """
        if self._state is DeviceState.ON or self._state is DeviceState.BUSY:
            return

        self._init_pin.value(1)
        self._state = DeviceState.ON

    def off(self):
        """
        Turns device off.
        """
        if self._state is DeviceState.OFF or self._state is DeviceState.BUSY:
            return

        self._init_pin.value(0)
        self._state = DeviceState.OFF

    def __str__(self):
        return super(OutputDevice, self).__str__() + \
        f"Class: {self.__class__.__name__}\n"
