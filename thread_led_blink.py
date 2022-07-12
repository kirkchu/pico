from machine import *
from utime import *
import _thread

bnPin = 22
ledPin = 0
isButtonDown = False
bn = Pin(bnPin, Pin.IN, Pin.PULL_DOWN)
led = Pin(ledPin, Pin.OUT)

def new_thread():
    while True:
        if isButtonDown:
            led.toggle()
        else:
            led.off()
        sleep(0.2)
 
_thread.start_new_thread(new_thread, ())

while True:
    isButtonDown = bn.value()
    sleep(0.01)
