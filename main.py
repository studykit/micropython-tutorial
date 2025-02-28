from writer import Writer
import korean_16

from machine import Pin, I2C
import ssd1306
import dht
import time


# OLED 디스플레이 설정 (I2C)
i2c = I2C(scl=Pin(12), sda=Pin(14))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

writer = Writer(display, korean_16)
Writer.set_textpos(display, 0, 0)

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

while True:
    # 출력 횟수를 추적하기 위한 카운터 증가
    try:
        count += 1
    except NameError:
        count = 1
    
    # 센서에서 온도와 습도 읽기
    temperature, humidity = read_sensor()
    
    # OLED 디스플레이 초기화
    display.fill(0)
    Writer.set_textpos(display, 0, 0)
 
    writer.printstring(f'습도: {humidity}%\n')
    writer.printstring(f"온도: {temperature}°\n")
    writer.printstring(f"CN: {count}")
   
    
    # 디스플레이 업데이트
    display.show()
    
    # 2초 대기
    time.sleep(2)
