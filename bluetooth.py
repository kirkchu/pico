from machine import *

uart = UART(0, baudrate=38400)

while True:
    n = uart.any()
    if n > 0:
        data = uart.read(n)
        uart.write(data)
        print(data)