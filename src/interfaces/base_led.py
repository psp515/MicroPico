from machine import Pin

class BaseLed:
    """
    Class represents led object with provided base functions.
    """

    pin: Pin()
    is_working: bool

    def __init__(self, pin: int):
        self._led = Pin(pin, Pin.OUT)
        self.is_working = False

    @property
    def state(self):
        """
        :return: Led is on
        """
        return self.is_working

    @property
    def led(self):
        """
        :return: Pin object that states led.
        """
        return self._led

    def on(self):
        """
        Turns led on.
        """
        pass

    def off(self):
        """Turns led off."""
        pass

    def blink(self, n=1, time_ms=100):
        """
        Blinks led

        :param n: Number of blinkS.
        :param time_ms: Single blink time.
        """
        pass