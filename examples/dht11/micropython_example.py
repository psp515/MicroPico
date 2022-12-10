from dht import DHT11
from machine import Pin
from utime import sleep

sensor = DHT11(Pin(0))

# drawbak it reads only integer value, while you are able to read one decimal place 

while True:
    sensor.measure()
    print("T", sensor.temperature())
    print("H", sensor.humidity())
    sleep(10)