from time import sleep
from micropico import Photorezistor

# Remember to use 10k rezistor

pr = Photorezistor(26)

while True:
    print(f'light: {pr.read_percent(3)} %')
    print(f'light: {pr.read()}')
    sleep(1)
