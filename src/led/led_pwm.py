from src.interfaces.output_pwm_device import OutputDevicePWM


class LedPWM(OutputDevicePWM):
    def __init__(self, pin: int):
        super().__init__(pin)

    def blink(self, n=1, animate=False, time_ms=100):
        pass

