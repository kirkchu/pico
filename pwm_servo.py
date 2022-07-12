from machine import *
from utime import *

servo = PWM(Pin(16))
servo.freq(50)

# 0度
servo.duty_u16(int(65535 * 0.025))
sleep(3)
# 180度
servo.duty_u16(int(65535 * 0.12))
sleep(3)
# 90度
servo.duty_u16(int(65535 * 0.0725))
sleep(3)

servo.deinit()
