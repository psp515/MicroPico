from machine import ADC, Pin

# TODO : class
# TODO : class description
# TODO : methods

class BaseADC:
    """
    Class for managing .

    Attributes
    ----------
    Public:

     : ADC
        .

    Methods
    --------
    Public:

    __init__ (self, adc_pin)
        Initializes ADC object and stores it in class.
    readPercent(self, precision)
        Returns value on analog pin in percent.
    read()
        Reads value on analog pin in .

    """
    def __init__(self, adc_pin):
        """
        Initializes ADC element.

        Parameters
        ----------
        adc_pin : int
            Photorezistor pin.
        max_read_value : int
            Maximal value that can be read from pin.
        """
        self._adc_element = ADC(Pin(adc_pin))

    @property
    def max_read_value(self):
        return 65535

    @property
    def adc_element(self):
        return self._adc_element

    def read_percent(self, precision=2):
        """
        Returns value on analog pin in percent.
        Parameters
        ----------

        precision : int

            Rounds percent value to 'precision' decimal places.
        TODO : 'precision'
        """
        return round(self._adc_element.read_u16() / 65535 * 100, precision)

    def read(self):
        """
        Reads value on analog pin.
        """
        return self._adc_element.read_u16()
