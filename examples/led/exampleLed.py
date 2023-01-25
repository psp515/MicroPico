from utime import sleep
from micropico import Led

led = Led(0)
print("Start")

sleep(1)
print("On")
led.on()
sleep(1)
print("Double Blink")
led.blink(n=2, blink_ms=500)
sleep(1)
print("off")
led.off()
sleep(1)
print("On")
led.on()
sleep(1)
print("Off")
led.off()
sleep(1)
print("Double Blink")
led.blink(n=2, blink_ms=500)

print("End")