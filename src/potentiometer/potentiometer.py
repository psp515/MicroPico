from src.enums.state_enum import DeviceState
from src.interfaces.analog_input_device import AnalogInputDevice
import array


class Potentiometer(AnalogInputDevice):
    """
    Class for managing potentiometer.
    """

    _options: array = []

    def __init__(self, pin: int, options: array = []):
        super().__init__(pin)
        self.options = options

    @property
    def options(self):
        """
        Property represents int array with options.
        Option ins represented in range
        0 - options[0] for first value
        options[0] - options[1] for second option etc.

        :return: Options array.
        """
        return self._options

    @options.setter
    def options(self, options: array):
        """
        Sets new options, but before validates options if they are in valid range for device.

        :param options: New options array.
        """
        if len(options) == 0:
            self._options = options
            return

        if any(self.max_read_value < value or value < 0 for value in options):
            return

        for i in range(1, len(options)):
            if options[i] <= options[i-1]:
                return

        self._options = options

    def selected_option(self):
        """
        :return: Returns index of actual selected option as integer or -1 if invalid.
        """

        if self._state is DeviceState.BUSY:
            return

        self._state = DeviceState.BUSY

        n = len(self._options)

        if n == 0:
            return -1

        for i in range(n):
            if self.value <= self._options[i]:
                self._state = DeviceState.ON
                return i

        self._state = DeviceState.ON

        return -1
