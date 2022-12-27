from micropico import DHT11
from utime import sleep

sensor = DHT11(0)

while True:
    sleep(2)
    print(f"Temperature: {sensor.temperature}")
    print(f"Humidity: {sensor.humidity}")