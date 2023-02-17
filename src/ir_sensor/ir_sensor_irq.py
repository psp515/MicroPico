from src.const import DEFAULT_SPAN
from src.interfaces.device_irq import IRQDevice
from machine import Pin


class IRSensorIRQ(IRQDevice):
    """
    Class represents PIR motion sensor for interrupts.
    """
    def __init__(self, pin: int,
                 callback,
                 trigger: int = Pin.IRQ_FALLING,
                 pull: int = Pin.PULL_UP,
                 span_ms: int = DEFAULT_SPAN):
        super().__init__(pin, callback, trigger, pull, span_ms)
