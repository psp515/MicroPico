from micropico import Ultrasonic
from utime import sleep

# Be aware that ultrasonic may use 5V power
# So check it in datasheet 

us = Ultrasonic(1, 0)
i = 1
while True:
    print("Measurement", i)
    print(us.distance)
    print("-------------------")
    sleep(3)
    i+=1