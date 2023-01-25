from micropico import LedPWM
from micropico import Photoresistor
from utime import sleep

led = LedPWM(0)
pr = Photoresistor(26)


prev = -1
while True:
    duty = pr.value
    led.on(duty, 2000)
    print(duty, led.duty)
    sleep(1)