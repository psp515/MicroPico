from utime import ticks_diff
from src.enums.receiver_enum import ReceiveState
from src.enums.state_enum import DeviceState
from src.interfaces.ir_rx_irq import IRReceiverIRQ
from src.nec_reciver.const import EDGES, TRIGGER_TIME_MS, START_MIN_ONE_BIT_US, START_MIN_ZERO_BIT_US, REPEAT_US, \
    ZERO_BIT_US, START_MAX_ZERO_REPEAT_BIT_US
from src.tools.ir_receive_message import IRReceiveMessage


class NECReceiver(IRReceiverIRQ):
    """
    Class represents NEC (8-bit) protocol receiver, could be used for receiving data from IR pilots.
    """

    def __init__(self, pin: int, callback):
        super().__init__(pin, callback, EDGES, TRIGGER_TIME_MS)

    def _parse_data(self, timer):
        message = None
        pulses_count = len(self._pulses)
        try:
            if self._number_of_edges < pulses_count:
                raise RuntimeError(ReceiveState.OVERRUN)

            start_one_width = ticks_diff(self._pulses[1], self._pulses[0])

            if start_one_width < START_MIN_ONE_BIT_US:
                raise RuntimeError(ReceiveState.BAD_START)

            start_zero_width = ticks_diff(self._pulses[2], self._pulses[1])

            # TODO  save prev if repeat send prev.
            
            if start_zero_width < START_MAX_ZERO_REPEAT_BIT_US and self._number_of_edges == pulses_count:
                raise RuntimeError(ReceiveState.BAD_START)
            elif start_zero_width > START_MAX_ZERO_REPEAT_BIT_US and pulses_count < self._number_of_edges :
                raise RuntimeError(ReceiveState.BAD_BLOCK)

            address = self._get_byte(3, 19, self._pulses)
            address_complement = self._get_byte(19, 35, self._pulses)
            command = self._get_byte(35, 51, self._pulses)
            command_complement = self._get_byte(51, 66, self._pulses)

            if address & address_complement != 0:
                raise RuntimeError(ReceiveState.BAD_ADDRESS)

            if command & command_complement != 0:
                raise RuntimeError(ReceiveState.BAD_DATA)

            state = ReceiveState.OK if start_zero_width > REPEAT_US else ReceiveState.REPEAT
            message = IRReceiveMessage(state, command, address)

        except RuntimeError as e:
            message = IRReceiveMessage(e.args[0])

        self._state = DeviceState.ON
        self.callback(self.initialized_pin, message)

    def _get_byte(self, start: int, stop: int, array: []):
        value = 0

        for i in range(start, stop, 2):
            value >>= 1
            if ticks_diff(array[i+1], array[i]) > ZERO_BIT_US:
                value |= 0x80

        return value
