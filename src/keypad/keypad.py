from machine import Pin
import utime

from src.exceptions.invalid_keyboard import InvalidKeyboardException


class Keypad:
    """
    Class for managing simple keypad (4x4 5x4 etc.).
    """

    def __init__(self, horizontal_pins, vertical_pins, keyboard=None):
        """
        Function initializes keypad.

        :param horizontal_pins: Horizontal (rows) pin list. (lines starting from left/right)
        :param vertical_pins: Vertical (columns) pin list. (lines starting from down/top)
        :param keyboard: List of strings.
        :param is_working: value can be read from
        """
        if keyboard is None:
            keyboard = [["1", "2", "3", "A"],
                        ["4", "5", "6", "B"],
                        ["7", "8", "9", "C"],
                        ["*", "0", "#", "D"]]

        self._horizontal_pins = []
        self._vertical_pins = []

        if len(horizontal_pins) != len(keyboard) or len(vertical_pins) != len(keyboard[0]):
            raise InvalidKeyboardException("Passed keyboard does not match pins.")


        self._init_horizontal_pins(horizontal_pins)
        self._init_vertical_pins(vertical_pins)

        self.keyboard = keyboard
        self.wait = False

        self.horizontal_pins_count = len(horizontal_pins)
        self.vertical_pins_count = len(vertical_pins)

    def _init_horizontal_pins(self, pins):
        """
        Initialize horizontal pins.

        :param pins: Horizontal pin list.
        """

        for pin in pins:
            self._horizontal_pins.append(Pin(pin, Pin.OUT))

    def _init_vertical_pins(self, pins):
        """
        Initialize vertical pins.

        :param pins: Vertiacal pin list.
        """

        for pin in pins:
            self._vertical_pins.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))

    def read(self):
        """
        If returns pressed key or "".
        """

        if self.wait:
            utime.sleep(0.3)
            self.wait = False

        for row in range(len(self._horizontal_pins)):
            self._horizontal_pins[row].value(1)
            for col in range(len(self._vertical_pins)):
                if self._vertical_pins[col].value() == 1:
                    self._horizontal_pins[row].value(0)
                    self.wait = True
                    return self.keyboard[row][col]

            self._horizontal_pins[row].value(0)

        return ""
