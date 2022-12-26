from dht import DHT11
from machine import Pin
from utime import sleep

sensor = DHT11(Pin(28))

# drawbak it reads only integer value, while you are able to read one decimal place 

while True:
    sleep(3)
    sensor.measure()
    print("T", sensor.temperature())
    print("H", sensor.humidity())