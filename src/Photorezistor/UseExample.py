
from time import sleep
from Photorezistor import Photorezistor

pr = Photorezistor(26)

while True:
    print(f'light: {pr.readPercent()} %')
    sleep(1) 