from utime import sleep
from micropico import DigitalLed

led = DigitalLed(0)
print("Start")

sleep(1)
print("On")
led.on()
sleep(1)
print("Double Blink")
led.blink(n=2, time_ms=200)
sleep(1)
print("off")
led.off()
sleep(1)
print("On")
led.on()
sleep(1)
print("Off")
led.off()

print("End")