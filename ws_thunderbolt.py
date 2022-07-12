import urandom

numpix = 8
strip = ws2812b.ws2812b(numpix, 0, 0)

def on(i, r, g, b):
    strip.set_pixel(i, r, g, b)
    strip.show()
    utime.sleep(0.1)
    strip.set_pixel(i, 0, 0, 0)
    strip.show()
    
while True:
    r = urandom.randint(0, 255)
    g = urandom.randint(0, 255)
    b = urandom.randint(0, 255)
        
    for i in range(numpix):
        on(i, r, g, b)

    for i in range(numpix - 2, 0, -1):
        on(i, r, g, b)
