from src.enums.state_enum import DeviceState
from src.interfaces.device import Device
from machine import Pin

class OutputDevice(Device):
    """
    Class represents led object with provided base functions.
    """

    _init_pin: Pin

    def __init__(self, pin: int):
        super().__init__(pin)
        self._init_pin = Pin(pin, Pin.OUT)

    @property
    def initialized_pin(self):
        """
        :return: Pin object representing device.
        """
        return self._init_pin

    def on(self):
        """
        Turns led on.
        """
        internal_state = self._state
        self._state = DeviceState.IN_ACTION

        if internal_state is DeviceState.ON:
            self._state = DeviceState.ON
            return

        self._init_pin.value(1)
        self._state = DeviceState.ON

    def off(self):
        """
        Turns led off.
        """
        internal_state = self._state
        self._state = DeviceState.IN_ACTION

        if internal_state is DeviceState.OFF:
            self._state = DeviceState.OFF
            return

        self._init_pin.value(0)
        self._state = DeviceState.OFF
