import array
from math import ceil

import utime
from machine import Pin

from src.exceptions.invalid_pulse_count import InvalidPulseCount

class BytesReciver:
    def __init__(self,
                 pin,
                 expected_pulses,
                 skip_pulses,
                 max_unchange_time,
                 byte_timespan):

        self._pin = pin
        self._expencted_pulses = expected_pulses
        self._max_unchange_time = max_unchange_time
        self._byte_timespan = byte_timespan
        self._skip_pulses = skip_pulses

    @micropython.native
    def capture_bytes(self):
        pin = Pin(28, Pin.IN, Pin.PULL_UP)
        pin_status, i, unchanged = 1, 0, 0
        transitions = bytearray(self._expencted_pulses)
        timestamp = utime.ticks_us()

        while unchanged < self._max_unchange_time:
            if pin_status != pin.value():
                if i >= self._expencted_pulses:
                    raise InvalidPulseCount("Got more than {} pulses".format(self._expencted_pulses))
                now = utime.ticks_us()
                transitions[i] = now - timestamp
                timestamp = now
                i += 1
                pin_status = 1 - pin_status
                unchanged = 0
            else:
                unchanged += 1

        if i != self._expencted_pulses:
            raise InvalidPulseCount("Expected {} but got {} pulses".format(self._expencted_pulses, i))

        return self._pulse_to_byte(transitions[self._skip_pulses:])

    def _pulse_to_byte(self, pulses):
        binary = self._calculate_binary(pulses)
        # pulses is twice as much as bits and 8bits = 1 byte
        last_byte_idx = ceil((len(pulses) - self._skip_pulses) / (2 * 8)) - 1
        buffer = array.array("B")

        for shift in range(last_byte_idx, -1, -1):
            buffer.append(binary >> shift * 8 & 0xFF)

        return buffer

    def _calculate_binary(self, pulses):
        binary = 0
        for idx in range(0, len(pulses), 2):
            binary = binary << 1 | int(pulses[idx] > self._byte_timespan)
        return binary
