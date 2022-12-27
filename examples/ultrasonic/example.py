from micropico import Ultrasonic
from utime import sleep
from micropico import LengthUnit

# Be aware that ultrasonic may use 5V power
# So check it in datasheet 

us = Ultrasonic(0, 1)
i = 1
while True:
    print("Measurement", i)
    print(us.distance)
    print("-------------------")
    sleep(3)
    i+=1