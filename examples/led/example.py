from src.led.led import Led
from utime import sleep

led = Led(0)

sleep(1)
led.on(255)
sleep(1)
led.blink(n=2)
sleep(1)
led.off()