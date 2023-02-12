from micropico import ButtonIRQ
from utime import sleep, ticks_diff, ticks_ms, ticks_add
from machine import Pin


led = Pin(25, Pin.OUT)
global ticks
prev = ticks_ms()
ticks = prev


def callback():
    print('Led On')
    global ticks
    led.value(1)
    ticks = ticks_add(ticks_ms(), 1000)


button = ButtonIRQ(0, callback)

print("Program Starting")
sleep(1)
i = 0

while True:
    now = ticks_ms()
    if prev != ticks:
        if ticks_diff(now, ticks) > 0 and led.value() == 1:
            led.value(0)
            print(f'{i} Led off')
            i += 1
            prev = ticks