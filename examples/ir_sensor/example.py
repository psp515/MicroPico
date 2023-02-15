from machine import Pin
from utime import sleep
from micropico import IRSensor, IRSensorType

led = Pin(25, Pin.OUT)
ir = IRSensor(28, IRSensorType.PIR)
#ir = IRSensor(28, IRSensorType.BEAM_BREAK)

led.low()
sleep(1)
i = 0

print('Program started')

while True:
    if ir.movement:
        print(f"{i}. LED On")
        led.high()
        sleep(1)
        i += 1
    else:
        print(f"{i}. Waiting for movement")
        led.low()
        sleep(0.1)
        i += 1
