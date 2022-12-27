from time import sleep
from micropico import Photoresistor

# Remember to use 10k rezistor

pr = Photoresistor(26)

while True:
    print(f'light: {pr.percent_value(3)} %')
    print(f'light: {pr.value()}')
    sleep(1)
