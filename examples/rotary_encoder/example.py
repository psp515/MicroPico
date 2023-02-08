from micropico import RotaryEncoder
from micropico import RotaryEncoderAction
from utime import sleep
encoder = RotaryEncoder(13, 14, 15)

i = 0

while True:
    action = encoder.action()
    if action is RotaryEncoderAction.Click:
        i += 1
        print(f"{i}. Click")
        sleep(0.2)
    elif action is RotaryEncoderAction.Clockwise:
        i += 1
        print(f"{i}. Clockwise {encoder.position}")
    elif action is RotaryEncoderAction.CounterClockwise:
        i += 1
        print(f"{i}. Counter Clockwise {encoder.position}")
    
    