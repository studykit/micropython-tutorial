from writer import Writer
import korean_16
from machine import Pin, I2C
import ssd1306


i2c = I2C(scl=Pin(12), sda=Pin(14))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

writer = Writer(display, korean_16)
Writer.set_textpos(display, 0, 0)
writer.printstring('습도: 20%\n')
writer.printstring("온도: 20°\n")
Writer.set_textpos(display, 0, 0)

# Writer.set_textpos(display, 0, 16)
display.show()
