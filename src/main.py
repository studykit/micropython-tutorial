from machine import Pin, I2C
from writer import Writer
import korean_16 as fonts
import ssd1306
import dht
import time

import clock

clock.setup()

# OLED 디스플레이 설정 (I2C)
i2c = I2C(scl=Pin(12), sda=Pin(14))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

writer = Writer(display, fonts, False)
writer.set_clip(True, True, False)

# DHT11 센서 설정
sensor = dht.DHT11(Pin(16))  # D0 핀은 GPIO16에 해당

def read_sensor():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        return temp, hum
    except:
        return "Error", "Error"

tick = True
while True:
    h, m = clock.now()
    if h > 12:
        h -= 12
        am_pm = "오후"
    else:
        am_pm = "오전"

    writer.set_textpos(display, 0, 0)

    if tick: 
        # 센서에서 온도와 습도 읽기
        temperature, humidity = read_sensor()
        fmt = f"{am_pm} {h:02d}:{m:02d}\n"
        writer.printstring(fmt)
        writer.printstring(f'습도   {humidity}%\n')
        writer.printstring(f"온도   {temperature}°\n")
    else:
        fmt = f"{am_pm} {h:02d} {m:02d}\n"
        writer.printstring(fmt)

    # OLED 디스플레이 초기화
    tick = not tick

    # 디스플레이 업데이트
    display.show()
    
    # 2초 대기
    time.sleep(1)
