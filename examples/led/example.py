from micropico import Led
from utime import sleep

led = Led(0)

sleep(1)
led.on(255)
sleep(1)
led.blink(n=2)
sleep(1)
led.off()
sleep(1)
led.on(128)
sleep(1)
led.on(255)
sleep(1)
led.off()

for i in range(256):
    led.on(i)

sleep(1)
led.off()