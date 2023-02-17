from machine import ADC, Pin

from src.const import MAX_ADC, PICO_PIN_VOLTAGE
from src.enums.state_enum import DeviceState
from src.interfaces.device import Device


class AnalogInputDevice(Device):
    """
    Class for managing adc sensor.
    """
    input_voltage: float
    _initialized_pin: ADC

    def __init__(self, pin: int, threshold: int = int(0.01 * MAX_ADC), input_voltage=PICO_PIN_VOLTAGE):
        """
        Initializes ADC sensor.

        :param adc_pin: Pin with ADC for sensor.
        :raises InvalidPinException: When invalid pin provided.
        """
        super().__init__(pin)

        self._initialized_pin = ADC(Pin(pin))
        self._threshold = threshold
        self.input_voltage = input_voltage
        self._state = DeviceState.ON

    @property
    def initialized_pin(self):
        """
        :return: ADC object representing device.
        """
        return self._initialized_pin

    @property
    def max_read_value(self):
        """
        Returns maximal possible value that adc pin can return.

        :returns: Maximal read pin value.
        """
        return MAX_ADC

    @property
    def threshold(self):
        """
        The threshold is minimal required read value to consider device as working.
        If readed value is lower than threshold returned value is 0.
        :return: Threshold as int.
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = float(value)

    def over_threshold(self):
        """
        :return: True if received value is bigger than threshold else false.
        """
        return self.value >= self.threshold

    def percent_value(self, precision=2):
        """
        Returns value on analog pin in percent.

        :param precision: Precision of retruned value.
        :returns: Read value in percent or -1 when device is busy.
        """

        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY

        percent_value = round(self._value() / self.max_read_value * 100, precision)

        self._state = DeviceState.ON
        return percent_value

    @property
    def value(self):
        """
        Reads value from analog pin or -1 when device is busy.
        """

        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY

        value = self._value()

        self._state = DeviceState.ON
        return value

    @property
    def voltage(self):
        """
        Returns the voltage of the analogue device or -1 when device is busy.
        """
        if self._state is DeviceState.BUSY:
            return -1

        self._state = DeviceState.BUSY
        voltage = self._value() * self.input_voltage
        self._state = DeviceState.ON

        return voltage

    def _value(self):
        value = self._initialized_pin.read_u16()
        return value if value >= self.threshold else 0

    def __str__(self):
        super(AnalogInputDevice, self).__str__() + \
        f"Class: AnalogInputDevice\n"
