from micropico import Ultrasonic
from utime import sleep
from micropico import Unit

# Be aware that ultrasonic may use 5V power
# So check it in datasheet 

us = Ultrasonic(13, 14)
i = 1
while True:
    print("Measurement",i)
    # each get is different measurement so distances will differ
    print(us.get_distance(precision=2), "cm")
    print(us.get_distance(Unit.Meter, 3), "m")
    print(us.get_distance(Unit.Milimeter, 0), "mm")
    print(us.get_distance(Unit.Inch), "inch")
    print("-------------------")
    sleep(10)
    i+=1