import ws2812b
import utime

numpix = 8
strip = ws2812b.ws2812b(numpix, 0, 0)
# 第五燈紫色
strip.set_pixel(4, 255, 0, 255)
strip.show()

# 兩秒後關閉
utime.sleep(2)
strip.fill(0, 0, 0)
strip.show()
