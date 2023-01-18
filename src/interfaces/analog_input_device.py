from machine import ADC, Pin

from src.exceptions.invalid_pin_exception import InvalidPinException
from src.const import ADC_PINS, MAX_ADC

#TODO : Implement Device Class

class AnalogInputDevice:
    """
    Class for managing adc sensor.
    """
    input_voltage: float
    _adc_sensor: ADC

    def __init__(self, adc_pin, threshold: int = int(0.01 * MAX_ADC), input_voltage=3.3):
        """
        Initializes ADC sensor.

        :param adc_pin: Pin with ADC for sensor.
        :raises InvalidPinException: When invalid pin provided.
        """

        if adc_pin not in ADC_PINS:
            raise InvalidPinException(f"Provided pin ({adc_pin}) is not a ADC pin.")

        self._adc_sensor = ADC(Pin(adc_pin))
        self._threshold = threshold
        self.input_voltage = input_voltage

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

    def percent_value(self, precision=2):
        """
        Returns value on analog pin in percent.

        :param precision: Precision of retruned value.
        :returns: Read value in percent.
        """
        value = self._adc_sensor.read_u16()

        if value < self._threshold:
            return 0

        return round(value / self.max_read_value * 100, precision)

    @property
    def value(self):
        """
        Reads value from analog pin.
        """
        value = self._adc_sensor.read_u16()

        if value < self._threshold:
            return 0

        return value

    @property
    def voltage(self):
        """
        Returns the voltage of the analogue device.
        """
        return self.value * self.input_voltage
