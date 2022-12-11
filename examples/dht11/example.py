from micropico import DHT11
from utime import sleep

sensor = DHT11(0)

while True:
    print("T", sensor.temperature)
    print("H", sensor.humidity)
    print("-------------------")
    sleep(5)