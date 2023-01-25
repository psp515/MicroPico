from micropico import LedPWM
from micropico import Photoresistor
from utime import sleep

led = LedPWM(0)
pr = Photoresistor(26)

sleep(1)
led.on(animate_time_ms=400)
print(led.duty)
led.off(animate_time_ms=400)
print(led.duty)
led.on(animate_time_ms=400)
print(led.duty)
led.off(animate_time_ms=400)
print(led.duty)

sleep(1)
led.on(value=32000, animate_time_ms=800)
print(led.duty)
sleep(1)
led.off(animate_time_ms=800)
print(led.duty)
sleep(1)
led.on(value=22000, animate_time_ms=800)
print(led.duty)
sleep(1)
led.on(animate_time_ms=800)
print(led.duty)
sleep(1)
led.on(value=10000, animate_time_ms=800)
print(led.duty)
sleep(1)
led.off(animate_time_ms=800)
print(led.duty)

print("blinks")
sleep(1)
led.blink(n=3, blink_ms=400)
sleep(1)


led.on(animate_time_ms=800)
print(led.duty)
sleep(1)
print("blinks")
led.blink(n=3, blink_ms=800)
sleep(1)
led.off(animate_time_ms=800)
print(led.duty)



