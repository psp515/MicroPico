from machine import Pin

from src.const import DEFAULT_SPAN
from src.enums.state_enum import DeviceState
from src.interfaces.device import Device


class IRQDevice(Device):
    """
    Class created for representing irq device.
    """
    def __init__(self, pin: int, callback, trigger: int, pull: int, span_ms: int = DEFAULT_SPAN):
        super().__init__(pin)
        self._trigger_span = span_ms
        self._initialized_pin = Pin(pin, Pin.IN, pull)
        self._callback = callback
        self._initialized_pin.irq(trigger=trigger, handler=self._do_callback)
        self._state = DeviceState.ON

    @property
    def trigger_span(self):
        """
        Represents minimal time span between calling callback.
        :return: Minimal time span between presses in ms.
        """
        return self._trigger_span

    @trigger_span.setter
    def trigger_span(self, span_ms: int):
        """
        Represents minimal time span between  calling callback.
        :param span_ms: Span in ms.
        """
        if span_ms < 0:
            return

        self._trigger_span = span_ms

    @property
    def callback(self):
        """
        Callback is function triggered by irq. Function must have at least one parameter - pin it is callback pin.
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        self._callback = callback

    def _do_callback(self, pin):
        """
        Function created for performing other actions before calling function callback.
        """
        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        self._callback(pin=pin)

        self._state = DeviceState.ON

    def __str__(self):
        return super(IRQDevice, self).__str__() + \
               f"Class: IRQDevice\n"
