from micropico import NECReceiver
from utime import ticks_ms, ticks_diff
from src.tools.ir_receive_message import IRReceiveMessage

nr = 0
nrs = 0


def callback(pin, message):
    print(pin, message)
    global nr
    nr += 1
    if message.is_succesfull:
        global nrs
        nrs += 1


receiver = NECReceiver(0, callback)

last = ticks_ms()
time = last

print("Program Start")
print(receiver)

i = 0
while True:
    time = ticks_ms()
    if ticks_diff(time, last) > 10000:
        print(f"{i}. Number of received commands: {nr}")
        print(f"{i}. Number of successfully received commands: {nrs}")
        last = time
        i += 1
