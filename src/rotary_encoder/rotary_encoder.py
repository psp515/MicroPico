from machine import Pin

from src.enums.rotary_encoder_action import RotaryEncoderAction
from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice


class RotaryEncoder(InputDevice):
    """
    Class represents rotary encoder with button. Encoder detects rotations clockwise and counterclockwise.
    """
    _pin: []
    _init_pin: []

    # noinspection PyMissingConstructor
    def __init__(self, clk: int, dt: int, sw: int, min_pos: int = 0, max_pos: int = 100):
        self._pin = [clk, dt, sw]
        self._init_pin = [Pin(clk, Pin.IN, Pin.PULL_UP),
                          Pin(dt, Pin.IN, Pin.PULL_UP),
                          Pin(sw, Pin.IN, Pin.PULL_UP)]
        self._prev = self.clk.value()
        self._pos = 0
        self._state = DeviceState.ON
        self._min_pos = min_pos
        self._max_pos = max_pos

    @property
    def min_position(self):
        """
        Minimal position of rotary encoder.
        """
        return self._min_pos

    @min_position.setter
    def min_position(self, min_pos):
        self._min_pos = min_pos

    @property
    def max_position(self):
        """
        Maximal position of rotary encoder.
        """
        return self._max_pos

    @max_position.setter
    def max_position(self, max_pos):
        self._max_pos = max_pos

    @property
    def clk(self):
        """
        Clk input pin.
        """
        return self._init_pin[0]

    @property
    def dt(self):
        """
        dt input pin.
        """
        return self._init_pin[1]

    @property
    def sw(self):
        """
        sw input pin.
        """
        return self._init_pin[2]

    @property
    def initialized_pin(self):
        """
        Represents used initialized pins for device.
        :return: List of Pin objects (clk, dt, sw).
        """
        return self._init_pin

    @property
    def pin(self):
        """
        Represents used pins numbers for device.
        :return: List of numbers (clk, dt, sw).
        """
        return self._pin

    @property
    def position(self):
        """
        Returns rotator position since start, based od read value times.
        :return: int.
        """
        return self._pos

    def action(self):
        """
        Returns action read on device.

        :return: Element of RotaryEncoderAction.
        """
        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        action = self._read()

        self._state = DeviceState.ON

        return action

    def _read(self):
        val = self._init_pin[0].value()

        if val != self._prev:
            if val == 0:
                if self._init_pin[1].value() == 0:
                    self._pos = max(self._min_pos, self._pos - 1)
                    self._prev = val
                    return RotaryEncoderAction.CounterClockwise
                else:
                    self._pos = min(self._max_pos, self._pos + 1)
                    self._prev = val
                    return RotaryEncoderAction.Clockwise
            self._prev = val

        if self.sw.value() == 0:
            return RotaryEncoderAction.Click

        return RotaryEncoderAction.NoAction
