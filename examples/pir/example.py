from machine import Pin
from utime import sleep
from micropico import PIR

led = Pin(25, Pin.OUT)
pir = PIR(28)
led.low()
sleep(1)
i = 0

while True:
    if pir.movement:
        print(f"{i}. LED On")
        led.high()
        sleep(5)
        i+=1
    else:
        print(f"{i}. Waiting for movement")
        led.low()
        sleep(0.1)
        i+=1
