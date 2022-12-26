import array
from math import ceil
import utime
from machine import Pin

from src.exceptions.invalid_pulse_count import InvalidPulseCount

class BytesReciver:
    """
    Class created for receiving pulses and converting it to bytes.
    """
    def __init__(self,
                 pin: int,
                 expected_pulses: int,
                 skip_pulses: int,
                 max_unchange_time: int,
                 bit_timespan: int):
        """

        :param pin: Pin index.
        :param expected_pulses: Expected number of pulses.
        :param skip_pulses: Number of pulses to skip.
        :param max_unchange_time: Maximal time span of unchanging pulse
        :param bit_timespan: Minimal time requirement to read pulse as a 1 bit
        """

        self._pin = pin
        self._expencted_pulses = expected_pulses
        self._max_unchange_time = max_unchange_time
        self._byte_timespan = bit_timespan
        self._skip_pulses = skip_pulses

    def capture_bytes(self):
        """
        Captures pulses and converts them to bytes.
        :return: Array of bytes.
        """
        pulses = self.capture_pulses()
        return self._pulse_to_byte(pulses[self._skip_pulses:])

    @micropython.native
    def capture_pulses(self):
        """
        Function capures pulses.
        :return: Array of pulses.
        """
        pin = Pin(self._pin, Pin.IN, Pin.PULL_UP)
        pin_status, i, unchanged = 1, 0, 0
        pulses = bytearray(self._expencted_pulses)
        timestamp = utime.ticks_us()

        while unchanged < self._max_unchange_time:
            if pin_status != pin.value():
                if i >= self._expencted_pulses:
                    raise InvalidPulseCount(f"Invalid pulses number. Got more than {self._expencted_pulses} pulses")
                now = utime.ticks_us()
                pulses[i] = now - timestamp
                pin_status, unchanged, timestamp = 1 - pin_status, 0, now
                i += 1
            else:
                unchanged += 1

        if i != self._expencted_pulses:
            raise InvalidPulseCount(f"Invalid pulses number. Expected {self._expencted_pulses} but recived {i} pulses")

        return pulses

    def _pulse_to_byte(self, pulses):
        """
        Function converts pulses to bytes.
        :param pulses: Array of pulses.
        :return: Array of bytes.
        """
        binary = self._calculate_binary(pulses)
        # pulses is twice as much as bits and 8bits = 1 byte
        last_byte_idx = ceil((len(pulses) - self._skip_pulses) / (2 * 8)) - 1
        buffer = array.array("B")

        for shift in range(last_byte_idx, -1, -1):
            buffer.append(binary >> shift * 8 & 0xFF)

        return buffer

    def _calculate_binary(self, pulses):
        """
        Function used for calculating binary.
        :param pulses: Array of pulses
        :return: Binary.
        """
        binary = 0
        for idx in range(0, len(pulses), 2):
            binary = binary << 1 | int(pulses[idx] > self._byte_timespan)
        return binary
