

class BytesReciver:
    def __init__(self, pin):
        """
        :param pin: Pin ready to read data.
        """
        self._pin = pin
    def capture_bytes(self):
        pulses = self._pulse_to_byte()
        #todo

    def _pulse_to_byte(self):
        pass

    def _validate_bytes(self):
        pass