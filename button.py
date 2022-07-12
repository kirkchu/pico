from machine import *
from utime import *

bn = Pin(2, Pin.IN, Pin.PULL_DOWN)

n = 0
while True:
    if bn.value() == 1:
        print('button down: {}'.format(n))
        n += 1
    sleep(0.02)
