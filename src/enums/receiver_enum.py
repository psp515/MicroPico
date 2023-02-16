
class ReceiveState:
    OK = 0
    REPEAT = 1
    # Error Codes
    BAD_START = -1
    BAD_BLOCK = -2
    OVERRUN = -3
    BAD_DATA = -4
    BAD_ADDRESS = -5
