from utime import sleep
from micropico import Potentiometer

pt = Potentiometer(28)

while True:
    print(f"Value: {pt.value}, {pt.percent_value()} %")
    sleep(1)