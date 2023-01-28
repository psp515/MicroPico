from micropico import Button
from utime import sleep
from machine import Pin

button = Button(15)
led = Pin(25, Pin.OUT)

print("Program Starting")
sleep(1)
i = 0

while True:
    if button.pressed:
        led.high()
        i += 1
        print("Clicked", i)
    else:
        led.low()
