from machine import *
from utime import *
buzzPin = 15

buzz = PWM(Pin(buzzPin))
buzz.duty_u16(65535//2)
# Do
buzz.freq(523)
sleep(1)
# Re
buzz.freq(587)
sleep(1)
# Mi
buzz.freq(659)
sleep(1)
buzz.deinit()
