from src.interfaces.led_element import BaseLed
from utime import sleep_us

class Led(BaseLed):
    def blink(self, time=None):
        if time is None:
            time = self._default_action_time_ms
        timespan = self._calc_span_us(time, 3)

        self.duty = 0
        sleep_ms(timespan)
        self.on()
        sleep_ms(timespan)
        self.duty = self._duty
        sleep_ms(timespan)