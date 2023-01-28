from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice
from utime import ticks_ms, ticks_diff, sleep_ms


class Button(InputDevice):

    _last_read: int

    def __init__(self, pin: int, _pressed_span_ms=250):
        super().__init__(pin)
        self._last_read = ticks_ms()
        self._pressed_span = _pressed_span_ms

    @property
    def pressed_span(self):
        """
        Represents minimal time span between presses.
        :return: Minimal time span between presses in ms.
        """
        return self._pressed_span

    @pressed_span.setter
    def pressed_span(self, span):
        """
        Represents minimal time span between presses.
        :param span: Span in ms.
        """
        if span < 0:
            return

        self._pressed_span = span

    @property
    def pressed(self):
        """
        If button is pressed too soon function delays read.
        :return: True if button is pressed.
        """

        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        diff = ticks_diff(ticks_ms(), self._last_read)

        if diff < self._pressed_span:
            sleep_ms(self._pressed_span - diff)

        pressed = not bool(self._read())

        if pressed:
            self._last_read = ticks_ms()

        self._state = DeviceState.ON

        return pressed



