from src.led.led import Led
from src.photorezistor.photorezistor import Photorezistor
from utime import sleep

led = Led(0)
pr = Photorezistor(26)

while True:
    duty = pr.read()
    led.on(int(duty / led.step_constant))
    print(duty)
    sleep(1)

