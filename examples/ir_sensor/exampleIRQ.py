from micropico import IRSensorIRQ
from utime import sleep, ticks_diff, ticks_ms, ticks_add
from machine import Pin

led = Pin(25, Pin.OUT)
global ticks
prev = ticks_ms()
ticks = prev


def callback(pin):
    print('Led On')
    global ticks
    led.value(1)
    ticks = ticks_add(ticks_ms(), 1000)


# Works or PIR and Beam-Break beacause it bases
# on state change not on state value
ir = IRSensorIRQ(28, callback)

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
