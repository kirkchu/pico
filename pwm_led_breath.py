from machine import *
from utime import *

led = PWM(Pin(15))
led.freq(1000)

while True:
    for duty in range(65536):
        led.duty_u16(duty)
        sleep(0.0001)
    
    for duty in range(65535, -1, -1):
        led.duty_u16(duty)
        sleep(0.0001)
