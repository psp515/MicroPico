import array

from machine import Pin

from utime import ticks_ms, ticks_diff, sleep_ms

from src.enums.state_enum import DeviceState
from src.exceptions.invalid_keyboard import InvalidKeyboardException
from src.interfaces.input_device import InputDevice


class Keypad(InputDevice):
    """
    Class for managing simple keypad (4x4 5x4 etc.).
    """
    _horizontal_initialized_pin: array
    _vertical_initialized_pins: array
    _keyboard: array
    _pin: []
    _pressed_span: int

    # noinspection PyMissingConstructor
    def __init__(self, horizontal_pins: array,
                 vertical_pins: array,
                 keyboard: array = None,
                 pressed_span_ms: int = 250):
        if keyboard is None:
            keyboard = [["1", "2", "3", "A"],
                        ["4", "5", "6", "B"],
                        ["7", "8", "9", "C"],
                        ["*", "0", "#", "D"]]

        self._horizontal_initialized_pin = []
        self._vertical_initialized_pins = []

        if len(horizontal_pins) != len(keyboard) or len(vertical_pins) != len(keyboard[0]):
            raise InvalidKeyboardException("Passed keyboard does not match pins.")

        self._init_horizontal_pins(horizontal_pins)
        self._init_vertical_pins(vertical_pins)

        self._keyboard = keyboard
        self._last_read = ticks_ms()

        self._horizontal_pins = horizontal_pins
        self._vertical_pins = vertical_pins

        self._state = DeviceState.ON

        self._pressed_span = pressed_span_ms

    @property
    def pressed_span(self):
        """
        Represents minimal time span between presses.
        :return: Minimal time span between presses in ms.
        """
        return self._pressed_span

    @pressed_span.setter
    def pressed_span(self, span: int):
        """
        Represents minimal time span between presses.

        :param span: Span in ms.
        """
        if span < 0:
            return

        self._pressed_span = span

    @property
    def keyboard(self):
        """
        :return: keyboard passed in constructor
        """
        return self._keyboard

    @property
    def initialized_pin(self):
        """
        :return: Returns list [vertical pins, horizontal pins].
        """
        return [self._vertical_initialized_pins, self._horizontal_initialized_pin]

    @property
    def pin(self):
        """
        :return: Returns list [vertical pins numbers, horizontal pins numbers].
        """
        return [self._vertical_pins, self._horizontal_pins]

    def _init_horizontal_pins(self, pins):
        """
        Initialize horizontal pins.

        :param pins: Horizontal pin list.
        """

        for pin in pins:
            self._horizontal_initialized_pin.append(Pin(pin, Pin.OUT))

    def _init_vertical_pins(self, pins):
        """
        Initialize vertical pins.

        :param pins: Vertical pin list.
        """

        for pin in pins:
            self._vertical_initialized_pins.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))

    def read(self):
        """
        Returns pressed key or "". Also prevents from clicking keys too fast.
        """

        if self._state is DeviceState.BUSY:
            return ""

        self._state = DeviceState.BUSY

        key = self._read()

        self._state = DeviceState.ON
        return key

    def _read(self):
        diff = ticks_diff(ticks_ms(), self._last_read)

        if diff < self._pressed_span:
            sleep_ms(self._pressed_span - diff)

        for row in range(len(self._horizontal_initialized_pin)):
            self._horizontal_initialized_pin[row].value(1)
            for col in range(len(self._vertical_initialized_pins)):
                if self._vertical_initialized_pins[col].value() == 1:
                    self._horizontal_initialized_pin[row].value(0)
                    self._last_read = ticks_ms()
                    return self._keyboard[row][col]

            self._horizontal_initialized_pin[row].value(0)

        return ""
