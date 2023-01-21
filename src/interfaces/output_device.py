from src.enums.state_enum import DeviceState
from src.interfaces.device import Device
from machine import Pin

class OutputDevice(Device):
    """
    Class represents led object with provided base functions.
    """

    def __init__(self, pin: int):
        super().__init__(pin)
        self._init_pin = Pin(pin, Pin.OUT)

    def on(self):
        """
        Turns device on.
        """
        internal_state = self._state
        self._state = DeviceState.BUSY

        if internal_state is DeviceState.ON:
            self._state = DeviceState.ON
            return

        self._init_pin.value(1)
        self._state = DeviceState.ON

    def off(self):
        """
        Turns device off.
        """
        internal_state = self._state
        self._state = DeviceState.BUSY

        if internal_state is DeviceState.OFF:
            self._state = DeviceState.OFF
            return

        self._init_pin.value(0)
        self._state = DeviceState.OFF
