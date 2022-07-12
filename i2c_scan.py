from machine import *

print(I2C(0, sda=Pin(0), scl=Pin(1)).scan())
