from machine import Pin
from utime import ticks_ms, ticks_diff

from src.const import DEFAULT_SPAN
from src.enums.state_enum import DeviceState
from src.interfaces.device_irq import IRQDevice


class ButtonIRQ(IRQDevice):
    """
    Class represents button for interrupts.
    """
    def __init__(self, pin: int,
                 callback,
                 trigger: int = Pin.IRQ_FALLING,
                 pull: int = Pin.PULL_DOWN,
                 span_ms: int = DEFAULT_SPAN):
        self._last_press = ticks_ms()
        super().__init__(pin, callback, trigger, pull, span_ms)

    def _do_callback(self, pin: Pin):
        if self._state is DeviceState.BUSY:
            return

        if ticks_diff(ticks_ms(), self._last_press) < self._trigger_span:
            return

        self._state = DeviceState.BUSY

        self._last_press = ticks_ms()

        self._callback(pin)
        self._state = DeviceState.ON

