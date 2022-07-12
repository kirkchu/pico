from machine import *
from utime import *

led = PWM(Pin(15))
led.freq(800)

# 0 ~ 65535
led.duty_u16(65535 // 2)  # 32767 50%
sleep(3)

led.duty_u16(0)
sleep(1)
led.deinit()
