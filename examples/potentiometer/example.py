from utime import sleep
from micropico import Potentiometer

pt = Potentiometer(28)

while True:
    print(f"Value: {pt.read()}, {pt.read_percent()} %")
    sleep(1)