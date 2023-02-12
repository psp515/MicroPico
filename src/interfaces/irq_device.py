from machine import Pin

from src.enums.state_enum import DeviceState
from src.interfaces.device import Device


class IRQDevice(Device):
    """
    Class created for representing irq device.
    """
    def __init__(self, pin: int, callback, trigger: int, pull: int):
        super().__init__(pin)
        self._init_pin = Pin(pin, Pin.IN, pull)
        self._callback = callback
        self._init_pin.irq(trigger=trigger, handler=self._do_callback)
        self._state = DeviceState.ON

    def _do_callback(self, pin):
        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        self._callback()

        self._state = DeviceState.ON

    def __str__(self):
        return super(IRQDevice, self).__str__() + \
               f"Class: {Device.__class__.__name__}\n"
