from machine import *
from utime import *
pir = Pin(22, Pin.IN)

while True:
    print(pir.value())
    sleep(1)
