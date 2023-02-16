from micropico import NECReceiver
from utime import ticks_ms, ticks_diff
from src.tools.ir_receive_message import IRReceiveMessage

nr = 0
nrs = 1


def callback(pin, message: IRReceiveMessage):
    print(pin, message)
    global nr
    nr += 1
    if message.is_succesfull:
        global nrs
        nrs += 1


receiver = NECReceiver(0, callback)

last = ticks_ms()
time = last

while True:
    time = ticks_ms()
    if ticks_diff(time, last) > 3000:
        print(f"Number of received commands: {nr}")
        print(f"Number of successfully received commands: {nrs}")
        last = time
