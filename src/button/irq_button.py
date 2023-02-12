from machine import Pin
from utime import ticks_ms, ticks_diff

from src.enums.state_enum import DeviceState
from src.interfaces.irq_device import IRQDevice


class ButtonIRQ(IRQDevice):
    """
    Class represents button for interrupts.
    """
    def __init__(self, pin: int,
                 callback,
                 trigger: int = Pin.IRQ_FALLING,
                 pull: int = Pin.PULL_DOWN,
                 span_ms: int = 200):
        self._pressed_span = span_ms
        self._last_press = ticks_ms()
        super().__init__(pin, callback, trigger, pull)

    @property
    def pressed_span(self):
        """
        Represents minimal time span between presses.
        :return: Minimal time span between presses in ms.
        """
        return self._pressed_span

    @pressed_span.setter
    def pressed_span(self, span_ms):
        """
        Represents minimal time span between presses.
        :param span: Span in ms.
        """
        if span_ms < 0:
            return

        self._pressed_span = span_ms

    def _do_callback(self, pin):
        if self._state is DeviceState.BUSY:
            return

        now = ticks_ms()

        if ticks_diff(now, self._last_press) < self._pressed_span:
            return

        self._state = DeviceState.BUSY
        self._callback()

        self._state = DeviceState.ON

