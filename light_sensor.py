from machine import *
from utime import *
photo = machine.ADC(1)
while True:
    value = photo.read_u16()
    print(value)
    sleep(0.5)