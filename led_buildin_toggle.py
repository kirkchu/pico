from machine import *
from utime import *

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    sleep(1)

