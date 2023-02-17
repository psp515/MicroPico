from machine import Timer, Pin
from utime import ticks_us

from src.enums.state_enum import DeviceState
from src.interfaces.device_irq import IRQDevice


class IRReceiverIRQ(IRQDevice):
    def __init__(self, pin: int, callback, edges: int, trigger_after_ms: int):
        super().__init__(pin, callback, (Pin.IRQ_FALLING | Pin.IRQ_RISING), None)
        self._number_of_edges = edges
        self._trigger_after_ms = trigger_after_ms
        self._timer = Timer(-1)
        self._pulses = []

    def _do_callback(self, pin):
        pulse = ticks_us()

        if self._state is DeviceState.BUSY:
            self._pulses.append(pulse)
            return

        self._state = DeviceState.BUSY
        self._timer.init(mode=Timer.ONE_SHOT, period=self._trigger_after_ms, callback=self._parse_data)
        self._pulses = [pulse]

    def _parse_data(self, timer):
        """
        Function to implement in each protocol receive.
        Function should parse data and call callback.
        """
        pass

    def __str__(self):
        return super(IRReceiverIRQ, self).__str__() + \
               f"Class: IRReceiverIRQ\n"
