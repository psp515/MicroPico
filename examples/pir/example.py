from machine import Pin
from utime import sleep
from micropico import PIR

led = Pin(25, Pin.OUT)
pir = PIR(0)
led.low()
sleep(1)

while True:
    if pir.movement:
        print("LED On")
        led.high()
        sleep(1)
    else:
        print("Waiting for movement")
        led.low()
        sleep(1)
