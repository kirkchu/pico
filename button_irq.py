from machine import *
bn = Pin(2, Pin.IN, Pin.PULL_DOWN)
n = 0

def button_handler(pin):
    global n
    print('button down: {}'.format(n))
    n += 1
        
bn.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
