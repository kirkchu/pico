from machine import *
from utime import *

led = Pin(25, Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
