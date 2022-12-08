from micropico import Ultrasonic
from utime import sleep

# Be aware that ultrasonic might use 5V power

us = Ultrasonic(13, 14)

while True:
    print(us.get())
    sleep(1)