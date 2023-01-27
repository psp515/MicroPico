from micropico import LedPWM
from micropico import Photoresistor
from utime import sleep

led = LedPWM(0)
led.freq = 500
pr = Photoresistor(26)
sleep(1)

print("on/off")
led.on(animate_ms=400)
sleep(1)
led.off(animate_ms=400)
sleep(1)
led.on(animate_ms=400)
sleep(1)
led.off(animate_ms=400)



print("on/off/value")
sleep(1)
led.value(value=32000, animate_ms=800)
sleep(1)
led.off(animate_ms=800)
sleep(1)
led.value(value=22000, animate_ms=800)
sleep(1)
led.on(animate_ms=800)
sleep(1)
led.value(value=10000, animate_ms=800)
sleep(1)
led.off(animate_ms=800)

print("blinks")
sleep(1)
led.blink(n=3, blink_ms=400)

print("blinks/on/off")
sleep(1)
led.on(animate_ms=800)
sleep(1)
led.blink(n=3, blink_ms=800)

print("almost")
sleep(1)
led.off(animate_ms=800)

print("end")



