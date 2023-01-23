from micropico import PWMLed
from micropico import Photoresistor
from utime import sleep

led = PWMLed(0)
pr = Photoresistor(26)

sleep(1)
led.on(255)
sleep(1)
led.blink(n=2)
sleep(1)
led.off()

while True:
    duty = pr.value()
    led.on(int(duty / led.step_constant))
    print(duty)
    sleep(1)