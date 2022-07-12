import ws2812b
import utime

numpix = 8
strip = ws2812b.ws2812b(numpix, 0, 0)
strip.set_pixel(0, 139, 0, 0)
strip.set_pixel(1, 255, 0, 0)
strip.set_pixel(2, 255, 140, 0)
strip.set_pixel(3, 255, 255, 0)
strip.set_pixel(4, 0, 255, 0)
strip.set_pixel(5, 0, 0, 255)
strip.set_pixel(6, 75, 0, 130)
strip.set_pixel(7, 128, 0, 128)
strip.show()

utime.sleep(100)
strip.fill(0, 0, 0)
strip.show()

