from micropico import DHT11
from utime import sleep

sensor = DHT11(0)
i = 1

while True:
    print(f"--------- Read {i} ----------")
    print(f"Temperature: {sensor.temperature}")
    print(f"Humidity: {sensor.humidity}")
    i += 1
    sleep(2)
