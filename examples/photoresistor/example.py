from time import sleep
from micropico import Photoresistor

# Remember to use 10k rezistor

pr = Photoresistor(26, 3000)
i = 0

while True:
    print("------------",i,"------------")
    print(f'light: {pr.percent_value(3)} %')
    print(f'light: {pr.value}')
    sleep(1)
