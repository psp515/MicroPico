from machine import Pin

#TODO : Implement Device Class

class InputDevice:
    """
    Base class for input devices.
    """
    _pin: Pin

    def __init__(self, pin, pull=Pin.PULL_UP):
        self._pin = Pin(pin, Pin.IN, pull)

    def _state_to_boolean(self, state: int):
        """
        :param state: Device value.
        :return: State as boolean.
        """
        return bool(state)
