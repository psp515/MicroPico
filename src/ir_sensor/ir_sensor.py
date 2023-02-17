from time import ticks_us

from machine import Pin

from src.enums.ir_sensor_type import IRSensorType
from src.enums.state_enum import DeviceState
from src.interfaces.input_device import InputDevice


class IRSensor(InputDevice):
    """
    Class represents PIR motion sensor.
    """
    def __init__(self, pin: int, type: IRSensorType, pull: Pin = Pin.PULL_UP):
        super().__init__(pin, pull)
        self._last_movement = -1
        self._type = type

    @property
    def movement(self):
        """
        Property represents if some movement occurred.
        :return: True if sensor found movement else false.
        """
        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY

        moved = self._parse(self._read())

        if moved == 0:
            self._last_movement = ticks_us()

        self._state = DeviceState.ON

        return moved

    def _parse(self, value):
        if self._type is IRSensorType.PIR:
            return bool(value)

        return bool((value+1) % 2)

