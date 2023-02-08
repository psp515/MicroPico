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
    def __init__(self, clk: int, dt: int, sw: int):
        self._pin = [clk, dt, sw]
        self._init_pin = [Pin(clk, Pin.IN), Pin(dt, Pin.IN), Pin(sw, Pin.IN)]
        self._clk_val = self._pin[0].value()
        self._pos = 0
        self._state = DeviceState.ON

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
        :return: Tuple of Pin objects (clk, dt, sw).
        """
        return self._init_pin

    @property
    def pin(self):
        """
        Represents used pins numbers for device.
        :return: Tuple of numbers (clk, dt, sw).
        """
        return self._pin

    def position(self):
        """
        Returns rotator position since start, based od read value times.
        :return: int.
        """
        return self._pos

    def action(self):
        """
        Returns action read on device.

        :return: Enum
        """
        if self._state is DeviceState.BUSY:
            return

        action = self._read()

        self._state = DeviceState.ON

        return action

    def _read(self):
        if self.sw.value():
            return RotaryEncoderAction.Click

        val = self.clk.value()

        if val != self._clk_val:
            if self.dt.value() != val:
                self._pin += 1
                return RotaryEncoderAction.Clockwise
            else:
                self._pin -= 1
                return RotaryEncoderAction.CounterClockwise

        self._clk_val = val
        return RotaryEncoderAction.NoAction
