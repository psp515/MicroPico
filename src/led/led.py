from src.interfaces.output_device import OutputDevice


class Led(OutputDevice):
    def __init__(self, pin: int):
        super().__init__(pin)


    def blink(self, n=1, blink_ms=100):
        pass