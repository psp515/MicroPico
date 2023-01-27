from micropico import LedRGB
from micropico import LedRGBType
from utime import sleep

rgb = LedRGB(0, 2, 4, LedRGBType.Anode)


sleep(1)
rgb.on()
sleep(1)
rgb.off()


