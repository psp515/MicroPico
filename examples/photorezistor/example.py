from time import sleep
from photorezistor import Photorezistor

# Remember to upload all necessary files to RPIP board.

pr = Photorezistor(26)

while True:
    print(f'light: {pr.readPercent(3)} %')
    print(f'light: {pr.read()} %')
    sleep(1)
