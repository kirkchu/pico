from machine import *

led = Pin(25, Pin.OUT)
timer = Timer()
def tick(timer):
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=tick)
