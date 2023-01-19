from machine import Pin

from src.interfaces.device import Device


class InputDevice(Device):
    """
    Base class for input devices.
    """
    _init_pin: Pin

    def __init__(self, pin, pull=Pin.PULL_UP):
        super().__init__(pin)
        self._init_pin = Pin(pin, Pin.IN, pull)
