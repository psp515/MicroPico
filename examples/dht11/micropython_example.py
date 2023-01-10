from dht import DHT11
from machine import Pin
from utime import sleep

sensor = DHT11(Pin(0))

# drawbak it reads only integer value, while you are able to read float 

while True:
    sleep(2)
    sensor.measure()
    print("T", sensor.temperature())
    print("H", sensor.humidity())