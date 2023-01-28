from micropico import LedRGB
from micropico import LedRGBType
from utime import sleep

rgb = LedRGB(0, 2, 4, LedRGBType.Anode)

print("on/off")
sleep(1)
rgb.on(3000)
sleep(1)
rgb.off(3000)
sleep(1)

print('Colors')

sleep(1)
rgb.color(3000, 30000, 60000,3000)
sleep(1)
rgb.color(60000, 30000, 3000, 3000)
sleep(1)
rgb.color(3000, 60000, 30000, 3000)
sleep(1)
rgb.on(3000)
sleep(1)
rgb.off(3000)

print('Blink')

sleep(1)
rgb.color(0, 60000, 0, 1000)
sleep(1)
rgb.blink(60000, 0, 0, 3, 1000)
sleep(1)
rgb.off(1000)

print('end')
