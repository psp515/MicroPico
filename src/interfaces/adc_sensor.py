from machine import ADC, Pin

from src.exceptions.invalid_pin_exception import InvalidPinException
from src.const import ADC_PINS, MAX_ADC


class ADCSensor:
    """
    Class for managing adc sensor.
    """
    def __init__(self, adc_pin):
        """
        Initializes ADC sensor.

        :param adc_pin: Pin with ADC for sensor.
        :raises InvalidPinException: When invalid pin provided.
        """

        if adc_pin not in ADC_PINS:
            raise InvalidPinException(f"Provided pin ({adc_pin}) is not a ADC pin.")

        self._adc_sensor = ADC(Pin(adc_pin))

    @property
    def max_read_value(self):
        """
        Returns maximal possible value that adc pin can return.

        :returns: Maximal read pin value.
        """
        return MAX_ADC

    def read_percent(self, precision=2):
        """
        Returns value on analog pin in percent.

        :param precision: Precision of retruned value.
        :returns: Read value in percent.
        """
        return round(self._adc_sensor.read_u16() / self.max_read_value * 100, precision)

    def read(self):
        """
        Reads value from analog pin.
        """
        return self._adc_sensor.read_u16()