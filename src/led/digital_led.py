from machine import Pin
from utime import sleep_ms

from src.interfaces.base_led import BaseLed

class DigitalLed(BaseLed):
    def __init__(self, pin: int):
        super().__init__(pin)

    @property
    def state(self):
        return self.is_working

    @property
    def led(self):
        return self._led

    def on(self):
        if self.is_working:
            return

        self.is_working = True
        self._led.value(1)

    def off(self):
        if not self.is_working:
            return

        self.is_working = False
        self._led.value(0)


    def blink(self, n=1, time_ms=100):
        """
        Blinks led. If led is on additional function finish time extends by 200ms.
        (Turing off LED before blinks, turning led on after blinks)

        :param n: Number of blinkS.
        :param time_ms: Single blink time.
        """
        if time_ms < 20:
            time_ms = 20

        if self.is_working:
            self._led.value(0)
            sleep_ms(100)

        span = int(time_ms / 2)

        for _ in range(n):
            self._led.value(1)
            sleep_ms(span)
            self._led.value(0)
            sleep_ms(span)


        if self.is_working:
            sleep_ms(100)
            self._led.value(1)