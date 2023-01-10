from micropico import Led
from micropico import Photorezistor
from utime import sleep

led = Led(0)
pr = Photorezistor(26)

while True:
    duty = pr.value()
    led.on(int(duty / led.step_constant))
    print(duty)
    sleep(1)

