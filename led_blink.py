from machine import *
from utime import *

led = Pin(0, Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
